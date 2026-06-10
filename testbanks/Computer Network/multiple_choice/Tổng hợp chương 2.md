# Bộ câu hỏi trắc nghiệm - Chapter 2: Application Layer



## PHẦN 1 – PRINCIPLES OF NETWORK APPLICATIONS (Section 2.1)

### Lý thuyết

**Câu 1.** Trong lập trình network application, developer cần viết code chạy trên thành phần nào của mạng?

A. Routers và link-layer switches  
B. End systems (hosts)  
C. Cả end systems lẫn routers  
D. Chỉ trên servers chuyên dụng  

**Đáp án: B**  
*Giải thích: Developer chỉ cần viết software chạy trên các end systems. Network-core devices như routers không function ở application layer.*

---

**Câu 2.** Điểm khác biệt cơ bản giữa client-server architecture và P2P architecture là gì?

A. Client-server sử dụng TCP, P2P sử dụng UDP  
B. Client-server có server luôn bật và địa chỉ cố định; P2P không phụ thuộc (hoặc phụ thuộc rất ít) vào server chuyên dụng  
C. Client-server nhanh hơn P2P trong mọi trường hợp  
D. P2P không thể chia sẻ file, chỉ dùng để streaming  

**Đáp án: B**  
*Giải thích: Trong client-server, server luôn online với IP cố định. Trong P2P, các peer giao tiếp trực tiếp với nhau mà không qua server chuyên dụng.*

---

**Câu 3.** Trong ngữ cảnh của một communication session giữa hai process, process nào được gọi là "client"?

A. Process có địa chỉ IP cố định  
B. Process có khả năng xử lý nhiều request hơn  
C. Process khởi tạo giao tiếp (initiate the communication)  
D. Process nhận dữ liệu nhiều hơn  

**Đáp án: C**  
*Giải thích: Process khởi tạo kết nối ở đầu session được gọi là client; process chờ được liên hệ là server.*

---

**Câu 4.** Socket được định nghĩa là gì?

A. Địa chỉ IP kết hợp với port number  
B. Interface phần mềm giữa application layer và transport layer trong một host  
C. Một loại protocol để truyền dữ liệu  
D. Phần cứng kết nối máy tính với mạng  

**Đáp án: B**  
*Giải thích: Socket là software interface (cũng gọi là API) giữa application layer và transport layer; là "cánh cửa" để process gửi/nhận messages qua mạng.*

---

**Câu 5.** Để xác định một receiving process trên mạng Internet, cần hai thông tin nào?

A. Hostname và MAC address  
B. IP address của host và port number của process  
C. IP address và tên của application  
D. DNS name và bandwidth  

**Đáp án: B**  
*Giải thích: Cần IP address để xác định host và port number để xác định process/socket cụ thể đang chạy trên host đó.*

---

**Câu 6.** Web server thường sử dụng port number nào?

A. 25  
B. 53  
C. 80  
D. 110  

**Đáp án: C**  
*Giải thích: Port 80 là well-known port của HTTP (Web server). Port 25 là SMTP, 53 là DNS, 110 là POP3.*

---

**Câu 7.** Transport-layer protocol có thể cung cấp dịch vụ cho applications theo mấy chiều (dimensions)?

A. 2  
B. 3  
C. 4  
D. 5  

**Đáp án: C**  
*Giải thích: 4 chiều gồm: reliable data transfer, throughput, timing, và security.*

---

**Câu 8.** "Reliable data transfer" trong transport protocol có nghĩa là gì?

A. Dữ liệu được mã hóa trước khi gửi  
B. Dữ liệu được gửi với tốc độ đảm bảo  
C. Dữ liệu được đảm bảo đến đích chính xác và đầy đủ  
D. Dữ liệu được gửi trong thời gian giới hạn  

**Đáp án: C**  
*Giải thích: Reliable data transfer đảm bảo data gửi từ một đầu sẽ được nhận chính xác, đầy đủ ở đầu kia.*

---

**Câu 9.** Applications nào được gọi là "bandwidth-sensitive applications"?

A. Các ứng dụng chỉ cần ít băng thông  
B. Các ứng dụng yêu cầu throughput tối thiểu ở một mức cố định  
C. Các ứng dụng không quan tâm đến throughput  
D. Các ứng dụng sử dụng UDP  

**Đáp án: B**  
*Giải thích: Bandwidth-sensitive applications (như Internet telephony) cần throughput đảm bảo ở mức tối thiểu; nếu không đạt thì ứng dụng không hoạt động hiệu quả.*

---

**Câu 10.** TCP cung cấp những dịch vụ chính nào cho applications?

A. Connectionless service và unreliable data transfer  
B. Connection-oriented service và reliable data transfer  
C. Throughput guarantee và timing guarantee  
D. Encryption và data integrity  

**Đáp án: B**  
*Giải thích: TCP cung cấp connection-oriented service (handshaking trước khi truyền) và reliable data transfer (đảm bảo dữ liệu đến đúng và đủ).*

---

**Câu 11.** Điều nào sau đây mô tả đúng về UDP?

A. UDP có cơ chế handshaking trước khi truyền dữ liệu  
B. UDP đảm bảo dữ liệu được giao đúng thứ tự  
C. UDP là connectionless và cung cấp unreliable data transfer  
D. UDP có congestion-control mechanism  

**Đáp án: C**  
*Giải thích: UDP là connectionless (không handshaking), cung cấp unreliable data transfer và không có congestion control.*

---

**Câu 12.** Internet transport protocols hiện tại (TCP và UDP) KHÔNG cung cấp guarantees về điều gì?

A. Reliable data transfer  
B. Throughput và timing  
C. Connection establishment  
D. Error detection  

**Đáp án: B**  
*Giải thích: TCP và UDP không cung cấp throughput guarantees hay timing guarantees. TCP cung cấp reliability nhưng không đảm bảo tốc độ hay độ trễ.*

---

**Câu 13.** SSL (Secure Sockets Layer) thuộc về tầng nào?

A. Transport layer  
B. Network layer  
C. Application layer  
D. Link layer  

**Đáp án: C**  
*Giải thích: SSL là enhancement của TCP được implement ở application layer, không phải là transport protocol độc lập.*

---

**Câu 14.** Application-layer protocol định nghĩa những gì? (Chọn mô tả đầy đủ nhất)

A. Chỉ định dạng của messages  
B. Loại messages, syntax, semantics của các fields, và quy tắc gửi/nhận messages  
C. Cách routing packets qua mạng  
D. Cách mã hóa dữ liệu  

**Đáp án: B**  
*Giải thích: Application-layer protocol định nghĩa: types of messages, syntax, semantics của fields, và rules về khi nào/cách nào process gửi và respond to messages.*

---

**Câu 15.** Self-scalability của P2P architecture có nghĩa là gì?

A. P2P tự động cập nhật phần mềm  
B. Mỗi peer vừa tạo ra workload vừa thêm service capacity, nên hệ thống scale được mà không cần server infrastructure lớn  
C. P2P không cần ISP  
D. P2P tự động phát hiện và sửa lỗi  

**Đáp án: B**  
*Giải thích: Mỗi peer khi download cũng đồng thời upload cho peers khác, tạo ra khả năng tự mở rộng mà không tăng gánh nặng lên server tập trung.*

---

**Câu 16.** Tại sao P2P architecture gặp thách thức với "ISP Friendly"?

A. P2P không tương thích với các ISP lớn  
B. P2P chuyển upstream traffic từ server lên residential ISPs, gây stress cho ISPs vốn được thiết kế cho asymmetrical (nhiều downstream hơn upstream)  
C. ISP tính phí cao hơn cho P2P  
D. P2P yêu cầu bandwidth quá lớn từ ISP  

**Đáp án: B**  
*Giải thích: Residential ISPs được thiết kế cho asymmetrical bandwidth (nhiều downstream hơn upstream), nhưng P2P tạo ra nhiều upstream traffic từ clients, gây quá tải.*

---

**Câu 17.** Elastic applications là gì?

A. Ứng dụng yêu cầu throughput tối thiểu cố định  
B. Ứng dụng có thể sử dụng nhiều hoặc ít bandwidth tuỳ theo availability  
C. Ứng dụng chỉ chạy trên TCP  
D. Ứng dụng không cần reliable data transfer  

**Đáp án: B**  
*Giải thích: Elastic applications (như email, file transfer, web) hoạt động được với mức throughput bất kỳ; càng nhiều throughput càng tốt nhưng không yêu cầu tối thiểu.*

---

### Vận dụng

**Câu 18.** Trong P2P file sharing (như BitTorrent), khi Peer A download file từ Peer B, trong session đó:

A. Peer A là server, Peer B là client  
B. Peer A là client, Peer B là server  
C. Cả hai đều là client  
D. Cả hai đều là server  

**Đáp án: B**  
*Giải thích: Trong context của session này, Peer A đang download (yêu cầu), nên là client; Peer B đang upload (phục vụ), nên là server.*

---

**Câu 19.** Một developer đang xây dựng ứng dụng video streaming thời gian thực cần truyền với mức tối thiểu 10 kbps và chấp nhận mất một số gói tin. Nên chọn transport protocol nào?

A. TCP vì có reliable data transfer  
B. UDP vì không có congestion control, cho phép truyền ở tốc độ mong muốn và chấp nhận mất gói  
C. TCP vì có connection-oriented service  
D. UDP vì có timing guarantee  

**Đáp án: B**  
*Giải thích: Ứng dụng loss-tolerant và cần minimum rate nên dùng UDP để tránh overhead của TCP's congestion control. TCP sẽ throttle khi mạng tắc nghẽn.*

---

**Câu 20.** Một ứng dụng chuyển file tài chính cần đảm bảo không mất dữ liệu. Nên chọn protocol nào và tại sao?

A. UDP vì nhanh hơn  
B. TCP vì cung cấp reliable data transfer  
C. UDP vì ít overhead hơn  
D. Cả TCP và UDP đều phù hợp  

**Đáp án: B**  
*Giải thích: Ứng dụng tài chính là "no-loss" application, cần TCP's reliable data transfer để đảm bảo không mất, không lỗi, không trùng dữ liệu.*

---

**Câu 21.** Hai browsers trên hai máy tính khác nhau muốn giao tiếp trực tiếp với nhau trong một web application sử dụng client-server architecture. Điều này có thể không?

A. Có, hai browsers luôn giao tiếp trực tiếp  
B. Không, trong client-server architecture, clients không giao tiếp trực tiếp với nhau  
C. Có, nhưng chỉ qua port 80  
D. Không, vì HTTP không hỗ trợ  

**Đáp án: B**  
*Giải thích: Đặc điểm của client-server architecture là clients không giao tiếp trực tiếp với nhau; mọi giao tiếp đều qua server.*

---

**Câu 22.** Một process muốn gửi message đến process khác trên host có IP 192.168.1.10, đang chạy mail server. Destination address cần bao gồm gì?

A. Chỉ IP address: 192.168.1.10  
B. IP address 192.168.1.10 và port number 25  
C. IP address 192.168.1.10 và tên ứng dụng "SMTP"  
D. MAC address và port number  

**Đáp án: B**  
*Giải thích: Cần IP address để định danh host và port number (25 cho SMTP) để định danh process/socket. MAC address không dùng trong application layer.*

---

**Câu 23.** Skype ban đầu dùng UDP cho Internet telephony, nhưng thiết kế để fallback sang TCP khi cần. Lý do nào sau đây giải thích tại sao?

A. TCP nhanh hơn UDP  
B. Nhiều firewalls block UDP traffic, nên cần TCP như backup  
C. TCP cung cấp timing guarantees tốt hơn  
D. UDP không hỗ trợ encryption  

**Đáp án: B**  
*Giải thích: Nhiều firewalls được cấu hình để block UDP traffic, nên Internet telephony apps thường dùng TCP làm backup khi UDP bị block.*

---

**Câu 24.** So sánh giữa một ứng dụng multiplayer game online và một ứng dụng email về transport service requirements:

A. Cả hai đều cần timing guarantees và không cần reliable transfer  
B. Game cần timing constraints chặt và loss-tolerant; email cần reliable transfer và không cần timing  
C. Email cần timing constraints hơn game vì phải gửi ngay  
D. Cả hai đều cần bandwidth-sensitive service  

**Đáp án: B**  
*Giải thích: Game online cần tight timing (100s of msec) và có thể chấp nhận mất gói; email là no-loss application nhưng không cần timing guarantee.*

---

**Câu 25.** Application layer của một host chỉ có control ở phía nào của socket?

A. Transport-layer side  
B. Application-layer side  
C. Cả hai phía  
D. Không có control phía nào  

**Đáp án: B**  
*Giải thích: Developer có toàn quyền control ở application-layer side của socket, nhưng rất ít control ở transport-layer side (chỉ chọn protocol và một vài parameters).*

---

### Vận dụng cao

**Câu 26.** Một công ty đang xây dựng service phân phối phần mềm (file lớn) đến hàng triệu người dùng. So với client-server, tại sao P2P architecture phù hợp hơn?

A. P2P nhanh hơn vì sử dụng UDP  
B. Trong P2P, distribution time không tăng tuyến tính theo số peers vì mỗi peer cũng contribute upload capacity; chi phí server/bandwidth không tăng đột biến  
C. P2P không cần Internet connection  
D. P2P đảm bảo security tốt hơn  

**Đáp án: B**  
*Giải thích: Trong client-server, distribution time tăng tuyến tính với N peers (server phải upload NF bits). Trong P2P, mỗi peer nhận được cũng redistribute, nên total upload capacity tăng theo N, giữ distribution time ổn định.*

---

**Câu 27.** Một application cần đảm bảo "mỗi bit gửi sẽ đến đích trong vòng 100ms". TCP có cung cấp guarantee này không? Phân tích:

A. Có, TCP đảm bảo timing thông qua congestion control  
B. Có, TCP đảm bảo timing vì là connection-oriented  
C. Không, TCP và UDP đều không cung cấp timing guarantees; ứng dụng phải tự thiết kế để cope với việc này  
D. Không, chỉ UDP mới có thể đạt được timing yêu cầu  

**Đáp án: C**  
*Giải thích: Internet transport protocols (TCP và UDP) không cung cấp timing guarantees. Real-time applications phải thiết kế để cope với sự vắng mặt của timing guarantee.*

---

**Câu 28.** Tại sao việc confine application software chỉ ở end systems (không ở network core) lại thúc đẩy sự phát triển nhanh của Internet applications?

A. Vì network core devices đắt tiền hơn  
B. Vì developer không cần quan tâm đến cơ sở hạ tầng mạng bên dưới; có thể tạo và deploy ứng dụng mới nhanh chóng mà không cần thay đổi network infrastructure  
C. Vì end systems có processing power mạnh hơn routers  
D. Vì application software chạy ở end systems sẽ tự động secure hơn  

**Đáp án: B**  
*Giải thích: Việc giới hạn application software ở edge cho phép develop và deploy applications nhanh chóng mà không cần sửa đổi network core, tạo điều kiện cho innovation.*

---

**Câu 29.** Xét ba thách thức của P2P (ISP Friendly, Security, Incentives). Thách thức nào liên quan đến vấn đề "freerider"?

A. ISP Friendly  
B. Security  
C. Incentives  
D. Cả ba  

**Đáp án: C**  
*Giải thích: Incentive challenge là làm sao thuyết phục users volunteer bandwidth, storage và computation. Nếu không có incentive tốt, users sẽ chỉ download mà không upload (freerider problem).*

---

**Câu 30.** Một application developer muốn dùng SSL cho application của mình. Họ phải làm gì?

A. Cài đặt SSL ở tầng transport layer của hệ điều hành  
B. Thay TCP bằng SSL  
C. Include SSL code vào cả client và server side của application ở application layer  
D. Yêu cầu ISP cung cấp SSL support  

**Đáp án: C**  
*Giải thích: SSL là application-layer enhancement của TCP. Developer phải include SSL code (libraries/classes) vào cả client và server programs; SSL xử lý encryption trước khi pass data xuống TCP socket.*

---

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

## PHẦN 4 – ELECTRONIC MAIL IN THE INTERNET (Section 2.4)

### Lý thuyết

**Câu 68.** Ba major components của Internet e-mail system là gì?

A. User agents, email clients, và SMTP  
B. User agents, mail servers, và SMTP  
C. Mail servers, DNS servers, và POP3  
D. SMTP, IMAP, và POP3  

**Đáp án: B**  
*Giải thích: Ba components chính: user agents (đọc/viết email), mail servers (mailboxes, message queues), và SMTP (protocol truyền mail).*

---

**Câu 69.** SMTP là gì và dùng protocol tầng dưới nào?

A. Simple Mail Transfer Protocol; dùng UDP  
B. Simple Mail Transfer Protocol; dùng TCP  
C. Secure Mail Transfer Protocol; dùng SSL  
D. Standard Mail Transfer Protocol; dùng IP  

**Đáp án: B**  
*Giải thích: SMTP (Simple Mail Transfer Protocol) là application-layer protocol chính cho Internet email, sử dụng TCP's reliable data transfer service để truyền mail.*

---

**Câu 70.** SMTP có giới hạn quan trọng gì về format của message?

A. Chỉ hỗ trợ file nhỏ hơn 10MB  
B. Yêu cầu toàn bộ message body phải ở dạng 7-bit ASCII  
C. Không hỗ trợ attachments  
D. Chỉ truyền text, không có hình ảnh  

**Đáp án: B**  
*Giải thích: SMTP là legacy technology, yêu cầu body của mọi messages phải ở dạng 7-bit ASCII. Binary data (images, audio) phải được encode sang ASCII trước khi gửi.*

---

**Câu 71.** SMTP là push hay pull protocol?

A. Pull protocol  
B. Push protocol  
C. Cả hai tùy cấu hình  
D. Không phải pull cũng không phải push  

**Đáp án: B**  
*Giải thích: SMTP là push protocol – sending mail server pushes email đến receiving mail server. TCP connection được initiate bởi machine muốn gửi file.*

---

**Câu 72.** Tại sao SMTP thường không dùng intermediate mail servers?

A. Vì SMTP không hỗ trợ routing  
B. SMTP direct connection từ sender's server đến recipient's server; nếu recipient's server down, message ở lại sender's server và retry sau  
C. Vì intermediate servers sẽ đọc nội dung email  
D. Vì intermediate servers quá đắt  

**Đáp án: B**  
*Giải thích: SMTP tạo direct TCP connection giữa sending và receiving mail servers. Nếu Bob's server down, Alice's server giữ message và retry (thường mỗi 30 phút) cho đến khi thành công hoặc hết thời gian.*

---

**Câu 73.** So sánh SMTP và HTTP: điểm khác biệt về cách handle document gồm text và images?

A. SMTP không hỗ trợ images  
B. HTTP encapsulates mỗi object trong HTTP response riêng; SMTP đặt tất cả objects của message vào một message  
C. HTTP không hỗ trợ attachments  
D. Cả hai xử lý giống nhau  

**Đáp án: B**  
*Giải thích: HTTP encapsulates từng object (text, image) trong HTTP response message riêng. SMTP đặt tất cả objects (cả text lẫn attachments sau khi encode) vào một message duy nhất.*

---

**Câu 74.** POP3 protocol hoạt động qua ba phases nào theo thứ tự?

A. Authentication → Update → Transaction  
B. Connection → Authorization → Transfer  
C. Authorization → Transaction → Update  
D. Login → Download → Logout  

**Đáp án: C**  
*Giải thích: POP3 gồm 3 phases: (1) Authorization – authenticate user, (2) Transaction – retrieve/delete messages, (3) Update – thực hiện các deletion sau khi quit.*

---

**Câu 75.** IMAP khác POP3 ở điểm quan trọng nào?

A. IMAP nhanh hơn POP3  
B. IMAP maintain user state information across sessions và cho phép tạo remote folders, quản lý mail trên server  
C. IMAP không yêu cầu authentication  
D. POP3 hỗ trợ nhiều folders hơn IMAP  

**Đáp án: B**  
*Giải thích: IMAP maintain state across sessions (folder names, message-folder associations) và cho phép manage mail trên server. POP3 không có server-side state across sessions và không có remote folder management.*

---

**Câu 76.** Tại sao user agent thường không dialogue trực tiếp với recipient's mail server bằng SMTP?

A. Vì SMTP quá phức tạp  
B. Vì user agent không thể handle trường hợp recipient's server down; cần relay qua sender's mail server để retry  
C. Vì recipient's server chỉ nhận từ trusted servers  
D. Vì SMTP không hỗ trợ direct connections  

**Đáp án: B**  
*Giải thích: Nếu user agent gửi trực tiếp và recipient's server down, email bị mất. Qua sender's mail server, server có thể hold và retry. Sender's server là "reliable middleman".*

---

**Câu 77.** Web-based email (như Gmail) dùng protocol gì giữa browser và mail server?

A. SMTP để cả gửi lẫn nhận  
B. POP3 để cả gửi lẫn nhận  
C. HTTP giữa browser và mail server; SMTP giữa các mail servers  
D. IMAP cho tất cả  

**Đáp án: C**  
*Giải thích: Web email dùng HTTP giữa browser và mail server (thay vì POP3/IMAP để receive và SMTP để send). Nhưng giữa các mail servers, vẫn dùng SMTP.*

---

**Câu 78.** Email header line nào là bắt buộc (required) theo RFC 5322?

A. Subject: và Date:  
B. From: và To:  
C. Content-Type: và MIME-Version:  
D. Reply-To: và Cc:  

**Đáp án: B**  
*Giải thích: Theo RFC 5322, mọi email header phải có From: và To:. Subject: và các header khác là optional.*

---

### Vận dụng

**Câu 79.** Bob thường check email từ nhiều thiết bị (laptop, phone, máy tính công ty). POP3 "download-and-delete" mode có phù hợp không?

A. Có, vì download-and-delete nhanh hơn  
B. Không, vì sau khi download ở một thiết bị, email bị xóa khỏi server và các thiết bị khác không thể truy cập  
C. Có, vì mode này encrypt email tốt hơn  
D. Không, vì download-and-delete không hoạt động trên mobile  

**Đáp án: B**  
*Giải thích: Với download-and-delete, email bị xóa khỏi server sau khi download từ một thiết bị. Bob sẽ không thể truy cập email đó từ các thiết bị khác. Nên dùng IMAP hoặc download-and-keep.*

---

**Câu 80.** Tại sao SMTP encode binary data (như image) sang 7-bit ASCII trước khi gửi, trong khi HTTP thì không?

A. Vì SMTP cần nén dữ liệu  
B. SMTP là legacy protocol được thiết kế trong thời kỳ bandwidth khan hiếm và chỉ xử lý ASCII; HTTP được thiết kế sau nên linh hoạt hơn với data types  
C. Vì SMTP cần security  
D. HTTP không hỗ trợ binary data  

**Đáp án: B**  
*Giải thích: SMTP RFC gốc từ 1982 giới hạn body 7-bit ASCII do constraints thời đó. HTTP được thiết kế sau (1990s) không có hạn chế này và có thể carry binary data trực tiếp.*

---

**Câu 81.** Một SMTP session transcript có lệnh "RCPT TO: <bob@hamburger.edu>". Lệnh này có tác dụng gì?

A. Xác định người gửi  
B. Xác định người nhận email  
C. Bắt đầu truyền nội dung email  
D. Kết thúc session  

**Đáp án: B**  
*Giải thích: RCPT TO chỉ định email address của recipient. MAIL FROM chỉ định sender. DATA bắt đầu truyền nội dung.*

---

**Câu 82.** Nếu Alice's mail server down khi cô ấy muốn gửi email, điều gì xảy ra?

A. Email bị mất ngay lập tức  
B. User agent của Alice gửi trực tiếp đến Bob's server  
C. Không có gì xảy ra; email không thể gửi cho đến khi Alice's server lên lại  
D. Alice có thể complain với system administrator; server sẽ retry khi online trở lại  

**Đáp án: D**  
*Giải thích: Đây là lợi thế của việc relay qua Alice's mail server. Nếu Alice's server down, Alice có thể complain với sysadmin. Khi server lên lại, nó sẽ retry việc gửi.*

---

### Vận dụng cao

**Câu 83.** Phân tích tại sao email system cần 2-step procedure (user agent → sender's server → recipient's server) thay vì direct (user agent → recipient's server)?

A. Vì SMTP không cho phép direct connections  
B. Vì user agent không có cơ chế retry khi recipient's server down; relay qua sender's server tạo reliable intermediate store-and-forward; nếu recipient's server down, sender's server retry tự động  
C. Vì user agent không biết IP của recipient's server  
D. Vì direct connection sẽ không secure  

**Đáp án: B**  
*Giải thích: 2-step procedure đảm bảo reliability: sender's server có thể retry nhiều lần (mỗi 30 phút) cho đến thành công. User agent thường offline và không thể retry. Đây là store-and-forward design.*

---

**Câu 84.** Tại sao IMAP là lựa chọn tốt hơn POP3 cho người dùng nomadic (dùng nhiều thiết bị)?

A. IMAP nhanh hơn POP3  
B. IMAP maintain server-side folder hierarchy và state across sessions; user có thể truy cập cùng mail structure từ bất kỳ device nào; POP3 chỉ quản lý mail cục bộ trên từng device  
C. IMAP encrypt email tốt hơn  
D. IMAP dùng ít bandwidth hơn POP3  

**Đáp án: B**  
*Giải thích: IMAP giữ folders và mail trên server, maintain state across sessions. Dù dùng device nào, user thấy cùng một mailbox structure. POP3 thường download mail về local, tạo sự không nhất quán giữa các devices.*

---

## PHẦN 5 – DNS (Section 2.5)

### Lý thuyết

**Câu 85.** DNS là gì? Hãy chọn định nghĩa đầy đủ nhất:

A. Một Web server đặc biệt  
B. Hệ thống distributed database implement trong hierarchy của DNS servers, kết hợp với application-layer protocol cho phép hosts query database đó  
C. Một loại encryption protocol  
D. Một cơ chế routing trong Internet  

**Đáp án: B**  
*Giải thích: DNS là (1) distributed database implement trong hierarchy of DNS servers và (2) application-layer protocol cho phép hosts query database đó.*

---

**Câu 86.** DNS protocol chạy trên transport protocol nào và port number nào?

A. TCP, port 80  
B. TCP, port 53  
C. UDP, port 53  
D. UDP, port 25  

**Đáp án: C**  
*Giải thích: DNS protocol chạy trên UDP và sử dụng port 53.*

---

**Câu 87.** Ba loại DNS servers trong hierarchy là gì?

A. Primary, Secondary, và Tertiary  
B. Root, TLD (Top-Level Domain), và Authoritative  
C. Local, Regional, và Global  
D. Client, Proxy, và Origin  

**Đáp án: B**  
*Giải thích: Hierarchy DNS servers gồm: Root DNS servers (13 servers labeled A-M), TLD servers (com, org, edu, country codes), và Authoritative servers (của từng organization).*

---

**Câu 88.** Local DNS server (default name server) có vai trò gì?

A. Lưu trữ toàn bộ DNS database  
B. Nhận DNS queries từ hosts và forward vào DNS server hierarchy như một proxy  
C. Là authoritative server cho tất cả hostnames  
D. Chỉ phục vụ các TLD servers  

**Đáp án: B**  
*Giải thích: Local DNS server nhận queries từ hosts và forward vào hierarchy. Nó không thuộc hierarchy chính thức nhưng là central trong DNS architecture.*

---

**Câu 89.** DNS cung cấp những services nào ngoài hostname-to-IP translation?

A. Email encryption và authentication  
B. Host aliasing, mail server aliasing, và load distribution  
C. Bandwidth allocation và traffic shaping  
D. Certificate management và security  

**Đáp án: B**  
*Giải thích: DNS cung cấp thêm: host aliasing (canonical vs alias hostnames), mail server aliasing (MX records), và load distribution (rotates IP addresses cho replicated servers).*

---

**Câu 90.** Trong DNS load distribution, khi nhiều servers cùng phục vụ một hostname (như cnn.com), DNS làm gì khi nhận query?

A. Trả về IP của server gần nhất  
B. Trả về IP của server ít tải nhất  
C. Trả về toàn bộ set of IP addresses nhưng rotate thứ tự, để phân tán traffic  
D. Chỉ trả về một IP duy nhất  

**Đáp án: C**  
*Giải thích: DNS trả về toàn bộ set of IP addresses nhưng rotate thứ tự trong mỗi reply. Client thường gửi request đến IP đầu tiên, nên rotation phân phối traffic.*

---

**Câu 91.** Recursive query trong DNS là gì?

A. Query được gửi nhiều lần đến cùng một server  
B. Query mà DNS server được hỏi phải tự tìm câu trả lời thay mặt cho querying host, rồi trả kết quả về cho host  
C. Query chỉ đến root servers  
D. Query sử dụng TCP thay vì UDP  

**Đáp án: B**  
*Giải thích: Recursive query: DNS server "chịu trách nhiệm" tìm câu trả lời thay mặt cho client. Trái với iterative query, nơi server trả về referral để client tự query tiếp.*

---

**Câu 92.** Iterative query trong DNS là gì?

A. Query được lặp đi lặp lại đến cùng một server  
B. Server chỉ trả về best answer nó biết (thường là referral đến server khác), client tự query tiếp cho đến khi có câu trả lời cuối  
C. Query sử dụng multiple TCP connections  
D. Query yêu cầu server cache kết quả  

**Đáp án: B**  
*Giải thích: Iterative query: mỗi server trả về referral đến server tiếp theo mà nó biết, client (thường là local DNS server) phải tự gửi query tiếp theo.*

---

**Câu 93.** DNS resource record (RR) có format gì?

A. (Name, IP, TTL)  
B. (Name, Value, Type, TTL)  
C. (Hostname, Address, Protocol)  
D. (Key, Value, Expiry)  

**Đáp án: B**  
*Giải thích: DNS RR là 4-tuple: (Name, Value, Type, TTL). TTL là time-to-live, xác định khi nào record nên bị xóa khỏi cache.*

---

**Câu 94.** DNS record Type=A có ý nghĩa gì?

A. Name là domain, Value là hostname của authoritative DNS server  
B. Name là hostname, Value là IP address  
C. Name là alias hostname, Value là canonical hostname  
D. Name là domain, Value là canonical name của mail server  

**Đáp án: B**  
*Giải thích: Type A record: Name = hostname, Value = IP address. Đây là standard hostname-to-IP mapping.*

---

**Câu 95.** DNS record Type=NS có ý nghĩa gì?

A. Name là hostname, Value là IP address  
B. Name là domain, Value là hostname của authoritative DNS server cho domain đó  
C. Name là alias hostname, Value là canonical hostname  
D. Name là domain, Value là IP của mail server  

**Đáp án: B**  
*Giải thích: Type NS record: Name = domain (như foo.com), Value = hostname của authoritative DNS server. Dùng để route DNS queries trong chain.*

---

**Câu 96.** DNS record Type=CNAME có ý nghĩa gì?

A. Name là hostname, Value là IP address  
B. Name là domain, Value là hostname của NS server  
C. Name là alias hostname, Value là canonical hostname  
D. Name là domain, Value là mail server hostname  

**Đáp án: C**  
*Giải thích: Type CNAME: Name = alias hostname, Value = canonical hostname. Cho phép querying hosts biết canonical name của một hostname.*

---

**Câu 97.** DNS record Type=MX có ý nghĩa gì?

A. Name là hostname, Value là IP address  
B. Name là alias hostname của mail server, Value là canonical name của mail server  
C. Name là domain, Value là hostname của NS server  
D. Name là alias hostname, Value là canonical hostname của web server  

**Đáp án: B**  
*Giải thích: Type MX: Name = alias hostname của mail server, Value = canonical name của mail server. Cho phép mail servers có simple alias hostnames.*

---

**Câu 98.** DNS caching hoạt động như thế nào?

A. DNS servers lưu trữ vĩnh viễn tất cả hostname-to-IP mappings  
B. Khi DNS server nhận reply, nó cache mapping đó trong local memory; cached info bị discard sau một khoảng thời gian (TTL, thường 2 ngày)  
C. Chỉ local DNS servers mới cache  
D. Caching chỉ xảy ra tại root DNS servers  

**Đáp án: B**  
*Giải thích: Bất kỳ DNS server nào khi nhận reply đều có thể cache mapping đó. Cached entries bị discard sau TTL (thường ~2 ngày) vì hostnames/IPs có thể thay đổi.*

---

### Vận dụng

**Câu 99.** Để access trang web www.amazon.com, browser cần thực hiện gì trước khi gửi HTTP request?

A. Gửi SMTP message đến amazon.com  
B. Invoke DNS để translate www.amazon.com thành IP address, sau đó initiate TCP connection đến server tại IP đó port 80  
C. Gửi UDP packet đến amazon.com trực tiếp  
D. Contact FTP server của amazon.com trước  

**Đáp án: B**  
*Giải thích: Browser extract hostname → pass cho DNS client → DNS query → nhận IP → browser initiate TCP connection đến IP đó, port 80 → gửi HTTP request.*

---

**Câu 100.** Trong ví dụ DNS lookup cis.poly.edu muốn biết IP của gaia.cs.umass.edu, có bao nhiêu DNS messages được trao đổi (không tính caching)?

A. 2 messages  
B. 4 messages  
C. 8 messages  
D. 16 messages  

**Đáp án: C**  
*Giải thích: 4 query messages + 4 reply messages = 8 DNS messages tổng cộng (đến root, TLD, authoritative, và final reply về local DNS, rồi từ local DNS về client).*

---

**Câu 101.** Một registrar cần insert gì vào TLD com servers khi register networkutopia.com?

A. Chỉ IP address của Web server  
B. Type NS record (networkutopia.com, dns1.networkutopia.com) và Type A record (dns1.networkutopia.com, IP address)  
C. Chỉ MX records  
D. CNAME records cho tất cả subdomains  

**Đáp án: B**  
*Giải thích: Registrar insert: (1) NS record pointing đến authoritative DNS server và (2) Type A record providing IP của authoritative DNS server đó.*

---

**Câu 102.** DNS caching giúp gì trong ví dụ cis.poly.edu query gaia.cs.umass.edu?

A. Không giúp gì  
B. Nếu local DNS server đã cache IP của TLD edu servers, nó có thể bypass root DNS servers, giảm số messages cần gửi  
C. Caching chỉ giúp sau khi query giống hệt được gửi  
D. Caching giúp mã hóa query  

**Đáp án: B**  
*Giải thích: Nếu local DNS cache IP của TLD servers, nó không cần contact root servers. Có thể bắt đầu query từ TLD level, giảm latency và số messages.*

---

**Câu 103.** DNS attack nào send DNS queries với spoofed source address của target, gây ra DNS servers gửi large replies về target?

A. DDoS flooding attack  
B. Man-in-the-middle attack  
C. DNS poisoning attack  
D. DNS reflection/amplification attack  

**Đáp án: D**  
*Giải thích: Reflection/amplification attack: attacker gửi queries với spoofed source = target's IP. DNS servers gửi large replies về target. "Amplification" vì response lớn hơn query nhiều lần.*

---

**Câu 104.** Tại sao DDoS attack vào root DNS servers năm 2002 gây ít thiệt hại?

A. Root servers quá mạnh để bị tấn công  
B. Root servers được protect bởi packet filters blocking ICMP ping, và local DNS servers đã cache IP của TLD servers nên bypass được root servers  
C. Attacker dùng phương pháp không hiệu quả  
D. Root servers ở địa điểm bí mật  

**Đáp án: B**  
*Giải thích: Hai lý do: (1) Nhiều root servers có packet filters block ICMP ping. (2) Local DNS servers cache IP của TLD servers, cho phép bypass root servers entirely.*

---

### Vận dụng cao

**Câu 105.** Tại sao DNS không dùng single centralized server? Liệt kê các vấn đề:

A. Single server quá đắt để maintain  
B. Single point of failure (toàn Internet down nếu server crash), traffic volume quá lớn, distant centralized database gây latency cao cho users xa, và maintenance database khổng lồ cập nhật liên tục  
C. Single server không hỗ trợ IPv6  
D. Single server sẽ bị DDoS tấn công dễ dàng  

**Đáp án: B**  
*Giải thích: Bốn vấn đề của centralized DNS: (1) Single point of failure, (2) Traffic volume quá lớn, (3) Distant DB gây delay, (4) Maintenance (database lớn, cập nhật thường xuyên). DNS là ví dụ điển hình của distributed design.*

---

**Câu 106.** Một company muốn mail server và web server có cùng alias hostname "enterprise.com". Cần những DNS records nào?

A. Hai Type A records  
B. MX record cho mail server (alias → canonical mail server name) và CNAME record (hoặc A record) cho web server  
C. Hai Type NS records  
D. Hai CNAME records  

**Đáp án: B**  
*Giải thích: MX record cho phép enterprise.com alias đến canonical mail server name. Để phân biệt, client query MX record để tìm mail server, query CNAME/A record để tìm web server. Cả hai có thể share alias nhờ record types khác nhau.*

---

## PHẦN 6 – PEER-TO-PEER APPLICATIONS (Section 2.6)

### Lý thuyết

**Câu 107.** Trong client-server file distribution, nếu có N peers, server phải transmit tổng cộng bao nhiêu bits?

A. F bits  
B. N × F bits  
C. F/N bits  
D. √N × F bits  

**Đáp án: B**  
*Giải thích: Server phải gửi 1 copy của F-bit file đến mỗi trong N peers → tổng N×F bits server phải transmit.*

---

**Câu 108.** Distribution time của client-server architecture (D_cs) được tính theo công thức nào?

A. D_cs = F/us  
B. D_cs = NF/us  
C. D_cs = max(NF/us, F/dmin)  
D. D_cs = NF/(us + Σui)  

**Đáp án: C**  
*Giải thích: D_cs = max(NF/us, F/dmin). Hai bottlenecks: (1) Server phải transmit NF bits với rate us, (2) Slowest peer cần F/dmin giây để download.*

---

**Câu 109.** Distribution time của P2P architecture (D_P2P) được tính theo công thức nào?

A. D_P2P = max(F/us, F/dmin)  
B. D_P2P = max(F/us, F/dmin, NF/(us + Σui))  
C. D_P2P = NF/us  
D. D_P2P = F/(us × N)  

**Đáp án: B**  
*Giải thích: D_P2P = max(F/us, F/dmin, NF/(us + Σui)). Ba bottlenecks: (1) Server upload rate, (2) Slowest peer download, (3) Total system upload capacity phải ≥ NF bits.*

---

**Câu 110.** Trong BitTorrent, "torrent" là gì?

A. Tracker server  
B. Collection of all peers tham gia distribute một file cụ thể  
C. Một chunk của file  
D. Phần mềm BitTorrent client  

**Đáp án: B**  
*Giải thích: Torrent là tập hợp tất cả các peers đang tham gia distribute một file cụ thể. Một torrent có thể có ít hơn 10 hoặc hơn 1000 peers.*

---

**Câu 111.** Tracker trong BitTorrent có chức năng gì?

A. Lưu trữ toàn bộ file cần phân phối  
B. Infrastructure node theo dõi peers đang tham gia torrent  
C. Mã hóa các chunks  
D. Quản lý bandwidth của mỗi peer  

**Đáp án: B**  
*Giải thích: Tracker là infrastructure node track các peers đang participate trong torrent. Khi peer join, nó register với tracker và periodic inform tracker nó vẫn đang online.*

---

**Câu 112.** BitTorrent dùng kỹ thuật gì để quyết định chunk nào request trước?

A. Random selection  
B. Rarest first – request những chunks hiếm nhất trong số các neighbors trước  
C. Largest first  
D. Sequential order  

**Đáp án: B**  
*Giải thích: "Rarest first": Alice xác định chunks mà ít neighbors có nhất và request những chunks đó trước. Mục đích: redistribute rare chunks nhanh hơn, equalize số copies của mỗi chunk.*

---

**Câu 113.** BitTorrent dùng thuật toán "tit-for-tat" cho mục đích gì?

A. Quyết định chunk nào request  
B. Quyết định gửi chunks đến neighbors nào – ưu tiên những neighbors đang feed data với rate cao nhất  
C. Tìm tracker  
D. Mã hóa data truyền đi  

**Đáp án: B**  
*Giải thích: Tit-for-tat: Alice ưu tiên gửi chunks đến 4 neighbors đang feed data cho cô ấy với rate cao nhất (unchoked). Mỗi 30 giây, chọn thêm 1 random peer (optimistically unchoked) để khuyến khích giao tiếp mới.*

---

**Câu 114.** DHT (Distributed Hash Table) là gì?

A. Loại encryption algorithm  
B. Distributed P2P database lưu trữ (key, value) pairs phân tán trên millions of peers  
C. Centralized server quản lý file sharing  
D. Protocol để mã hóa torrent  

**Đáp án: B**  
*Giải thích: DHT là distributed database implement trong P2P network, lưu (key, value) pairs phân tán. Bất kỳ peer nào cũng có thể query với một key và nhận corresponding values.*

---

**Câu 115.** Trong circular DHT, mỗi peer cần biết thông tin về bao nhiêu peers khác (tối thiểu)?

A. Chỉ 1 peer  
B. 2 peers – immediate successor và immediate predecessor  
C. N/2 peers  
D. Tất cả N peers  

**Đáp án: B**  
*Giải thích: Trong circular DHT cơ bản, mỗi peer chỉ cần biết immediate successor và immediate predecessor (modulo 2n).*

---

**Câu 116.** Trade-off trong design của DHT là gì?

A. Security vs Performance  
B. Số neighbors mỗi peer phải track vs số messages cần gửi để resolve một query  
C. Bandwidth vs Storage  
D. Latency vs Reliability  

**Đáp án: B**  
*Giải thích: Nếu mỗi peer track nhiều neighbors → ít messages per query nhưng nhiều overhead. Nếu ít neighbors (circular) → ít overhead nhưng nhiều messages (N/2 trung bình). DHT tối ưu đạt O(log N) cho cả hai.*

---

### Vận dụng

**Câu 117.** Với N = 1.000.000 peers, us = 10u (server upload = 10× peer upload), F/u = 1 giờ. Distribution time của client-server là bao nhiêu so với P2P?

A. Client-server nhanh hơn vì có dedicated server  
B. Client-server mất hàng trăm giờ (NF/us tăng linear với N), P2P dưới 1 giờ bất kể N  
C. Cả hai đều mất khoảng 1 giờ  
D. P2P chậm hơn vì cần coordinate nhiều peers  

**Đáp án: B**  
*Giải thích: Client-server: D = NF/us = 1.000.000 × (1h/10) = 100.000 giờ (tăng linear với N). P2P: ổn định dưới 1 giờ vì total upload capacity tăng cùng với N peers.*

---

**Câu 118.** Trong BitTorrent, khi Alice join torrent mới, cô ấy liên hệ với ai đầu tiên?

A. Ngay lập tức liên hệ với tất cả peers  
B. Contact tracker, nhận danh sách peers, sau đó attempt TCP connections với subset of peers đó  
C. Contact root server để tìm file  
D. Gửi broadcast để tìm peers  

**Đáp án: B**  
*Giải thích: Alice register với tracker → tracker trả về list ~50 peers → Alice attempt concurrent TCP connections với peers đó → neighboring peers là những peers TCP connection thành công.*

---

**Câu 119.** Tại sao trong BitTorrent, "optimistically unchoked" peer được chọn ngẫu nhiên mỗi 30 giây?

A. Để test network performance  
B. Để cho new peers có cơ hội nhận chunks (dù chưa upload nhiều) và tìm trading partners mới tốt hơn  
C. Để random distribute bandwidth  
D. Để reduce congestion  

**Đáp án: B**  
*Giải thích: Random "optimistically unchoked" peer cho phép: (1) New peers có thể nhận data dù chưa có gì để upload, (2) Cả hai peers có thể tìm thấy trading partners tốt hơn hiện tại.*

---

**Câu 120.** Trong DHT với n=4, peers có IDs {1, 3, 4, 5, 8, 10, 12, 15}. Key 11 được store tại peer nào?

A. Peer 10  
B. Peer 12  
C. Peer 15  
D. Peer 8  

**Đáp án: B**  
*Giải thích: Key stored tại peer có ID là closest successor của key. Key 11 → closest successor là peer 12 (12 > 11 và không có peer nào giữa 11 và 12).*

---

**Câu 121.** Trong circular DHT, nếu peer 5 đột ngột leave, peer 4 cần cập nhật state như thế nào?

A. Không cần cập nhật  
B. Peer 4 replace first successor (peer 5) bằng second successor (peer 8), rồi hỏi peer 8 về successor tiếp theo của nó  
C. Peer 4 broadcast đến tất cả peers  
D. Peer 4 contact tracker  

**Đáp án: B**  
*Giải thích: Peer 4 phát hiện peer 5 chết (không respond ping). Peer 4: (1) Set first successor = peer 8, (2) Hỏi peer 8 về ID/IP của successor của nó (peer 10) → set peer 10 làm second successor.*

---

### Vận dụng cao

**Câu 122.** Tại sao P2P distribution time không tăng tuyến tính theo N (như client-server)?

A. P2P dùng faster network  
B. Trong P2P, mỗi peer khi receive data cũng trở thành distributor; total upload capacity (us + Σui) tăng theo N, offsetting demand NF/total_capacity  
C. P2P compress dữ liệu tốt hơn  
D. P2P bypass bottleneck links  

**Đáp án: B**  
*Giải thích: Khi N tăng, demand tăng (NF bits cần distribute) nhưng total supply cũng tăng (thêm N peers × ui upload capacity). Ratio NF/(us+Σui) không nhất thiết tăng mạnh theo N.*

---

**Câu 123.** BitTorrent sử dụng Kademlia DHT như thế nào trong hệ thống của mình?

A. Để encrypt file chunks  
B. Như distributed tracker: key là torrent identifier, value là IP addresses của peers trong torrent đó; tìm peer responsible cho key để track torrent  
C. Để routing TCP connections  
D. Để compress chunks trước khi transfer  

**Đáp án: B**  
*Giải thích: BitTorrent dùng Kademlia DHT làm distributed tracker. Key = torrent ID, Value = IP của peers trong torrent. Peer mới query DHT với torrent ID để tìm tracker peer và biết list of current peers.*

---

**Câu 124.** So sánh mesh overlay với circular DHT: trade-off về số neighbors và số messages?

A. Cả hai đều tương đương  
B. Mesh: mỗi peer track N peers → 1 message per query; Circular: mỗi peer track 2 peers → N/2 messages trung bình per query; DHT với shortcuts đạt O(log N) cho cả hai  
C. Circular luôn tốt hơn mesh  
D. Mesh không thể implement trong thực tế  

**Đáp án: B**  
*Giải thích: Trade-off rõ ràng: Mesh (O(N) neighbors, O(1) messages) ↔ Circular (O(1) neighbors, O(N) messages). DHT tối ưu với shortcuts đạt O(log N) cho cả hai metric.*

---

## PHẦN 7 – SOCKET PROGRAMMING (Section 2.7)

### Lý thuyết

**Câu 125.** Sự khác biệt chính giữa UDP socket và TCP socket trong socket programming là gì?

A. UDP socket dùng AF_INET, TCP socket dùng AF_INET6  
B. UDP socket (SOCK_DGRAM) connectionless, gắn destination address mỗi packet; TCP socket (SOCK_STREAM) connection-oriented, thiết lập connection trước khi gửi data  
C. UDP socket hỗ trợ encryption, TCP socket thì không  
D. TCP socket nhanh hơn UDP socket vì connection-oriented  

**Đáp án: B**  
*Giải thích: UDP: SOCK_DGRAM, attach destination để mỗi packet, không handshaking. TCP: SOCK_STREAM, phải connect() để establish connection trước khi gửi data.*

---

**Câu 126.** Trong UDP socket programming, server phải bind() port number. Điều này có tác dụng gì?

A. Tạo TCP connection  
B. Gán port number cho server socket để packets đến port đó được directed đến socket này  
C. Encrypt communications  
D. Start listening cho TCP connections  

**Đáp án: B**  
*Giải thích: bind() gán port number cho socket. Khi packet đến server's IP tại port đó, hệ điều hành direct packet đến socket đã bind port number đó.*

---

**Câu 127.** Trong TCP socket programming, server tạo hai loại sockets. Đó là gì?

A. Send socket và receive socket  
B. Welcoming socket (serverSocket) nhận initial contacts; connection socket (connectionSocket) dedicated cho từng client  
C. Primary socket và backup socket  
D. UDP socket và TCP socket  

**Đáp án: B**  
*Giải thích: serverSocket (welcoming door): accept initial connections. connectionSocket: được tạo khi client connect, dedicated cho client đó, dùng để communicate.*

---

**Câu 128.** Lệnh serverSocket.listen(1) trong TCP server có tác dụng gì?

A. Bắt đầu gửi data  
B. Server bắt đầu listen cho TCP connection requests từ clients; parameter chỉ định max queued connections  
C. Server connect đến client  
D. Server bind port number  

**Đáp án: B**  
*Giải thích: listen() đặt server vào trạng thái chờ TCP connection requests. Parameter (1) là maximum số queued connections.*

---

**Câu 129.** Trong UDP client, khi gọi clientSocket.sendto(message, (serverName, serverPort)), thông tin nào được tự động thêm bởi OS (không cần code explicitly)?

A. Message content  
B. Source address (source IP và source port number)  
C. Destination IP address  
D. Checksum  

**Đáp án: B**  
*Giải thích: Code explicitly gán destination address. Source address (IP và port) được tự động attach bởi underlying OS, không cần lập trình viên làm thủ công.*

---

**Câu 130.** Điểm khác biệt quan trọng giữa TCPClient và UDPClient trong việc gửi data là gì?

A. TCPClient dùng UDP, UDPClient dùng TCP  
B. TCPClient chỉ cần drop bytes vào TCP connection (không cần attach destination address mỗi lần); UDPClient phải attach destination address với mỗi packet  
C. TCPClient không cần tạo socket  
D. UDPClient nhanh hơn vì gửi nhiều data hơn  

**Đáp án: B**  
*Giải thích: Sau khi TCP connection được establish, TCPClient dùng send() mà không cần specify destination. UDPClient dùng sendto() và phải include (serverName, serverPort) với mỗi message vì connectionless.*

---

### Vận dụng

**Câu 131.** Một developer muốn viết ứng dụng truyền file lớn và cần đảm bảo không mất dữ liệu. Nên chọn SOCK_DGRAM hay SOCK_STREAM?

A. SOCK_DGRAM vì nhanh hơn  
B. SOCK_STREAM vì TCP cung cấp reliable, ordered byte stream delivery  
C. SOCK_DGRAM vì ít overhead hơn  
D. Không quan trọng  

**Đáp án: B**  
*Giải thích: SOCK_STREAM = TCP socket. TCP đảm bảo reliable, ordered, error-free delivery – cần thiết cho file transfer. SOCK_DGRAM = UDP, unreliable.*

---

**Câu 132.** Trong TCP server code, tại sao connectionSocket.close() được gọi sau khi gửi response, nhưng serverSocket vẫn mở?

A. Để tiết kiệm bộ nhớ  
B. connectionSocket phục vụ client đó xong nên đóng; serverSocket (welcoming socket) tiếp tục mở để accept connections từ clients mới  
C. Cả hai nên đóng cùng lúc  
D. connectionSocket.close() cũng đóng serverSocket  

**Đáp án: B**  
*Giải thích: connectionSocket là dedicated cho một client cụ thể; sau khi phục vụ xong thì đóng. serverSocket là welcoming socket luôn open để có thể accept clients mới.*

---

**Câu 133.** Tại sao trong UDP programming, server cần extract clientAddress từ recvfrom() và dùng nó khi sendto()?

A. Để log thông tin kết nối  
B. Vì UDP connectionless, server không có dedicated connection tới client; phải dùng source address từ received packet như return address để gửi reply  
C. Để verify authentication  
D. Để check message size  

**Đáp án: B**  
*Giải thích: UDP không có pre-established connection. Server dùng clientAddress (IP + port của client) extracted từ incoming packet như "return address" để gửi reply về đúng client.*

---

**Câu 134.** Khi client TCP gọi clientSocket.connect((serverName, serverPort)), điều gì xảy ra bên dưới?

A. Chỉ gửi một message đến server  
B. Three-way handshake được thực hiện ở transport layer, thiết lập TCP connection; sau đó client có thể gửi/nhận data  
C. UDP connection được thiết lập  
D. Server tạo một process mới  

**Đáp án: B**  
*Giải thích: connect() trigger three-way handshake ở transport layer (transparent với application). Sau khi handshake xong, TCP connection được establish và application có thể gửi data.*

---

### Vận dụng cao

**Câu 135.** Khi viết một proprietary network application, developer phải cẩn thận điều gì về port numbers?

A. Phải dùng port numbers lớn hơn 1024  
B. Phải tránh dùng well-known port numbers đã được assign cho standard protocols (như 80, 25, 53); nên dùng port numbers không reserved  
C. Phải đăng ký port number với IANA  
D. Không có hạn chế nào về port numbers  

**Đáp án: B**  
*Giải thích: Well-known port numbers (như 80/HTTP, 25/SMTP, 53/DNS) đã được reserve cho standard protocols. Proprietary applications phải dùng port numbers khác để tránh conflicts.*

---

**Câu 136.** Phân biệt "open" network applications và "proprietary" network applications:

A. Open applications free, proprietary phải trả phí  
B. Open applications implement protocols defined in RFCs (publicly available), cho phép independent developers interoperate; proprietary dùng private protocols, chỉ developer đó có thể build compatible clients/servers  
C. Open applications chạy trên Linux, proprietary chạy trên Windows  
D. Không có sự khác biệt quan trọng  

**Đáp án: B**  
*Giải thích: Open (như HTTP, FTP) – spec public trong RFC, Firefox có thể talk to Apache vì cả hai follow HTTP RFC. Proprietary (như Skype) – protocol private, chỉ Skype build compatible software.*

---

## PHẦN 8 – CÂU HỎI TỔNG HỢP (Cross-Section)

### Vận dụng

**Câu 137.** Một developer cần chọn giữa client-server và P2P architecture cho một ứng dụng streaming video đến millions of users. Đâu là phân tích đúng nhất?

A. Client-server luôn tốt hơn vì có server mạnh  
B. P2P phù hợp hơn vì self-scalability: mỗi viewer cũng distribute video, không tạo linear scaling problem cho server; chi phí infrastructure thấp hơn nhiều  
C. P2P không phù hợp vì video cần reliable transfer  
D. Client-server phù hợp hơn vì P2P không hỗ trợ video  

**Đáp án: B**  
*Giải thích: Với millions of users, client-server cần server phải transmit N×F bits (bottleneck cực lớn). P2P: distribution time gần như flat với N, chi phí không tăng tuyến tính.*

---

**Câu 138.** HTTP, FTP, SMTP và DNS đều là application-layer protocols chạy trên TCP/UDP. Nhưng DNS khác ba protocols kia ở điểm quan trọng nào?

A. DNS dùng UDP, các protocols kia dùng TCP  
B. DNS không phải application users interact trực tiếp; DNS là core network function (hostname-to-IP translation) được invoke bởi các applications khác  
C. DNS không cần authentication  
D. DNS chỉ chạy trên root servers  

**Đáp án: B**  
*Giải thích: HTTP, FTP, SMTP là applications users trực tiếp dùng. DNS là "behind the scenes" service cho các applications khác dùng; users không interact trực tiếp với DNS.*

---

**Câu 139.** Web cache hoạt động giống với concept nào trong DNS?

A. DNS recursion  
B. DNS caching – cả hai cache responses để giảm latency và reduce traffic về origin (root servers cho DNS, origin web servers cho Web cache)  
C. DNS authoritative servers  
D. DNS TLD servers  

**Đáp án: B**  
*Giải thích: Cả Web cache và DNS cache đều cache responses từ "source of truth" để serve repeated requests locally, giảm latency và reduce traffic về gốc.*

---

**Câu 140.** Tại sao email cần 3 protocols (SMTP, POP3/IMAP, HTTP) trong khi Web chỉ cần HTTP?

A. Email phức tạp hơn về mặt kỹ thuật  
B. Email có sender (push: SMTP) và receiver (pull: POP3/IMAP/HTTP) phases với khác nhau về direction; SMTP là push protocol không phù hợp để retrieve mail  
C. Email cần encryption nhiều hơn  
D. Email support nhiều file formats hơn  

**Đáp án: B**  
*Giải thích: SMTP (push) để transfer mail giữa servers. Nhưng users retrieve mail là pull operation – cần POP3/IMAP (hoặc HTTP cho web email). SMTP không thể dùng để pull vì nó là push protocol.*

---

**Câu 141.** Khi Alice gửi email cho Bob, con đường của email là gì?

A. Alice's agent → Bob's agent trực tiếp  
B. Alice's agent → (SMTP) → Alice's mail server → (SMTP) → Bob's mail server → (POP3/IMAP/HTTP) → Bob's agent  
C. Alice's agent → DNS server → Bob's mail server → Bob's agent  
D. Alice's agent → (HTTP) → Alice's mail server → (SMTP) → Bob's mail server  

**Đáp án: B**  
*Giải thích: Đường đi chuẩn: Alice's UA dùng SMTP gửi đến Alice's server → Alice's server dùng SMTP relay đến Bob's server → Bob's UA dùng POP3/IMAP/HTTP pull từ Bob's server.*

---

**Câu 142.** Cả HTTP và SMTP đều dùng persistent connections. Điểm khác nhau quan trọng là gì?

A. HTTP nhanh hơn SMTP  
B. HTTP là pull protocol (client pull data từ server); SMTP là push protocol (sender push đến receiver); TCP connection initiated bởi machine muốn receive (HTTP) vs muốn send (SMTP)  
C. SMTP dùng encryption, HTTP không  
D. HTTP hỗ trợ binary data, SMTP không  

**Đáp án: B**  
*Giải thích: HTTP: Pull – TCP initiated bởi machine muốn receive file. SMTP: Push – TCP initiated bởi machine muốn send file. Đây là fundamental architectural difference.*

---

**Câu 143.** Tổng số DNS messages khi cis.poly.edu hỏi gaia.cs.umass.edu với 4 levels (host → local → root → TLD → authoritative) dùng iterative queries là bao nhiêu?

A. 4 messages  
B. 6 messages  
C. 8 messages  
D. 10 messages  

**Đáp án: C**  
*Giải thích: 8 messages: 4 query messages (host→local, local→root, local→TLD, local→authoritative) + 4 reply messages (mỗi pair) = 8 tổng cộng.*

---

**Câu 144.** Một application gửi data ở rate 32 kbps. Tại sao nên dùng UDP thay vì TCP cho ứng dụng này?

A. Vì UDP có throughput guarantee 32 kbps  
B. Vì TCP's congestion control có thể throttle application xuống dưới 32 kbps khi mạng tắc; UDP bypass congestion control, cho phép application pump at desired rate  
C. Vì UDP nhanh hơn TCP trong mọi tình huống  
D. Vì TCP không hỗ trợ real-time applications  

**Đáp án: B**  
*Giải thích: TCP congestion control có thể reduce sending rate khi network congested, xuống dưới required 32 kbps. UDP không có congestion control nên sender có thể transmit at desired rate (dù actual throughput phụ thuộc network).*

---

**Câu 145.** Tại sao data centers (với hundreds of thousands of servers) thay thế single server trong client-server architecture cho các large-scale services?

A. Vì single server đắt hơn data center  
B. Vì single server không thể handle requests từ hàng triệu concurrent clients; data center tạo powerful virtual server bằng cách distribute load  
C. Vì data center dễ bảo mật hơn  
D. Vì data center sử dụng P2P protocols  

**Đáp án: B**  
*Giải thích: Popular services (Google, Amazon, Facebook) nhận hàng tỷ requests; single server sẽ overwhelmed. Data center với hàng trăm nghìn servers distribute load để create a virtually powerful server.*

---

### Vận dụng cao

**Câu 146.** Một social networking app muốn track user's IP address qua servers (server-tracked) nhưng gửi messages trực tiếp user-to-user (P2P messages). Đây là kiến trúc gì?

A. Pure client-server  
B. Pure P2P  
C. Hybrid architecture – kết hợp client-server (track IPs via servers) và P2P (direct user-to-user messages)  
D. Overlay network  

**Đáp án: C**  
*Giải thích: Đây là hybrid architecture (như nhiều instant messaging apps): servers track IP addresses (client-server element), nhưng actual messages đi trực tiếp P2P mà không qua servers.*

---

**Câu 147.** Phân tích tại sao Internet telephony có thể hoạt động ổn dù không có timing guarantees từ transport layer?

A. Vì Internet có timing guarantees ẩn  
B. Applications được thiết kế để "cope" – dùng buffering, adaptive coding, jitter compensation; trong thực tế delay thường đủ nhỏ để acceptable  
C. VoIP apps dùng secret protocols với timing guarantees  
D. Không thể, Internet telephony không hoạt động tốt  

**Đáp án: B**  
*Giải thích: Dù không có guarantees, Internet thường provide satisfactory service. VoIP apps dùng clever design tricks: playback buffers, adaptive coding rates, packet loss concealment để cope với variable delay và loss.*

---

**Câu 148.** Trong thiết kế Web cache, nếu một object có thể stale (cached nhưng đã bị modify ở origin), cơ chế nào giải quyết vấn đề này mà không cần luôn fetch từ origin?

A. Cache tự động refresh mỗi phút  
B. Conditional GET với If-Modified-Since: nếu object chưa thay đổi, server trả 304 Not Modified (không có body), cache dùng bản đang có; chỉ fetch khi thực sự changed  
C. Cache không giải quyết được vấn đề này  
D. Cache dùng hash để verify freshness  

**Đáp án: B**  
*Giải thích: Conditional GET là elegant solution: kiểm tra staleness với minimal overhead. Nếu object unchanged → 304 (không tốn bandwidth truyền object). Nếu changed → 200 OK với fresh object.*

---

**Câu 149.** Tại sao DHT được gọi là "Distributed Hash Table" – vai trò của "hash" là gì?

A. DHT mã hóa data bằng hash function  
B. Hash function map non-integer keys (như content names, social security numbers) sang integer IDs trong range [0, 2n-1] – cùng space với peer IDs – cho phép assign keys to peers một cách deterministic  
C. Hash function để compress data  
D. Hash function verify tính toàn vẹn của data  

**Đáp án: B**  
*Giải thích: Hash function là cầu nối: chuyển arbitrary keys (strings) thành integers trong cùng không gian với peer IDs. Nhờ đó có thể define rule "assign key to closest peer" một cách nhất quán.*

---

**Câu 150.** Một company triển khai Web cache với hit rate 0.6. Access link của company là 10 Mbps. Average object 1 Mbit, request rate 8 req/sec. Không có cache, traffic intensity trên access link là:

A. 0.3  
B. 0.6  
C. 0.8  
D. 1.0  

**Đáp án: C**  
*Giải thích: Traffic intensity = (8 req/s × 1 Mbit) / 10 Mbps = 8/10 = 0.8. Với cache (hit rate 0.6), chỉ 40% requests qua access link: intensity = 0.8 × 0.4 = 0.32, giảm đáng kể.*

---

**Câu 151.** Phân tích: tại sao "rarest first" trong BitTorrent giúp hệ thống hoạt động hiệu quả hơn "random first"?

A. Rarest first download nhanh hơn về tốc độ bits  
B. Rarest first equalize số copies của mỗi chunk trong torrent; nếu dùng random, một số chunks có thể trở nên cực kỳ hiếm khi ít peers có nó, gây bottleneck vào cuối download  
C. Rarest first ít tiêu tốn bandwidth hơn  
D. Rarest first secure hơn  

**Đáp án: B**  
*Giải thích: Rarest first ensures chunks được redistribute trước khi trở nên "critically rare". Nếu một chunk chỉ còn 1 peer có, nó có thể trở thành bottleneck. Rarest first prevent scenario này bằng cách prioritize redistribution của rare chunks.*

---

**Câu 152.** Tại sao P2P architecture gặp thách thức về "Security" nhiều hơn client-server?

A. P2P không dùng encryption  
B. P2P nature high-distributed và open: không có single point of control/trust, bất kỳ peer nào cũng tham gia, khó verify identity, khó enforce security policies  
C. P2P dùng protocol yếu hơn  
D. P2P không có authentication  

**Đáp án: B**  
*Giải thích: P2P không có central authority để verify participants, enforce policies, hay audit behavior. Attackers có thể join P2P network và behave maliciously. Đây là fundamental challenge của distributed open systems.*

---

**Câu 153.** Khi access link của một institution bị congested (traffic intensity ≈ 1), có hai giải pháp: upgrade link hoặc install cache. So sánh hai giải pháp:

A. Upgrade link luôn tốt hơn  
B. Cả hai giảm access link intensity; nhưng cache rẻ hơn (public-domain software trên inexpensive PCs) và có thể hiệu quả hơn upgrade link nếu hit rate đủ cao  
C. Cache không giúp ích gì  
D. Upgrade link là option duy nhất  

**Đáp án: B**  
*Giải thích: Upgrade link 15→100 Mbps giảm intensity xuống 0.15 (delay ~2s). Cache với hit rate 0.4 giảm intensity xuống 0.6 (delay ~1.2s), thậm chí tốt hơn về response time với chi phí thấp hơn nhiều.*

---

**Câu 154.** Liên hệ giữa DNS và layered architecture: DNS là application-layer protocol nhưng phục vụ cho các application-layer protocols khác. Điều này minh họa nguyên tắc gì?

A. DNS là transport-layer protocol  
B. Nguyên tắc "edge complexity": much of Internet's complexity được đặt ở edge (end systems). DNS implement critical name-to-address translation ở application layer (edge), không cần modify network core  
C. DNS vi phạm layer principle  
D. DNS là exception, không có ý nghĩa thiết kế  

**Đáp án: B**  
*Giải thích: DNS minh họa edge-based design: core function (hostname resolution) được implement ở application layer tại edge, không cần routers/core biết về DNS. Reflects Internet design philosophy: put complexity at edges.*

---

**Câu 155.** Trong socket programming với TCP, nếu server cần phục vụ nhiều clients đồng thời, giải pháp đơn giản nhất là gì?

A. Dùng nhiều server ports  
B. Sau khi serverSocket.accept() tạo connectionSocket cho client mới, server spawn a new thread/process để handle connectionSocket đó, trong khi main process tiếp tục listen cho connections mới  
C. Dùng UDP thay vì TCP  
D. Chỉ có thể phục vụ một client tại một thời điểm  

**Đáp án: B**  
*Giải thích: Classic pattern cho concurrent TCP servers: main loop accept() → spawn thread/process với connectionSocket → main loop quay lại accept() để serve clients khác. Mỗi connectionSocket được handled independently.*

---

## PHẦN 9 – CÂU HỎI BỔ SUNG VÀ NÂNG CAO

**Câu 156.** Một URL như http://www.someSchool.edu/someDept/pic.gif gồm những thành phần nào?

A. Protocol, port, và file name  
B. Protocol (http), hostname (www.someSchool.edu), và path name (/someDept/pic.gif)  
C. IP address, port, và file name  
D. Protocol, DNS name, và checksum  

**Đáp án: B**  
*Giải thích: URL gồm: hostname của server chứa object và path name của object. Browser parse hostname để DNS lookup, sau đó request object theo path.*

---

**Câu 157.** Trong HTTP/1.1 (default), connections là persistent hay non-persistent?

A. Non-persistent by default  
B. Persistent by default với pipelining  
C. Non-persistent với pipelining  
D. Depends on server  

**Đáp án: B**  
*Giải thích: Default mode của HTTP là persistent connections với pipelining. Non-persistent phải được configured explicitly (e.g., qua "Connection: close" header).*

---

**Câu 158.** HTTP status code "301 Moved Permanently" có ý nghĩa gì?

A. Request thành công  
B. Object đã bị moved vĩnh viễn; URL mới được specify trong Location header; client software tự động retrieve từ URL mới  
C. Server bị down  
D. Authentication required  

**Đáp án: B**  
*Giải thích: 301 Moved Permanently – object đã move đến URL mới. Response chứa Location header với new URL. Client software (browser) tự động redirect đến new URL.*

---

**Câu 159.** Trong POP3, lệnh nào được dùng để retrieve một message cụ thể?

A. GET  
B. FETCH  
C. retr  
D. DOWNLOAD  

**Đáp án: C**  
*Giải thích: Trong POP3 transaction phase, lệnh "retr [number]" dùng để retrieve (download) một message cụ thể. Các lệnh khác: list (liệt kê), dele (đánh dấu xóa), quit.*

---

**Câu 160.** Tại sao trong SMTP transcript, client gửi một dòng chỉ chứa dấu chấm "." trên một dòng riêng?

A. Để compress message  
B. Để indicate end of message (end of DATA)  
C. Để bắt đầu một message mới  
D. Để kiểm tra connection  

**Đáp án: B**  
*Giải thích: Trong SMTP, sau phần DATA, một dòng chỉ chứa "." (CRLF.CRLF) signal end of message. Server nhận dấu này và biết message đã complete.*

---

**Câu 161.** Tại sao local DNS servers thường có thể bypass root DNS servers?

A. Local servers có authority cao hơn root servers  
B. Local servers cache IP addresses của TLD servers từ previous queries; không cần hỏi root servers nếu đã biết TLD server  
C. Root servers block queries từ local servers  
D. Local servers resolve tất cả queries locally  

**Đáp án: B**  
*Giải thích: DNS caching cho phép local DNS server cache IPs của TLD servers. Với hầu hết queries, local server đã biết TLD server nào cần contact → bypass root servers hoàn toàn.*

---

**Câu 162.** Trong P2P circular DHT với n bits, identifier space có bao nhiêu possible values?

A. n values  
B. 2n values  
C. n² values  
D. 2^n values  

**Đáp án: D**  
*Giải thích: Identifier space là [0, 2^n - 1], có tổng 2^n possible integer values. Mỗi identifier được represent bằng n bits.*

---

**Câu 163.** IMAP có feature nào mà POP3 không có, hữu ích khi connection tới mail server có bandwidth thấp?

A. IMAP compress email  
B. IMAP cho phép fetch chỉ message header hoặc chỉ một part của MIME message, tránh download toàn bộ large attachments không cần thiết  
C. IMAP không cần authentication  
D. IMAP dùng UDP để nhanh hơn  

**Đáp án: B**  
*Giải thích: IMAP commands cho phép fetch chỉ headers hoặc specific parts của message. Hữu ích với low-bandwidth connections: user có thể xem subject/sender trước khi quyết định download full message.*

---

**Câu 164.** Tại sao Web servers sử dụng "stateless protocol" lại là lợi thế cho scalability?

A. Stateless giúp encrypt messages nhanh hơn  
B. Server không cần allocate resources để duy trì session state cho mỗi client; có thể handle nhiều concurrent connections hơn với cùng memory/processing  
C. Stateless giúp server verify client nhanh hơn  
D. Stateless giúp reduce bandwidth  

**Đáp án: B**  
*Giải thích: Stateless design: mỗi request self-contained, server xử lý xong là forget. Không cần maintain per-client state → tiết kiệm memory và processing → scale to thousands of concurrent connections.*

---

**Câu 165.** Trong BitTorrent, "choked" peers là gì?

A. Peers đã download xong file  
B. Peers không nhận chunks từ Alice (vì không trong top 4 uploaders và không phải optimistically unchoked peer hiện tại)  
C. Peers có bandwidth thấp  
D. Peers bị tracker block  

**Đáp án: B**  
*Giải thích: Alice unchoke 4 top uploaders và 1 random optimistic peer. Tất cả các peers khác là "choked" – không nhận chunks từ Alice trong interval đó.*

---

**Câu 166.** HTTP KHÔNG stateless hoàn toàn trong thực tế vì lý do gì?

A. Vì HTTP dùng TCP  
B. Vì cookies tạo user session layer trên HTTP stateless, cho phép server track users across multiple requests  
C. Vì persistent connections maintain state  
D. Vì SSL thêm state  

**Đáp án: B**  
*Giải thích: HTTP bản thân là stateless, nhưng cookies tạo một lớp "state" ở application level: server có thể identify và track user qua cookie ID, effectively creating session state.*

---

**Câu 167.** Trong DNS man-in-the-middle attack, attacker làm gì?

A. Attacker flood DNS servers với packets  
B. Attacker intercept queries từ hosts và return bogus replies, có thể redirect users đến attacker's website  
C. Attacker insert malicious records vào DNS server's cache  
D. Attacker tắt DNS servers  

**Đáp án: B**  
*Giải thích: Man-in-the-middle attack: attacker sit between client và DNS server, intercept legitimate queries và send bogus replies với attacker-controlled IPs, redirecting users.*

---

**Câu 168.** Trong DNS poisoning attack, attacker làm gì?

A. Attacker DDoS DNS servers  
B. Attacker gửi bogus replies đến DNS server, trick server accept và cache bogus records vào cache của nó  
C. Attacker intercept DNS queries  
D. Attacker thay đổi physical DNS server hardware  

**Đáp án: B**  
*Giải thích: DNS poisoning (cache poisoning): attacker inject bogus records vào DNS cache. Các hosts sau đó query server này sẽ nhận bogus records, bị redirect đến attacker's sites.*

---

**Câu 169.** Nếu thêm shortcuts vào circular DHT, có thể đạt được complexity O(log N) cho cả số neighbors và số messages. Tại sao O(log N) là acceptable?

A. O(log N) là tối ưu tuyệt đối  
B. O(log N) tăng rất chậm với N: với N = 1 triệu peers, log₂(1M) ≈ 20 neighbors và 20 messages – hoàn toàn manageable so với N = 1M  
C. O(log N) tương đương O(1)  
D. O(log N) không scalable  

**Đáp án: B**  
*Giải thích: O(log N) là excellent scaling. Dù N tăng 1000x, số neighbors/messages chỉ tăng thêm ~10. Đây là practical "sweet spot" giữa memory overhead (neighbors) và communication overhead (messages).*

---

**Câu 170.** Khi một trang web được phân phối qua CDN (như Akamai), request resolution xảy ra như thế nào?

A. Client trực tiếp connect đến Akamai headquarters  
B. DNS resolution được sử dụng để direct client đến CDN cache gần nhất; khi browser resolves hostname, Akamai's DNS trả về IP của cache server gần client nhất  
C. Client broadcast để tìm CDN node gần nhất  
D. CDN không liên quan đến DNS  

**Đáp án: B**  
*Giải thích: CDN dùng DNS-based redirection: khi client resolve content hostname, CDN's DNS server trả về IP của geographically/topologically close cache server, không phải origin. Đây là core CDN mechanism.*

---

**Câu 171.** Phân tích tại sao tit-for-tat là crucial cho sự tồn tại của BitTorrent:

A. Tit-for-tat encrypt data tốt hơn  
B. Nếu không có tit-for-tat (hoặc tương đương), majority of users sẽ là freeriders (chỉ download, không upload), làm sụp đổ hệ thống vì không đủ upload capacity để phân phối file  
C. Tit-for-tat giúp tìm file nhanh hơn  
D. Tit-for-tat giúp tracker track peers tốt hơn  

**Đáp án: B**  
*Giải thích: Tit-for-tat tạo incentive: nếu bạn không upload, không ai upload cho bạn. Điều này khuyến khích users contribute bandwidth. Nếu không có mechanism này, BitTorrent có thể fail vì freerider problem.*

---

**Câu 172.** Khi một FTP session bắt đầu, thứ tự các connections được thiết lập là gì?

A. Data connection trước, sau đó control connection  
B. Control connection (port 21) được thiết lập trước và maintain suốt session; data connection (port 20) được tạo mỗi khi cần transfer file  
C. Cả hai được thiết lập đồng thời  
D. Không cần control connection nếu đã authenticate  

**Đáp án: B**  
*Giải thích: Client initiate control connection đến server port 21 trước. Qua control connection, user gửi credentials và commands. Mỗi file transfer tạo một new data connection, sau đó close.*

---

**Câu 173.** Tại sao SMTP trong năm 2023 vẫn yêu cầu 7-bit ASCII cho message body là một "archaic characteristic"?

A. ASCII không secure  
B. Thiết kế 1982 khi bandwidth khan hiếm và không có multimedia; ngày nay không ai email chỉ text thuần ASCII; phải encode images/binary sang ASCII rồi decode lại – không cần thiết và inefficient  
C. ASCII không hỗ trợ Unicode  
D. ASCII không có error correction  

**Đáp án: B**  
*Giải thích: 7-bit ASCII limit là legacy constraint hợp lý năm 1982 nhưng problematic ngày nay: mọi attachment phải encode (Base64 thường) tăng kích thước 33%, và phải decode. HTTP không có hạn chế này.*

---

**Câu 174.** Trong P2P DHT, tại sao cần peer phải track cả first và second successors (không chỉ first successor) để handle churn?

A. Để tăng tốc độ query  
B. Nếu first successor đột ngột leave (peer churn), peer cần biết second successor để maintain connectivity trong ring; nếu chỉ track first successor, ring sẽ bị broken  
C. Để cân bằng load  
D. Để security  

**Đáp án: B**  
*Giải thích: P2P systems có high churn rate. Nếu peer chỉ biết first successor và successor đó leave đột ngột, peer không biết successor tiếp theo → ring bị broken. Second successor là backup cho continuity.*

---

**Câu 175.** Xét kịch bản: traffic intensity trên access link = 0.97. Nếu thêm Web cache với hit rate 0.3, traffic intensity mới trên access link là bao nhiêu?

A. 0.97  
B. 0.679  
C. 0.3  
D. 0.7  

**Đáp án: B**  
*Giải thích: Chỉ (1-0.3) = 70% requests đi qua access link. Traffic intensity mới = 0.97 × 0.7 = 0.679. Giảm từ 0.97 (gần bão hòa) xuống 0.679 (manageable).*

---

**Câu 176.** Điểm giống nhau cơ bản giữa HTTP và SMTP là gì?

A. Cả hai đều stateless  
B. Cả hai truyền files giữa các hosts dùng TCP, cả hai dùng persistent connections, cả hai dùng human-readable (ASCII) command/header format  
C. Cả hai dùng cùng port number  
D. Cả hai không cần authentication  

**Đáp án: B**  
*Giải thích: HTTP và SMTP: cả hai transfer files dùng TCP, dùng persistent connections, dùng ASCII-readable message format với headers và command lines. Khác nhau ở push/pull nature và ASCII restriction của SMTP.*

---

**Câu 177.** Tại sao application-layer protocol được phân biệt với network application?

A. Không có sự phân biệt  
B. Application-layer protocol (như HTTP) là chỉ một component của network application (như Web); Web application còn gồm HTML format, browsers, servers – protocol chỉ là "giao thức giao tiếp" của application  
C. Application-layer protocol là tầng dưới của application  
D. Network application không cần application-layer protocol  

**Đáp án: B**  
*Giải thích: Web application = HTML format + browsers (Firefox, Chrome) + web servers (Apache, Nginx) + HTTP protocol. HTTP là một piece (albeit important) chứ không phải toàn bộ Web application.*

---

**Câu 178.** Peer trong BitTorrent có thể "selfishly" leave torrent sau khi download xong. Điều gì ngăn mọi peer làm vậy?

A. BitTorrent protocol block peers rời torrent  
B. Không có mechanism kỹ thuật bắt buộc; sự thành công của BitTorrent phụ thuộc vào users altruistically ở lại seed; tit-for-tat incentivize sharing khi đang download nhưng không bắt buộc seeding  
C. Tracker track và block peers rời sớm  
D. ISP block peers rời torrent  

**Đáp án: B**  
*Giải thích: BitTorrent không có hard enforcement cho seeding sau khi download. Tit-for-tat hoạt động trong download phase (trading). Seeding sau đó là voluntary/altruistic. Đây cũng là lý do "leech vs seed ratio" quan trọng trong cộng đồng.*

---

**Câu 179.** Khi một Web page chứa 10 objects và browser mở 5 parallel TCP connections (non-persistent mode), cần bao nhiêu TCP connections và bao nhiêu RTTs để fetch tất cả?

A. 10 connections, 20 RTTs  
B. 11 connections tổng cộng (1 cho HTML + 10 cho objects); với parallel connections, chỉ cần 2 RTTs cho HTML + 2 RTTs cho 10 objects (2 rounds × 5 parallel)  
C. 5 connections, 10 RTTs  
D. 10 connections, 10 RTTs  

**Đáp án: B**  
*Giải thích: HTML: 1 connection, 2 RTTs. 10 objects với 5 parallel: 2 rounds (5+5), mỗi round 2 RTTs → 4 RTTs cho objects. Total: ~6 RTTs và 11 TCP connections. Parallel giảm đáng kể so với serial (20+ RTTs).*

---

**Câu 180.** Tại sao DNS được thiết kế là distributed system thay vì centralized?

A. Vì distributed systems rẻ hơn  
B. Centralized DNS sẽ có: single point of failure, không scale được với traffic volume khổng lồ, latency cao cho users xa, và maintenance database cực lớn cập nhật constant – tất cả không thể chấp nhận được với Internet scale  
C. Vì DNS không cần centralized authority  
D. Vì centralized DNS sẽ quá secure  

**Đáp án: B**  
*Giải thích: Centralized design fail ở Internet scale về reliability (SPOF), scalability (traffic), performance (latency), và maintainability. DNS hierarchical distributed design giải quyết tất cả issues này.*
