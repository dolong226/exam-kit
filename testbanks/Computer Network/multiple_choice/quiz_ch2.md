# Bộ câu hỏi trắc nghiệm - Chapter 2: Application Layer

---

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

