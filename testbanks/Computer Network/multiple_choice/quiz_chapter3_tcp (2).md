# Quiz: Chapter 3 — Transport Layer (Sections 3.5 – 3.8) Phần IV,V,VI
# Computer Networking: A Top-Down Approach (Kurose & Ross)

---


## PHẦN IV: Flow Control (Section 3.5.5)

**Câu 29.** Mục đích của Flow Control trong TCP là gì?

A. Ngăn sender gửi quá nhanh làm tắc nghẽn các router trên đường truyền.  
B. Ngăn sender gửi quá nhanh làm tràn receive buffer của receiver.  
C. Điều chỉnh tốc độ gửi dựa trên chất lượng đường truyền vật lý.  
D. Đảm bảo dữ liệu được nhận đúng thứ tự.

**Đáp án: B**  
*Giải thích: Flow control là "speed-matching" — đồng bộ tốc độ gửi của sender với tốc độ đọc dữ liệu của application tại receiver. Đây khác với congestion control, vốn liên quan đến tắc nghẽn trong network.*

---

**Câu 30.** Biến `rwnd` (receive window) được tính như thế nào?

A. rwnd = RcvBuffer  
B. rwnd = RcvBuffer – (LastByteRcvd – LastByteRead)  
C. rwnd = LastByteRcvd – LastByteRead  
D. rwnd = RcvBuffer / 2

**Đáp án: B**  
*Giải thích: rwnd = lượng spare room trong receive buffer = tổng dung lượng buffer trừ đi phần đang chứa data chưa được application đọc. Đây là lượng data tối đa sender có thể gửi thêm mà không làm tràn buffer.*

---

**Câu 31.** Host A (sender) đảm bảo không làm tràn receive buffer của Host B (receiver) bằng điều kiện nào?

A. cwnd ≤ rwnd  
B. LastByteSent – LastByteAcked ≤ rwnd  
C. NextSeqNum – SendBase ≤ rwnd  
D. LastByteSent ≤ RcvBuffer

**Đáp án: B**  
*Giải thích: Lượng data in-flight (đã gửi nhưng chưa ACK) = LastByteSent - LastByteAcked. Đây không được vượt quá rwnd mà receiver thông báo.*

---

**Câu 32.** Vấn đề gì xảy ra khi rwnd = 0 và Host B không có data để gửi về Host A?

A. Kết nối TCP bị reset tự động.  
B. Host A dừng gửi vĩnh viễn vì không nhận được cập nhật rwnd mới.  
C. Host A bị block và không biết khi nào buffer của B có chỗ trống.  
D. Host B gửi segment trống để thông báo khi buffer có chỗ trống.

**Đáp án: C**  
*Giải thích: Khi rwnd = 0, Host A dừng gửi. Nhưng TCP chỉ gửi segment cập nhật rwnd khi có data hoặc ACK để gửi. Nếu B không có data, A không bao giờ biết rwnd đã tăng → A bị block mãi mãi.*

---

**Câu 33.** TCP giải quyết vấn đề "rwnd = 0 deadlock" như thế nào?

A. Kết nối bị đóng và khởi tạo lại.  
B. Host A tiếp tục gửi các segment 1-byte data khi B thông báo rwnd = 0.  
C. Host A gửi probe segment định kỳ đến B để hỏi về rwnd.  
D. Host B chủ động gửi WINDOW UPDATE segment khi có chỗ trống.

**Đáp án: B**  
*Giải thích: TCP spec quy định: khi B thông báo rwnd = 0, A phải tiếp tục gửi các segment chứa 1 byte data. B sẽ ACK những segment này (và discard data nếu buffer đầy). Khi buffer có chỗ, ACK trả về sẽ có rwnd > 0, "mở khóa" A.*

---

**Câu 34.** Flow control và congestion control khác nhau ở điểm nào cốt lõi nhất?

A. Flow control dùng timer, congestion control dùng ACK.  
B. Flow control bảo vệ receiver buffer, congestion control bảo vệ network (routers).  
C. Flow control chỉ áp dụng ở sender, congestion control áp dụng ở cả hai phía.  
D. Flow control là cơ chế tầng link, congestion control là cơ chế tầng transport.

**Đáp án: B**  
*Giải thích: Flow control: ngăn sender làm tràn receive buffer của receiver (end-system concern). Congestion control: ngăn sender làm quá tải routers trong network (network concern). Cả hai đều throttle sender nhưng vì lý do khác nhau.*

---

## PHẦN V: TCP Connection Management (Section 3.5.6)

**Câu 35.** Trong Three-Way Handshake, thứ tự các segment được trao đổi là gì?

A. SYN → SYN+ACK → ACK  
B. SYN → ACK → SYN+ACK  
C. SYN+ACK → SYN → ACK  
D. ACK → SYN → SYN+ACK

**Đáp án: A**  
*Giải thích: (1) Client gửi SYN (SYN=1, seq=client_isn). (2) Server trả SYNACK (SYN=1, seq=server_isn, ACK=client_isn+1). (3) Client gửi ACK (SYN=0, ACK=server_isn+1). Sau bước 3, kết nối được thiết lập.*

---

**Câu 36.** Trong three-way handshake, ai là người đầu tiên cấp phát (allocate) buffers và variables cho kết nối?

A. Chỉ client allocate sau khi gửi SYN.  
B. Server allocate sau khi nhận SYN và gửi SYNACK; client allocate sau khi nhận SYNACK.  
C. Cả hai cùng allocate đồng thời.  
D. Chỉ server allocate vì client chỉ là người gửi.

**Đáp án: B**  
*Giải thích: Server allocate buffers và variables khi nhận SYN và gửi SYNACK (bước 2). Client allocate sau khi nhận SYNACK (bước 3). Việc server allocate sớm này là nguyên nhân tạo ra lỗ hổng SYN flood attack.*

---

**Câu 37.** Trong quá trình đóng kết nối TCP (connection teardown), bao nhiêu segment được trao đổi?

A. 2 segment (FIN và ACK)  
B. 3 segment  
C. 4 segment (FIN, ACK, FIN, ACK)  
D. Tùy thuộc vào bên nào khởi tạo đóng kết nối

**Đáp án: C**  
*Giải thích: Thông thường: (1) Client gửi FIN. (2) Server gửi ACK. (3) Server gửi FIN. (4) Client gửi ACK. Mỗi chiều cần một FIN và một ACK riêng biệt vì TCP là full-duplex.*

---

**Câu 38.** Mục đích của trạng thái TIME_WAIT trong TCP là gì?

A. Chờ để tất cả packets in-flight được giao hết.  
B. Cho phép client resend ACK cuối cùng nếu ACK bị mất, và đảm bảo các segment cũ trong network hết thời gian tồn tại.  
C. Đợi server xác nhận đã nhận FIN trước khi đóng.  
D. Cân bằng tải cho các kết nối mới trên cùng port.

**Đáp án: B**  
*Giải thích: TIME_WAIT (thường 30s đến 2 phút) đảm bảo: (1) Nếu ACK cuối bị mất, server sẽ retransmit FIN và client có thể resend ACK. (2) Đảm bảo không có "stray" segment từ kết nối cũ nằm trong network khi kết nối mới với cùng parameters được tạo.*

---

**Câu 39.** SYN Flood Attack lợi dụng điểm yếu nào của TCP?

A. TCP không kiểm tra tính hợp lệ của source IP address.  
B. Server allocate resources (buffers, variables) sau khi nhận SYN, trước khi hoàn thành three-way handshake.  
C. TCP sequence number có thể đoán được.  
D. TCP không có cơ chế xác thực (authentication) người dùng.

**Đáp án: B**  
*Giải thích: Attacker gửi hàng nghìn SYN với source IP giả. Server allocate resources cho mỗi "half-open connection." Resources bị cạn kiệt trước khi handshake hoàn tất. Legitimate clients bị từ chối dịch vụ (DoS).*

---

**Câu 40.** SYN Cookies giải quyết SYN Flood như thế nào?

A. Server giới hạn số lượng SYN nhận được mỗi giây.  
B. Server không allocate resources khi nhận SYN; thay vào đó tạo ISN là hash function của connection parameters, chỉ tạo kết nối khi nhận ACK hợp lệ.  
C. Server kiểm tra source IP trong database blacklist trước khi xử lý SYN.  
D. Server yêu cầu client gửi SYN hai lần để xác minh.

**Đáp án: B**  
*Giải thích: Với SYN cookies, server tạo ISN = hash(src IP, dst IP, src port, dst port, secret). Gửi SYNACK nhưng không lưu state. Khi nhận ACK = ISN+1, server tính lại hash để verify. Chỉ legitimate clients (nhận được SYNACK và gửi ACK đúng) mới tạo được kết nối.*

---

**Câu 41.** Khi host nhận được TCP SYN trên port không có ứng dụng nào đang lắng nghe, nó phản hồi bằng gì?

A. Không phản hồi (drop silently).  
B. Gửi SYNACK với window size = 0.  
C. Gửi TCP segment với RST bit = 1.  
D. Gửi ICMP Port Unreachable message.

**Đáp án: C**  
*Giải thích: TCP host gửi RST segment khi nhận SYN cho port không match với socket nào. Điều này nói với sender: "Tôi không có socket cho segment này, đừng gửi lại." (UDP thì khác: gửi ICMP Destination Unreachable.)*

---

## PHẦN VI: Principles of Congestion Control (Section 3.6)

**Câu 42.** Sự khác biệt cốt lõi giữa congestion control và flow control là gì?

A. Congestion control hoạt động ở tầng network, flow control ở tầng transport.  
B. Congestion control ngăn overloading network (routers), flow control ngăn overloading receiver buffer.  
C. Congestion control phản ứng với packet loss, flow control phản ứng với delay.  
D. Congestion control là end-to-end, flow control là hop-by-hop.

**Đáp án: B**  
*Giải thích: Đây là phân biệt quan trọng. Flow control: bảo vệ receiver's buffer. Congestion control: bảo vệ network infrastructure (routers, links). Cả hai đều throttle sender nhưng vì lý do hoàn toàn khác nhau.*

---

**Câu 43.** Trong Congestion Scenario 1 (2 senders, router với infinite buffers), điều gì xảy ra với throughput khi sending rate vượt R/2?

A. Throughput tiếp tục tăng tuyến tính.  
B. Throughput giữ nguyên ở R/2 (link saturation).  
C. Throughput giảm về 0.  
D. Throughput dao động ngẫu nhiên quanh R/2.

**Đáp án: B**  
*Giải thích: Với infinite buffer, không có packet loss. Nhưng link capacity bị chia đều cho 2 connections → max throughput mỗi connection = R/2. Gửi nhanh hơn chỉ làm queue dài hơn, không tăng được throughput.*

---

**Câu 44.** "Chi phí" của congestion trong Scenario 1 (infinite buffers) là gì?

A. Packet loss.  
B. Queuing delay tăng đến vô cực khi sending rate tiến đến R/2.  
C. Throughput giảm.  
D. Retransmissions lãng phí bandwidth.

**Đáp án: B**  
*Giải thích: Với infinite buffer, không mất gói nhưng delay tăng không giới hạn khi aggregate sending rate tiến đến link capacity R. Đây là cost đầu tiên của congestion: large queuing delays.*

---

**Câu 45.** Trong Scenario 2 (finite buffers, retransmission), "offered load" λ'in khác λin ở điểm nào?

A. λ'in bao gồm cả original data và retransmitted data.  
B. λ'in chỉ bao gồm retransmitted data.  
C. λ'in nhỏ hơn λin vì một số packets bị drop.  
D. λ'in = λin khi không có loss.

**Đáp án: A**  
*Giải thích: λin = rate của original data. λ'in (offered load) = λin + retransmissions. Khi có packet loss, sender phải retransmit, làm offered load vào network cao hơn actual data throughput.*

---

**Câu 46.** Đâu là "chi phí" của congestion thể hiện trong Scenario 2 mà không có trong Scenario 1?

A. Queuing delay tăng cao.  
B. Sender phải dùng bandwidth để retransmit các packet bị mất do buffer overflow.  
C. Throughput tối đa bị giới hạn bởi link capacity.  
D. Receiver phải xử lý duplicate packets.

**Đáp án: B**  
*Giải thích: Với finite buffers, packets bị drop → retransmissions. Bandwidth dùng cho retransmission là "wasted work." Thêm vào đó, nếu sender timeout sớm (premature timeout), cả original và retransmitted copy có thể cùng đến receiver → bandwidth lãng phí gấp đôi.*

---

**Câu 47.** Trong Scenario 3 (4 senders, multihop paths), tại sao throughput của kết nối A-C có thể giảm về 0 khi offered load tăng?

A. Vì link giữa A và R1 bị tắc nghẽn.  
B. Vì traffic của B-D chiếm toàn bộ buffer tại R2, không còn chỗ cho traffic A-C.  
C. Vì A-C và B-D dùng cùng destination port.  
D. Vì router R1 không đủ processing power.

**Đáp án: B**  
*Giải thích: Khi load của B-D rất cao, nó chiếm hầu hết buffer tại R2 (shared bottleneck). Traffic A-C từ R1 đến R2 bị drop tại R2. Công sức R1 bỏ ra để forward A-C packets đến R2 trở nên lãng phí hoàn toàn.*

---

**Câu 48.** "Chi phí" thứ ba của congestion, đặc trưng cho multihop scenario, là gì?

A. Receiver phải xử lý quá nhiều ACK.  
B. Bandwidth ở các upstream links bị lãng phí khi packet bị drop ở downstream router.  
C. Timeout interval phải tăng theo hàm mũ.  
D. Application layer bị chậm do congestion window nhỏ.

**Đáp án: B**  
*Giải thích: Khi packet bị drop tại router thứ n trong đường đi, toàn bộ công sức truyền packet qua n-1 router trước đó đều bị lãng phí. Capacity của n-1 upstream links đó có thể phục vụ packet khác tốt hơn.*

---

**Câu 49.** Hai phương pháp tiếp cận congestion control ở mức tổng quát là gì?

A. Proactive control và reactive control.  
B. End-to-end congestion control và network-assisted congestion control.  
C. Window-based control và rate-based control.  
D. Soft control và hard control.

**Đáp án: B**  
*Giải thích: End-to-end: network không cung cấp feedback, end systems tự suy ra congestion từ behavior (packet loss, delay). Ví dụ: TCP. Network-assisted: routers cung cấp explicit feedback về congestion state. Ví dụ: ATM ABR.*

---

**Câu 50.** TCP sử dụng phương pháp nào cho congestion control và tại sao?

A. Network-assisted, vì IP layer cung cấp congestion signals.  
B. End-to-end, vì IP layer không cung cấp explicit congestion feedback.  
C. Hybrid, kết hợp cả hai phương pháp.  
D. Rate-based, dựa trên Explicit Rate setting của routers.

**Đáp án: B**  
*Giải thích: IP cung cấp "best-effort" service và không có cơ chế báo congestion cho end systems. TCP phải tự suy ra congestion từ packet loss (timeout, triple duplicate ACK) và delay variations.*

---

**Câu 51.** Trong ATM ABR congestion control, EFCI bit có chức năng gì?

A. Cho phép receiver thông báo về lỗi checksum.  
B. Router set bit này trong data cell để báo congestion; receiver set CI bit trong RM cell trả về sender.  
C. Source set bit này để yêu cầu explicit rate setting.  
D. Network set bit này để drop packet có priority thấp.

**Đáp án: B**  
*Giải thích: EFCI (Explicit Forward Congestion Indication): congested switch set EFCI=1 trong data cell. Khi RM cell đến destination, nếu data cell cuối có EFCI=1, destination set CI=1 trong RM cell trả về, thông báo congestion cho source.*

---
