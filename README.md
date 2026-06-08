# StudyKit 

Bộ công cụ học tập hỗ trợ hai chế độ: **trắc nghiệm** và **tự luận**, với giao diện **CLI** và **GUI**.

## Tính năng

- **Trắc nghiệm (Quiz)**: Import file test bank → làm bài → xem điểm → xuất báo cáo câu sai
- **Tự luận (Essay)**: Import câu hỏi + đáp án → AI chấm điểm → xem kết quả *(sắp ra)*
- **CLI**: Giao diện terminal đẹp với Rich
- **GUI**: Giao diện đồ họa với CustomTkinter *(sắp ra)*

## Cài đặt nhanh

```bash
# Clone repo
git clone <repo-url>
cd studykit

# Tạo virtual environment
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows

# Cài đặt
pip install -e .               # chỉ CLI + quiz
pip install -e ".[gui]"        # thêm GUI
pip install -e ".[all]"        # tất cả tính năng
```

## Sử dụng CLI

```bash
# Xem danh sách test bank
studykit list

# Làm quiz (hiện đáp án + giải thích sau mỗi câu)
studykit quiz testbanks/sample_quiz.yaml --show-answer

# Làm quiz (chỉ xem kết quả cuối)
studykit quiz testbanks/sample_quiz.yaml

# Làm quiz với số câu hỏi giới hạn và trộn ngẫu nhiên
studykit quiz testbanks/sample_quiz.yaml --limit 10 --shuffle
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

## Roadmap

| Version |     Tính năng     |
|---------|-------------------|
| v1      | CLI + Trắc nghiệm |
| v2      | GUI + Trắc nghiệm |
| v3      | Tự luận + AI chấm |