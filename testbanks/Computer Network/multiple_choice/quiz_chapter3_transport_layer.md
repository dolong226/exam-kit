# Bộ câu hỏi trắc nghiệm — Chapter 3: Transport Layer
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

## PHẦN 3: Section 3.3 — Connectionless Transport: UDP

**Câu 33.** UDP được định nghĩa trong RFC nào?

A. RFC 793  
B. RFC 768  
C. RFC 1700  
D. RFC 1071  

**Đáp án: B**

*Giải thích: UDP được định nghĩa trong RFC 768.*

---

**Câu 34.** Tại sao UDP được gọi là "connectionless"?

A. Vì UDP không có checksum  
B. Vì không có handshaking giữa sending và receiving transport-layer entities trước khi gửi segment  
C. Vì UDP không dùng port numbers  
D. Vì UDP không thể truyền dữ liệu lớn  

**Đáp án: B**

*Giải thích: UDP là connectionless vì không có bước handshaking (thiết lập kết nối) nào giữa sender và receiver trước khi gửi segment. UDP "blasts away" không cần formal preliminaries.*

---

**Câu 35.** UDP header có bao nhiêu fields, mỗi field bao nhiêu bytes?

A. 6 fields, mỗi field 2 bytes  
B. 4 fields, mỗi field 2 bytes  
C. 4 fields, mỗi field 4 bytes  
D. 8 fields, mỗi field 1 byte  

**Đáp án: B**

*Giải thích: UDP header chỉ có 4 fields, mỗi field 2 bytes: source port, destination port, length, và checksum. Tổng cộng 8 bytes overhead.*

---

**Câu 36.** Field "length" trong UDP segment chỉ định điều gì?

A. Kích thước chỉ của data field  
B. Số bytes trong toàn bộ UDP segment (header + data)  
C. Số lượng packets trong message  
D. Kích thước của IP datagram chứa segment  

**Đáp án: B**

*Giải thích: Length field chỉ định số bytes trong toàn bộ UDP segment, bao gồm cả header. Cần có field này vì data field có thể có kích thước khác nhau giữa các segments.*

---

**Câu 37.** UDP checksum được tính như thế nào?

A. CRC của toàn bộ packet  
B. 1s complement của tổng tất cả các 16-bit words trong segment  
C. MD5 hash của data  
D. XOR của tất cả bytes trong segment  

**Đáp án: B**

*Giải thích: UDP sender tính 1s complement của tổng tất cả 16-bit words trong segment (với overflow được wrapped around), đặt kết quả vào checksum field. Receiver cộng tất cả 16-bit words (kể cả checksum) — nếu không có lỗi, kết quả sẽ là toàn bộ 1s (1111111111111111).*

---

**Câu 38.** Tại sao UDP cần checksum dù nhiều link-layer protocols cũng đã có error checking?

A. Vì UDP checksum nhanh hơn  
B. Vì không phải tất cả links đều có error checking, và bit errors có thể xảy ra khi segment được lưu trong router memory  
C. Vì link-layer checksum không đủ độ chính xác  
D. Vì đây là yêu cầu bắt buộc của RFC  

**Đáp án: B**

*Giải thích: Đây là ví dụ về end-end principle: không phải mọi link đều cung cấp error checking, và errors có thể xảy ra trong router memory. Vì vậy UDP phải tự cung cấp error detection ở transport layer như một "safety measure".*

---

**Câu 39.** "End-end principle" trong thiết kế hệ thống phát biểu điều gì?

A. Error checking chỉ cần thực hiện ở end systems  
B. Certain functionality phải được implemented on an end-end basis; functions ở lower levels có thể redundant nếu chúng ta đã có chúng ở higher level  
C. Routers không cần thực hiện error checking  
D. Tất cả protocols phải hoạt động end-to-end  

**Đáp án: B**

*Giải thích: End-end principle (Saltzer 1984) phát biểu rằng vì certain functionality (như error detection) phải được implemented on an end-end basis, các functions ở lower levels có thể redundant hoặc ít giá trị so với chi phí thực hiện chúng ở higher level.*

---

**Câu 40.** Khi UDP nhận được segment có lỗi (damaged), UDP xử lý như thế nào?

A. Yêu cầu retransmission  
B. Tự sửa lỗi  
C. Discard segment hoặc chuyển lên application với cảnh báo — nhưng không recover  
D. Gửi NAK về sender  

**Đáp án: C**

*Giải thích: UDP cung cấp error detection (checksum) nhưng không recover from errors. Một số implementations discard damaged segment, một số khác chuyển lên application với warning.*

---

**Câu 41.** Lý do nào sau đây khiến application developer chọn UDP thay vì TCP?

A. UDP đảm bảo delivery còn TCP thì không  
B. UDP có connection state giúp theo dõi packets  
C. UDP có finer application-level control, no connection establishment delay, no connection state, và smaller header overhead  
D. UDP có congestion control tốt hơn TCP  

**Đáp án: C**

*Giải thích: Có 4 lý do chính để chọn UDP: (1) finer control về data gửi và thời điểm gửi, (2) không có connection establishment delay, (3) không có connection state (server hỗ trợ nhiều clients hơn), (4) header overhead nhỏ hơn (8 bytes vs 20 bytes của TCP).*

---

**Câu 42.** TCP segment có bao nhiêu bytes header overhead so với UDP?

A. TCP: 8 bytes, UDP: 20 bytes  
B. TCP: 20 bytes, UDP: 8 bytes  
C. TCP: 32 bytes, UDP: 16 bytes  
D. TCP: 16 bytes, UDP: 8 bytes  

**Đáp án: B**

*Giải thích: TCP segment có 20 bytes header overhead trong mỗi segment, trong khi UDP chỉ có 8 bytes. Đây là một trong những lý do UDP được ưu tiên cho applications cần nhỏ gọn.*

---

**Câu 43.** DNS thường dùng UDP thay vì TCP vì lý do gì?

A. UDP đảm bảo tính toàn vẹn dữ liệu tốt hơn  
B. UDP không cần connection establishment, tránh delay khi query — nếu không nhận reply thì ứng dụng tự thử lại  
C. DNS messages quá lớn cho TCP  
D. TCP không hỗ trợ DNS protocol  

**Đáp án: B**

*Giải thích: DNS dùng UDP vì không cần connection establishment (tránh TCP's three-way handshake delay). Nếu DNS query bị mất, ứng dụng tự thử gửi đến name server khác hoặc retry — không cần TCP's reliable delivery.*

---

**Câu 44.** Tại sao việc sử dụng UDP cho multimedia applications (như video streaming) còn gây tranh cãi?

A. UDP quá chậm cho multimedia  
B. UDP không có congestion control, có thể gây high loss rates và "crowd out" TCP sessions  
C. UDP không hỗ trợ multicasting  
D. UDP không thể truyền audio  

**Đáp án: B**

*Giải thích: UDP không có congestion control. Nếu mọi người đều stream video qua UDP không kiểm soát, sẽ có quá nhiều packet overflow tại routers, gây loss rates cao và ảnh hưởng đến TCP sessions vốn có congestion control (TCP sẽ giảm rate).*

---

**Câu 45.** Ứng dụng nào sau đây thường chạy trên UDP? (Chọn đáp án đúng nhất)

A. HTTP, FTP, Email  
B. DNS, SNMP, RIP routing protocol, multimedia  
C. Telnet, SSH, HTTPS  
D. Tất cả ứng dụng Internet  

**Đáp án: B**

*Giải thích: UDP thường được dùng cho: DNS (name translation), SNMP (network management), RIP (routing protocol), NFS (remote file server), và nhiều multimedia applications. HTTP, FTP, Email, Telnet đều dùng TCP.*

---

**Câu 46.** Một application có thể có reliable data transfer khi dùng UDP không?

A. Không, hoàn toàn không thể  
B. Có, nếu built reliability (acknowledgments, retransmission) vào chính application  
C. Có, nhưng chỉ với UDP version 2  
D. Không, vì UDP header không hỗ trợ sequence numbers  

**Đáp án: B**

*Giải thích: Có thể có reliable data transfer qua UDP nếu reliability được build trực tiếp vào application (thêm acknowledgment và retransmission mechanisms). Điều này cho phép application vừa có reliable transfer vừa tránh TCP's congestion control constraints — nhưng đây là công việc phức tạp.*

---

**Câu 47.** Tại sao các real-time applications như Internet phone phản ứng kém với TCP's congestion control?

A. TCP quá phức tạp cho real-time applications  
B. TCP throttles sender khi congestion, gây delay — real-time apps cần minimum sending rate và không thể tolerate quá nhiều delay  
C. TCP không thể truyền audio  
D. TCP header quá lớn cho audio data  

**Đáp án: B**

*Giải thích: Real-time applications cần minimum sending rate và không muốn delay segment transmission. TCP's congestion control mechanism throttles sender khi có congestion, điều này không phù hợp. Các ứng dụng này cũng có thể tolerate một ít data loss, nên TCP's reliable delivery không cần thiết.*

---

**Câu 48.** Overflow trong UDP checksum calculation được xử lý như thế nào?

A. Bị bỏ qua  
B. Được wrapped around (cộng bit carry vào kết quả)  
C. Gây lỗi và restart checksum  
D. Segment bị discard  

**Đáp án: B**

*Giải thích: Khi tính tổng các 16-bit words, nếu có overflow (carry bit), bit đó được wrapped around — cộng vào sum. Sau đó lấy 1s complement của sum để ra checksum.*

---

---

## PHẦN 4: Section 3.4 — Principles of Reliable Data Transfer

**Câu 49.** Tại sao vấn đề reliable data transfer được coi là một trong những vấn đề quan trọng nhất trong networking?

A. Vì nó chỉ ảnh hưởng đến TCP  
B. Vì nó xảy ra không chỉ ở transport layer mà còn ở link layer và application layer — là vấn đề trung tâm của networking  
C. Vì nó là vấn đề khó giải quyết nhất về mặt toán học  
D. Vì nó liên quan đến bảo mật mạng  

**Đáp án: B**

*Giải thích: Reliable data transfer là vấn đề trung tâm vì nó xuất hiện ở nhiều tầng: transport layer (TCP), link layer, và application layer. Hiểu nguyên lý này là nền tảng để hiểu toàn bộ networking.*

---

**Câu 50.** rdt1.0 là protocol cho channel như thế nào?

A. Channel có bit errors  
B. Channel có thể mất packets  
C. Channel hoàn toàn reliable (perfectly reliable channel)  
D. Channel có reordering  

**Đáp án: C**

*Giải thích: rdt1.0 là protocol đơn giản nhất, giả định underlying channel hoàn toàn reliable — không có bit errors, không mất packets. FSM của nó chỉ có một state ở mỗi phía.*

---

**Câu 51.** Trong rdt1.0, receiver có cần gửi feedback về sender không?

A. Có, gửi ACK cho mỗi packet  
B. Có, gửi NAK nếu có lỗi  
C. Không, vì channel perfectly reliable nên không có gì sai được  
D. Có, gửi sequence number  

**Đáp án: C**

*Giải thích: Với perfectly reliable channel, receiver không cần gửi bất kỳ feedback nào về sender. Không có gì có thể xảy ra sai, nên không cần ACK hay NAK.*

---

**Câu 52.** ARQ (Automatic Repeat reQuest) protocols dựa trên những cơ chế nào?

A. Chỉ checksums  
B. Error detection, receiver feedback (ACK/NAK), và retransmission  
C. Sequence numbers và timers  
D. Flow control và congestion control  

**Đáp án: B**

*Giải thích: ARQ protocols yêu cầu ba cơ chế: (1) Error detection để receiver phát hiện bit errors, (2) Receiver feedback (ACK/NAK) để thông báo cho sender, (3) Retransmission để sender gửi lại packet lỗi.*

---

**Câu 53.** Trong rdt2.0, khi receiver nhận được packet không bị lỗi, nó gửi gì?

A. NAK  
B. ACK  
C. Sequence number  
D. Không gửi gì  

**Đáp án: B**

*Giải thích: Receiver gửi ACK (positive acknowledgment) khi packet nhận được không bị lỗi, và NAK (negative acknowledgment) khi packet bị corrupt.*

---

**Câu 54.** rdt2.0 có "fatal flaw" (lỗi chết người) nào?

A. Không thể xử lý packet loss  
B. Không xử lý được trường hợp ACK/NAK bị corrupt  
C. Không có sequence numbers  
D. Quá chậm vì stop-and-wait  

**Đáp án: B**

*Giải thích: rdt2.0 không xử lý khả năng ACK hoặc NAK bị corrupt. Nếu ACK/NAK bị lỗi, sender không biết receiver đã nhận đúng hay chưa và không thể quyết định gửi lại hay tiếp tục.*

---

**Câu 55.** Stop-and-wait protocol là gì?

A. Protocol dừng hoàn toàn khi có lỗi  
B. Protocol chỉ gửi packet mới khi đã nhận ACK cho packet trước đó  
C. Protocol chờ timeout trước khi gửi  
D. Protocol dừng khi receiver buffer đầy  

**Đáp án: B**

*Giải thích: Stop-and-wait protocol: sender gửi một packet, rồi chờ (stop) cho đến khi nhận ACK từ receiver trước khi gửi packet tiếp theo (wait). rdt2.0 là một stop-and-wait protocol.*

---

**Câu 56.** Giải pháp nào được chọn trong rdt2.1 để xử lý ACK/NAK bị corrupt?

A. Bỏ qua corrupt ACK/NAK  
B. Thêm sequence numbers để receiver phân biệt packet mới hay retransmission  
C. Dùng nhiều checksums hơn  
D. Tăng timeout  

**Đáp án: B**

*Giải thích: rdt2.1 thêm sequence numbers vào data packets. Khi sender nhận ACK/NAK bị corrupt, nó retransmit packet với cùng sequence number. Receiver dùng sequence number để phân biệt packet mới hay duplicate/retransmission.*

---

**Câu 57.** Trong rdt2.1 (stop-and-wait), bao nhiêu bit sequence number là đủ và tại sao?

A. 4 bits, vì cần 16 sequence numbers  
B. 1 bit, vì chỉ cần phân biệt packet hiện tại (0 hoặc 1)  
C. 8 bits, vì cần nhiều sequence numbers  
D. 32 bits, để tương thích với TCP  

**Đáp án: B**

*Giải thích: Với stop-and-wait, 1-bit sequence number là đủ. Receiver chỉ cần biết packet nhận được là packet hiện tại (sequence number khớp) hay retransmission của packet trước (sequence number trùng). Chỉ cần hai giá trị: 0 và 1.*

---

**Câu 58.** Sự khác biệt chính giữa rdt2.1 và rdt2.2 là gì?

A. rdt2.2 thêm timers  
B. rdt2.2 loại bỏ NAK — receiver chỉ gửi ACK với sequence number của packet được acknowledge, thay vì gửi NAK  
C. rdt2.2 dùng 2-bit sequence number  
D. rdt2.2 hỗ trợ pipelining  

**Đáp án: B**

*Giải thích: rdt2.2 là NAK-free protocol. Thay vì gửi NAK, receiver gửi ACK cho packet cuối cùng nhận đúng. Nếu sender nhận duplicate ACK (hai ACK cho cùng một packet), nó biết receiver chưa nhận đúng packet tiếp theo.*

---

**Câu 59.** rdt3.0 giải quyết thêm vấn đề gì so với rdt2.2?

A. Bit errors trong data  
B. Corrupt ACK/NAK  
C. Packet loss (mất gói tin hoàn toàn)  
D. Reordering của packets  

**Đáp án: C**

*Giải thích: rdt3.0 xử lý channel có thể vừa corrupt bits vừa mất packets. rdt3.0 thêm countdown timer để detect packet loss — nếu không nhận ACK trong thời gian nhất định, sender retransmit.*

---

**Câu 60.** Trong rdt3.0, tại sao không thể chờ quá lâu trước khi retransmit?

A. Timer sẽ bị hỏng  
B. Receiver sẽ timeout  
C. Worst-case delay rất khó ước lượng, và protocol nên recover từ packet loss càng sớm càng tốt  
D. Congestion window sẽ giảm  

**Đáp án: C**

*Giải thích: Worst-case maximum delay rất khó ước lượng trong thực tế. Hơn nữa, protocol nên recover từ loss càng nhanh càng tốt. Nên trong thực tế, sender chọn một timeout value mà loss là "likely, although not guaranteed" đã xảy ra.*

---

**Câu 61.** Tại sao rdt3.0 còn được gọi là "alternating-bit protocol"?

A. Vì packet sequence numbers luân phiên giữa 0 và 1  
B. Vì sender và receiver luân phiên gửi  
C. Vì bits trong header luân phiên giữa 0 và 1  
D. Vì ACK và NAK luân phiên  

**Đáp án: A**

*Giải thích: Sequence numbers trong rdt3.0 luân phiên giữa 0 và 1 (chỉ dùng 1-bit sequence number), nên còn được gọi là "alternating-bit protocol".*

---

**Câu 62.** Khi sender trong rdt3.0 không nhận ACK và timeout, nó không biết điều gì?

A. IP address của receiver  
B. Liệu data packet bị mất, ACK bị mất, hay chỉ bị delay quá lâu  
C. Sequence number nào cần dùng  
D. Kích thước của packet  

**Đáp án: B**

*Giải thích: Từ góc nhìn của sender, khi timeout và không có ACK, nó không thể biết: data packet bị mất, ACK của receiver bị mất, hay cả hai chỉ bị delay. Trong mọi trường hợp, hành động là như nhau: retransmit.*

---

**Câu 63.** Vấn đề hiệu năng cơ bản của rdt3.0 (stop-and-wait) là gì?

A. Không xử lý được bit errors  
B. Sender utilization rất thấp vì phải chờ ACK trước khi gửi packet tiếp theo  
C. Sequence numbers bị overflow  
D. Checksum không đủ mạnh  

**Đáp án: B**

*Giải thích: Với stop-and-wait, sender chỉ gửi được một packet rồi ngồi chờ. Trong ví dụ (RTT=30ms, L/R=0.008ms), Usender = 0.00027 — chỉ 0.027% thời gian sender thực sự gửi dữ liệu. Throughput thực tế chỉ 267 kbps trên đường 1 Gbps!*

---

**Câu 64.** Pipelining giải quyết vấn đề hiệu năng của stop-and-wait như thế nào?

A. Tăng tốc độ xử lý tại receiver  
B. Cho phép sender gửi nhiều packets mà không cần chờ ACK, tăng utilization  
C. Giảm kích thước header  
D. Loại bỏ việc cần checksum  

**Đáp án: B**

*Giải thích: Pipelining cho phép sender truyền nhiều packets liên tiếp ("fill the pipeline") mà không phải chờ ACK từng cái. Nếu gửi được 3 packets trước khi chờ ACK, utilization tăng gấp 3 lần.*

---

**Câu 65.** Pipelining đặt ra những yêu cầu gì so với stop-and-wait?

A. Không có yêu cầu mới  
B. Cần range of sequence numbers lớn hơn, sender và receiver phải buffer nhiều packet hơn  
C. Chỉ cần 1-bit sequence number  
D. Không cần checksum nữa  

**Đáp án: B**

*Giải thích: Pipelining đòi hỏi: (1) Range of sequence numbers lớn hơn (mỗi in-transit packet cần sequence number unique), (2) Sender phải buffer packets đã gửi nhưng chưa được ACK, (3) Receiver cũng có thể cần buffer correctly received packets.*

---

**Câu 66.** Trong GBN (Go-Back-N), "N" biểu thị điều gì?

A. Số lượng total packets được gửi  
B. Window size — số lượng maximum unacknowledged packets in the pipeline  
C. Number of retransmissions allowed  
D. Số sequence numbers có thể dùng  

**Đáp án: B**

*Giải thích: N là window size trong GBN — số lượng tối đa packets đã gửi nhưng chưa được ACK có thể tồn tại đồng thời trong pipeline. GBN là một sliding-window protocol.*

---

**Câu 67.** Trong GBN, khi có timeout, sender xử lý như thế nào?

A. Chỉ gửi lại packet bị mất  
B. Gửi lại tất cả packets đã gửi nhưng chưa được ACK  
C. Dừng gửi và chờ ACK  
D. Tăng window size  

**Đáp án: B**

*Giải thích: Đây là lý do tên gọi "Go-Back-N" — khi timeout, sender "go back" và gửi lại TẤT CẢ packets đã gửi nhưng chưa ACK, không chỉ packet bị mất. Sender dùng single timer cho oldest unacknowledged packet.*

---

**Câu 68.** Trong GBN, receiver xử lý out-of-order packets như thế nào?

A. Buffer lại và chờ packet còn thiếu  
B. Discard (loại bỏ) và gửi lại ACK cho packet in-order gần nhất  
C. Chấp nhận và gửi selective ACK  
D. Gửi NAK cho packet bị mất  

**Đáp án: B**

*Giải thích: GBN receiver discard tất cả out-of-order packets và gửi ACK cho packet in-order gần nhất đã nhận đúng. Điều này đơn giản hóa receiver (không cần buffer), nhưng có thể gây retransmit nhiều packets không cần thiết.*

---

**Câu 69.** ACK trong GBN là loại gì?

A. Selective ACK (chỉ ACK từng packet riêng lẻ)  
B. Cumulative ACK (ACK cho tất cả packets đến và bao gồm sequence number n)  
C. Negative ACK  
D. Piggybacked ACK  

**Đáp án: B**

*Giải thích: GBN dùng cumulative acknowledgments: ACK với sequence number n có nghĩa là "tất cả packets có sequence number đến n đã được nhận correctly." Đây là lý do tự nhiên khi receiver chỉ deliver packets theo thứ tự.*

---

**Câu 70.** GBN có vấn đề gì khi window size và bandwidth-delay product đều lớn?

A. Cần quá nhiều memory  
B. Một single packet error có thể khiến sender retransmit rất nhiều packets không cần thiết  
C. Sequence numbers overflow  
D. Timer không đủ chính xác  

**Đáp án: B**

*Giải thích: Khi window size và bandwidth-delay product lớn, pipeline có thể chứa nhiều packets. Một lỗi duy nhất khiến GBN retransmit toàn bộ window — phần lớn là không cần thiết. Đây là lý do ra đời Selective Repeat.*

---

**Câu 71.** Selective Repeat (SR) khác GBN ở điểm nào cơ bản nhất?

A. SR không dùng sequence numbers  
B. SR chỉ retransmit những packets mà sender suspect là bị lỗi/mất, không gửi lại toàn bộ window  
C. SR dùng larger window size  
D. SR không cần ACK  

**Đáp án: B**

*Giải thích: SR avoid unnecessary retransmissions bằng cách chỉ retransmit những packets cụ thể mà receiver không nhận đúng. Receiver sẽ individually acknowledge từng packet correctly received.*

---

**Câu 72.** Trong SR, receiver xử lý out-of-order packets như thế nào?

A. Discard chúng như GBN  
B. Buffer chúng cho đến khi missing packets arrive, rồi deliver một batch lên upper layer  
C. Yêu cầu retransmit ngay lập tức  
D. Gửi NAK cho missing packets  

**Đáp án: B**

*Giải thích: SR receiver buffer các out-of-order packets cho đến khi các missing packets (có sequence number thấp hơn) được nhận. Sau đó deliver một batch packets theo thứ tự lên upper layer.*

---

**Câu 73.** Trong SR, mỗi packet có timer riêng. Tại sao?

A. Để đồng bộ hóa với receiver  
B. Vì chỉ packet cụ thể đó sẽ được retransmit khi timeout, không phải toàn bộ window  
C. Để đo RTT chính xác hơn  
D. Vì đây là yêu cầu của RFC  

**Đáp án: B**

*Giải thích: SR retransmit individual packets, không phải toàn bộ window như GBN. Do đó, mỗi packet cần timer riêng — khi timer của packet nào expire, chỉ packet đó được retransmit.*

---

**Câu 74.** Tại sao trong SR, receiver phải re-acknowledge những packets trong [rcv_base-N, rcv_base-1] (đã nhận trước đó)?

A. Để kiểm tra data integrity  
B. Nếu không có ACK cho send_base truyền đến sender, sender sẽ retransmit, và sender window sẽ không tiến được nếu receiver không ACK lại  
C. Để cập nhật receive window  
D. Đây là lỗi thiết kế của SR  

**Đáp án: B**

*Giải thích: Sender và receiver không có identical view về những gì đã được ACK. Nếu ACK của send_base bị mất, sender sẽ retransmit nó. Nếu receiver không ACK lại packet này, sender window không thể move forward — deadlock xảy ra.*

---

**Câu 75.** Với SR protocol, window size tối đa phải nhỏ hơn hoặc bằng bao nhiêu so với sequence number space?

A. Bằng sequence number space  
B. Một nửa (1/2) sequence number space  
C. Một phần tư (1/4) sequence number space  
D. Không có giới hạn  

**Đáp án: B**

*Giải thích: Window size của SR phải ≤ (kích thước sequence number space)/2. Nếu không, có thể xảy ra nhầm lẫn: receiver không thể phân biệt một packet là retransmission của packet cũ hay là packet mới (do sequence number bị wrap around và trùng lặp).*

---

**Câu 76.** Vấn đề "SR receiver dilemma with too-large windows" là gì?

A. Buffer tràn  
B. Receiver không thể phân biệt retransmission của packet cũ với transmission của packet mới do sequence numbers trùng lặp  
C. Window quá lớn gây tràn sequence numbers  
D. Timer không đủ thời gian  

**Đáp án: B**

*Giải thích: Với window size quá lớn, sequence numbers wrap around. Receiver có thể nhận packet với sequence number 0 mà không biết đó là retransmission của packet đầu tiên hay packet mới (packet thứ 5). Đây là lý do cần giới hạn window size ≤ (seq space)/2.*

---

**Câu 77.** Trong bảng tổng kết (Table 3.1), vai trò của "Timer" là gì?

A. Đồng bộ hóa clocks giữa sender và receiver  
B. Timeout/retransmit một packet, vì packet hoặc ACK của nó có thể bị mất  
C. Đo RTT  
D. Kiểm soát flow  

**Đáp án: B**

*Giải thích: Timer được dùng để timeout và retransmit packets vì packet (hoặc ACK của nó) có thể bị mất. Premature timeout cũng có thể xảy ra (packet chưa bị mất nhưng timer đã expire), gây duplicate copies tại receiver.*

---

**Câu 78.** Trong bảng tổng kết, vai trò của "Sequence Number" là gì?

A. Xác định IP address của sender  
B. Đánh số thứ tự packets; receiver dùng để detect lost packets và duplicate copies  
C. Mã hóa dữ liệu  
D. Xác định port number  

**Đáp án: B**

*Giải thích: Sequence numbers dùng để đánh số thứ tự packets từ sender đến receiver. Gaps trong sequence numbers cho phép receiver detect lost packets; duplicate sequence numbers cho phép detect duplicate copies.*

---

**Câu 79.** Tại sao packet reordering trong network là vấn đề đối với reliable data transfer?

A. Reordering làm tăng delay  
B. Old copies của packet có thể xuất hiện với sequence number đã được dùng lại, gây nhầm lẫn cho receiver  
C. Routers không thể xử lý reordered packets  
D. Checksum bị sai khi packets bị reordered  

**Đáp án: B**

*Giải thích: Khi packets có thể bị reorder, old copies của packet với sequence/ACK number x có thể xuất hiện bất kỳ lúc nào, dù sender/receiver window không còn chứa x. Điều này có thể gây nhầm lẫn nếu sequence number được reuse.*

---

**Câu 80.** TCP giả định packet không thể "sống" trong network quá bao lâu, để đảm bảo sequence number không bị tái sử dụng quá sớm?

A. 30 giây  
B. 1 phút  
C. 3 phút  
D. 10 phút  

**Đáp án: C**

*Giải thích: Theo TCP extensions cho high-speed networks (RFC 1323), maximum packet lifetime được giả định là khoảng 3 phút. Điều này đảm bảo sequence number không bị reuse trước khi all old packets với sequence number đó đã "chết" trong network.*

---

---

## PHẦN 5: Câu hỏi Tổng hợp và Vận dụng Tư duy

**Câu 81.** So sánh hai phát biểu: (A) "Transport layer cung cấp giao tiếp giữa hai hosts" và (B) "Network layer cung cấp giao tiếp giữa hai processes". Phát biểu nào đúng?

A. Cả A và B đều đúng  
B. Chỉ A đúng  
C. Chỉ B đúng  
D. Cả A và B đều sai — phải đổi ngược lại  

**Đáp án: D**

*Giải thích: Phải đổi ngược: Transport layer cung cấp logical communication giữa các processes (process-to-process), còn Network layer cung cấp logical communication giữa các hosts (host-to-host). Đây là sự phân biệt then chốt cần nắm vững.*

---

**Câu 82.** Khi đang download web page, chạy FTP session, và hai Telnet sessions — có bao nhiêu transport-layer processes và transport layer cần làm gì?

A. 1 process, transport layer chỉ forward data  
B. 4 processes, transport layer phải demultiplex incoming data đến đúng từng process  
C. 4 processes, transport layer không cần làm gì thêm  
D. 2 processes, chỉ cần một socket  

**Đáp án: B**

*Giải thích: Có 4 application processes (1 HTTP, 1 FTP, 2 Telnet). Transport layer phải demultiplex incoming segments đến đúng process dựa trên port numbers. Đây là ví dụ về multiplexing/demultiplexing trong thực tế.*

---

**Câu 83.** Tại sao TCP server có thể hỗ trợ ít clients hơn UDP server trong cùng điều kiện hardware?

A. TCP protocol phức tạp hơn về mặt lập trình  
B. TCP duy trì connection state (buffers, parameters) cho mỗi connection; UDP không có connection state nên server tốn ít tài nguyên hơn cho mỗi client  
C. UDP nhanh hơn TCP về mặt xử lý  
D. TCP cần nhiều port numbers hơn  

**Đáp án: B**

*Giải thích: TCP phải maintain connection state cho mỗi connection: receive/send buffers, congestion-control parameters, sequence/ACK numbers. Điều này tiêu tốn bộ nhớ server. UDP không có connection state — server có thể phục vụ nhiều clients active hơn.*

---

**Câu 84.** Nếu một UDP server nhận segment từ client A (IP: 1.1.1.1, port: 5000) và segment từ client B (IP: 2.2.2.2, port: 5000) cùng đến destination port 6000 của server — điều gì xảy ra?

A. Segment của B bị reject vì conflict port  
B. Cả hai segments đi đến cùng một UDP socket trên server  
C. Server tạo hai sockets khác nhau  
D. Chỉ segment đến trước được xử lý  

**Đáp án: B**

*Giải thích: UDP socket được xác định bởi (destination IP, destination port). Vì cả hai đều đến destination port 6000 của server, chúng sẽ đi đến cùng socket. Server phải dùng source IP/port từ segment để biết ai đang giao tiếp.*

---

**Câu 85.** Trong kịch bản tương tự nhưng dùng TCP — hai TCP segments từ client A và B đến cùng destination port 6000 — điều gì xảy ra?

A. Cùng kết quả như UDP — đi đến cùng một socket  
B. Hai connection sockets khác nhau được tạo, vì TCP dùng 4-tuple để demultiplex  
C. Segment B bị reject  
D. Server không thể phân biệt  

**Đáp án: B**

*Giải thích: TCP dùng 4-tuple (src IP, src port, dst IP, dst port). Client A và B có source IP khác nhau, nên 4-tuple khác nhau → hai connection sockets khác nhau. Đây là tính năng quan trọng cho phép TCP server xử lý nhiều clients đồng thời.*

---

**Câu 86.** Tại sao SNMP (network management) chọn UDP mặc dù reliability quan trọng?

A. SNMP data quá nhỏ cho TCP  
B. Network management phải hoạt động khi network đang stressed — chính xác lúc reliable, congestion-controlled data transfer khó đạt được  
C. SNMP không cần reliable delivery  
D. TCP không hỗ trợ SNMP protocol  

**Đáp án: B**

*Giải thích: SNMP cần hoạt động khi mạng đang có vấn đề (stressed state) — chính lúc TCP's congestion control gây khó khăn nhất. UDP cho phép SNMP gửi management data ngay cả trong điều kiện mạng tồi tệ.*

---

**Câu 87.** Xét rdt2.0: Khi sender nhận ACK bị corrupt, tại sao "hỏi lại" (asking "What did you say?") không phải giải pháp tốt?

A. Vì sẽ gây thêm network traffic  
B. Vì "What did you say?" cũng có thể bị corrupt, dẫn đến infinite loop  
C. Vì receiver không hiểu câu hỏi  
D. Vì đây không phải kỹ thuật networking chuẩn  

**Đáp án: B**

*Giải thích: Nếu "What did you say?" cũng bị corrupt, receiver sẽ không biết đó là một phần của dictation hay request to repeat. Receiver có thể reply "What did you say?" lại, dẫn đến trao đổi không bao giờ kết thúc — "heading down a difficult path".*

---

**Câu 88.** So sánh rdt2.1 và rdt2.2: Tại sao rdt2.2 (NAK-free) có thể thay thế hoàn toàn rdt2.1?

A. Vì rdt2.2 nhanh hơn  
B. Vì duplicate ACK có tác dụng tương đương NAK — nhận 2 ACK cho cùng packet n nghĩa là packet n+1 chưa nhận đúng  
C. Vì rdt2.1 có lỗi  
D. Vì RFC yêu cầu NAK-free  

**Đáp án: B**

*Giải thích: Khi sender nhận duplicate ACK (hai ACK cho cùng sequence number), nó biết receiver đã nhận packet đó nhưng chưa nhận đúng packet tiếp theo — tương đương NAK. Vì vậy NAK không cần thiết, rdt2.2 dùng ACK với sequence number.*

---

**Câu 89.** Trong rdt3.0, tại sao premature timeout (timeout khi packet chưa thực sự bị mất) không phá vỡ tính correctness của protocol?

A. Vì premature timeout không bao giờ xảy ra trong thực tế  
B. Vì sequence numbers cho phép receiver detect và discard duplicate packets  
C. Vì receiver sẽ không gửi ACK cho duplicate  
D. Vì timer đủ dài để premature timeout không xảy ra  

**Đáp án: B**

*Giải thích: Khi premature timeout xảy ra và sender retransmit, receiver nhận duplicate packet. Nhờ sequence numbers, receiver detect đây là duplicate và discard nó (hoặc re-ACK). Correctness không bị ảnh hưởng, chỉ hiệu năng giảm đôi chút.*

---

**Câu 90.** Tính toán sender utilization: RTT = 30ms, L/R = 0.008ms, stop-and-wait. Utilization xấp xỉ bao nhiêu?

A. 50%  
B. 27%  
C. 2.7%  
D. 0.027%  

**Đáp án: D**

*Giải thích: Usender = (L/R) / (RTT + L/R) = 0.008ms / (30ms + 0.008ms) ≈ 0.008/30.008 ≈ 0.00027 = 0.027%. Sender chỉ gửi dữ liệu 0.027% thời gian — minh họa rõ vấn đề của stop-and-wait trên high-bandwidth, high-latency links.*

---

**Câu 91.** Nếu dùng pipelining với window size = 3 thay vì stop-and-wait trong ví dụ trên, utilization tăng lên bao nhiêu?

A. 3 lần → ~0.081%  
B. 3 lần → ~0.081%, chứ không đạt 100%  
C. 100% vì pipeline đầy  
D. Không thay đổi  

**Đáp án: A**

*Giải thích: Với window size 3, sender có thể gửi 3 packets trước khi chờ ACK → utilization tăng gấp 3 lần: 3 × 0.00027 ≈ 0.00081 = 0.081%. Để đạt utilization cao, cần window size lớn hơn nhiều (≥ RTT×R/L ≈ 3750 packets).*

---

**Câu 92.** Trong GBN với window size N=4, sequence numbers 0-7 (3-bit), packets 0-3 được gửi. Packet 2 bị mất. Receiver nhận packets 3, sau đó sender retransmit. Receiver phải nhận lại packets nào?

A. Chỉ packet 2  
B. Packets 2, 3  
C. Packets 2, 3, 4, 5 (tất cả packets sent but unACK'd)  
D. Packets 0, 1, 2, 3  

**Đáp án: B**

*Giải thích: Khi packet 2 bị mất, receiver discard packet 3 (out-of-order) và gửi lại ACK1. Khi timeout, sender phải gửi lại từ packet 2 trở đi. Vì chỉ packets 2 và 3 đã được gửi lúc đó (window size 4, nhưng chỉ gửi được đến 3), sender retransmit 2, 3.*

---

**Câu 93.** Trong SR với window size N=4, sequence numbers 0-7, packets 0-3 được gửi. Packet 2 bị mất, nhưng 0, 1, 3 nhận đúng. Receiver làm gì?

A. Discard 3, chờ 2  
B. Buffer 3, gửi ACK0, ACK1, ACK3; chờ packet 2 retransmit  
C. Gửi NAK2  
D. Re-request từ packet 0  

**Đáp án: B**

*Giải thích: SR receiver buffer correctly received out-of-order packets. Receiver gửi ACK0, ACK1, ACK3 (individual ACKs). Packet 3 được buffer. Khi packet 2 được retransmit và nhận, receiver deliver 2, 3, 4, 5 (nếu có) lên upper layer.*

---

**Câu 94.** Khi so sánh GBN và SR: Điều nào sau đây đúng?

A. GBN có receiver phức tạp hơn SR  
B. SR có sender phức tạp hơn GBN (cần timer riêng cho từng packet) nhưng receiver cũng phức tạp hơn (cần buffer), trong khi GBN đơn giản hóa receiver bằng cách discard out-of-order packets  
C. GBN luôn hiệu quả hơn SR  
D. SR và GBN identical về hiệu năng  

**Đáp án: B**

*Giải thích: Trade-off: GBN có receiver đơn giản (không buffer) nhưng retransmit nhiều hơn cần thiết. SR retransmit ít hơn nhưng receiver phức tạp hơn (cần buffer out-of-order packets) và sender cần timer riêng cho mỗi packet.*

---

**Câu 95.** Sequence number space cần bao nhiêu để GBN với window size N hoạt động đúng?

A. Ít nhất N sequence numbers  
B. Ít nhất N+1 sequence numbers  
C. Ít nhất 2N sequence numbers  
D. Bất kỳ kích thước nào  

**Đáp án: B**

*Giải thích: GBN cần ít nhất N+1 sequence numbers. Nếu chỉ có N sequence numbers, receiver có thể nhầm lẫn giữa duplicate của packet cũ nhất trong window và packet mới ngoài window.*

---

**Câu 96.** Tại sao HTTP vẫn dùng TCP dù TCP có connection-establishment delay?

A. Vì HTTP payload quá lớn cho UDP  
B. Vì reliability là critical cho web pages với text — mất dữ liệu không thể chấp nhận  
C. Vì UDP không thể truyền HTML  
D. Vì HTTP là oldest protocol  

**Đáp án: B**

*Giải thích: HTTP dùng TCP vì reliability là critical cho web pages — người dùng không thể chấp nhận web page bị thiếu từ hay ảnh bị corrupt. Connection delay của TCP được trade-off cho reliability.*

---

**Câu 97.** Trong UDP checksum: Tổng ba 16-bit words là 0100101011000010, 1s complement là gì và có nghĩa gì?

A. 0100101011000010, không thay đổi  
B. 1011010100111101 — đây là checksum gửi đi  
C. 0000000000000000  
D. 1111111111111111  

**Đáp án: B**

*Giải thích: 1s complement được tính bằng cách đổi tất cả 0 thành 1 và 1 thành 0. 0100101011000010 → 1011010100111101. Receiver cộng checksum này với sum và kết quả phải là 1111111111111111 nếu không có lỗi.*

---

**Câu 98.** Nếu network layer đảm bảo orderly delivery (không reorder), điều này có ảnh hưởng gì đến thiết kế reliable data transfer protocol không?

A. Không có ảnh hưởng gì  
B. Có thể đơn giản hóa protocol — không cần lo về sequence number reuse do reordering  
C. Loại bỏ hoàn toàn cần checksum  
D. Loại bỏ cần ACK/NAK  

**Đáp án: B**

*Giải thích: Nếu channel không reorder packets (giả định trong Section 3.4), protocol đơn giản hơn — không cần lo về old packets xuất hiện với sequence numbers cũ. Trong thực tế Internet, packets CAN be reordered, nên cần cẩn thận với sequence number reuse.*

---

**Câu 99.** Điểm chung nào giữa GBN và TCP mà sách đề cập?

A. Cùng window size  
B. GBN uses sequence numbers, cumulative acknowledgments, checksums, và timeout/retransmit — tất cả cũng được dùng trong TCP  
C. Cùng 3-way handshake  
D. Cùng flow control mechanism  

**Đáp án: B**

*Giải thích: Sách nhận xét rằng GBN "incorporates almost all of the techniques" sẽ gặp khi học TCP: sequence numbers, cumulative acknowledgments, checksums, và timeout/retransmit. TCP xây dựng trên nền tảng GBN nhưng phức tạp hơn.*

---

**Câu 100.** Câu nào phản ánh đúng nhất mối quan hệ giữa transport layer services và network layer services?

A. Transport layer hoàn toàn độc lập với network layer  
B. Transport layer có thể augment (bổ sung) services của network layer nhưng bị ràng buộc bởi service model của network layer  
C. Network layer phải đảm bảo reliability trước khi transport layer có thể cung cấp reliability  
D. Transport layer và network layer cung cấp cùng loại dịch vụ  

**Đáp án: B**

*Giải thích: Transport protocol services thường bị ràng buộc bởi network layer, nhưng không hoàn toàn. Transport protocol CÓ THỂ cung cấp reliable transfer (TCP) dù IP unreliable, hay cung cấp encryption dù network layer không đảm bảo confidentiality. Tuy nhiên, delay/bandwidth guarantees thì không thể nếu network layer không cung cấp.*

---

**Câu 101.** Điều gì xảy ra nếu UDP senders không bị kiểm soát và tất cả stream video high-bitrate qua UDP cùng lúc?

A. Mạng sẽ hoạt động tốt hơn do không có congestion control overhead  
B. Quá nhiều packet overflow tại routers → high loss rates → TCP senders giảm rate → toàn bộ network degraded  
C. UDP sẽ tự động điều chỉnh rate  
D. Chỉ UDP packets bị ảnh hưởng, TCP hoạt động bình thường  

**Đáp án: B**

*Giải thích: Đây là vấn đề của unregulated UDP: nếu mọi người stream qua UDP, routers bị overloaded, loss rates tăng cao. Điều này còn "crowd out" TCP sessions — vì TCP có congestion control nên sẽ giảm rate xuống, khiến UDP dominates bandwidth một cách bất công.*

---

**Câu 102.** Xét tình huống: Một gaming application cần latency cực thấp và có thể chịu một ít packet loss. Nên dùng UDP hay TCP, và lý do?

A. TCP vì reliability quan trọng trong gaming  
B. UDP vì: không có connection setup delay, không bị throttled bởi congestion control, có finer control — ứng dụng có thể tự implement minimal recovery nếu cần  
C. Phải dùng TCP vì gaming cần authentication  
D. Không có protocol nào phù hợp  

**Đáp án: B**

*Giải thích: Real-time gaming cần low latency hơn reliability tuyệt đối. UDP phù hợp hơn: không delay từ handshaking hay congestion control throttling. Application tự quản lý recovery nếu cần. Đây là lý do nhiều game engines dùng UDP với custom reliability layer.*

---

**Câu 103.** Tại sao sequence number space của GBN cần lớn hơn SR (GBN cần N+1, SR cần 2N)?

A. GBN xử lý nhiều packets hơn  
B. GBN dùng cumulative ACKs (không biết rõ packet nào được ACK riêng lẻ), còn SR dùng individual ACKs — receiver window trong GBN có thể overlap với sender window theo cách nguy hiểm hơn  
C. SR cần nhiều sequence numbers hơn cho buffering  
D. Không có sự khác biệt về sequence number space requirement  

**Đáp án: B**

*Giải thích: GBN receiver không buffer out-of-order packets và dùng cumulative ACK. Điều này tạo ra tình huống nguy hiểm khác với SR khi sequence numbers wrap around. SR có thể dùng individual ACKs nên receiver window hoạt động độc lập hơn với sender window.*

---

**Câu 104.** Reliable data transfer protocol cần bao nhiêu trong số các thành phần sau: checksum, sequence numbers, ACK, timer?

A. Chỉ cần checksum và ACK  
B. Chỉ cần sequence numbers và timer  
C. Tất cả đều cần thiết — mỗi thứ giải quyết một vấn đề riêng biệt  
D. Chỉ cần timer và ACK  

**Đáp án: C**

*Giải thích: Mỗi cơ chế có vai trò riêng: Checksum detect bit errors; Sequence numbers detect lost/duplicate packets và maintain order; ACK/NAK cho sender biết trạng thái nhận; Timer detect packet loss khi không có feedback. Thiếu một cái là không đủ.*

---

**Câu 105.** So sánh packet switching (best-effort IP) với circuit switching: Tại sao TCP có thể cung cấp reliable transfer trên IP mà không cần thay đổi infrastructure?

A. TCP sửa lỗi tại network layer  
B. TCP implements reliability hoàn toàn trong end systems — sử dụng sequence numbers, ACKs, timers, và retransmission mà không yêu cầu sự hỗ trợ từ network  
C. TCP yêu cầu routers đặc biệt  
D. TCP mua bandwidth đảm bảo từ ISP  

**Đáp án: B**

*Giải thích: Đây là sức mạnh của kiến trúc phân tầng và end-end principle: TCP hoàn toàn implement reliability trong end systems, chỉ dùng IP's best-effort service. Network infrastructure (routers) không biết gì về TCP's reliability mechanisms.*

---

**Câu 106.** Nếu một application cần cả high reliability VÀ real-time delivery với minimal latency — đây có phải conflict không, và giải quyết thế nào?

A. Không phải conflict — TCP giải quyết được cả hai  
B. Đây là fundamental tension: reliability đòi hỏi retransmission (gây latency), real-time cần low latency (ít tolerance cho retransmission)  
C. UDP giải quyết được cả hai  
D. Chỉ có thể có một trong hai  

**Đáp án: B**

*Giải thích: Đây là fundamental tension trong transport design. Giải pháp thực tế: dùng UDP với application-level reliability có selective recovery (chỉ recover những packets truly critical, bỏ qua những packets quá cũ). Ví dụ: QUIC protocol, WebRTC.*

---

**Câu 107.** Trong ví dụ household analogy, nếu dịch vụ bưu điện không đảm bảo thư đến trong 3 ngày, Ann và Bill có thể tự đảm bảo delivery trong 3 ngày không?

A. Có, Ann và Bill có thể đảm bảo điều này  
B. Không — Ann và Bill không thể cung cấp delay guarantee nếu postal service không cung cấp  
C. Có, nếu họ dùng express delivery  
D. Không liên quan đến transport/network layer  

**Đáp án: B**

*Giải thích: Đây minh họa ràng buộc của transport layer: services mà transport protocol cung cấp bị ràng buộc bởi services của network layer. Nếu IP không đảm bảo delay hay bandwidth, TCP cũng không thể đảm bảo những điều này.*

---

**Câu 108.** Tại sao Web servers hiện đại thường dùng threads (lightweight subprocesses) thay vì tạo process mới cho mỗi connection?

A. Threads nhanh hơn processes  
B. Giảm overhead của việc tạo process; nhiều connection sockets có thể được attached đến cùng một process thông qua threads  
C. Threads không cần port numbers  
D. Bắt buộc bởi HTTP specification  

**Đáp án: B**

*Giải thích: Tạo process mới cho mỗi connection rất tốn kém. Threads nhẹ hơn nhiều. Với high-performance Web server, nhiều connection sockets (với identifiers khác nhau) có thể được attached đến cùng một process thông qua threads — tiết kiệm tài nguyên đáng kể.*

---

**Câu 109.** Xét GBN: Nếu window size = 10 và packets 0-9 đều được gửi, nhưng ACK của packets 0-4 bị mất và chỉ ACK5-9 arrive. Sender làm gì khi timer của packet 0 expire?

A. Gửi lại chỉ packet 0  
B. Gửi lại tất cả packets 0-9 (tất cả còn trong window vì cumulative ACK chưa advance base)  
C. Gửi lại packets 0-4  
D. Không làm gì  

**Đáp án: B**

*Giải thích: GBN dùng cumulative ACK. Vì ACK0-4 bị mất, sender không thể advance window base (base vẫn là 0). Khi timer của packet 0 expire, sender phải gửi lại TẤT CẢ packets từ base đến nextseqnum-1, tức là 0-9. Đây là inefficiency của GBN.*

---

**Câu 110.** Một điểm quan trọng nào về relationship giữa transport layer và sockets cần phân biệt?

A. Mỗi process chỉ có thể có một socket  
B. Transport layer không deliver data trực tiếp đến process mà đến intermediary socket; mỗi socket có unique identifier  
C. Sockets chỉ tồn tại ở application layer  
D. Sockets chỉ được dùng bởi TCP, không phải UDP  

**Đáp án: B**

*Giải thích: Transport layer không deliver data trực tiếp đến process mà đến socket (như "cánh cửa" giữa process và network). Một process có thể có nhiều sockets. Socket identifier format khác nhau giữa UDP (2-tuple) và TCP (4-tuple).*

---

**Câu 111.** Trong SR, tại sao sender và receiver "will not always have an identical view of what has been received correctly"?

A. Vì họ dùng different clocks  
B. Vì ACKs có thể bị mất trong transit — sender không biết receiver đã nhận packet nào cho đến khi ACK arrive  
C. Vì SR không dùng checksums  
D. Vì SR dùng cumulative ACKs  

**Đáp án: B**

*Giải thích: ACKs có thể bị mất. Receiver có thể đã nhận và ACK'd packet X, nhưng ACK bị mất → sender vẫn nghĩ packet X chưa được nhận. Điều này có nghĩa sender/receiver windows không nhất thiết coincide — là đặc điểm quan trọng của SR.*

---

**Câu 112.** Tổng kết so sánh: Điều gì phân biệt rõ nhất rdt3.0 với rdt2.2?

A. rdt3.0 có checksum, rdt2.2 thì không  
B. rdt3.0 xử lý packet loss bằng countdown timer; rdt2.2 chỉ xử lý bit errors  
C. rdt3.0 hỗ trợ pipelining  
D. rdt3.0 dùng NAK, rdt2.2 thì không  

**Đáp án: B**

*Giải thích: rdt2.2 xử lý bit errors (corrupt packets) thông qua checksum, sequence numbers, và ACKs. rdt3.0 thêm xử lý packet loss bằng countdown timer — sender sẽ retransmit nếu không nhận ACK trong khoảng thời gian nhất định.*

---

**Câu 113.** Nếu không có sequence numbers trong rdt3.0, điều gì sẽ xảy ra khi có premature timeout?

A. Protocol vẫn hoạt động đúng  
B. Receiver không thể phân biệt retransmitted packet với new data packet  
C. Timer sẽ không bao giờ expire  
D. Sender sẽ không retransmit  

**Đáp án: B**

*Giải thích: Không có sequence numbers, khi sender retransmit do premature timeout, receiver nhận duplicate packet nhưng không biết đó là duplicate. Nó sẽ deliver duplicate data lên upper layer, gây lỗi. Sequence numbers là cơ chế bắt buộc để detect duplicates.*

---

**Câu 114.** Mục đích của sliding window trong GBN/SR là gì ngoài việc cho phép pipelining?

A. Tăng tốc độ checksum  
B. Kiểm soát số lượng unacknowledged packets — liên quan đến flow control và congestion control mà sẽ học ở Section 3.5 và 3.7  
C. Giảm header overhead  
D. Đồng bộ clocks  

**Đáp án: B**

*Giải thích: Window size N giới hạn số unacknowledged packets. Đây không chỉ là vì pipelining — sách chỉ ra rằng flow control (Section 3.5) và congestion control (Section 3.7) là những lý do khác để giới hạn sender. Window size sẽ được set dựa trên receiver's buffer capacity và network congestion level.*

---

**Câu 115.** Câu nào sau đây mô tả đúng nhất transport layer trong kiến trúc Internet?

A. Transport layer là tầng duy nhất đảm bảo delivery  
B. Transport layer là cầu nối giữa application processes và network infrastructure, cung cấp logical process-to-process communication và (tùy protocol) error detection, reliable transfer, và congestion control  
C. Transport layer chỉ đơn giản là forward data từ application xuống network  
D. Transport layer chỉ hoạt động với TCP, UDP được xử lý ở application layer  

**Đáp án: B**

*Giải thích: Đây là mô tả toàn diện về transport layer: extends IP's host-to-host delivery thành process-to-process delivery, cung cấp error detection ở minimum, và (với TCP) cung cấp reliable transfer và congestion control.*

---

**Câu 116.** Thuật ngữ "segment" trong transport layer và "datagram" trong network layer phản ánh điều gì về kiến trúc phân tầng?

A. Hai tầng dùng cùng một loại packet  
B. Mỗi tầng có đơn vị dữ liệu riêng: segment (transport), datagram (network), frame (data link) — encapsulation xảy ra khi chuyển qua các tầng  
C. Segment lớn hơn datagram  
D. Datagram chứa nhiều segments  

**Đáp án: B**

*Giải thích: Kiến trúc phân tầng có protocol data units (PDU) riêng cho mỗi tầng: application message → transport segment (thêm transport header) → network datagram (encapsulate segment, thêm IP header) → data link frame. Mỗi tầng thêm header information cho mục đích riêng.*

---

**Câu 117.** Tại sao reliable data transfer "on top of" unreliable service lại khả thi mà không cần thay đổi network layer?

A. Không khả thi — cần sửa đổi network layer  
B. Vì reliability mechanisms (checksums, ACKs, retransmit, sequence numbers) hoàn toàn implemented trong end systems — không yêu cầu intermediate nodes biết hay làm gì  
C. Vì IP thực ra không unreliable  
D. Vì routers hỗ trợ TCP  

**Đáp án: B**

*Giải thích: End-end principle cho phép điều này: reliability được implement hoàn toàn ở end systems thông qua checksums, sequence numbers, ACKs, và timers. Intermediate routers chỉ forward packets best-effort — không biết gì về transport layer mechanisms.*

---

**Câu 118.** Nếu link-layer protocol đã đảm bảo error-free delivery trên mỗi link, UDP vẫn cần checksum không?

A. Không, vì link-layer đã xử lý  
B. Có — end-end principle: errors có thể xảy ra trong router memory; không phải mọi link đều có error checking; end-to-end checking là safety net cần thiết  
C. Không, chỉ TCP cần checksum  
D. Có, nhưng chỉ vì RFC yêu cầu  

**Đáp án: B**

*Giải thích: Ngay cả khi tất cả links đảm bảo error-free, bits có thể bị corrupt khi segment được stored trong router memory. Hơn nữa, không phải mọi links đều có error checking. End-end principle: error detection ở transport layer là safety net cần thiết bất kể lower layers có làm gì.*

---

**Câu 119.** Trong thiết kế protocol, tại sao rdt series (rdt1.0 → rdt3.0) được xây dựng incrementally thay vì thiết kế rdt3.0 ngay từ đầu?

A. Vì cần nhiều thời gian để tính toán  
B. Incremental design giúp hiểu tại sao mỗi mechanism (checksum, sequence numbers, ACK, timer) là cần thiết — mỗi version giải quyết thêm một loại vấn đề khi model phức tạp dần  
C. Vì rdt3.0 quá phức tạp để thiết kế từ đầu  
D. Vì đây là requirement của RFC  

**Đáp án: B**

*Giải thích: Cách tiếp cận incremental là pedagogical design: rdt1.0 (perfect channel) → rdt2.0 (bit errors) → rdt2.1 (corrupt ACK/NAK) → rdt2.2 (NAK-free) → rdt3.0 (packet loss). Mỗi bước thêm một mechanism để giải quyết vấn đề mới. Điều này giúp hiểu tại sao mỗi cơ chế tồn tại.*

---

**Câu 120.** Câu hỏi tổng hợp cuối: Một developer thiết kế protocol truyền file qua mạng unreliable. Cần ít nhất những cơ chế nào, và tại sao?

A. Chỉ cần checksum  
B. Checksum (detect errors), sequence numbers (detect loss/duplicates), ACK/NAK (feedback), và timer (detect lost packets) — mỗi cơ chế giải quyết một failure mode riêng biệt  
C. Chỉ cần timer và retransmit  
D. Không cần gì nếu dùng reliable physical links  

**Đáp án: B**

*Giải thích: File transfer cần reliable delivery. Trên unreliable channel: (1) Checksum detect bit errors; (2) Sequence numbers phân biệt new data vs retransmission, detect lost packets; (3) ACK/NAK cho sender biết trạng thái; (4) Timer detect mất cả packet lẫn ACK. Đây chính xác là những gì Table 3.1 tổng kết — tất cả đều cần thiết.*

---

*Hết bộ câu hỏi Chapter 3 — Transport Layer (Sections 3.1–3.4)*
*Tổng: 120 câu | Sections 3.1–3.4 + Tổng hợp*
