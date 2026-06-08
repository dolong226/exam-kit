# Quiz: Chapter 3 — Transport Layer (Sections 3.5 – 3.8) Phần X,XI,XII
# Computer Networking: A Top-Down Approach (Kurose & Ross)

---

## PHẦN X: Câu hỏi Tổng hợp & Vận dụng Tư duy

**Câu 71.** Xét một TCP connection giữa Host A và Host B. Host A gửi file 500,000 byte, MSS = 1000 byte, initial seq number = 0. Segment thứ 3 sẽ có sequence number bằng bao nhiêu?

A. 2  
B. 1,000  
C. 2,000  
D. 3,000

**Đáp án: C**  
*Giải thích: Segment 1: seq = 0 (bytes 0-999). Segment 2: seq = 1000 (bytes 1000-1999). Segment 3: seq = 2000 (bytes 2000-2999). Sequence number = byte-stream number của byte đầu tiên trong segment.*

---

**Câu 72.** Giả sử EstimatedRTT = 100ms, SampleRTT mới = 116ms, α = 0.125. EstimatedRTT mới là bao nhiêu?

A. 100ms  
B. 102ms  
C. 108ms  
D. 116ms

**Đáp án: B**  
*Giải thích: EstimatedRTT = 0.875 × 100 + 0.125 × 116 = 87.5 + 14.5 = 102ms. EWMA giảm trọng số của sample mới, tạo ra sự mượt mà.*

---

**Câu 73.** Sau khi tính được EstimatedRTT = 102ms và DevRTT = 5ms, TimeoutInterval sẽ là bao nhiêu?

A. 102ms  
B. 107ms  
C. 122ms  
D. 142ms

**Đáp án: C**  
*Giải thích: TimeoutInterval = EstimatedRTT + 4·DevRTT = 102 + 4×5 = 102 + 20 = 122ms.*

---

**Câu 74.** Trong three-way handshake, segment đầu tiên (SYN) từ client có những đặc điểm gì? (Chọn phát biểu đúng nhất)

A. SYN=1, data payload, seq=client_isn, ack=0.  
B. SYN=1, không có data payload, seq=client_isn, ack field chưa có giá trị có nghĩa.  
C. SYN=1, ACK=1, seq=client_isn, ack=0.  
D. SYN=0, seq=client_isn, chứa data của HTTP request.

**Đáp án: B**  
*Giải thích: SYN segment: SYN bit = 1, không chứa application-layer data, seq = client_isn (ngẫu nhiên). ACK bit = 0 (chưa có gì để ACK). Segment này dùng để đồng bộ ISN và bắt đầu handshake.*

---

**Câu 75.** Host A gửi segment seq=92, 8 bytes. ACK từ B bị mất. Timeout xảy ra. Sau khi A retransmit, B nhận được segment. B sẽ làm gì?

A. Gửi lại ACK=100 và lưu data như thường lệ.  
B. Discard data (đã có rồi) và gửi ACK=100 để báo cho A.  
C. Gửi RST segment vì nhận duplicate.  
D. Giữ duplicate data trong buffer và chờ application đọc.

**Đáp án: B**  
*Giải thích: Khi nhận retransmit của segment đã nhận, B phát hiện duplicate (via sequence number), discard data nhưng vẫn gửi ACK=100 để A biết data đã nhận thành công (stop retransmit).*

---

**Câu 76.** Xét TCP Reno với cwnd = 12 MSS và ssthresh = 8 MSS đang ở Congestion Avoidance. Nếu nhận được 3 duplicate ACKs, cwnd và ssthresh mới là bao nhiêu?

A. cwnd = 1 MSS, ssthresh = 6 MSS  
B. cwnd = 6 MSS, ssthresh = 6 MSS  
C. cwnd = 9 MSS, ssthresh = 6 MSS  
D. cwnd = 6 MSS, ssthresh = 12 MSS

**Đáp án: C**  
*Giải thích: Triple dup ACK với TCP Reno: ssthresh = cwnd/2 = 12/2 = 6 MSS. cwnd = ssthresh + 3·MSS = 6 + 3 = 9 MSS. Chuyển sang Fast Recovery. (Nếu là TCP Tahoe: cwnd = 1 MSS, ssthresh = 6 MSS.)*

---

**Câu 77.** Trong giai đoạn Slow Start với cwnd = 4 MSS, ssthresh = 8 MSS, host nhận được 4 ACK mới. cwnd tiếp theo sẽ là bao nhiêu?

A. 5 MSS  
B. 8 MSS  
C. 8 MSS (và chuyển sang Congestion Avoidance)  
D. 4 MSS (giữ nguyên vì ssthresh = 8)

**Đáp án: B**  
*Giải thích: Slow Start: mỗi ACK tăng cwnd thêm 1 MSS. 4 ACK → cwnd = 4+4 = 8 MSS. Khi cwnd = ssthresh = 8, chuyển sang Congestion Avoidance. Vì vậy đáp án C chính xác hơn nhưng B mô tả giá trị. Đáp án C đầy đủ nhất.*

*Ghi chú: Đáp án chính xác nhất là 8 MSS và chuyển sang Congestion Avoidance (B và C đều đúng về giá trị, C đúng hơn về context).*

---

**Câu 78.** Tại sao việc TCP không đo SampleRTT cho retransmitted segments lại đặt ra vấn đề khi EstimatedRTT cao bất thường?

A. Vì sender không thể biết segment nào cần retransmit.  
B. Vì nếu RTT cao, timeout xảy ra thường xuyên, hầu hết segments bị retransmit → ít sample mới → EstimatedRTT không update → vòng lặp bất lợi.  
C. Vì receiver không gửi ACK cho retransmitted segments.  
D. Vì TCP không thể phân biệt timeout và triple dup ACK.

**Đáp án: B**  
*Giải thích: Khi network rất congested, nhiều segments cần retransmit → không đo được SampleRTT → EstimatedRTT stale → timeout interval có thể không phản ánh network state thực tế. Đây là một trong những challenges của TCP timer management.*

---

**Câu 79.** So sánh hành vi của TCP và GBN: trong TCP, nếu ACK cho segment n bị mất nhưng ACK cho segment n+1 đến, TCP có retransmit segment n không?

A. Có, vì TCP phải retransmit toàn bộ window như GBN.  
B. Không, vì ACK cho n+1 là cumulative ACK ngầm xác nhận n đã nhận.  
C. Có, nhưng chỉ sau khi timeout của segment n.  
D. Không, nhưng TCP sẽ gửi NACK để thông báo.

**Đáp án: B**  
*Giải thích: Đây là điểm khác biệt quan trọng giữa TCP và GBN thuần túy. ACK(n+1) nghĩa là "tôi đã nhận hết đến byte n+1-1," ngầm xác nhận segment n. GBN sẽ retransmit tất cả từ n, TCP chỉ retransmit tối đa 1 segment.*

---

**Câu 80.** Tại sao một ứng dụng như Telnet thường gửi segments rất nhỏ (1 byte data)?

A. Vì Telnet protocol giới hạn kích thước segment tối đa là 1 byte.  
B. Vì Telnet là interactive application — mỗi keystroke cần được truyền ngay lập tức, không chờ buffer đầy.  
C. Vì TCP header overhead quá lớn để đóng gói nhiều bytes.  
D. Vì server yêu cầu nhận từng byte để echo lại ngay lập tức.

**Đáp án: B**  
*Giải thích: Telnet là real-time interactive — người dùng muốn thấy phản hồi ngay khi gõ phím. Mỗi keystroke → 1 byte TCP segment (dù header 20 bytes = overhead 95%). Điều này dẫn đến "silly window syndrome" và các tối ưu hóa như Nagle's algorithm.*

---

**Câu 81.** Điều gì xảy ra với TCP connection nếu intermediate router bị quá tải (tắc nghẽn)?

A. Router thông báo cho TCP endpoint để giảm tốc độ gửi.  
B. Packets bị drop tại router buffer → sender nhận timeout hoặc duplicate ACKs → congestion control giảm cwnd.  
C. TCP tự động tìm đường đi khác không qua router bị tắc nghẽn.  
D. Router buffer packets và gửi sau khi congestion giảm.

**Đáp án: B**  
*Giải thích: TCP dùng end-to-end congestion control. Router không thông báo trực tiếp cho TCP. Packet loss là signal ngầm: timeout hoặc 3 dup ACKs → TCP giảm cwnd. Đây là cơ chế TCP suy ra congestion từ network behavior.*

---

**Câu 82.** Tại sao TCP splitting (như Google/Akamai sử dụng) có thể giảm latency từ 4·RTT xuống ~RTT?

A. Vì front-end server xử lý requests nhanh hơn data center.  
B. Vì client kết nối TCP đến front-end gần (RTT_FE nhỏ), front-end có persistent connection với large cwnd đến backend (bỏ qua slow start).  
C. Vì TCP splitting dùng UDP thay vì TCP cho kết nối backend.  
D. Vì front-end cache toàn bộ content, không cần kết nối backend.

**Đáp án: B**  
*Giải thích: Thông thường: 1 RTT handshake + 3 RTTs slow start = 4 RTT. Với TCP splitting: client đến front-end gần (RTT_FE ≈ 0), front-end đến backend có persistent connection với cwnd lớn (không slow start). Tổng ≈ RTT_FE + RTT_BE + processing ≈ RTT.*

---

**Câu 83.** Xét formula throughput = 1.22·MSS/(RTT·√L) trong TCP. Nếu cần đạt 10 Gbps với MSS = 1500 bytes, RTT = 100ms, loss rate L phải nhỏ đến mức nào?

A. L < 10^-3  
B. L < 10^-6  
C. L < 10^-9  
D. L < 2×10^-10

**Đáp án: D**  
*Giải thích: Theo sách: để đạt 10 Gbps với MSS = 1500 bytes, RTT = 100ms, L phải ≈ 2×10^-10 — tức là 1 loss event mỗi 5 tỷ segments. Đây là lý do cần các TCP variants mới (như CUBIC, BBR) cho high-speed networks.*

---

**Câu 84.** Khi TCP connection mới được establish, cwnd = 1 MSS và ssthresh thường được khởi tạo là bao nhiêu?

A. 1 MSS  
B. 8 MSS  
C. Một giá trị rất lớn (thường 64 KB hoặc lớn hơn).  
D. Bằng rwnd của receiver.

**Đáp án: C**  
*Giải thích: ssthresh ban đầu thường được đặt rất lớn (64 KB hay lớn hơn) để Slow Start có thể tăng cwnd tự do cho đến khi phát hiện congestion lần đầu. Sau đó ssthresh được cập nhật = cwnd/2.*

---

**Câu 85.** Trong Figure 3.52 (FSM của TCP congestion control), trạng thái nào không có trong TCP Tahoe?

A. Slow Start  
B. Congestion Avoidance  
C. Fast Recovery  
D. Timeout handling

**Đáp án: C**  
*Giải thích: TCP Tahoe chỉ có Slow Start và Congestion Avoidance. Khi bất kỳ loss event nào (timeout hay 3 dup ACKs), Tahoe đều set cwnd=1 MSS và quay về Slow Start. Fast Recovery là đóng góp của TCP Reno.*

---

**Câu 86.** Tại sao UDP không phù hợp để ngăn SYN flood tương tự TCP?

A. Vì UDP không có port numbers.  
B. Vì UDP là connectionless — không có handshake và state allocation như TCP, nên không có "half-open connection" vấn đề.  
C. Vì UDP dùng checksum mạnh hơn TCP.  
D. Vì UDP không hỗ trợ IP spoofing.

**Đáp án: B**  
*Giải thích: UDP không có connection state. Mỗi UDP datagram được xử lý độc lập. Không có "handshake" → không có "half-open connection" → không có resource allocation trước khi communicate → SYN flood không áp dụng cho UDP.*

---

**Câu 87.** Điều gì sẽ xảy ra nếu TCP KHÔNG có mechanism để xử lý "rwnd = 0" (không gửi 1-byte probe)?

A. Kết nối hoạt động bình thường nhưng chậm hơn.  
B. Kết nối bị deadlock vĩnh viễn — sender không bao giờ biết receiver buffer có chỗ trống.  
C. Receiver tự động gửi WINDOW UPDATE khi buffer có chỗ.  
D. Sender sẽ timeout và retransmit toàn bộ data.

**Đáp án: B**  
*Giải thích: Nếu không có 1-byte probe: sender dừng gửi khi rwnd=0. B chỉ gửi segment khi có data hoặc ACK. Nếu B không có data, nó không gửi segment update rwnd. A bị block mãi mãi — đây là deadlock thực sự, không phải chỉ chậm.*

---

**Câu 88.** Trong context của TCP congestion control, "bandwidth probing" có nghĩa là gì?

A. Gửi probe packets để đo bandwidth của network.  
B. Tăng dần cwnd để tìm "ngưỡng congestion," sau đó back off và bắt đầu tăng lại.  
C. Sử dụng công cụ đo network như ping để estimate capacity.  
D. Router thông báo available bandwidth cho sender.

**Đáp án: B**  
*Giải thích: TCP "probes" bandwidth bằng cách tăng cwnd đến khi loss event xảy ra (congestion onset), sau đó giảm, rồi lại tăng. Quá trình này lặp đi lặp lại để "explore" available bandwidth — không có global information, chỉ local observation.*

---

**Câu 89.** Câu nào mô tả chính xác nhất về SACK (Selective Acknowledgment)?

A. SACK thay thế hoàn toàn cumulative ACK trong TCP.  
B. SACK cho phép receiver ACK các out-of-order segments riêng lẻ, giúp sender chỉ retransmit đúng segments bị mất.  
C. SACK là bắt buộc trong tất cả TCP implementations theo RFC.  
D. SACK chỉ hoạt động khi combine với UDP.

**Đáp án: B**  
*Giải thích: SACK (RFC 2018) là extension tùy chọn. Receiver có thể báo chính xác các "blocks" đã nhận được (dù out of order). Sender biết đúng đâu là "gaps" và chỉ retransmit những gì thực sự bị mất, không lãng phí bandwidth.*

---

**Câu 90.** Vì sao TIME_WAIT thường kéo dài 2×MSL (Maximum Segment Lifetime)?

A. Để đảm bảo server có thể gửi thêm data sau khi nhận FIN.  
B. Để đảm bảo cả hai chiều: nếu ACK cuối bị mất và server retransmit FIN (1 MSL), client cần chờ FIN đến (1 MSL) rồi mới timeout.  
C. Để cho phép application code xử lý việc đóng socket.  
D. Theo quy định của RFC về minimum wait time cho TCP.

**Đáp án: B**  
*Giải thích: MSL = maximum time a packet can exist in network. TIME_WAIT = 2 MSL: 1 MSL để ACK cuối có thể đến server, + 1 MSL phòng server retransmit FIN (do ACK bị mất) và FIN đó đến client. Sau 2 MSL, tất cả "stray" packets đều đã expired.*

---

## PHẦN XI: Câu hỏi Tích hợp Đa Section

**Câu 91.** Xét toàn bộ quá trình một TCP connection: thiết lập → truyền data → đóng. Đâu là thứ tự đúng của các cơ chế được sử dụng?

A. Congestion control → Three-way handshake → Flow control → Four-way teardown.  
B. Three-way handshake → (Slow Start + Congestion Avoidance) × flow control → Four-way teardown với TIME_WAIT.  
C. UDP handshake → Slow Start → AIMD → Connection termination.  
D. SYN flood → SYN cookies → SYNACK → Data transfer.

**Đáp án: B**  
*Giải thích: Đúng thứ tự: Three-way handshake (SYN, SYNACK, ACK) → Data transfer với congestion control (Slow Start → Congestion Avoidance, xen kẽ Fast Recovery khi cần) và flow control (rwnd) → Four-way teardown (FIN, ACK, FIN, ACK) → TIME_WAIT.*

---

**Câu 92.** Tại sao TCP reliable data transfer "phức tạp hơn" so với rdt3.0 (Stop-and-Wait) đơn giản?

A. Vì TCP phải handle cả congestion control, không chỉ reliability.  
B. Vì TCP dùng pipelining (nhiều segments in-flight), single retransmission timer, cumulative ACKs, fast retransmit, và RTT estimation — tất cả phải hoạt động đồng thời.  
C. Vì TCP phải handle cả IPv4 và IPv6.  
D. Vì TCP cần tương thích ngược với TCP Tahoe.

**Đáp án: B**  
*Giải thích: rdt3.0 là stop-and-wait với một packet in-flight. TCP dùng pipelining (window-based), phải quản lý nhiều unACKed segments với single timer, cumulative ACKs gây ambiguity, fast retransmit từ dup ACKs, và dynamic RTT estimation — phức tạp hơn nhiều.*

---

**Câu 93.** Nếu network hoàn toàn không có congestion và receiver buffer rất lớn, yếu tố nào giới hạn throughput của TCP?

A. Congestion window (cwnd).  
B. Chỉ còn receive window (rwnd) giới hạn.  
C. MSS và RTT.  
D. Số lượng segments trong flight.

**Đáp án: B**  
*Giải thích: Sending rate ≤ min(cwnd, rwnd)/RTT. Nếu không có congestion, cwnd tăng mãi (không bị reset). Giới hạn còn lại là rwnd (flow control của receiver) và bandwidth vật lý của link.*

---

**Câu 94.** Một researcher muốn thiết kế transport protocol cho video streaming real-time. Lý do nào khiến họ KHÔNG chọn TCP?

A. TCP không hỗ trợ multimedia data.  
B. TCP congestion control có thể làm giảm throughput đột ngột trong khi streaming cần constant rate; TCP cũng thêm delay từ retransmissions (stale data vô nghĩa với video real-time).  
C. TCP có overhead header quá lớn cho multimedia.  
D. TCP không thể xử lý đủ nhanh tốc độ cao của video streaming.

**Đáp án: B**  
*Giải thích: Hai vấn đề chính: (1) AIMD gây "saw-tooth" throughput — bad cho constant bitrate streaming. (2) TCP retransmit mọi packet → if delay lớn, "recovered" packet đã lỗi thời (playback đã qua). Tốt hơn là drop với UDP và xử lý tại application layer.*

---

**Câu 95.** Hãy phân tích: Khi xảy ra timeout trong TCP, tại sao "nhân đôi TimeoutInterval" (exponential backoff) lại là phản ứng đúng thay vì tính lại từ EstimatedRTT?

A. Vì sau timeout, EstimatedRTT chưa được update (chưa nhận SampleRTT mới).  
B. Vì timeout thường do network congestion — network đang bận, gửi lại ngay sẽ làm tình trạng tệ hơn; exponential backoff cho network thời gian phục hồi.  
C. Vì ACK của retransmit không thể dùng để tính SampleRTT.  
D. Cả A, B, và C đều đúng.

**Đáp án: D**  
*Giải thích: Tất cả ba lý do đều đúng: (A) Sau timeout, không có SampleRTT mới để cập nhật. (B) Exponential backoff là "congestion-friendly" behavior — back off khi network congested. (C) Retransmitted segments không được đo SampleRTT (Karn's algorithm).*

---

**Câu 96.** Tại sao cần exactly THREE-way handshake thay vì two-way để thiết lập TCP connection?

A. Vì three-way đảm bảo cả hai phía đã biết ISN của nhau và xác nhận rằng kết nối khả dụng theo cả hai chiều.  
B. Vì router cần xác nhận kết nối nên cần thêm một round-trip.  
C. Vì hai-way handshake không đủ bandwidth.  
D. Vì security yêu cầu ít nhất 3 bước xác thực.

**Đáp án: A**  
*Giải thích: Two-way handshake (SYN, SYNACK) chỉ xác nhận server nhận được SYN của client và đồng ý kết nối. Nhưng server không biết client đã nhận SYNACK chưa (connection khả dụng client→server chưa?). Three-way (thêm ACK từ client) đảm bảo cả hai chiều hoạt động và cả hai bên biết ISN của nhau.*

---

**Câu 97.** Trong môi trường high-bandwidth (10 Gbps), tại sao TCP AIMD truyền thống không hiệu quả?

A. Vì MSS quá nhỏ so với bandwidth.  
B. Vì additive increase quá chậm để fill link capacity sau mỗi loss event — cần hàng nghìn RTTs để khôi phục cwnd về W sau khi bị cắt xuống W/2.  
C. Vì TCP không hỗ trợ jumbo frames.  
D. Vì round-trip time quá nhỏ cho AIMD hoạt động.

**Đáp án: B**  
*Giải thích: Ví dụ: W = 83,333 segments, RTT = 100ms. Sau loss, cwnd = W/2. Để khôi phục về W cần W/2 × RTT = ~4,167 giây. Trong thời gian đó, network underutilized. Đây là lý do cần TCP CUBIC, BBR cho high-bandwidth environments.*

---

**Câu 98.** Xét một scenario: cwnd = 8 MSS, ssthresh = 4 MSS, nhận được 1 ACK mới. Đang ở trạng thái nào và cwnd mới là bao nhiêu?

A. Slow Start, cwnd = 9 MSS.  
B. Congestion Avoidance, cwnd = 8 + MSS×(MSS/8MSS) = 8 + 1/8 MSS ≈ 8.125 MSS.  
C. Fast Recovery, cwnd = 9 MSS.  
D. Slow Start, cwnd = 8 MSS (không tăng vì đã qua ssthresh).

**Đáp án: B**  
*Giải thích: cwnd (8 MSS) > ssthresh (4 MSS) → đang ở Congestion Avoidance. Mỗi ACK: cwnd += MSS²/cwnd = 1 MSS²/8 MSS = 1/8 MSS ≈ 0.125 MSS. Sau 8 ACKs (1 RTT): cwnd tăng 1 MSS. Không tăng 1 MSS ngay như Slow Start.*

---

**Câu 99.** Giải thích tại sao TCP được coi là "distributed asynchronous optimization algorithm" trong ngữ cảnh bandwidth allocation.

A. Vì TCP sử dụng distributed hash table để allocate bandwidth.  
B. Vì mỗi TCP sender điều chỉnh cwnd dựa trên local information (ACKs, loss) mà không cần global coordination, nhưng kết quả tổng thể hội tụ đến efficient và fair bandwidth allocation.  
C. Vì TCP dùng asynchronous I/O để gửi data.  
D. Vì TCP được thiết kế để chạy trên distributed computing systems.

**Đáp án: B**  
*Giải thích: Mỗi TCP sender là một "agent" độc lập, chỉ quan sát local behavior (ACKs đến, loss events). Không có central controller. Nhưng Kelly (1998) chứng minh: AIMD converges đến điểm tối ưu — maximize aggregate throughput trong khi achieve fair allocation — một kết quả ấn tượng về distributed optimization.*

---

**Câu 100.** Tổng kết: Nhận định nào sau đây là SAI về TCP?

A. TCP cung cấp reliable, in-order byte stream delivery.  
B. TCP dùng both flow control (rwnd) và congestion control (cwnd) để throttle sender.  
C. TCP intermediate routers duy trì connection state để hỗ trợ reliability.  
D. TCP dùng three-way handshake để establish connection và four-way teardown để close.

**Đáp án: C**  
*Giải thích: Đây là nhận định SAI. TCP là end-to-end protocol — intermediate routers KHÔNG duy trì TCP connection state. Routers chỉ xử lý IP datagrams. TCP state (sequence numbers, ACKs, buffers, variables) chỉ tồn tại tại hai end systems.*

---

## PHẦN XII: Câu hỏi Nâng cao — Phân tích và So sánh

**Câu 101.** So sánh: Tại sao ATM ABR dùng rate-based control còn TCP dùng window-based control?

A. Vì ATM có dedicated circuits nên biết exact capacity; TCP phải probe.  
B. ATM ABR có explicit rate feedback từ routers (RM cells), cho phép source tính toán chính xác rate tối đa. TCP không có network feedback, nên dùng window (số bytes in-flight) và điều chỉnh dựa trên loss signals.  
C. Vì ATM nhanh hơn TCP nên dùng rate-based.  
D. Không có sự khác biệt thực chất — cả hai đều control rate.

**Đáp án: B**  
*Giải thích: ATM ABR: routers set ER field trong RM cells → source biết exact rate có thể gửi. TCP: end-to-end, không có router feedback → dùng window mechanism và suy ra congestion từ packet loss/delay.*

---

**Câu 102.** Xét TCP Vegas: cách phát hiện congestion của nó khác TCP Reno như thế nào?

A. Vegas dùng packet loss như Reno nhưng phản ứng sớm hơn.  
B. Vegas phát hiện congestion từ RTT tăng (queuing delay) TRƯỚC khi packet loss xảy ra, cho phép giảm rate một cách proactive.  
C. Vegas dùng network-assisted congestion control từ routers.  
D. Vegas không có slow start — bắt đầu ngay ở Congestion Avoidance.

**Đáp án: B**  
*Giải thích: TCP Reno phản ứng với congestion SAU khi packet đã bị drop. TCP Vegas: RTT tăng = router buffers đang fill up = congestion sắp xảy ra → giảm rate linearly trước khi loss. Proactive thay vì reactive. Đây là tiền thân của BBR (Bottleneck Bandwidth and RTT).*

---

**Câu 103.** Khi hai TCP connections share cùng một bottleneck link, AIMD hội tụ như thế nào về mặt hình học?

A. Hội tụ theo đường thẳng đứng.  
B. Hội tụ dọc theo đường 45-degree (equal bandwidth share) thông qua zigzag pattern: increase along 45° (equal additive increase) → loss → reduce toward origin (multiplicative decrease toward half).  
C. Hội tụ đến điểm random trên full-utilization line.  
D. Không hội tụ — dao động mãi không ổn định.

**Đáp án: B**  
*Giải thích: Geometric proof: additive increase = di chuyển song song với đường 45° (tăng đều cả hai connections). Multiplicative decrease = di chuyển về phía origin × 0.5. Hai chuyển động này kéo throughput point đến giao điểm của equal-share line và full-utilization line.*

---

**Câu 104.** Xét DCCP — tại sao nó được thiết kế thay vì dùng UDP trực tiếp cho multimedia?

A. DCCP nhanh hơn UDP.  
B. DCCP cung cấp UDP-like unreliable service nhưng thêm congestion control tương thích TCP — giảm "unfairness" với TCP mà không ép dùng TCP reliability.  
C. DCCP hỗ trợ multicast tốt hơn UDP.  
D. DCCP có checksums mạnh hơn UDP.

**Đáp án: B**  
*Giải thích: Vấn đề: UDP không có congestion control → unfair với TCP (crowds out TCP traffic). DCCP = UDP-like (no reliability, low overhead) + application-selectable congestion control (TCP-compatible) → multimedia apps có thể "be a good citizen" trên network mà không cần full TCP.*

---

**Câu 105.** Khi segment TCP có PSH bit được set, điều đó có nghĩa gì?

A. Segment này là priority và phải được forward trước.  
B. Receiver nên pass data lên upper layer ngay lập tức, không chờ buffer thêm.  
C. Sender yêu cầu ACK ngay lập tức.  
D. Segment chứa dữ liệu mã hóa.

**Đáp án: B**  
*Giải thích: PSH (Push) bit yêu cầu receiver "push" data lên application layer ngay lập tức thay vì buffer cho đến khi có đủ data. Trong thực tế, PSH, URG và urgent data pointer ít được sử dụng nhưng tồn tại trong spec.*

---

**Câu 106.** Tại sao TCP connection teardown cần 4 segments (thay vì 2)?

A. Vì cần thêm round-trip để deallocate resources tại routers.  
B. Vì TCP là full-duplex — mỗi chiều cần đóng độc lập (FIN + ACK cho mỗi hướng), cho phép half-close (một bên đóng gửi nhưng vẫn nhận).  
C. Vì TCP cần verify không còn data in-flight trước khi đóng.  
D. Vì RST segments có thể làm gián đoạn quá trình.

**Đáp án: B**  
*Giải thích: Full-duplex: bên A có thể đóng sending direction (FIN → ACK) trong khi bên B vẫn tiếp tục gửi data. Đây là "half-close." Sau khi B xong, B gửi FIN → A gửi ACK. Tổng: 4 segments. Nếu cả hai muốn đóng cùng lúc, có thể simultaneous close với cũng 4 segments.*

---

**Câu 107.** Trong context của reliability, tại sao một TCP sender có thể retransmit segment dù không bị loss (premature timeout)?

A. Vì TCP không phân biệt được loss và delay.  
B. Vì nếu TimeoutInterval ước lượng quá nhỏ (SampleRTT variance lớn), segment có thể bị timeout trước khi ACK về dù không bị mất — chỉ bị delay.  
C. Vì duplicate detection ở receiver không hoạt động.  
D. Vì congestion window quá nhỏ.

**Đáp án: B**  
*Giải thích: Premature timeout: timeout xảy ra trước khi ACK về, dù segment không bị mất. Hệ quả: sender retransmit, receiver nhận duplicate (detect bằng seq number và discard), ACK original đến sau cũng được xử lý. Tăng unnecessary load lên network.*

---

**Câu 108.** Trong three-way handshake, tại sao server gửi server_isn trong SYNACK mà không dùng client_isn + 1 như ACK number?

A. Vì server muốn xác nhận sequence number riêng của mình cho luồng data từ server đến client.  
B. Vì ACK number là cho hướng client → server, còn server_isn là starting point cho hướng server → client (independent stream).  
C. Vì security yêu cầu server phải chọn số ngẫu nhiên.  
D. Cả A và B đều đúng.

**Đáp án: D**  
*Giải thích: TCP full-duplex có HAI luồng byte độc lập: client→server (dùng client_isn) và server→client (dùng server_isn). ACK trong SYNACK = client_isn+1 (xác nhận luồng C→S). server_isn là starting sequence number của luồng S→C. Ngẫu nhiên vì lý do security (tránh stale segments từ old connections).*

---

**Câu 109.** Phân tích: Tại sao TCP không thể dùng single timeout cho toàn bộ window giống như GBN đơn giản?

A. Vì TCP window quá lớn.  
B. Vì với pipelining, nhiều segments có thể đang in-flight đồng thời với các timeout intervals khác nhau. Timer phải gắn với oldest unACKed segment, không phải window tổng thể.  
C. Vì single timeout sẽ gây quá nhiều retransmissions.  
D. Vì TCP sử dụng hardware timer không cho phép multiple instances.

**Đáp án: B**  
*Giải thích: TCP recommended implementation dùng single timer nhưng gắn với oldest unACKed segment (SendBase). Khi timer expire, retransmit segment với seq nhỏ nhất chưa ACK. Khi nhận ACK mới, restart timer nếu còn unACKed segments. Đây là cách quản lý timer hiệu quả mà không cần timer per-segment.*

---

**Câu 110.** Giả sử một TCP connection đang ở Congestion Avoidance với cwnd = 16 MSS. Xảy ra timeout. Sau đó cwnd tăng đến ssthresh rồi tiếp tục. Tại cwnd = ssthresh + 2 MSS, connection đang ở giai đoạn nào và cwnd được tính thế nào?

A. Slow Start, cwnd tăng +1 MSS mỗi ACK.  
B. Congestion Avoidance, cwnd tăng +MSS²/cwnd mỗi ACK (≈ 1 MSS/RTT).  
C. Fast Recovery, cwnd tăng +1 MSS mỗi dup ACK.  
D. Slow Start vì chưa đạt ssthresh ban đầu.

**Đáp án: B**  
*Giải thích: Timeout với cwnd=16: ssthresh = 16/2 = 8 MSS, cwnd = 1 MSS, Slow Start. Khi cwnd đạt ssthresh=8: chuyển sang Congestion Avoidance (linear). Tại cwnd = ssthresh+2 = 10 MSS: đang ở Congestion Avoidance, mỗi ACK tăng MSS²/10MSS = 0.1 MSS, sau 10 ACKs (1 RTT) tăng 1 MSS.*

---

**Câu 111.** Nếu một TCP sender liên tục nhận được ACKs nhưng cwnd không bao giờ vượt quá rwnd, điều này cho thấy điều gì?

A. Network đang congested.  
B. Receiver đang là bottleneck — application tại receiver đọc data chậm, fill buffer → rwnd nhỏ → flow control limiting throughput, không phải congestion control.  
C. Sender đang bị firewall throttle.  
D. MSS quá nhỏ.

**Đáp án: B**  
*Giải thích: Nếu cwnd < rwnd: congestion limiting. Nếu cwnd ≥ rwnd và throughput thấp: flow control limiting — receiver buffer đầy do application đọc chậm. Đây là cách phân biệt hai loại bottleneck: network (congestion) hay receiver (flow control).*

---

**Câu 112.** Khi nmap gửi SYN đến target host và nhận lại RST, điều đó có ý nghĩa gì với attacker?

A. Target host không tồn tại.  
B. Port đó closed nhưng host accessible — không có firewall blocking trên path đó đến port đó.  
C. Target host đang congested.  
D. Target host dùng SYN cookies.

**Đáp án: B**  
*Giải thích: RST response = host reached + port closed. Nếu nhận SYNACK: port open. Nếu không nhận gì: firewall likely blocking (packet never reached host or RST being dropped). RST = "I'm reachable, but no service on this port."*

---

**Câu 113.** Trong scenario 2 của congestion control, nếu sender có thể biết chắc chắn packet bị lost (không phải timeout sớm), throughput đạt được như thế nào?

A. Throughput = offered load (không có overhead).  
B. Throughput < offered load vì một phần bandwidth dùng cho retransmissions.  
C. Throughput bằng offered load × 2/3.  
D. Throughput = 0 khi offered load cao.

**Đáp án: B**  
*Giải thích: Ngay cả khi chỉ retransmit khi biết chắc bị lost (không premature timeout), bandwidth vẫn bị chia: một phần cho original data, một phần cho retransmissions. Khi offered load = R/2, throughput ≈ R/3 (1/3 bandwidth dùng cho retransmissions do loss). Cost không thể tránh của finite-buffer congestion.*

---

**Câu 114.** Giải thích "piggybacking" trong ngữ cảnh TCP Telnet example.

A. Sender gửi data và ACK trong cùng một segment để tiết kiệm bandwidth.  
B. ACK cho data theo hướng này được "đính kèm" vào segment data theo hướng ngược lại — thay vì gửi ACK-only segment riêng.  
C. TCP header được đính kèm vào IP header để giảm overhead.  
D. Multiple data streams được ghép lại trong một TCP segment.

**Đáp án: B**  
*Giải thích: Trong Telnet example: server nhận 'C' từ client và muốn echo 'C' ngược lại. Thay vì gửi hai segment riêng (1 ACK + 1 data), server "piggyback" ACK vào segment data echo — segment có cả ACK field và data field đều valid. Tiết kiệm một round-trip.*

---

**Câu 115.** Tại sao SCTP (Stream Control Transmission Protocol) có thể hữu ích hơn TCP cho một số ứng dụng?

A. SCTP nhanh hơn TCP vì không có congestion control.  
B. SCTP hỗ trợ multi-streaming (nhiều logical streams trong 1 connection) — loss ở stream này không chặn delivery của stream khác (head-of-line blocking problem của TCP).  
C. SCTP cung cấp encryption tốt hơn TCP.  
D. SCTP không cần handshake.

**Đáp án: B**  
*Giải thích: TCP có head-of-line blocking: nếu segment bị mất, toàn bộ byte stream bị block cho đến khi receive được retransmit. SCTP multiplexes nhiều streams: loss ở stream A không block stream B. Hữu ích cho HTTP/2-like workloads (QUIC/HTTP3 cũng giải quyết vấn đề này tương tự).*

---

**Câu 116.** Trong network-assisted congestion control, "choke packet" là gì?

A. Packet bị drop vì network congested.  
B. Packet được router gửi trực tiếp đến source để báo "tôi đang congested, hãy giảm tốc độ gửi."  
C. Packet dùng để probe network capacity.  
D. Packet có priority cao được forward trước trong congested network.

**Đáp án: B**  
*Giải thích: Trong direct network feedback approach: congested router gửi choke packet ngược về source, thông báo source giảm tốc độ. Đây là explicit congestion signaling từ network, khác với TCP end-to-end approach (suy ra congestion từ loss/delay).*

---

**Câu 117.** Phân tích tình huống: Hai TCP connections A và B cùng share bottleneck link R. A có RTT = 10ms, B có RTT = 100ms. Theo lý thuyết, ai sẽ nhận được bandwidth nhiều hơn và tại sao?

A. Bandwidth bằng nhau vì AIMD công bằng.  
B. A nhận được nhiều hơn vì RTT nhỏ hơn → cwnd tăng nhanh hơn (nhiều RTT/giây) → chiếm bandwidth nhanh hơn khi capacity rảnh.  
C. B nhận nhiều hơn vì cần bù cho delay cao.  
D. Không thể dự đoán vì phụ thuộc vào application data.

**Đáp án: B**  
*Giải thích: AIMD tăng 1 MSS mỗi RTT. A có 10 RTTs mỗi giây, B có 1 RTT mỗi giây. Khi có packet loss và cả hai giảm cwnd × 0.5, A tăng trở lại nhanh gấp 10 lần B. A "grabs" bandwidth quay trở lại nhanh hơn nhiều. RTT inequality = AIMD unfairness trong practice.*

---

**Câu 118.** Xem xét EFCI trong ATM ABR: cơ chế này tương tự với mechanism nào trong TCP?

A. Tương tự checksum — detect error.  
B. Tương tự Explicit Congestion Notification (ECN) — router mark packet để signal congestion, receiver notify sender, không cần drop packet để signal congestion.  
C. Tương tự SYN cookies — prevent resource exhaustion.  
D. Tương tự SACK — selective acknowledgment.

**Đáp án: B**  
*Giải thích: EFCI (ATM) = ECN (TCP/IP): router sets congestion bit trong packet khi congested. Receiver notifies sender. Sender giảm rate. Cả hai đều là "proactive" congestion signal — không cần drop packet để signal congestion, khác với TCP traditional (loss-based). ECN được định nghĩa trong RFC 3168.*

---

**Câu 119.** Trong Scenario 3 (multihop, 4 senders), kết luận thiết kế quan trọng nhất cho network design là gì?

A. Router nên có infinite buffer để tránh drop.  
B. Cần cơ chế để không lãng phí upstream bandwidth khi packet sẽ bị drop downstream — "wasted work" problem.  
C. Tất cả connections nên có cùng RTT.  
D. Chỉ nên có tối đa 2 connections trên mỗi link.

**Đáp án: B**  
*Giải thích: Key insight từ Scenario 3: khi packet bị drop ở hop thứ n, toàn bộ bandwidth ở n-1 hops trước đó bị lãng phí. Điều này motivate các cơ chế như: router có thể ưu tiên packets đã traverse nhiều hops (đã đầu tư nhiều bandwidth), early congestion detection trước khi drop, và explicit congestion notification.*

---

**Câu 120.** Tổng kết về TCP: Nhận định nào sau đây ĐÚNG nhất về bản chất của TCP congestion control như một distributed algorithm?

A. TCP là centralized algorithm — một entity duy nhất quyết định rate cho tất cả connections.  
B. Mỗi TCP sender độc lập điều chỉnh cwnd dựa trên local observations (ACKs, loss), không có global knowledge hay explicit coordination. Kết quả hội tụ đến efficient và approximately fair allocation — một ví dụ điển hình về "emergence" trong distributed systems.  
C. TCP cần infrastructure hỗ trợ từ routers để hoạt động đúng đắn.  
D. TCP fairness chỉ đạt được khi tất cả connections có cùng RTT và MSS.

**Đáp án: B**  
*Giải thích: TCP congestion control là distributed, asynchronous, local-information-based algorithm. Mỗi sender tự điều chỉnh dựa trên ACKs và loss. Không có global coordinator. Kelly (1998) chứng minh convergence đến optimal allocation. Đây là một trong những thành tựu thiết kế đẹp nhất trong networking — đơn giản, robust, và provably efficient.*

---

*Hết — 120 câu trắc nghiệm bao gồm Section 3.5 đến 3.8*

---



| Section | Nội dung | Số câu |
|---------|----------|--------|
| 3.5.1–3.5.2 | TCP Connection & Segment Structure | 12 |
| 3.5.3 | RTT Estimation & Timeout | 8 |
| 3.5.4 | Reliable Data Transfer | 8 |
| 3.5.5 | Flow Control | 6 |
| 3.5.6 | Connection Management | 7 |
| 3.6 | Principles of Congestion Control | 10 |
| 3.7 (Slow Start) | TCP Congestion Control — Slow Start | 7 |
| 3.7 (CA & FR) | Congestion Avoidance & Fast Recovery | 8 |
| 3.7.1 | Fairness | 4 |
| Tổng hợp cơ bản | Multi-section integration | 20 |
| Nâng cao | Analysis & Comparison | 20 |
| **Tổng** | | **110 (+ 10 phụ)** |
