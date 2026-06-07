import os
import sys

# Lấy đường dẫn tuyệt đối của thư mục gốc (exam-kit)
root_dir = os.path.dirname(os.path.abspath(__file__))

# Định nghĩa đường dẫn tới thư mục studykit (nơi chứa core và cli)
studykit_dir = os.path.join(root_dir, "studykit")

# Ép Python phải quét vào bên trong thư mục studykit trước
if os.path.exists(studykit_dir):
    sys.path.insert(0, studykit_dir)
sys.path.insert(0, root_dir)

# Bây giờ import sẽ chạy mượt mà vì Python đã biết studykit ở đâu
from cli.app import app as cli_app


def main() -> None:
    """Điểm khởi chạy chính của ứng dụng."""
    cli_app()


if __name__ == "__main__":
    main()