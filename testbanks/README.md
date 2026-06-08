# Thư mục Test Banks

Thư mục này chứa các bộ đề (test bank) được sử dụng trong ứng dụng. Hệ thống sẽ tự động quét thư mục này để nạp dữ liệu mỗi khi chạy.

## Định dạng tệp
Tất cả các bộ đề phải được viết bằng định dạng **YAML** (`.yaml` hoặc `.yml`) để đảm bảo tính dễ đọc và dễ chỉnh sửa.

## Cấu trúc Schema (Theo `core/models.py`)

Một file test bank hợp lệ cần có các trường sau:

- `title` (Bắt buộc): Tên của bộ đề.
- `description` (Tùy chọn): Mô tả ngắn gọn.
- `questions` (Bắt buộc): Danh sách các câu hỏi. Mỗi câu hỏi bao gồm:
  - `id` (Bắt buộc): Mã duy nhất của câu hỏi (dùng để theo dõi kết quả).
  - `type` (Tùy chọn): `multiple_choice` (mặc định) hoặc `essay`.
  - `content` (Bắt buộc): Nội dung câu hỏi.
  - `choices` (Bắt buộc nếu là trắc nghiệm): Danh sách các lựa chọn.
  - `correct_answer` (Bắt buộc): 
    - Với trắc nghiệm: Là **số thứ tự (index)** của đáp án đúng, bắt đầu từ `0`.
    - Với tự luận: Là chuỗi văn bản chứa đáp án/dàn ý mẫu.
  - `explanation` (Tùy chọn): Giải thích chi tiết cho đáp án.

## Lưu ý về hiển thị
- Nội dung văn bản (`content`, `explanation`) hỗ trợ định dạng nhiều dòng trong YAML bằng cách dùng dấu `|` hoặc `>`.
- Có thể chèn trực tiếp các ký hiệu toán học hoặc mã HTML/CSS vào nội dung. Ở chế độ GUI sau này, ứng dụng sẽ được cấu hình để render các định dạng này nếu cần.