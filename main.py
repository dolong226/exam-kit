import os
import sys

# Lấy đường dẫn tuyệt đối của thư mục gốc (exam-kit)
root_dir = os.path.dirname(os.path.abspath(__file__))

# Định nghĩa đường dẫn tới thư mục studykit (nơi chứa core, cli, gui)
studykit_dir = os.path.join(root_dir, "studykit")

# Ép Python phải quét vào bên trong thư mục studykit trước
if os.path.exists(studykit_dir):
    sys.path.insert(0, studykit_dir)
sys.path.insert(0, root_dir)


def main() -> None:
    """
    Điểm khởi chạy chính.
    - python main.py               CLI mode (Typer)
    - python main.py --gui         GUI mode (CustomTkinter)
    - python main.py gui           GUI mode (alias)
    """
    args = sys.argv[1:]

    # Kiểm tra xem có yêu cầu GUI không
    if args and args[0] in ("--gui", "gui"):
        # Xóa flag khỏi argv để không làm rối Typer nếu sau này dùng hybrid
        sys.argv = [sys.argv[0]]
        _launch_gui()
    else:
        _launch_cli()


def _launch_cli() -> None:
    from cli.app import app as cli_app
    cli_app()


def _launch_gui() -> None:
    try:
        import customtkinter  # noqa: F401
    except ImportError:
        print(
            "Lỗi: Thư viện 'customtkinter' chưa được cài đặt.\n"
            "Chạy:  pip install customtkinter\n"
            "hoặc:  pip install -r requirements.txt"
        )
        sys.exit(1)

    from gui.app import launch_gui
    launch_gui()


if __name__ == "__main__":
    main()

