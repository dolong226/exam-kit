import os
import sys

root_dir = os.path.dirname(os.path.abspath(__file__))
studykit_dir = os.path.join(root_dir, "studykit")



def main() -> None:
    """
    Điểm khởi chạy chính.
    Khi chạy file exe, sẽ mở GUI ngay.
    """
    _launch_gui()


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

    from studykit.gui.app import launch_gui
    launch_gui()


if __name__ == "__main__":
    main()
