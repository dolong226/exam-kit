"""
core/grader.py — Bộ chấm tự luận dùng Anthropic API.

Luồng hoạt động:
  1. Nhận câu hỏi + đáp án mẫu + bài làm của user
  2. Gọi LLM với prompt được thiết kế để trả về JSON chuẩn
  3. Parse JSON → EssayGradeResult
  4. Fallback rõ ràng nếu API lỗi hoặc JSON không parse được
"""

import json
import os
from typing import Optional

from .models import EssayGradeResult, GradeLevel, GraderConfig, Question


# ── Prompt ────────────────────────────────────────────────────────────────────

_SYSTEM_PROMPT_VI = """\
Bạn là giám khảo chấm bài tự luận. Nhiệm vụ của bạn là so sánh bài làm \
của học sinh với đáp án mẫu và đưa ra đánh giá KHÁCH QUAN, CHÍNH XÁC.

Quy tắc chấm:
- EXCELLENT  (90–100%): Bài làm nắm đầy đủ và chính xác trọng tâm, diễn đạt rõ ràng.
- GOOD       (65–89%) : Đúng trọng tâm chính, có thể thiếu vài chi tiết nhỏ.
- PARTIAL    (30–64%) : Có một số ý đúng nhưng còn nhiều thiếu sót hoặc nhầm lẫn.
- INCORRECT  (0–29%)  : Bài làm sai hoặc không liên quan đến yêu cầu.

Lưu ý:
- Không yêu cầu học sinh phải dùng đúng từng chữ trong đáp án mẫu, \
miễn là ý nghĩa tương đương là được.
- Nếu strict_mode=true, hãy chấm nghiêm hơn: yêu cầu đủ các ý chính.
- Phản hồi PHẢI là JSON hợp lệ, không có markdown, không có giải thích thêm ngoài JSON.

Trả về đúng định dạng JSON sau:
{
  "grade": "excellent" | "good" | "partial" | "incorrect",
  "score_pct": <số nguyên 0-100>,
  "feedback": "<nhận xét ngắn gọn bằng tiếng Việt, 2-4 câu>"
}
"""

_SYSTEM_PROMPT_EN = """\
You are an essay grading assistant. Compare the student's answer with the \
reference answer and give an OBJECTIVE, ACCURATE assessment.

Grading rubric:
- EXCELLENT  (90–100%): Fully captures the key ideas, clearly expressed.
- GOOD       (65–89%) : Gets the main point, may miss minor details.
- PARTIAL    (30–64%) : Some correct ideas but significant gaps or errors.
- INCORRECT  (0–29%)  : Answer is wrong or irrelevant.

Rules:
- Do NOT require word-for-word match with the reference — equivalent meaning is fine.
- If strict_mode=true, be stricter: all key points must be present.
- Response MUST be valid JSON only, no markdown, no extra text outside the JSON.

Return exactly this JSON format:
{
  "grade": "excellent" | "good" | "partial" | "incorrect",
  "score_pct": <integer 0-100>,
  "feedback": "<concise feedback in English, 2-4 sentences>"
}
"""


def _build_user_message(question: Question, user_answer: str, strict_mode: bool) -> str:
    return (
        f"Câu hỏi: {question.content}\n\n"
        f"Đáp án mẫu: {question.correct_answer}\n\n"
        f"Bài làm của học sinh: {user_answer}\n\n"
        f"strict_mode: {str(strict_mode).lower()}"
    )


def _parse_llm_response(raw: str) -> tuple[str, int, str]:
    """
    Parse JSON từ LLM response.
    Trả về (grade_str, score_pct, feedback).
    Raise ValueError nếu không parse được.
    """
    # Strip markdown fences nếu LLM vẫn trả về dù đã dặn không
    text = raw.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        text = "\n".join(
            l for l in lines
            if not l.strip().startswith("```")
        ).strip()

    data = json.loads(text)

    grade_str = str(data.get("grade", "")).lower()
    valid_grades = {g.value for g in GradeLevel}
    if grade_str not in valid_grades:
        raise ValueError(f"grade không hợp lệ: {grade_str!r}")

    score_pct = int(data.get("score_pct", 0))
    score_pct = max(0, min(100, score_pct))

    feedback = str(data.get("feedback", "")).strip()
    if not feedback:
        raise ValueError("feedback rỗng")

    return grade_str, score_pct, feedback


# ── Public API ────────────────────────────────────────────────────────────────

def grade_essay(
    question: Question,
    user_answer: str,
    config: Optional[GraderConfig] = None,
) -> EssayGradeResult:
    """
    Chấm một câu tự luận bằng LLM.

    Args:
        question:    Câu hỏi (phải là type=essay, có correct_answer)
        user_answer: Bài làm của user
        config:      GraderConfig, dùng default nếu None

    Returns:
        EssayGradeResult — luôn trả về, không raise exception.
        Nếu có lỗi API, trả về grade=INCORRECT, error chứa thông báo.
    """
    if config is None:
        config = GraderConfig()

    base = dict(
        question_id=question.id,
        question_content=question.content,
        user_answer=user_answer,
        reference_answer=str(question.correct_answer),
        explanation=question.explanation,
    )

    # Resolve API key
    api_key = config.api_key or os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return EssayGradeResult(
            **base,
            grade=GradeLevel.INCORRECT,
            score_pct=0,
            feedback="",
            error=(
                "Chưa cấu hình ANTHROPIC_API_KEY. "
                "Đặt biến môi trường hoặc truyền api_key vào GraderConfig."
            ),
        )

    # Gọi Anthropic API
    try:
        import anthropic  # lazy import — không bắt buộc ở v1/v2

        client = anthropic.Anthropic(api_key=api_key)
        system = _SYSTEM_PROMPT_VI if config.language == "vi" else _SYSTEM_PROMPT_EN
        user_msg = _build_user_message(question, user_answer, config.strict_mode)

        message = client.messages.create(
            model=config.model,
            max_tokens=512,
            system=system,
            messages=[{"role": "user", "content": user_msg}],
        )

        raw = message.content[0].text
        grade_str, score_pct, feedback = _parse_llm_response(raw)

        return EssayGradeResult(
            **base,
            grade=GradeLevel(grade_str),
            score_pct=score_pct,
            feedback=feedback,
        )

    except ImportError:
        return EssayGradeResult(
            **base,
            grade=GradeLevel.INCORRECT,
            score_pct=0,
            feedback="",
            error=(
                "Thư viện 'anthropic' chưa được cài đặt. "
                "Chạy: pip install anthropic"
            ),
        )
    except Exception as exc:  # noqa: BLE001
        return EssayGradeResult(
            **base,
            grade=GradeLevel.INCORRECT,
            score_pct=0,
            feedback="",
            error=f"Lỗi khi gọi API: {exc}",
        )


def grade_essay_batch(
    questions: list[Question],
    user_answers: list[str],
    config: Optional[GraderConfig] = None,
) -> list[EssayGradeResult]:
    """
    Chấm nhiều câu tự luận tuần tự.
    questions và user_answers phải cùng độ dài.
    """
    if len(questions) != len(user_answers):
        raise ValueError("questions và user_answers phải cùng số lượng")
    return [
        grade_essay(q, a, config)
        for q, a in zip(questions, user_answers)
    ]
