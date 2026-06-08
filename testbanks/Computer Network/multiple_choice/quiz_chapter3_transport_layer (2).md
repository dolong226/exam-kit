# Bộ câu hỏi trắc nghiệm — Chapter 3: Transport Layer Phần III,IV
## (Kurose & Ross — Computer Networking: A Top-Down Approach)

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
