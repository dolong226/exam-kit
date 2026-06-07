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
        markdown_lines.append("🎉 Tuyệt vời! Bạn đã hoàn thành xuất sắc và không làm sai câu nào.")
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