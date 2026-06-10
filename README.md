# StudyKit 

Bộ công cụ học tập hỗ trợ hai chế độ: **trắc nghiệm** và **tự luận**, với giao diện **CLI** và **GUI**.

## Installation

```bash
# Clone repository
git clone https://github.com/dolong226/exam-kit.git

# Move into project directory
cd exam-kit

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Cấu trúc test bank

Test bank là file YAML hoặc JSON đặt trong thư mục `testbanks/`.  
Xem hướng dẫn chi tiết tại [`testbanks/README.md`](testbanks/README.md).

## Cấu trúc thư mục

```
studykit/
├── studykit/           # Package chính
│   ├── core/           # Logic nghiệp vụ (parser, engine, models)
│   ├── cli/            # Giao diện CLI (Typer + Rich)
│   └── gui/            # Giao diện GUI (CustomTkinter)
├── testbanks/          # Thư mục chứa file câu hỏi
│   ├── README.md       # Hướng dẫn tạo test bank
│   └── example/        # Ví dụ mẫu
├── outputs/            # File báo cáo câu sai xuất ra
├── tests/              # Unit tests
├── config/             # Cấu hình ứng dụng
└── main.py             # Entry point dự phòng
```
