# Bộ câu hỏi trắc nghiệm — Chapter 3: Transport Layer Phần I,II
## (Kurose & Ross — Computer Networking: A Top-Down Approach)

---

## PHẦN 1: Section 3.1 — Introduction and Transport-Layer Services

**Câu 1.** Transport layer nằm ở vị trí nào trong kiến trúc phân tầng mạng?

A. Giữa physical layer và data link layer  
B. Giữa application layer và network layer  
C. Giữa data link layer và network layer  
D. Trên application layer  

**Đáp án: B**

*Giải thích: Transport layer nằm trực tiếp giữa application layer (tầng ứng dụng) và network layer (tầng mạng), đóng vai trò cầu nối cung cấp dịch vụ giao tiếp logic giữa các application processes trên các hosts khác nhau.*

---

**Câu 2.** "Logical communication" trong transport layer có nghĩa là gì?

A. Hai hosts được kết nối bằng một đường vật lý trực tiếp  
B. Từ góc nhìn của application, hai hosts như thể được kết nối trực tiếp, dù thực tế có thể qua nhiều routers  
C. Dữ liệu được mã hóa trước khi truyền  
D. Transport layer đảm bảo không có gói tin nào bị mất  

**Đáp án: B**

*Giải thích: "Logical communication" có nghĩa là từ góc nhìn của application process, chúng như thể giao tiếp trực tiếp với nhau, bất kể thực tế dữ liệu phải đi qua bao nhiêu routers và các loại kết nối vật lý khác nhau.*

---

**Câu 3.** Transport-layer protocols được thực thi (implemented) ở đâu?

A. Trong các routers trung gian  
B. Trong các switches  
C. Chỉ trong end systems (hosts)  
D. Cả trong routers và end systems  

**Đáp án: C**

*Giải thích: Transport-layer protocols chỉ được implemented trong end systems. Routers chỉ xử lý đến network-layer fields của datagram, không kiểm tra hay xử lý transport-layer segment bên trong.*

---

**Câu 4.** Quá trình transport layer chia application message thành các phần nhỏ hơn và gắn header vào mỗi phần được gọi là gì?

A. Fragmentation  
B. Encapsulation tạo ra transport-layer segment  
C. Multiplexing  
D. Demultiplexing  

**Đáp án: B**

*Giải thích: Phía gửi, transport layer nhận application message, có thể chia nhỏ thành các chunks và thêm transport-layer header vào mỗi chunk để tạo ra transport-layer segment (gói tin của transport layer).*

---

**Câu 5.** Điểm khác biệt cơ bản nhất giữa transport-layer protocol và network-layer protocol là gì?

A. Transport layer xử lý nhanh hơn network layer  
B. Transport layer cung cấp logical communication giữa các processes, trong khi network layer cung cấp logical communication giữa các hosts  
C. Network layer đáng tin cậy hơn transport layer  
D. Transport layer chỉ hoạt động trên Internet, còn network layer hoạt động trên mọi mạng  

**Đáp án: B**

*Giải thích: Đây là sự phân biệt then chốt: network layer cung cấp host-to-host delivery (giao tiếp giữa hai máy), còn transport layer mở rộng thành process-to-process delivery (giao tiếp giữa các tiến trình chạy trên máy).*

---

**Câu 6.** Trong ví dụ về hộ gia đình (household analogy), Ann và Bill tương ứng với thành phần nào?

A. Network-layer protocol  
B. Postal service (dịch vụ bưu điện)  
C. Transport-layer protocol  
D. Application layer  

**Đáp án: C**

*Giải thích: Ann và Bill là người thu/phân phát thư trong nội bộ mỗi nhà (end system), tương ứng với transport-layer protocol. Dịch vụ bưu điện vận chuyển thư giữa hai nhà (house-to-house) tương ứng với network-layer protocol.*

---

**Câu 7.** Theo ví dụ household analogy, "postal service" tương ứng với thành phần nào?

A. Transport-layer protocol  
B. Application process  
C. Network-layer protocol  
D. Physical layer  

**Đáp án: C**

*Giải thích: Dịch vụ bưu điện vận chuyển thư từ nhà này sang nhà khác (house-to-house), tương ứng với network-layer protocol cung cấp host-to-host delivery.*

---

**Câu 8.** Dịch vụ nào mà transport protocol có thể cung cấp dù network layer không cung cấp?

A. Giảm độ trễ truyền dẫn  
B. Tăng băng thông kênh truyền  
C. Reliable data transfer ngay cả khi network layer không đáng tin cậy  
D. Định tuyến (routing) gói tin  

**Đáp án: C**

*Giải thích: Một ví dụ điển hình: TCP cung cấp reliable data transfer dù IP (network layer) là unreliable. Transport protocol cũng có thể dùng encryption để đảm bảo confidentiality dù network layer không đảm bảo điều này.*

---

**Câu 9.** Internet cung cấp bao nhiêu transport-layer protocol cho application layer?

A. Một (chỉ TCP)  
B. Hai (TCP và UDP)  
C. Ba (TCP, UDP, và IP)  
D. Bốn  

**Đáp án: B**

*Giải thích: Internet cung cấp hai transport-layer protocols: UDP (User Datagram Protocol — unreliable, connectionless) và TCP (Transmission Control Protocol — reliable, connection-oriented).*

---

**Câu 10.** IP service model được mô tả là gì?

A. Reliable delivery service  
B. Connection-oriented service  
C. Best-effort delivery service  
D. Guaranteed bandwidth service  

**Đáp án: C**

*Giải thích: IP là "best-effort delivery service" — nó cố gắng hết sức để deliver segment nhưng không đảm bảo: không đảm bảo delivery, không đảm bảo thứ tự, và không đảm bảo tính toàn vẹn của dữ liệu. Vì vậy IP được coi là unreliable service.*

---

**Câu 11.** Trách nhiệm cơ bản nhất (most fundamental responsibility) của cả UDP và TCP là gì?

A. Mã hóa dữ liệu  
B. Mở rộng host-to-host delivery của IP thành process-to-process delivery (transport-layer multiplexing và demultiplexing)  
C. Định tuyến gói tin qua mạng  
D. Kiểm soát tắc nghẽn  

**Đáp án: B**

*Giải thích: Cả UDP và TCP đều phải thực hiện multiplexing/demultiplexing để mở rộng dịch vụ IP (host-to-host) thành dịch vụ process-to-process. Đây là chức năng tối thiểu bắt buộc của transport layer.*

---

**Câu 12.** UDP cung cấp những dịch vụ tối thiểu nào?

A. Reliable data transfer và congestion control  
B. Process-to-process data delivery và error checking  
C. Connection establishment và flow control  
D. Encryption và authentication  

**Đáp án: B**

*Giải thích: UDP chỉ cung cấp hai dịch vụ tối thiểu: (1) process-to-process data delivery thông qua multiplexing/demultiplexing, và (2) error checking thông qua checksum. UDP không cung cấp reliable transfer, congestion control hay connection establishment.*

---

**Câu 13.** TCP cung cấp thêm dịch vụ gì so với UDP? (Chọn câu đúng nhất)

A. Chỉ reliable data transfer  
B. Reliable data transfer và congestion control  
C. Chỉ congestion control  
D. Fast delivery và low latency  

**Đáp án: B**

*Giải thích: TCP cung cấp thêm (1) reliable data transfer sử dụng flow control, sequence numbers, acknowledgments, timers; và (2) congestion control để ngăn một TCP connection làm ngập mạng. Congestion control là dịch vụ phục vụ cho cả Internet, không chỉ cho ứng dụng.*

---

**Câu 14.** Tại sao thuật ngữ "segment" được dùng cho cả TCP và UDP packets trong sách giáo khoa này?

A. Vì chúng có cùng cấu trúc header  
B. Để tránh nhầm lẫn với thuật ngữ "datagram" vốn được dùng cho network-layer packet  
C. Vì đây là thuật ngữ chuẩn trong mọi RFC  
D. Vì TCP và UDP có cùng kích thước tối đa  

**Đáp án: B**

*Giải thích: Sách chọn dùng "segment" cho cả TCP và UDP packets để tránh nhầm lẫn, vì "datagram" đã được dùng cho network-layer packet. Thực tế, các RFC thường dùng "segment" cho TCP và "datagram" cho UDP.*

---

**Câu 15.** Nếu network-layer protocol không thể đảm bảo delay hay bandwidth, thì transport protocol có thể đảm bảo điều này không?

A. Có, TCP có thể đảm bảo cả delay và bandwidth  
B. Có, nhưng chỉ UDP mới làm được điều này  
C. Không, vì services của transport protocol bị ràng buộc bởi service model của network layer  
D. Có, thông qua cơ chế congestion control  

**Đáp án: C**

*Giải thích: Services mà transport protocol có thể cung cấp thường bị ràng buộc bởi service model của underlying network-layer protocol. Tuy nhiên, có những dịch vụ nhất định (như reliable transfer hay encryption) vẫn có thể được cung cấp dù network layer không hỗ trợ.*

---

## PHẦN 2: Section 3.2 — Multiplexing and Demultiplexing

**Câu 16.** Demultiplexing là gì?

A. Quá trình thu thập dữ liệu từ nhiều sockets và đóng gói thành segments  
B. Quá trình phân phối dữ liệu từ transport-layer segment đến đúng socket  
C. Quá trình chia nhỏ application message thành các segments  
D. Quá trình mã hóa dữ liệu trước khi gửi  

**Đáp án: B**

*Giải thích: Demultiplexing là công việc deliver dữ liệu trong transport-layer segment đến đúng socket tại receiving host. Transport layer kiểm tra các fields trong segment để xác định socket đích.*

---

**Câu 17.** Multiplexing là gì?

A. Quá trình giải mã dữ liệu nhận được  
B. Quá trình thu thập dữ liệu từ nhiều sockets, đóng gói với header information, và chuyển xuống network layer  
C. Quá trình kiểm tra lỗi trong segment  
D. Quá trình thiết lập kết nối TCP  

**Đáp án: B**

*Giải thích: Multiplexing là việc gathering data chunks từ các sockets khác nhau ở source host, encapsulating mỗi chunk với header information (để dùng cho demultiplexing sau này), tạo segments và chuyển xuống network layer.*

---

**Câu 18.** Port numbers có kích thước bao nhiêu bit?

A. 8-bit  
B. 16-bit  
C. 32-bit  
D. 64-bit  

**Đáp án: B**

*Giải thích: Mỗi port number là một số 16-bit, có giá trị từ 0 đến 65535.*

---

**Câu 19.** Well-known port numbers là những port nào?

A. 0 đến 255  
B. 0 đến 1023  
C. 1024 đến 49151  
D. 49152 đến 65535  

**Đáp án: B**

*Giải thích: Port numbers từ 0 đến 1023 được gọi là well-known port numbers, được dành riêng cho các well-known application protocols như HTTP (port 80) và FTP (port 21).*

---

**Câu 20.** HTTP sử dụng port number nào theo mặc định?

A. 21  
B. 53  
C. 80  
D. 443  

**Đáp án: C**

*Giải thích: HTTP sử dụng well-known port number 80. FTP dùng port 21, DNS dùng port 53.*

---

**Câu 21.** Khi tạo UDP socket và không bind port cụ thể, transport layer sẽ tự động gán port number trong khoảng nào?

A. 0 đến 1023  
B. 1024 đến 65535  
C. 49152 đến 65535  
D. 32768 đến 65535  

**Đáp án: B**

*Giải thích: Transport layer tự động gán một port number trong range 1024 đến 65535 mà hiện chưa được dùng bởi UDP port nào khác trong host đó.*

---

**Câu 22.** Một UDP socket được xác định đầy đủ bởi những gì?

A. Chỉ destination port number  
B. Source IP address và source port number  
C. Destination IP address và destination port number  
D. Source IP, source port, destination IP, và destination port  

**Đáp án: C**

*Giải thích: UDP socket được xác định đầy đủ bởi một 2-tuple: (destination IP address, destination port number). Hệ quả: hai UDP segments có source IP/port khác nhau nhưng cùng destination IP và destination port sẽ được gửi đến cùng một socket.*

---

**Câu 23.** Nếu hai UDP segments có cùng destination IP address và destination port number nhưng khác source IP address, chúng sẽ được xử lý như thế nào?

A. Bị loại bỏ vì conflict  
B. Gửi đến hai sockets khác nhau  
C. Gửi đến cùng một destination socket  
D. Được merge lại thành một segment  

**Đáp án: C**

*Giải thích: Vì UDP socket được xác định bởi 2-tuple (destination IP, destination port), hai segments có cùng destination sẽ đi đến cùng một socket, bất kể source khác nhau.*

---

**Câu 24.** Source port number trong UDP segment phục vụ mục đích gì chính?

A. Xác định ứng dụng gửi trên máy nguồn  
B. Đóng vai trò "return address" để receiver có thể gửi reply lại  
C. Tính checksum  
D. Xác định thứ tự của segment  

**Đáp án: B**

*Giải thích: Source port number đóng vai trò "return address" — khi B muốn reply cho A, B sẽ dùng source port của A-to-B segment làm destination port trong B-to-A segment.*

---

**Câu 25.** Một TCP socket được xác định đầy đủ bởi bao nhiêu giá trị?

A. 2 (destination IP và destination port)  
B. 3 (source IP, destination IP, destination port)  
C. 4 (source IP, source port, destination IP, destination port)  
D. 1 (chỉ destination port)  

**Đáp án: C**

*Giải thích: TCP socket được xác định bởi 4-tuple: (source IP address, source port number, destination IP address, destination port number). Đây là điểm khác biệt quan trọng so với UDP chỉ cần 2-tuple.*

---

**Câu 26.** Hai TCP segments đến từ cùng destination port nhưng khác source IP address sẽ được demultiplex đến đâu?

A. Cùng một socket  
B. Hai sockets khác nhau  
C. Bị loại bỏ  
D. Gửi đến welcoming socket  

**Đáp án: B**

*Giải thích: Vì TCP dùng 4-tuple để demultiplex, hai segments có source IP khác nhau sẽ đi đến hai sockets khác nhau. Đây là khác biệt quan trọng so với UDP.*

---

**Câu 27.** Trong TCP server, "welcoming socket" (hay server socket) có vai trò gì?

A. Xử lý tất cả dữ liệu từ clients  
B. Chờ đợi connection-establishment requests từ TCP clients  
C. Lưu trữ dữ liệu đã nhận  
D. Thực hiện error checking  

**Đáp án: B**

*Giải thích: Welcoming socket (server socket) chỉ có nhiệm vụ chờ connection-establishment requests từ clients. Khi có request, server tạo một connection socket mới để xử lý kết nối đó.*

---

**Câu 28.** Khi host C có hai HTTP connections đến server B, cả hai dùng destination port 80. Server B phân biệt chúng như thế nào?

A. Qua timestamp của kết nối  
B. Không thể phân biệt được  
C. Qua source IP address và source port number  
D. Qua sequence number  

**Đáp án: C**

*Giải thích: Server B dùng 4-tuple để demultiplex: tuy cùng destination port 80, nhưng hai connections từ Host C có source port khác nhau (26145 và 7532), nên server tạo hai connection sockets khác nhau.*

---

**Câu 29.** Với persistent HTTP, client và server dùng bao nhiêu TCP connection socket?

A. Một socket mới cho mỗi request/response  
B. Cùng một server socket trong suốt thời gian kết nối  
C. Hai sockets — một gửi, một nhận  
D. Số sockets bằng số request  

**Đáp án: B**

*Giải thích: Với persistent HTTP, client và server exchange HTTP messages qua cùng một server socket trong suốt thời gian của persistent connection. Non-persistent HTTP thì ngược lại — tạo và đóng một TCP connection mới cho mỗi request/response.*

---

**Câu 30.** Điều gì xảy ra khi Web server dùng non-persistent HTTP về mặt socket?

A. Chỉ cần một socket cho toàn bộ session  
B. Một TCP connection (và socket) mới được tạo và đóng cho mỗi request/response  
C. Server dùng UDP thay vì TCP  
D. Tất cả requests dùng chung một socket  

**Đáp án: B**

*Giải thích: Non-persistent HTTP tạo và đóng một TCP connection mới cho mỗi cặp request/response. Việc tạo và đóng socket liên tục này có thể ảnh hưởng nghiêm trọng đến hiệu năng của busy Web server.*

---

**Câu 31.** Tại sao multiplexing/demultiplexing không chỉ là vấn đề của Internet transport protocols?

A. Vì tất cả protocols đều dùng port numbers  
B. Vì đây là vấn đề phát sinh bất cứ khi nào một single protocol ở một tầng được dùng bởi nhiều protocols ở tầng trên  
C. Vì chỉ UDP mới cần demultiplexing  
D. Vì routers cũng cần multiplexing  

**Đáp án: B**

*Giải thích: Multiplexing/demultiplexing là vấn đề cần thiết cho mọi mạng máy tính, bất cứ khi nào một single protocol ở một tầng phục vụ nhiều protocols ở tầng cao hơn.*

---

**Câu 32.** Port scanning (ví dụ dùng nmap) hoạt động dựa trên nguyên lý nào?

A. Giải mã traffic của mạng  
B. Xác định ports nào đang mở (accepting connections) để suy ra applications đang chạy  
C. Tấn công brute force vào server  
D. Kiểm tra địa chỉ MAC của thiết bị  

**Đáp án: B**

*Giải thích: Port scanners như nmap tuần tự kiểm tra các ports để xác định port nào đang open (accepting TCP connections hoặc responding to UDP). Từ đó có thể map port đến application đang chạy.*

---

---

