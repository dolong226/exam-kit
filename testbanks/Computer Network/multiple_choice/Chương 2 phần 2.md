# Bộ câu hỏi trắc nghiệm - Chapter 2: Application Layer



## PHẦN 2 – THE WEB AND HTTP (Section 2.2)

### Lý thuyết

**Câu 31.** HTTP (HyperText Transfer Protocol) sử dụng transport protocol nào?

A. UDP  
B. TCP  
C. SSL  
D. IP  

**Đáp án: B**  
*Giải thích: HTTP sử dụng TCP làm underlying transport protocol.*

---

**Câu 32.** Tại sao HTTP được gọi là "stateless protocol"?

A. HTTP không có header  
B. HTTP server không lưu bất kỳ thông tin trạng thái nào về clients  
C. HTTP không dùng cookies  
D. HTTP không có response code  

**Đáp án: B**  
*Giải thích: HTTP server không maintain state information về clients. Nếu client request cùng object hai lần, server gửi lại như thể lần đầu tiên.*

---

**Câu 33.** Non-persistent HTTP connections có đặc điểm gì?

A. Một TCP connection phục vụ nhiều HTTP requests  
B. Mỗi TCP connection chỉ truyền đúng một request/response, sau đó đóng  
C. HTTP requests được gửi mà không cần TCP connection  
D. Server giữ connection mở vô thời hạn  

**Đáp án: B**  
*Giải thích: Trong non-persistent connections, mỗi TCP connection được đóng sau khi server gửi xong object. Mỗi connection chỉ transport đúng một request và một response.*

---

**Câu 34.** RTT (Round-Trip Time) được định nghĩa là gì?

A. Thời gian để server xử lý một request  
B. Thời gian để một packet nhỏ đi từ client đến server và quay lại  
C. Thời gian để truyền toàn bộ file  
D. Thời gian để thiết lập TCP connection  

**Đáp án: B**  
*Giải thích: RTT là thời gian để một small packet đi từ client đến server rồi quay lại client, bao gồm propagation, queuing, và processing delays.*

---

**Câu 35.** Khi dùng non-persistent HTTP để lấy một trang web có base HTML và 10 JPEG, tổng thời gian response xấp xỉ là bao nhiêu (cho base HTML file)?

A. 1 RTT + transmission time  
B. 2 RTT + transmission time  
C. 3 RTT + transmission time  
D. Chỉ transmission time  

**Đáp án: B**  
*Giải thích: 1 RTT cho TCP three-way handshake (first two parts) + 1 RTT cho HTTP request/response = 2 RTT + file transmission time.*

---

**Câu 36.** Persistent HTTP connections với pipelining có ưu điểm gì so với non-persistent?

A. Sử dụng ít memory hơn  
B. Cho phép nhiều requests được gửi liên tiếp trên cùng một TCP connection mà không cần chờ replies, giảm số RTT cần thiết  
C. Encryption tốt hơn  
D. Tương thích với nhiều server hơn  

**Đáp án: B**  
*Giải thích: Persistent connections tránh overhead của việc establish new TCP connection cho mỗi object. Pipelining cho phép gửi multiple requests back-to-back mà không chờ replies.*

---

**Câu 37.** Trong HTTP request message, dòng đầu tiên được gọi là gì và chứa những gì?

A. Header line – chứa cookie information  
B. Request line – chứa method field, URL field, và HTTP version field  
C. Status line – chứa status code và phrase  
D. Entity body – chứa dữ liệu được gửi  

**Đáp án: B**  
*Giải thích: Dòng đầu của HTTP request là request line, gồm: method (GET/POST/HEAD/PUT/DELETE), URL, và HTTP version.*

---

**Câu 38.** HTTP method nào được dùng để gửi form data với data được đặt trong entity body?

A. GET  
B. HEAD  
C. POST  
D. PUT  

**Đáp án: C**  
*Giải thích: POST method đặt user-entered data vào entity body. GET cũng có thể gửi form data nhưng append vào URL.*

---

**Câu 39.** HTTP status code "304 Not Modified" có ý nghĩa gì?

A. File đã bị xóa khỏi server  
B. Object không thay đổi kể từ lần cached; client/cache có thể dùng bản cached  
C. Server không hỗ trợ phiên bản HTTP được yêu cầu  
D. Request có lỗi cú pháp  

**Đáp án: B**  
*Giải thích: 304 Not Modified được trả về khi conditional GET và object chưa thay đổi. Server không gửi object trong response body, tiết kiệm bandwidth.*

---

**Câu 40.** Cookie technology bao gồm những components nào?

A. Chỉ cookie file trên client  
B. Cookie header trong HTTP response, cookie header trong HTTP request, cookie file trên end system, và back-end database tại Web site  
C. Cookie file và session ID  
D. Chỉ server-side database  

**Đáp án: B**  
*Giải thích: Cookie technology gồm 4 components: (1) Set-cookie header trong response, (2) cookie header trong request, (3) cookie file trên client, (4) back-end database tại Web site.*

---

**Câu 41.** Web cache (proxy server) đóng vai trò gì trong mạng?

A. Chỉ là server  
B. Chỉ là client  
C. Vừa là server (với browsers) vừa là client (với origin servers)  
D. Là trung gian không có vai trò lưu trữ  

**Đáp án: C**  
*Giải thích: Web cache vừa là server khi nhận requests từ và gửi responses cho browsers, vừa là client khi gửi requests đến và nhận responses từ origin servers.*

---

**Câu 42.** Conditional GET là gì và dùng để làm gì?

A. GET request chỉ dùng để lấy hình ảnh  
B. GET request kèm theo If-Modified-Since header để kiểm tra xem cached object có còn up-to-date không  
C. GET request yêu cầu xác thực người dùng  
D. GET request với điều kiện về bandwidth  

**Đáp án: B**  
*Giải thích: Conditional GET gồm GET method + If-Modified-Since header. Nếu object chưa thay đổi kể từ ngày đó, server trả về 304 Not Modified (không kèm object), tiết kiệm bandwidth.*

---

**Câu 43.** HTTP status code "404 Not Found" có nghĩa là gì?

A. Server không hỗ trợ HTTP version được yêu cầu  
B. Request không được server hiểu  
C. Requested document không tồn tại trên server  
D. Object đã được chuyển đến URL mới  

**Đáp án: C**  
*Giải thích: 404 Not Found nghĩa là server không tìm thấy requested document.*

---

**Câu 44.** Header line "Host:" trong HTTP request có tác dụng gì?

A. Chỉ định địa chỉ IP của client  
B. Chỉ định hostname của server chứa object, cần thiết cho Web proxy caches  
C. Xác định loại browser của client  
D. Chỉ định ngôn ngữ ưa thích  

**Đáp án: B**  
*Giải thích: Host header chỉ định hostname của server chứa object. Dù đã có TCP connection, thông tin này cần thiết đặc biệt cho Web proxy caches.*

---

**Câu 45.** HTTP method HEAD được dùng để làm gì?

A. Gửi data lên server  
B. Lấy HTML headers của trang  
C. Nhận HTTP response message nhưng không có requested object trong body – thường dùng để debug  
D. Xóa object trên server  

**Đáp án: C**  
*Giải thích: HEAD method giống GET nhưng server không include object trong response. Thường dùng bởi application developers để debug.*

---

### Vận dụng

**Câu 46.** Một trang web có base HTML file và 5 JPEG images, tất cả trên cùng một server. Dùng non-persistent HTTP (serial), cần tổng cộng bao nhiêu TCP connections?

A. 1  
B. 5  
C. 6  
D. 11  

**Đáp án: C**  
*Giải thích: 1 connection cho base HTML + 5 connections cho 5 JPEG = 6 TCP connections tổng cộng.*

---

**Câu 47.** Một Web cache có hit rate 0.4. 40% requests được phục vụ bởi cache với delay 10ms, 60% từ origin server với delay 2.01 giây. Average delay là bao nhiêu?

A. Khoảng 0.4 giây  
B. Khoảng 1.2 giây  
C. Khoảng 2 giây  
D. Khoảng 0.6 giây  

**Đáp án: B**  
*Giải thích: 0.4 × 0.01s + 0.6 × 2.01s = 0.004 + 1.206 ≈ 1.21 giây, xấp xỉ 1.2 giây.*

---

**Câu 48.** Một institutional network có access link 15 Mbps, average object size 1 Mbit, request rate 15 requests/sec. Traffic intensity trên access link là bao nhiêu?

A. 0.15  
B. 0.5  
C. 1.0  
D. 1.5  

**Đáp án: C**  
*Giải thích: Traffic intensity = (15 requests/sec × 1 Mbit) / 15 Mbps = 15/15 = 1.0. Intensity = 1 nghĩa là delay tăng vô hạn.*

---

**Câu 49.** Khi user Susan lần đầu truy cập Amazon.com, server tạo ra và gán gì cho Susan?

A. Một username và password  
B. Một unique identification number, tạo entry trong database, gửi Set-cookie header  
C. Một session token tạm thời  
D. Một IP address riêng  

**Đáp án: B**  
*Giải thích: Server tạo unique ID, tạo entry trong back-end database, rồi gửi Set-cookie header trong HTTP response chứa ID đó.*

---

**Câu 50.** Tại sao Web caching có thể giúp cải thiện performance mà không cần upgrade access link?

A. Cache làm giảm số lượng TCP connections  
B. Cache giảm traffic trên access link, giảm traffic intensity và do đó giảm queuing delay  
C. Cache tăng tốc độ xử lý của server  
D. Cache nén dữ liệu trước khi truyền  

**Đáp án: B**  
*Giải thích: Với hit rate đáng kể, chỉ một phần requests cần đi qua access link, giảm traffic intensity xuống dưới 1.0 và giảm delay đáng kể.*

---

**Câu 51.** Một browser gửi request: "GET /page.html HTTP/1.1" kèm "Connection: close". Điều này nghĩa là gì?

A. Browser yêu cầu persistent connection  
B. Browser yêu cầu server đóng TCP connection sau khi gửi xong object (non-persistent)  
C. Browser muốn mã hóa kết nối  
D. Browser yêu cầu server compress response  

**Đáp án: B**  
*Giải thích: Header "Connection: close" cho server biết browser muốn non-persistent connection; server sẽ đóng TCP connection sau khi gửi xong requested object.*

---

**Câu 52.** Cookie có thể bị coi là "invasion of privacy" vì lý do nào?

A. Cookie làm chậm tốc độ browser  
B. Kết hợp cookies và user-supplied information, Web site có thể biết nhiều về user và bán thông tin cho bên thứ ba  
C. Cookie chiếm nhiều dung lượng ổ đĩa  
D. Cookie có thể chứa virus  

**Đáp án: B**  
*Giải thích: Web site dùng cookies kết hợp với account information có thể track detailed behavior của user và tiềm ẩn nguy cơ bán thông tin đó cho third parties.*

---

**Câu 53.** Content Distribution Networks (CDNs) như Akamai hoạt động dựa trên nguyên lý gì?

A. Tập trung tất cả content vào một server mạnh  
B. Cài đặt nhiều geographically distributed caches khắp Internet để localize traffic  
C. Compress content để giảm bandwidth  
D. Sử dụng P2P để phân phối content  

**Đáp án: B**  
*Giải thích: CDN cài nhiều caches phân tán địa lý khắp Internet, giúp serve content từ location gần user nhất, giảm latency và localize traffic.*

---

**Câu 54.** Trong conditional GET, giá trị của If-Modified-Since header phải bằng gì?

A. Ngày hiện tại  
B. Ngày cache lưu object  
C. Giá trị Last-Modified header từ response trước đó của server  
D. Ngày user truy cập lần đầu  

**Đáp án: C**  
*Giải thích: Cache gửi If-Modified-Since với giá trị chính xác bằng Last-Modified header mà server đã gửi trước đó, để server biết version nào cache đang giữ.*

---

### Vận dụng cao

**Câu 55.** Institutional network có LAN 100 Mbps, access link 15 Mbps. Tính traffic intensity trên LAN nếu avg object size 1 Mbit, request rate 15 req/sec:

A. 0.01  
B. 0.15  
C. 1.0  
D. 15  

**Đáp án: B**  
*Giải thích: (15 req/s × 1 Mbit) / 100 Mbps = 15/100 = 0.15. Traffic intensity 0.15 trên LAN chỉ tạo vài chục ms delay, có thể bỏ qua.*

---

**Câu 56.** Tại sao stateless nature của HTTP làm cho Web servers có hiệu suất cao hơn?

A. Stateless giúp servers không cần authenticate users  
B. Không cần duy trì state về từng client giúp thiết kế server đơn giản hơn và cho phép handle hàng ngàn concurrent TCP connections  
C. Stateless giúp tăng security  
D. Stateless giúp servers compress dữ liệu tốt hơn  

**Đáp án: B**  
*Giải thích: Stateless design đơn giản hóa server design và cho phép engineers phát triển high-performance servers có thể xử lý hàng ngàn simultaneous connections mà không cần track state của từng client.*

---

**Câu 57.** Khi cookie kết hợp với user account information (tên, địa chỉ, credit card), điều gì có thể xảy ra từ góc độ business?

A. Website có thể cung cấp one-click shopping vì đã có đủ thông tin; đây là ví dụ về session layer được tạo trên HTTP stateless  
B. Website phải hỏi lại thông tin mỗi lần truy cập  
C. Website không thể kết hợp hai loại thông tin này  
D. Cookie sẽ bị xóa ngay khi user đăng nhập  

**Đáp án: A**  
*Giải thích: Kết hợp cookie ID với user account tạo nên user session layer trên HTTP stateless. Website biết user là ai và có thể enable features như one-click shopping.*

---

**Câu 58.** Nếu Web cache hit rate tăng từ 0.4 lên 0.7, và delay từ cache là 10ms, delay từ Internet là 2 giây, thì average delay thay đổi như thế nào?

A. Tăng  
B. Giảm từ ~1.2s xuống còn ~0.6s  
C. Không thay đổi  
D. Giảm từ ~1.2s xuống còn ~0.1s  

**Đáp án: B**  
*Giải thích: Với hit rate 0.7: 0.7×0.01 + 0.3×2.01 ≈ 0.007 + 0.603 = 0.61s. So với hit rate 0.4: ~1.21s. Tăng hit rate giảm đáng kể average delay.*

---

## PHẦN 3 – FILE TRANSFER: FTP (Section 2.3)

### Lý thuyết

**Câu 59.** FTP khác HTTP ở điểm đặc biệt nào về cách sử dụng TCP connections?

A. FTP dùng UDP, HTTP dùng TCP  
B. FTP dùng hai parallel TCP connections: một control connection và một data connection  
C. FTP không dùng TCP  
D. HTTP dùng hai connections, FTP chỉ dùng một  

**Đáp án: B**  
*Giải thích: FTP sử dụng 2 parallel TCP connections: control connection (port 21) cho commands/replies, và data connection (port 20) cho actual file transfer.*

---

**Câu 60.** Thuật ngữ "out-of-band" trong FTP có nghĩa là gì?

A. FTP truyền dữ liệu ngoài phạm vi mạng  
B. FTP gửi control information trên một connection riêng biệt với data connection  
C. FTP không sử dụng TCP  
D. FTP truyền dữ liệu mà không cần authentication  

**Đáp án: B**  
*Giải thích: FTP gửi control info (commands) trên control connection riêng biệt với data connection. Ngược lại, HTTP gửi control info "in-band" trong cùng connection với dữ liệu.*

---

**Câu 61.** FTP control connection sử dụng port number nào và data connection sử dụng port nào?

A. Control: port 80, Data: port 443  
B. Control: port 21, Data: port 20  
C. Control: port 25, Data: port 110  
D. Control: port 20, Data: port 21  

**Đáp án: B**  
*Giải thích: FTP control connection dùng port 21, data connection dùng port 20.*

---

**Câu 62.** Tại sao FTP bị giới hạn số sessions đồng thời so với HTTP?

A. FTP server có phần cứng kém hơn  
B. FTP server phải maintain state về từng user (current directory, account association), làm hạn chế số sessions đồng thời  
C. FTP dùng quá nhiều bandwidth  
D. FTP không hỗ trợ parallel connections  

**Đáp án: B**  
*Giải thích: FTP server phải track state cho mỗi session (user account, current directory), việc này constrains tổng số sessions có thể maintain. HTTP thì stateless nên không bị giới hạn này.*

---

**Câu 63.** FTP command "RETR filename" dùng để làm gì?

A. Lưu file lên remote host  
B. Liệt kê files trong directory  
C. Lấy (download) file từ remote host  
D. Xóa file trên remote host  

**Đáp án: C**  
*Giải thích: RETR (retrieve) dùng để lấy file từ current directory của remote host, gây ra việc remote host initiate data connection và gửi file.*

---

**Câu 64.** FTP data connections là persistent hay non-persistent?

A. Persistent – một data connection cho toàn bộ session  
B. Non-persistent – một data connection cho mỗi file transfer, sau đó đóng  
C. Depends on server configuration  
D. Persistent với pipelining  

**Đáp án: B**  
*Giải thích: FTP gửi đúng một file trên một data connection rồi đóng. Nếu transfer file khác, một data connection mới được tạo. Control connection thì vẫn mở suốt session.*

---

### Vận dụng

**Câu 65.** Một user FTP muốn chuyển 5 files. Sẽ có bao nhiêu data connections được tạo và bao nhiêu control connections?

A. 5 data connections và 5 control connections  
B. 5 data connections và 1 control connection  
C. 1 data connection và 1 control connection  
D. 1 data connection và 5 control connections  

**Đáp án: B**  
*Giải thích: FTP dùng 1 control connection suốt session, nhưng tạo 1 data connection cho mỗi file. 5 files = 5 data connections, 1 control connection.*

---

**Câu 66.** So sánh FTP và HTTP: cả hai đều là file transfer protocols dùng TCP, nhưng khác nhau điểm nào quan trọng nhất?

A. HTTP không secure, FTP thì secure  
B. HTTP gửi control info in-band (cùng connection với data); FTP gửi control info out-of-band (connection riêng)  
C. HTTP hỗ trợ các file lớn hơn FTP  
D. FTP nhanh hơn HTTP vì dùng parallel connections  

**Đáp án: B**  
*Giải thích: Khác biệt nổi bật nhất: HTTP in-band (request/response header cùng connection với data), FTP out-of-band (control connection riêng với data connection). FTP cũng stateful, HTTP thì stateless.*

---

### Vận dụng cao

**Câu 67.** FTP server phải maintain state "user's current directory". Điều này tạo ra hệ quả gì so với HTTP?

A. FTP nhanh hơn HTTP  
B. FTP có thể handle ít concurrent sessions hơn HTTP vì overhead của state management, và không scale tốt bằng HTTP với nhiều concurrent users  
C. FTP secure hơn HTTP  
D. FTP không cần authentication  

**Đáp án: B**  
*Giải thích: State maintenance cho mỗi session tốn resources (memory, processing). HTTP stateless nên một server có thể handle hàng ngàn concurrent connections; FTP stateful nên bị giới hạn.*

---
