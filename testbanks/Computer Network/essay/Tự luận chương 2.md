

# === Định dạng Tự luận ===


# Chương 2: Tầng ứng dụng

## Câu 1. Liệt kê năm ứng dụng Internet không độc quyền và các giao thức tầng ứng dụng mà chúng sử dụng.

Web: HTTP; truyền file: FTTP; đăng nhập từ xa: Telnet; Network News: NTTP; email: SMTP.

## Câu 2. Sự khác biệt giữa kiến trúc mạng (network architecture) và kiến trúc ứng dụng (application architecture) là gì?

Kiến trúc mạng đề cập đến việc tổ chức quá trình giao tiếp thành các tầng (ví dụ: kiến trúc Internet 5 tầng). Mặt khác, kiến trúc ứng dụng thiết kế bởi nhà phát triển ứng dụng và quy định cấu trúc tổng thể của ứng dụng (ví dụ: client-server hoặc P2P).

## Câu 3. Trong một phiên giao tiếp giữa một cặp tiến trình, tiến trình nào là client và tiến trình nào là server?

Tiến trình khởi tạo giao tiếp là client; tiến trình chờ đợi liên hệ là server.

## Câu 4. Đối với ứng dụng chia sẻ file P2P, bạn có đồng ý với nhận định: Không có khái niệm phía client và phía server trong một phiên giao tiếp không?

Không. Mọi phiên giao tiếp đều có phía client và phía server. Trong ứng dụng chia sẻ file P2P, peer đang nhận file thường là client và peer đang gửi file thường là server.

## Câu 5. Thông tin nào được sử dụng bởi một tiến trình chạy trên một host để xác định một tiến trình chạy trên một host khác?

Địa chỉ IP của host đích và port number của socket đích.

## Câu 6. Giả sử bạn muốn thực hiện một giao dịch từ một client từ xa đến một server càng nhành càng tốt. Bạn sẽ sử dụng UDP hay TCP? Tại sao?

Sẽ sử dụng UDP. Vì UDP là giao thức hướng không kết nối (connectionless), nó tránh được độ trễ phát sinh do quá trình bắt tay ba bước của TCP, giúp dữ liệu được gửi đi nhanh hơn ngay lập tức.

## Câu 8. Liệt kê bốn lớp dịch vụ chính mà một giao thức tầng giao vận có thể cung cấp. Đối với mỗi lớp dịch vụ, chỉ ra TCP hoặc UDP (hoặc cả hai) có cung cấp dịch vụ đó hay không.

- Truyền dữ liệu đáng tin cậy (TCP có, UDP không).
- Đảm bảo thông lượng (TCP, UDP đều không).
- Đảm bảo thời gian (TCP, UDP đều không).
- Bảo mật (Cả TCP và UDP đều không tích hợp sẵn, nhưng TCP có thể được tăng cường với SSL/TLS_.

## Câu 10. Giao thức bắt tay (handshaking protocol) là gì?

Một giao thức sử dụng bắt tay nếu hai thực thể giao tiếp trao đổi các gói điều khiển trước khi thực sự gửi dữ liệu cho nhau. SMTP sử dụng bắt tay ở tầng ứng dụng, trong khi HTTP thì không.

## Câu 11. Tại sao HTTP, FTP, SMTP và POP3 chạy trên TCP thay vì UDP?

Nhắc lại:
HTTP (HyperText Transfer Protocol)
- Là giao thức dùng để truyền tải các trang web giữa trình duyệt và máy chủ web.
- Cách hoạt động:
    - Khi truy cập: https://www.google.com
    - Trình duyệt gửi yêu cầu:
        - GET / HTTP/1.1
        - Host: google.com
    - Máy chủ trả về:
        - HTTP/1.1 200 OK
        - Content-Type: text/html
- Đặc điểm:
    - Hoạt động theo mô hình Client-Server.
    - Stateless (không nhớ trạng thái giữa các lần gửi yêu cầu).
    - Dùng TCP làm giao thức vận chuyển.
    - Mặc định cổng: HTTP (80), HTTPS (443).
- Các phương thức phổ biến: GET (lấy dữ liệu), POST (gửi dữ liệu), PUT (cập nhật dữ liệu), DELETE (xóa dữ liệu).
FTP (File Transfer Protocol)
- FTP được thiết kế để truyền tệp giữa hai máy tính.
- Cách hoạt động: FTP sử dụng hai kết nối TCP.
    - Control Connection: dùng gửi lệnh.
        - USER alice
        - PASS 123456
    - Data connection: Truyền dữ liệu thực tế.
        - RETR report.pdf
- Cổng FTP: control (21), data (20).
- Một số lệnh: USER (Tên đăng nhập), PASS, LIST (danh sách file), RETR (Retrive: tải xuống file), STOR (tải lên file), QUIT.
- Nhược điểm:
    - FTP truyền Username, Password, Dữ liệu dưới dạng plaintext, kẻ tấn công có thể nghe lén.
    - Ngày nay thường dùng: SFTP, FTPS.
SMTP (Simple Mail Transfer Protocol)
- Dùng để gửi email, không dùng để đọc.
- Luồng hoạt động: Người gửi → SMTP Server Gmail → SMTP Server người nhận → Hộp thư người nhận.
- Port 25.
- Một phiên SMTP đơn giản:
    - Client: HELO mail.com
    - Server: 250 OK
    - Client: MAIL FROM:<abc@gmail.com>
    - Server: 250 OK
    - Client: RCPT TO :<xyz@yahoo.com>
    - Server: 250 OK
    - Client: DATA
    - Client: ………..
- Đặc điểm:
    - Push protocol (đẩy thư đi).
    - Dùng TCP.
    - Không dùng để đọc email.
POP3 (Post Office Protocol Version 3)
- Dùng để nhận email từ mail server về máy người dùng.
- Luồng: Mail Server → POP3 → Outlook/Thunderbird.
- Port 110.
- Quy trình:
    - USER alice
    - PASS 123456
    - STAT
    - RETR 1
    - DELE 1
- Nhược điểm:  Sau khi tải thư có thể bị xóa trên server; khó đồng bộ nhiều thiết bị.
POP3 và SMTP phối hợp như nào?
- Khi gửi email: Người gửi → SMTP → Mail Server → SMTP → Mail Server người nhận.
- Khi nhận email: Mail Server → POP3 → Người nhận
POP3 và IMAP?
- IMAP ra đời để khắc phục hạn chế lớn nhất của POP3: email ngày nay có thể được đọc trên nhiều thiết bị.
- IMAP (Internet Message Access Protocol) là giao thức cho phép truy cập và quản lý email trực tiếp trên mail server.
- Khác với POP3, IMAP không mặc định tải toàn bộ thư về máy rồi xóa trên server.
- Port: IMAP (143), IMAPS (993). Ngày nay hầu hết dùng 993.
Trả lời:
Các ứng dụng gắn với giao thức này yêu cầu tất cả dữ liệu ứng dụng phải được nhận theo đúng thứ tự và không bị mất mát. TCP cung cấp đảm bảo tính nguyên vẹn dữ liệu.

## Câu 12. Xem xét một trang web thương mai điện tử muốn lưu lại hồ sơ mua hàng của từng khách hàng. Mô tả cách thực hiện điều này bằng cookie.

Khi người dùng truy cập trang web lần đầu, trang web trả về một số cookie. Số cookie này được lưu trữ trên host của người dùng và do trình duyệt quản lý. Trong mỗi lần truy cập tiếp theo, trình duyệt gửi lại số cookie đó cho trang web. Do đó trang web biết khi nào người dùng này đang truy cập trang web.

## Câu 13. Mô tả cách Web caching (bộ nhớ cache Web) có thể làm giảm độ trễ trong việc nhận một đối tượng được yêu cầu. Web caching sẽ làm giảm độ trễ cho tất cả các đối tượng được người dùng yêu cầu hay chỉ một số đối tượng? Tại sao?

Nhắc lại:
Web Caching là kỹ thuật lưu tạm dữ liệu web đã truy cập trước đó để lần sau không cần lấy lại từ server gốc, giúp tăng tốc độ truy cập và giảm tải mạng.
Cache Hit và Cache Miss
304 Not Modified: Không cần lấy dữ liệu mới vì không có chỉnh sửa.
Trả lời: Web caching có thể mang nội dung mong muốn đến gần người dùng hơn, có thể là nằm trên cùng mạng LAN mà host của người dùng được kết nối. Web caching có thể làm giảm độ trễ cho tất cả các đối tượng, ngay cả những đối tượng không được lưu trong cache, vì caching làm giảm lưu lượng giao thông trên các đường truyền.

## Câu 15. Tại sao nói rằng FTP gửi thông tin điều khiển “out-of-band” (ngoài băng tần)?

FTP sử dụng hai kết nối TCP song song, một kết nối để gửi thông tin điều khiển (như yêu cầu truyền file) và một kết nối khác để thực sự truyền file. Bởi vì thông tin điều khiển không được gửi qua cùng một kết nối để truyền file, nên FTP gửi thông tin điều khiển “out-of-band”.

## Câu 16. Giả sử Alice, với một tài khoản email trên nền web (như Hotmail hoặc Gmail), gửi một tin nhắn cho Bob, người truy cập thư từ mail server của mình bằng POP3. Thảo luận cách tin nhắn đi từ host của Alice đến host của Bob. Hãy chắc chắn liệt kê chuỗi các giao thức tầng ứng dụng được sử dụng để di chuyển tin nhắn giữa hai host.

Host của Alice → HTTP → Mail server của Alice → SMTP → Mail server của Bob → POP3 → Host của Bob.

## Câu 18. ** Từ góc độ người dùng, sự khác biệt giữa chế độ "tải xuống và xóa" (download-and-delete) và "tải xuống và giữ lại" (download-and-keep) trong POP3 là gì?

** Với chế độ tải xuống và xóa, sau khi người dùng lấy tin nhắn từ POP server, các tin nhắn đó sẽ bị xóa. Điều này gây vấn đề cho người dùng hay di chuyển, người muốn truy cập tin nhắn từ nhiều máy khác nhau (PC văn phòng, PC ở nhà, v.v.). Trong cấu hình tải xuống và giữ lại, tin nhắn không bị xóa sau khi người dùng lấy tin nhắn. Điều này cũng có thể bất tiện, vì mỗi lần người dùng lấy các tin nhắn đã lưu từ một máy tính mới, tất cả các tin nhắn chưa bị xóa sẽ được chuyển sang máy tính mới đó (bao gồm cả những tin nhắn rất cũ).

## Câu 26. ** Trong Phần 2.7, UDP server được mô tả chỉ cần 1 socket, trong khi TCP server cần 2 socket. Tại sao? Nếu TCP server hỗ trợ n kết nối đồng thời, mỗi kết nối từ một host client khác nhau, thì TCP server sẽ cần bao nhiêu socket?

** UDP server chỉ cần 1 socket vì UDP là giao thức không trạng thái/không kết nối; tất cả dữ liệu từ vô số các client khác nhau đều gửi chung vào một cổng (socket) duy nhất đó. TCP server cần 2 socket ban đầu vì TCP hướng kết nối: 1 socket dùng để thường trực lắng nghe (welcoming socket) và 1 socket dành riêng được tạo ra để phục vụ cho client vừa kết nối xong. Nếu hỗ trợ n kết nối đồng thời, TCP server sẽ cần tổng cộng n + 1 socket (1 socket lắng nghe chung và n socket phục vụ riêng biệt cho n client).

## Câu 27. ** Đối với ứng dụng client-server qua TCP, tại sao chương trình server phải được thực thi trước chương trình client? Đối với ứng dụng client-server qua UDP, tại sao chương trình client có thể được thực thi trước chương trình server?

** Với TCP, trước khi gửi được bất kỳ dữ liệu nào, client phải khởi tạo một phiên "bắt tay" (thiết lập kết nối) với server. Để việc bắt tay thành công, chương trình server buộc phải chạy trước để mở một socket đón đợi kết nối. Với UDP, hoàn toàn không có quá trình thiết lập kết nối nào cả. Client cứ việc đóng gói dữ liệu và đẩy vào mạng lưới gửi đến địa chỉ đích, không cần quan tâm server có đang chạy và sẵn sàng nhận hay không. Do đó client hoàn toàn có thể chạy trước (dù gói tin gửi đi có thể sẽ bị rớt/thất lạc nếu server chưa thực thi).

## Câu 28. Đúng hai sai.Một người dùng yêu cầu một trang Web bao gồm một đoạn văn bản và ba hình ảnh. Đối với trang này, client sẽ gửi một thông điệp yêu cầu (request) và nhận bốn thông điệp phản hồi (response). 

Sai
Persistent HTTP và non-persistent HTTP không khác nhau ở số lượng request. Chúng khác nhau ở số lượng kết nối TCP.
Ví dụ trang web gồm 4 đối tượng, client vẫn phải gửi 4 request và nhận 4 response trong cả 2 trường hợp.

## Câu 28. Đúng hai sai. Hai trang web riêng biệt có thể được gửi qua cùng một kết nối kiên trì (persistent connection).

Đúng. Đây là ưu điểm của persistent HTTP: nhiều đối tượng nằm trên cùng một server có thể được truyền tải qua một kết nối TCP duy nhất mà không cần đóng/mở liên tục.

## Câu 28. Đúng hai sai.Với kết nối không kiên trì giữa trình duyệt và origin server, một phân đoạn TCP (TCP segment) đơn lẻ có thể mang hai thông điệp yêu cầu HTTP Khác nhau.

Sai. Trong non-per connection, mỗi kết nối TCP chỉ phục vụ duy nhất một thông điệp yêu cầu và một thông điệp phản hồi, sau đó kết nối sẽ bị đóng lại. Do đó, một phân đoạn TCP không thể chứa hai yêu cầu HTTP khác nhau.

## Câu 28. Đúng hai sai.Dòng header  “Date:” trong response của HTTP cho biết thời điểm đối tượng trong response được sửa đổi lần cuối.

Sai. Dòng “Date:” biểu thị thời gian server tạo ra và gửi thông điệp phản hồi đó. Thời điểm đối tượng được sửa đổi lần cuối được biểu thị bằng dòng header Last-Modified:.

## Câu 28. Đúng hai sai.HTTP response không bao giờ có phần message body trống.

Sai. Có nhiều HTTP response có phần body trống, ví dụ như phản hồi có mã trạng thái 304 Not Modified hoặc 204 No Content.
