from pathlib import Path
from typing import Union
from .models import QuizResult


def export_wrong_answers(result: QuizResult, output_path: Union[str, Path]) -> Path:
    """
    Trích xuất danh sách câu hỏi làm sai từ kết quả làm bài và xuất ra tệp Markdown (.md).
    Trả về đối tượng Path dẫn tới file vừa tạo.
    """
    path = Path(output_path)
    # Tự động tạo các thư mục cha nếu chưa có (Ví dụ thư mục outputs/)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    markdown_lines = [
        "BÁO CÁO CÁC CÂU HỎI LÀM SAI",
        f"- **Kết quả chung:** Đạt {result.score_string} câu.",
        f"- **Số lượng câu cần ôn tập lại:** {len(result.wrong_responses)} câu.",
        "\n---\n"
    ]
    
    if not result.wrong_responses:
        markdown_lines.append("Tuyệt vời! Bạn đã hoàn thành xuất sắc và không làm sai câu nào.")
    else:
        for idx, resp in enumerate(result.wrong_responses, 1):
            markdown_lines.append(f"Câu hỏi {idx}: {resp.question_content}")
            markdown_lines.append(f"- **Câu trả lời của bạn:** `{resp.user_answer}`")
            markdown_lines.append(f"- **Đáp án mẫu chính xác:** `{resp.correct_answer}`")
            
            if resp.explanation:
                
                clean_exp = resp.explanation.strip()
                markdown_lines.append(f"- **Giải thích chi tiết:**\n  ```text\n  {clean_exp}\n  ```")
                
            markdown_lines.append("\n" + "-" * 30 + "\n")
            
    # Dùng utf-8 để hiện thị tiếng Việt
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(markdown_lines))
        
    return path

def export_essay_grades(
    grades: list,  # list[EssayGradeResult]
    output_path,
    testbank_title: str = "",
) -> "Path":
    """
    Xuất kết quả chấm tự luận ra file Markdown.
    Nhận list[EssayGradeResult] để tránh circular import.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    total = len(grades)
    avg_score = int(sum(g.score_pct for g in grades) / total) if total else 0

    grade_icons = {
        "excellent": "🟢",
        "good": "🔵",
        "partial": "🟡",
        "incorrect": "🔴",
    }

    lines = [
        f"# BÁO CÁO CHẤM TỰ LUẬN",
        f"",
        f"**Bộ đề:** {testbank_title}" if testbank_title else "",
        f"**Tổng số câu:** {total}",
        f"**Điểm trung bình:** {avg_score}/100",
        f"",
        "---",
        "",
    ]
    lines = [l for l in lines if l is not None]

    for idx, g in enumerate(grades, 1):
        icon = grade_icons.get(g.grade if isinstance(g.grade, str) else g.grade.value, "⚪")
        grade_val = g.grade if isinstance(g.grade, str) else g.grade.value
        lines += [
            f"## Câu {idx}  {icon} {grade_val.upper()} — {g.score_pct}/100",
            f"",
            f"**Câu hỏi:** {g.question_content}",
            f"",
            f"**Bài làm của bạn:**",
            f"> {g.user_answer}",
            f"",
            f"**Đáp án mẫu:**",
            f"> {g.reference_answer}",
            f"",
        ]
        if g.error:
            lines += [f"**⚠ Lỗi chấm:** {g.error}", ""]
        elif g.feedback:
            lines += [f"**Nhận xét:** {g.feedback}", ""]

        if g.explanation:
            lines += [f"**Giải thích gốc:** {g.explanation}", ""]

        lines.append("---\n")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return path