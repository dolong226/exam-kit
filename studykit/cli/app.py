import typer
from pathlib import Path
from typing import Optional

from studykit.core.models import QuizConfig, QuizMode
from studykit.core.parser import parse_testbank
from studykit.core.quiz_engine import QuizSession
from studykit.core.reporter import export_wrong_answers
from cli import display

# Khởi tạo Typer App
app = typer.Typer(help="Bộ công cụ hỗ trợ học tập đa năng (CLI/GUI).")


@app.command()
def run(
    file_path: Path = typer.Argument(
        ..., 
        help="Đường dẫn đến file test bank (.yaml)",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True
    ),
    mode: str = typer.Option(
        "multiple_choice", 
        "--mode", "-m", 
        help="Chế độ học: 'multiple_choice' (trắc nghiệm) hoặc 'essay' (tự luận)."
    ),
    immediate: bool = typer.Option(
        False, 
        "--immediate", "-i", 
        help="True: Hiện đáp án và giải thích ngay lập tức sau mỗi câu hỏi."
    )
):
    """Bắt đầu một phiên làm bài Quiz dựa trên file test bank được cung cấp."""
    
    # 1. Chuẩn hóa chế độ học tập
    try:
        quiz_mode = QuizMode(mode.lower())
    except ValueError:
        typer.secho(f"Chế độ '{mode}' không hợp lệ. Vui lòng chọn 'multiple_choice' hoặc 'essay'.", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # 2. Đọc và phân tích cấu trúc file Test Bank
    try:
        testbank = parse_testbank(file_path)
    except Exception as e:
        typer.secho(f"Lỗi nạp dữ liệu: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # 3. Khởi tạo cấu hình và phiên làm bài (Engine)
    config = QuizConfig(mode=quiz_mode, show_explanation_immediately=immediate)
    session = QuizSession(testbank, config)

    # Kiểm tra xem bộ đề có câu hỏi nào thuộc chế độ đã chọn không
    if not session.questions:
        typer.secho(f" Không tìm thấy câu hỏi nào thuộc chế độ '{quiz_mode.value}' trong file này.", fg=typer.colors.YELLOW)
        raise typer.Exit()

    # 4. Giao diện chào mừng
    display.print_banner(testbank.title, testbank.description)

    # 5. Vòng lặp duyệt câu hỏi liên tục (Hiển thị trực tiếp, không tạo file trung gian)
    total_q = len(session.questions)
    while True:
        question = session.get_next_question()
        if not question:
            break
            
        current_idx = session.current_index + 1
        
        # Hiển thị câu hỏi lên terminal và nhận đáp án từ user
        user_raw_input = display.display_question(current_idx, total_q, question)
        
        # Nếu là trắc nghiệm, chuyển ký tự chữ cái (A, B, C...) thành số nguyên index (0, 1, 2...) trước khi nạp vào core
        if quiz_mode == QuizMode.MULTIPLE_CHOICE:
            engine_answer = display.CHOICE_LETTERS.index(user_raw_input)
        else:
            engine_answer = user_raw_input

        # Nộp bài lên engine chấm điểm
        response = session.submit_answer(engine_answer)
        
        # Nếu cấu hình bật chế độ hiện giải thích luôn
        if config.show_explanation_immediately:
            # Format lại đáp án hiển thị bằng Chữ cái (A, B, C..) đối với trắc nghiệm để người dùng dễ đọc
            if quiz_mode == QuizMode.MULTIPLE_CHOICE:
                response.correct_answer = display.CHOICE_LETTERS[int(response.correct_answer)]
            display.display_immediate_feedback(response)

    # 6. Đóng gói kết quả tổng quát
    result = session.get_result()
    report_file_path = None

    # 7. Nếu có câu sai, tự động trích xuất ghi ra file báo cáo dạng Markdown (.md)
    if result.wrong_responses:
        # Đặt tên file theo định dạng: tên_file_gốc.wrong.md nằm trong thư mục outputs/
        output_dir = Path("outputs")
        output_file_name = f"{file_path.stem}.wrong.md"
        report_file_path = output_dir / output_file_name
        
        # Điều hướng sang module reporter để ghi tệp
        export_wrong_answers(result, report_file_path)

    # 8. Render kết quả màn hình cuối cùng
    # Chuẩn hóa lại toàn bộ text đáp án đúng sang dạng chữ cái A,B,C để in kết quả cuối
    if quiz_mode == QuizMode.MULTIPLE_CHOICE:
        for resp in result.wrong_responses:
            resp.correct_answer = display.CHOICE_LETTERS[int(resp.correct_answer)]
            
    display.display_final_result(result, report_path=str(report_file_path) if report_file_path else None)


if __name__ == "__main__":
    app()