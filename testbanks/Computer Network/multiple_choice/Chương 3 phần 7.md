# Bộ câu hỏi trắc nghiệm — Chapter 3: Transport Layer Phần V
## (Kurose & Ross — Computer Networking: A Top-Down Approach)

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
