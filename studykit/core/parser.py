import re
import random
import yaml
from pathlib import Path
from pydantic import ValidationError
from typing import Union
from .models import TestBank, Question, QuizMode

_LETTERS = "ABCDEFGH"

# Tên folder (case-insensitive) → QuizMode
_FOLDER_MODE_MAP = {
    "trắc nghiệm": QuizMode.MULTIPLE_CHOICE,
    "trac nghiem": QuizMode.MULTIPLE_CHOICE,
    "multiple_choice": QuizMode.MULTIPLE_CHOICE,
    "multiplechoice": QuizMode.MULTIPLE_CHOICE,
    "tự luận": QuizMode.ESSAY,
    "tu luan": QuizMode.ESSAY,
    "essay": QuizMode.ESSAY,
}


def detect_mode_from_path(file_path: Union[str, Path]) -> Union[QuizMode, None]:
    """
    Đọc tên các folder cha của file để suy ra QuizMode.
    VD: testbanks/Toán/Trắc nghiệm/bai1.md → MULTIPLE_CHOICE
    Trả về None nếu không xác định được.
    """
    path = Path(file_path)
    for part in path.parts:
        key = part.strip().lower()
        if key in _FOLDER_MODE_MAP:
            return _FOLDER_MODE_MAP[key]
    return None


MAX_QUESTIONS = 50  # Giới hạn tối đa một phiên làm bài


def parse_testbank(
    file_path: Union[str, Path],
    shuffle: bool = False,
    shuffle_choices: bool = False,
) -> TestBank:
    """
    Đọc file testbank và trả về TestBank.
    Hỗ trợ:
      - .yaml / .yml  → YAML parser
      - .md / .markdown → Markdown parser (tự động nhận dạng loại câu hỏi từ folder)

    shuffle=True        : xáo trộn thứ tự câu hỏi.
    shuffle_choices=True: xáo trộn thứ tự đáp án A/B/C/D (chỉ trắc nghiệm).
                          correct_answer được cập nhật lại đúng theo vị trí mới.

    Giới hạn: nếu file có > MAX_QUESTIONS câu, chọn ngẫu nhiên MAX_QUESTIONS câu.
    """
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file: {path.absolute()}")

    suffix = path.suffix.lower()

    if suffix in (".yaml", ".yml"):
        tb = _parse_yaml(path)
    elif suffix in (".md", ".markdown"):
        mode = detect_mode_from_path(path)
        tb = _parse_markdown(path, mode=mode)
    else:
        raise ValueError(
            f"Định dạng file '{suffix}' không được hỗ trợ. Dùng .yaml hoặc .md"
        )

    questions = list(tb.questions)

    # 1. Giới hạn số câu: nếu vượt MAX_QUESTIONS thì sample ngẫu nhiên
    if len(questions) > MAX_QUESTIONS:
        questions = random.sample(questions, MAX_QUESTIONS)

    # 2. Xáo trộn thứ tự câu hỏi
    if shuffle:
        random.shuffle(questions)

    # 3. Xáo trộn đáp án (chỉ trắc nghiệm) — phải cập nhật lại correct_answer
    if shuffle_choices:
        questions = [_shuffle_question_choices(q) for q in questions]

    tb = TestBank(title=tb.title, description=tb.description, questions=questions)
    return tb


def _shuffle_question_choices(q: Question) -> Question:
    """
    Xáo trộn danh sách choices của một câu trắc nghiệm.
    Cập nhật correct_answer (index) theo vị trí mới của đáp án đúng.
    Câu tự luận hoặc câu không có choices được trả về nguyên vẹn.
    """
    if q.type != QuizMode.MULTIPLE_CHOICE or not q.choices:
        return q

    old_correct_idx = int(q.correct_answer)
    correct_text = q.choices[old_correct_idx]  # lưu lại text đáp án đúng

    # Tạo list mới đã shuffle
    new_choices = list(q.choices)
    random.shuffle(new_choices)

    new_correct_idx = new_choices.index(correct_text)  # tìm lại vị trí mới

    return Question(
        id=q.id,
        type=q.type,
        content=q.content,
        choices=new_choices,
        correct_answer=new_correct_idx,
        explanation=q.explanation,
    )


# ── YAML parser ───────────────────────────────────────────────────────────────

def _parse_yaml(path: Path) -> TestBank:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Lỗi cú pháp YAML trong '{path.name}':\n{e}")

    if not data:
        raise ValueError(f"File '{path.name}' rỗng hoặc không có dữ liệu.")

    try:
        return TestBank(**data)
    except ValidationError as e:
        raise ValueError(f"Dữ liệu không khớp schema trong '{path.name}':\n{e}")


# ── Markdown parser ───────────────────────────────────────────────────────────

def _parse_markdown(path: Path, mode: Union[QuizMode, None] = None) -> TestBank:
    """
    Parse file Markdown. Tự động nhận dạng trắc nghiệm hay tự luận dựa vào
    tham số `mode` (suy ra từ folder cha).

    === Định dạng Trắc nghiệm ===
        **Câu N.** Nội dung câu hỏi
        A. Lựa chọn A
        B. Lựa chọn B
        **Đáp án: B**
        *Giải thích: ...*

    === Định dạng Tự luận ===
        ## Câu N. Nội dung câu hỏi (có thể nhiều dòng)

        Đây là đáp án mẫu, nằm ngay dưới câu hỏi.
        Có thể nhiều dòng.

        *Giải thích: ...* (tùy chọn)

    Câu hỏi tự luận được phân tách bởi dòng trống hoặc câu hỏi tiếp theo.
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Lấy title từ H1
    title = path.stem
    description = None

    h1_match = re.search(r"^#(?!#)\s+(.+)", text, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()

    bq_lines = re.findall(r"^>\s*(.+)", text, re.MULTILINE)
    if bq_lines:
        description = " ".join(bq_lines).strip()

    # Quyết định parser
    if mode == QuizMode.ESSAY:
        questions = _parse_essay_blocks(text, path.name)
    else:
        # Mặc định trắc nghiệm (hoặc mode == MULTIPLE_CHOICE)
        questions = _parse_mc_blocks(text, path.name)

    if not questions:
        mode_hint = "tự luận (## Câu N.)" if mode == QuizMode.ESSAY else "trắc nghiệm (**Câu N.**)"
        raise ValueError(
            f"Không tìm thấy câu hỏi nào trong '{path.name}'.\n"
            f"Đảm bảo file dùng định dạng {mode_hint}."
        )

    return TestBank(title=title, description=description, questions=questions)


# ── Multiple Choice blocks ────────────────────────────────────────────────────

def _parse_mc_blocks(text: str, filename: str) -> list:
    """Tách và parse từng block trắc nghiệm."""
    question_pattern = re.compile(
        r"(?=\*\*Câu\s+\d+[\.\)]\*\*|\*\*\d+[\.\)]\*\*(?!\s*\*))",
        re.MULTILINE,
    )
    blocks = question_pattern.split(text)
    questions = []
    for block in blocks:
        q = _parse_mc_block(block.strip())
        if q is not None:
            questions.append(q)
    return questions


def _clean_md(text: str) -> str:
    """Bỏ markdown bold/italic/blockquote."""
    text = re.sub(r"\*{1,3}(.*?)\*{1,3}", r"\1", text)
    text = re.sub(r"_{1,3}(.*?)_{1,3}", r"\1", text)
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    return text.strip()


def _parse_mc_block(block: str) -> Union[Question, None]:
    if not block:
        return None

    lines = [l.rstrip() for l in block.splitlines()]
    lines = [l for l in lines if l and not re.match(r"^-{3,}$", l)]
    if not lines:
        return None

    header_re = re.compile(r"\*\*(?:Câu\s+)?(\d+)[\.\)]\*\*\s*(.*)", re.IGNORECASE)
    m = header_re.match(lines[0])
    if not m:
        return None

    q_id_num = m.group(1)
    q_content_first = _clean_md(m.group(2))

    choice_re = re.compile(r"^(?:\*\*\s*)?([A-H])[\.\)]\*?\*?\s+(.+)", re.IGNORECASE)
    answer_re = re.compile(r"(?:\*\*)?(?:Đáp\s*án|Answer)\s*:\s*([A-H])", re.IGNORECASE)
    expl_re = re.compile(r"^\*?(?:Giải\s*thích|Explanation)\s*:\s*(.*)\*?$", re.IGNORECASE)

    content_lines = [q_content_first] if q_content_first else []
    choices: list = []
    correct_letter = ""
    explanation_parts: list = []

    i = 1
    while i < len(lines):
        if choice_re.match(lines[i]) or answer_re.search(lines[i]):
            break
        cleaned = _clean_md(lines[i])
        if cleaned:
            content_lines.append(cleaned)
        i += 1

    while i < len(lines):
        cm = choice_re.match(lines[i])
        if cm:
            choices.append(_clean_md(cm.group(2)))
            i += 1
            continue

        am = answer_re.search(lines[i])
        if am:
            correct_letter = am.group(1).upper()
            i += 1
            continue

        em = expl_re.match(lines[i])
        if em:
            expl_text = _clean_md(em.group(1))
            if expl_text:
                explanation_parts.append(expl_text)
            i += 1
            while i < len(lines) and not choice_re.match(lines[i]) and not answer_re.search(lines[i]):
                cleaned = _clean_md(lines[i])
                if cleaned:
                    explanation_parts.append(cleaned)
                i += 1
            continue

        i += 1

    content = " ".join(content_lines).strip()
    if not content or not choices or not correct_letter or correct_letter not in _LETTERS:
        return None

    correct_index = _LETTERS.index(correct_letter)
    if correct_index >= len(choices):
        return None

    return Question(
        id=f"q{q_id_num}",
        type=QuizMode.MULTIPLE_CHOICE,
        content=content,
        choices=choices,
        correct_answer=correct_index,
        explanation=" ".join(explanation_parts) if explanation_parts else None,
    )


# ── Essay blocks ──────────────────────────────────────────────────────────────

def _parse_essay_blocks(text: str, filename: str) -> list:
    """
    Parse tự luận. Format:

        ## Câu N. Nội dung câu hỏi
        (dòng trống)
        Đây là đáp án mẫu.
        Có thể nhiều dòng.
        (dòng trống)
        *Giải thích: ...* (tùy chọn)

    Câu hỏi bắt đầu bằng ## (H2).
    Đáp án là toàn bộ nội dung giữa câu hỏi và câu tiếp theo (hoặc cuối file).
    """
    # Split theo heading H2: ## Câu N. hoặc ## N.
    # Dùng lookahead để giữ lại delimiter
    block_pattern = re.compile(
        r"(?=^##\s+(?:Câu\s+)?\d+[\.\)])",
        re.MULTILINE,
    )
    blocks = block_pattern.split(text)

    expl_re = re.compile(r"^\*?(?:Giải\s*thích|Explanation)\s*:\s*(.*)\*?$", re.IGNORECASE)

    questions = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = [l.rstrip() for l in block.splitlines()]
        lines = [l for l in lines if not re.match(r"^-{3,}$", l)]
        if not lines:
            continue

        # Dòng đầu: ## Câu N. nội dung
        header_re = re.compile(r"^##\s+(?:Câu\s+)?(\d+)[\.\)]\s*(.*)", re.IGNORECASE)
        hm = header_re.match(lines[0])
        if not hm:
            continue

        q_id_num = hm.group(1)
        q_content_first = hm.group(2).strip()

        # Gom thêm dòng nội dung câu hỏi cho đến dòng trống đầu tiên
        content_lines = [q_content_first] if q_content_first else []
        i = 1
        while i < len(lines) and lines[i].strip():
            content_lines.append(lines[i].strip())
            i += 1

        # Bỏ qua dòng trống giữa câu hỏi và đáp án
        while i < len(lines) and not lines[i].strip():
            i += 1

        # Gom đáp án: các dòng không phải giải thích, cho đến dòng trống hoặc hết
        answer_lines = []
        explanation_parts = []

        while i < len(lines):
            line = lines[i]
            em = expl_re.match(line)
            if em:
                # Đây là dòng giải thích
                expl_text = _clean_md(em.group(1))
                if expl_text:
                    explanation_parts.append(expl_text)
                i += 1
                # Đọc tiếp các dòng giải thích (nếu nhiều dòng)
                while i < len(lines) and lines[i].strip():
                    explanation_parts.append(_clean_md(lines[i]))
                    i += 1
                break
            elif not line.strip():
                # Dòng trống → kết thúc đáp án (nếu đã có đáp án)
                if answer_lines:
                    i += 1
                    # Xem tiếp có giải thích không
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                    # Kiểm tra dòng tiếp theo có phải giải thích không
                    if i < len(lines):
                        em2 = expl_re.match(lines[i])
                        if em2:
                            expl_text = _clean_md(em2.group(1))
                            if expl_text:
                                explanation_parts.append(expl_text)
                            i += 1
                            while i < len(lines) and lines[i].strip():
                                explanation_parts.append(_clean_md(lines[i]))
                                i += 1
                    break
                else:
                    i += 1
                    continue
            else:
                answer_lines.append(line.strip())
                i += 1

        content = " ".join(content_lines).strip()
        answer = "\n".join(answer_lines).strip()

        if not content or not answer:
            continue

        questions.append(Question(
            id=f"q{q_id_num}",
            type=QuizMode.ESSAY,
            content=content,
            choices=None,
            correct_answer=answer,
            explanation=" ".join(explanation_parts) if explanation_parts else None,
        ))

    return questions