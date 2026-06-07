from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from core.models import Question, QuizResult, UserResponse

# Khởi tạo một console dùng chung cho toàn bộ app
console = Console()

# Danh sách ký tự đại diện cho các phương án trắc nghiệm
CHOICE_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H"]


def print_banner(title: str, description: str = None) -> None:
    """In ra tiêu đề chào mừng của bộ đề một cách đẹp mắt."""
    console.clear()
    console.print(Panel.fit(
        f"[bold cyan] QUIZ MASTER CLI v0.1.0[/bold cyan]\n"
        f"[bold yellow]Bộ đề:[/bold yellow] {title}\n"
        f"[italic white]{description or ''}[/italic white]",
        border_style="cyan"
    ))
    console.print("\n")


def display_question(index: int, total: int, question: Question) -> str:
    """Hiển thị câu hỏi, danh sách lựa chọn (nếu có) và yêu cầu người dùng nhập đáp án."""
    console.print(f"[bold magenta]Câu hỏi {index}/{total}:[/bold magenta] [bold white]{question.content}[/bold white]")
    
    if question.choices:
        console.print("\n[dim]Các phương án lựa chọn:[/dim]")
        for i, choice in enumerate(question.choices):
            letter = CHOICE_LETTERS[i] if i < len(CHOICE_LETTERS) else str(i)
            console.print(f"  [bold green]{letter}.[/bold green] {choice}")
            
        # Tạo danh sách các lựa chọn hợp lệ để validate đầu vào (A, B, C, D...)
        valid_choices = [CHOICE_LETTERS[i] for i in range(len(question.choices))]
        user_input = Prompt.ask(
            "\n👉 Nhập lựa chọn của bạn", 
            choices=valid_choices, 
            case_sensitive=False
        ).upper()
        return user_input
    else:
        # Chế độ tự luận
        console.print("\n[dim](Nhập câu trả lời của bạn xuống dòng dưới)[/dim]")
        user_input = Prompt.ask("Câu trả lời")
        return user_input


def display_immediate_feedback(response: UserResponse) -> None:
    """Hiển thị kết quả Đúng/Sai và giải thích ngay lập tức sau mỗi câu hỏi."""
    console.print("\n" + "-" * 40)
    if response.is_correct:
        console.print("[bold green]ĐÚNG RỒI![/bold green]")
    else:
        console.print("[bold red]SAI MẤT RỒI![/bold red]")
        console.print(f"Đáp án chính xác là: [bold yellow]{response.correct_answer}[/bold yellow]")
        
    if response.explanation:
        console.print(Panel(
            f"[bold cyan]Giải thích chi tiết:[/bold cyan]\n{response.explanation}",
            border_style="dim"
        ))
    console.print("-" * 40 + "\n")
    Prompt.ask("[italic]Ấn Enter để tiếp tục[/italic]")
    console.print("\n")


def display_final_result(result: QuizResult, report_path: str = None) -> None:
    """Hiển thị bảng tổng kết điểm số tổng thể và đường dẫn file báo cáo câu hỏi sai."""
    console.print("\n" + "=" * 50)
    console.print(Panel.fit(
        f"[bold green]HOÀN THÀNH BÀI KIỂM TRA![/bold green] \n\n"
        f"Điểm số của bạn: [bold gold1]{result.score_string}[/bold gold1] "
        f"({result.correct_count}/{result.total_questions} câu đúng)",
        border_style="gold1",
        padding=(1, 5)
    ))

    # Vẽ bảng thống kê chi tiết
    table = Table(title="Tóm tắt phiên làm bài", show_header=True, header_style="bold magenta")
    table.add_column("Hạng mục", style="dim", width=25)
    table.add_column("Số lượng", justify="right")
    
    table.add_row("Tổng số câu hỏi đã làm", str(result.total_questions))
    table.add_row("[bold green]Số câu đúng[/bold green]", f"[bold green]{result.correct_count}[/bold green]")
    table.add_row("[bold red]Số câu sai[/bold red]", f"[bold red]{len(result.wrong_responses)}[/bold red]")
    
    console.print(table)

    if result.wrong_responses and report_path:
        console.print(f"\n [bold yellow]Lưu ý:[/bold yellow] Danh sách các câu làm sai và giải thích đã được xuất ra file:")
        console.print(f"[bold underline cyan]{report_path}[/bold underline cyan]\n")
    elif not result.wrong_responses:
        console.print("\n [bold light_goldenrod1]Tuyệt vời! Bạn đạt điểm tuyệt đối nên không cần xuất file sửa sai.[/bold light_goldenrod1]\n")