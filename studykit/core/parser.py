import re
import yaml
from pathlib import Path
from pydantic import ValidationError
from typing import Union
from .models import TestBank, Question, QuizMode

# Chữ cái đáp án hợp lệ
_LETTERS = "ABCDEFGH"


def parse_testbank(file_path: Union[str, Path]) -> TestBank:
    """
    Đọc file testbank và trả về TestBank.
    Hỗ trợ 2 định dạng tự động theo đuôi file:
      - .yaml / .yml  → YAML parser
      - .md / .markdown → Markdown parser
    """
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file: {path.absolute()}")

    suffix = path.suffix.lower()

    if suffix in (".yaml", ".yml"):
        return _parse_yaml(path)
    elif suffix in (".md", ".markdown"):
        return _parse_markdown(path)
    else:
        raise ValueError(
            f"Định dạng file '{suffix}' không được hỗ trợ. "
            "Dùng .yaml hoặc .md"
        )


# ── YAML parser (giữ nguyên logic cũ) ────────────────────────────────────────

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

def _parse_markdown(path: Path) -> TestBank:
    """
    Parse file Markdown theo format:

        # Tiêu đề bộ đề
        > Mô tả (tùy chọn, dòng blockquote đầu tiên)

        **Câu N.** Nội dung câu hỏi
        A. Lựa chọn A
        B. Lựa chọn B
        C. Lựa chọn C
        D. Lựa chọn D
        **Đáp án: B**
        *Giải thích: ...*

        ---   ← phân cách câu hỏi (tùy chọn)

    Quy tắc nhận dạng:
    - Câu hỏi: dòng bắt đầu bằng **Câu N.** hoặc **N.** hoặc N.
    - Lựa chọn: dòng bắt đầu bằng A. / A) / **A.** / - A.
    - Đáp án: dòng chứa "Đáp án:" hoặc "Answer:"
    - Giải thích: dòng bắt đầu bằng *Giải thích:* hoặc *Explanation:*
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # ── Lấy title từ heading H1 đầu tiên ─────────────────────────────────
    title = path.stem  # fallback = tên file
    description = None

    h1_match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()

    # Lấy description từ blockquote đầu tiên (dòng bắt đầu > )
    bq_match = re.search(r"^>\s*(.+)", text, re.MULTILINE)
    if bq_match:
        # Nối các dòng blockquote liên tiếp
        bq_lines = re.findall(r"^>\s*(.+)", text, re.MULTILINE)
        description = " ".join(bq_lines).strip() if bq_lines else None

    # ── Tách các block câu hỏi ────────────────────────────────────────────
    # Câu hỏi được nhận dạng bởi pattern: **Câu N.** hoặc **N.**
    # Dùng lookahead để split mà giữ lại delimiter
    question_pattern = re.compile(
        r"(?=\*\*Câu\s+\d+[\.\)]\*\*|\*\*\d+[\.\)]\*\*(?!\s*\*))",
        re.MULTILINE,
    )
    blocks = question_pattern.split(text)

    questions: list[Question] = []
    for block in blocks:
        q = _parse_question_block(block.strip())
        if q is not None:
            questions.append(q)

    if not questions:
        raise ValueError(
            f"Không tìm thấy câu hỏi nào trong '{path.name}'.\n"
            "Đảm bảo câu hỏi có định dạng: **Câu N.** hoặc **N.**"
        )

    return TestBank(title=title, description=description, questions=questions)


def _clean_md(text: str) -> str:
    """Bỏ markdown bold/italic/blockquote khỏi chuỗi."""
    text = re.sub(r"\*{1,3}(.*?)\*{1,3}", r"\1", text)  # *x* **x** ***x***
    text = re.sub(r"_{1,3}(.*?)_{1,3}", r"\1", text)
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    return text.strip()


def _parse_question_block(block: str) -> Union[Question, None]:
    """
    Parse một block text thành Question.
    Trả về None nếu block không hợp lệ.
    """
    if not block:
        return None

    lines = [l.rstrip() for l in block.splitlines()]
    lines = [l for l in lines if l and not re.match(r"^-{3,}$", l)]  # bỏ ---
    if not lines:
        return None

    # ── Dòng 1: số thứ tự + nội dung câu hỏi ────────────────────────────
    # Pattern: **Câu N.** Nội dung  hoặc  **N.** Nội dung
    header_re = re.compile(
        r"\*\*(?:Câu\s+)?(\d+)[\.\)]\*\*\s*(.*)", re.IGNORECASE
    )
    m = header_re.match(lines[0])
    if not m:
        return None

    q_id_num = m.group(1)
    q_content_first = _clean_md(m.group(2))

    # Gom thêm các dòng nội dung câu hỏi (cho đến khi gặp lựa chọn / đáp án)
    choice_re = re.compile(
        r"^(?:\*\*\s*)?([A-H])[\.\)]\*?\*?\s+(.+)", re.IGNORECASE
    )
    answer_re = re.compile(
        r"(?:\*\*)?(?:Đáp\s*án|Answer)\s*:\s*([A-H])", re.IGNORECASE
    )
    expl_re = re.compile(
        r"^\*?(?:Giải\s*thích|Explanation)\s*:\s*(.*)\*?$", re.IGNORECASE
    )

    content_lines = [q_content_first] if q_content_first else []
    choices: list[str] = []
    correct_letter: str = ""
    explanation_parts: list[str] = []

    i = 1
    # Tiếp tục đọc nội dung câu hỏi đến khi gặp dòng lựa chọn đầu tiên
    while i < len(lines):
        if choice_re.match(lines[i]) or answer_re.search(lines[i]):
            break
        cleaned = _clean_md(lines[i])
        if cleaned:
            content_lines.append(cleaned)
        i += 1

    # Đọc các lựa chọn
    while i < len(lines):
        cm = choice_re.match(lines[i])
        if cm:
            choices.append(_clean_md(cm.group(2)))
            i += 1
            continue

        # Đáp án
        am = answer_re.search(lines[i])
        if am:
            correct_letter = am.group(1).upper()
            i += 1
            continue

        # Giải thích
        em = expl_re.match(lines[i])
        if em:
            expl_text = _clean_md(em.group(1))
            if expl_text:
                explanation_parts.append(expl_text)
            i += 1
            # Đọc tiếp các dòng giải thích liên tiếp (nếu nhiều dòng)
            while i < len(lines) and not choice_re.match(lines[i]) and not answer_re.search(lines[i]):
                cleaned = _clean_md(lines[i])
                if cleaned:
                    explanation_parts.append(cleaned)
                i += 1
            continue

        i += 1

    # ── Validate ──────────────────────────────────────────────────────────
    content = " ".join(content_lines).strip()
    if not content:
        return None
    if not choices:
        return None
    if not correct_letter or correct_letter not in _LETTERS:
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