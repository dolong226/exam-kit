import yaml
from pathlib import Path
from pydantic import ValidationError
from typing import Union
from .models import TestBank

def parse_testbank(file_path: Union[str, Path]) -> TestBank:
    """
    Đọc, kiểm tra cú pháp YAML và validate schema bằng Pydantic.
    Trả về một đối tượng TestBank.
    """
    path = Path(file_path)
    
    # 1. Kiểm tra xem file có tồn tại không
    if not path.is_file():
        raise FileNotFoundError(f"Không tìm thấy file: {path.absolute()}")

    # 2. Đọc file và kiểm tra cú pháp YAML
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ValueError(f"Lỗi cú pháp YAML trong file '{path.name}':\n{e}")

    # Kiểm tra nếu file rỗng hoặc không chứa dữ liệu hợp lệ
    if not data:
        raise ValueError(f"File '{path.name}' rỗng hoặc không chứa dữ liệu hợp lệ.")

    # 3. Validate dữ liệu bằng Pydantic Model
    try:
        return TestBank(**data)
    except ValidationError as e:
        raise ValueError(f"Dữ liệu không khớp chuẩn schema (Models) trong file '{path.name}':\n{e}")