# Quiz: Chapter 3 — Transport Layer (Sections 3.5 – 3.8) Phần VII,VIII,IX
# Computer Networking: A Top-Down Approach (Kurose & Ross)

---


## PHẦN VII: TCP Congestion Control — Slow Start (Section 3.7)

**Câu 52.** Biến `cwnd` (congestion window) trong TCP giới hạn điều gì?

A. Kích thước tối đa của một TCP segment.  
B. Lượng unacknowledged data tối đa mà sender có thể có trong network.  
C. Số lượng TCP connections đồng thời.  
D. Tốc độ tối đa của receive buffer.

**Đáp án: B**  
*Giải thích: Điều kiện: LastByteSent – LastByteAcked ≤ min(cwnd, rwnd). cwnd giới hạn lượng data in-flight. Với RTT ổn định, sending rate ≈ cwnd/RTT.*

---

**Câu 53.** TCP coi event nào là "loss event" để trigger giảm tốc độ gửi?

A. Chỉ timeout.  
B. Chỉ triple duplicate ACK.  
C. Timeout hoặc nhận 3 duplicate ACKs.  
D. Bất kỳ duplicate ACK nào.

**Đáp án: C**  
*Giải thích: "Loss event" trong TCP congestion control = timeout OR receipt of 3 duplicate ACKs. Cả hai đều là dấu hiệu congestion, dù timeout nghiêm trọng hơn (packet hoặc ACK có thể bị mất lâu hơn).*

---

**Câu 54.** Trong giai đoạn Slow Start, cwnd tăng như thế nào?

A. Tăng 1 MSS mỗi RTT (linear increase).  
B. Tăng gấp đôi mỗi RTT (exponential increase).  
C. Tăng theo sqrt(cwnd) mỗi RTT.  
D. Giữ cố định cho đến khi nhận đủ ACK.

**Đáp án: B**  
*Giải thích: Slow Start: cwnd bắt đầu từ 1 MSS. Mỗi khi nhận ACK, cwnd tăng 1 MSS → sau 1 RTT cwnd nhân đôi. Tăng theo hàm mũ dù tên là "slow" start (slow vì bắt đầu từ 1 MSS, không phải slow về tốc độ tăng).*

---

**Câu 55.** Slow Start kết thúc theo những cách nào?

A. Chỉ khi cwnd đạt ssthresh.  
B. Chỉ khi xảy ra timeout.  
C. Khi cwnd ≥ ssthresh (→ Congestion Avoidance), khi timeout (→ Slow Start lại), hoặc khi nhận 3 dup ACKs (→ Fast Recovery).  
D. Khi cwnd đạt kích thước receive window.

**Đáp án: C**  
*Giải thích: Ba con đường thoát khỏi Slow Start: (1) cwnd đạt ssthresh → chuyển sang Congestion Avoidance. (2) Timeout → ssthresh=cwnd/2, cwnd=1 MSS, Slow Start lại từ đầu. (3) 3 duplicate ACKs → Fast Retransmit, Fast Recovery.*

---

**Câu 56.** Biến `ssthresh` (slow start threshold) được cập nhật như thế nào khi xảy ra loss event?

A. ssthresh = cwnd + 1 MSS  
B. ssthresh = cwnd / 2  
C. ssthresh = rwnd / 2  
D. ssthresh không thay đổi sau khi khởi tạo

**Đáp án: B**  
*Giải thích: Khi phát hiện congestion (loss event), ssthresh được set = cwnd/2. Đây là "lần cuối cwnd bắt đầu gây congestion ÷ 2" — một ước lượng an toàn về capacity của network.*

---

**Câu 57.** Giá trị khởi tạo của cwnd khi TCP connection mới được thiết lập là bao nhiêu?

A. ssthresh (thường 64 KB)  
B. rwnd của receiver  
C. 1 MSS  
D. 10 MSS

**Đáp án: C**  
*Giải thích: Theo RFC 3390, cwnd khởi tạo = 1 MSS (một số implement hiện đại có thể bắt đầu từ 10 MSS theo RFC 6928, nhưng giá trị chuẩn theo sách giáo khoa là 1 MSS).*

---

## PHẦN VIII: Congestion Avoidance & Fast Recovery (Section 3.7)

**Câu 58.** Trong giai đoạn Congestion Avoidance, cwnd tăng như thế nào?

A. Tăng gấp đôi mỗi RTT.  
B. Tăng 1 MSS mỗi RTT (additive increase).  
C. Tăng MSS²/cwnd mỗi RTT.  
D. Giữ nguyên cho đến khi loss event.

**Đáp án: B**  
*Giải thích: Congestion Avoidance dùng additive increase: cwnd tăng 1 MSS mỗi RTT (cụ thể: tăng MSS×(MSS/cwnd) mỗi khi nhận ACK → sau 1 RTT tăng tổng cộng 1 MSS). Thận trọng hơn Slow Start vì gần đến ngưỡng congestion.*

---

**Câu 59.** Khi xảy ra timeout trong Congestion Avoidance, TCP làm gì với cwnd và ssthresh?

A. ssthresh = cwnd/2, cwnd = ssthresh, chuyển sang Congestion Avoidance.  
B. ssthresh = cwnd/2, cwnd = 1 MSS, chuyển sang Slow Start.  
C. cwnd = cwnd/2, ssthresh không đổi.  
D. ssthresh = 1 MSS, cwnd = 1 MSS.

**Đáp án: B**  
*Giải thích: Timeout là dấu hiệu congestion nghiêm trọng. TCP phản ứng mạnh: ssthresh = cwnd/2, cwnd = 1 MSS, quay về Slow Start. Đây là phản ứng cùng với khi timeout xảy ra ở Slow Start.*

---

**Câu 60.** Khi nhận 3 duplicate ACKs trong Congestion Avoidance, TCP thực hiện gì?

A. ssthresh = cwnd/2, cwnd = 1 MSS, Slow Start.  
B. ssthresh = cwnd/2, cwnd = ssthresh + 3·MSS, Fast Recovery.  
C. ssthresh = cwnd/2, cwnd = ssthresh, Congestion Avoidance.  
D. cwnd không đổi, chỉ retransmit segment bị mất.

**Đáp án: B**  
*Giải thích: Triple dup ACK là loss event nhẹ hơn timeout (network vẫn đang deliver packets). TCP Reno: ssthresh = cwnd/2, cwnd = ssthresh + 3·MSS (3 MSS thêm vì đã nhận 3 dup ACK), chuyển sang Fast Recovery.*

---

**Câu 61.** Trong Fast Recovery, cwnd được điều chỉnh như thế nào?

A. cwnd giữ nguyên cho đến khi nhận ACK mới.  
B. Tăng 1 MSS cho mỗi duplicate ACK nhận được; khi ACK mới đến, cwnd = ssthresh, chuyển về Congestion Avoidance.  
C. Giảm dần về 1 MSS.  
D. Tăng gấp đôi mỗi RTT như Slow Start.

**Đáp án: B**  
*Giải thích: Fast Recovery: mỗi dup ACK → cwnd += 1 MSS (inflate window để đảm bảo throughput trong khi chờ retransmit). Khi nhận ACK mới (new ACK) → cwnd = ssthresh, transition về Congestion Avoidance (deflate).*

---

**Câu 62.** TCP Tahoe và TCP Reno phản ứng khác nhau như thế nào khi nhận 3 duplicate ACKs?

A. Không khác nhau — cả hai đều chuyển về Slow Start.  
B. Tahoe: cwnd = 1 MSS, Slow Start. Reno: cwnd = ssthresh + 3·MSS, Fast Recovery.  
C. Tahoe: Fast Recovery. Reno: Slow Start.  
D. Tahoe: cwnd giữ nguyên. Reno: cwnd = cwnd/2.

**Đáp án: B**  
*Giải thích: TCP Tahoe (phiên bản cũ) không có Fast Recovery — luôn set cwnd = 1 MSS khi loss. TCP Reno (phiên bản cải tiến) phân biệt timeout (nặng, → Slow Start) và triple dup ACK (nhẹ hơn, → Fast Recovery).*

---

**Câu 63.** AIMD là viết tắt của gì và mô tả hành vi nào của TCP?

A. Automatic Increase, Maximum Decrease — cwnd tăng tự động và giảm tối đa khi loss.  
B. Additive Increase, Multiplicative Decrease — cwnd tăng tuyến tính (1 MSS/RTT) và giảm nhân (×1/2) khi loss.  
C. Adaptive Increase, Minimal Decrease — cwnd tăng thích nghi và giảm nhỏ khi loss.  
D. Asymmetric Increase, Multiplicative Decrease — cwnd tăng không đều và giảm nhân khi loss.

**Đáp án: B**  
*Giải thích: AIMD = Additive Increase (CA: +1 MSS/RTT) + Multiplicative Decrease (chia đôi cwnd khi triple dup ACK). Tạo ra "saw-tooth" pattern, được chứng minh là optimal về mặt lý thuyết cho bandwidth allocation.*

---

**Câu 64.** "Saw-tooth" behavior của TCP cwnd xuất hiện do điều gì?

A. Timer tự động điều chỉnh cwnd theo chu kỳ.  
B. Additive increase (linear growth) xen kẽ với multiplicative decrease (halving) khi loss event xảy ra.  
C. Receiver window thay đổi theo ứng dụng.  
D. Congestion window bị giới hạn bởi ssthresh.

**Đáp án: B**  
*Giải thích: cwnd tăng tuyến tính (1 MSS/RTT trong CA) cho đến khi xảy ra loss → giảm đột ngột (×0.5) → tăng tuyến tính trở lại. Pattern này lặp lại tạo ra dạng "saw-tooth."*

---

**Câu 65.** TCP được gọi là "self-clocking" vì lý do gì?

A. Nó sử dụng hardware clock để đo RTT chính xác.  
B. Việc nhận ACKs (triggered bởi packets được deliver thành công) tự động kích hoạt tăng cwnd.  
C. Timeout tự điều chỉnh theo biến động của network.  
D. Send rate tự đồng bộ với receive rate thông qua rwnd.

**Đáp án: B**  
*Giải thích: TCP dùng ACKs như "clock ticks" để tăng cwnd. ACK đến = signal rằng segment đã được deliver thành công = network không congested = có thể gửi thêm. Cơ chế này tự vận hành mà không cần explicit signal từ network.*

---

**Câu 66.** Throughput trung bình của một TCP connection (theo mô hình macroscopic đơn giản) với W là cwnd khi loss xảy ra là bao nhiêu?

A. W / RTT  
B. W / (2 × RTT)  
C. 0.75 × W / RTT  
D. 1.5 × W / RTT

**Đáp án: C**  
*Giải thích: cwnd dao động từ W/2 đến W. Throughput trung bình = (W/2 + W)/2 ÷ RTT = 0.75W/RTT. Công thức phức tạp hơn (liên quan đến loss rate L): throughput ≈ 1.22·MSS/(RTT·√L).*

---

## PHẦN IX: Fairness trong TCP (Section 3.7.1)

**Câu 67.** TCP AIMD được coi là "fair" theo nghĩa nào?

A. Tất cả users nhận băng thông bằng nhau bất kể RTT.  
B. Các TCP connections chia sẻ bottleneck link bandwidth xấp xỉ bằng nhau (mỗi connection ~R/K với K connections).  
C. Connections có RTT lớn hơn nhận bandwidth lớn hơn để bù.  
D. UDP và TCP được ưu tiên bandwidth như nhau.

**Đáp án: B**  
*Giải thích: Về mặt lý thuyết (với cùng RTT và MSS), AIMD hội tụ đến equal sharing. Khi joint throughput < R: cả hai tăng. Khi loss: cả hai giảm × 0.5. Quá trình này hội tụ đến điểm giao nhau của "equal share line" và "full utilization line."*

---

**Câu 68.** Tại sao connections có RTT nhỏ hơn có lợi thế về bandwidth so với connections có RTT lớn hơn?

A. Vì RTT nhỏ hơn → timeout ít xảy ra hơn.  
B. Vì RTT nhỏ hơn → cwnd tăng nhanh hơn (nhiều ACK/giây hơn) → grab available bandwidth nhanh hơn.  
C. Vì RTT nhỏ hơn → ssthresh cao hơn.  
D. Vì RTT lớn hơn làm tăng xác suất packet loss.

**Đáp án: B**  
*Giải thích: cwnd tăng 1 MSS mỗi RTT. Connection có RTT nhỏ hơn có nhiều RTTs hơn trong cùng thời gian → tăng cwnd nhanh hơn → chiếm được bandwidth nhiều hơn khi bandwidth vừa được giải phóng.*

---

**Câu 69.** Tại sao nhiều multimedia applications chọn UDP thay vì TCP?

A. UDP nhanh hơn TCP vì không có handshake.  
B. UDP không bị throttle bởi congestion control — cho phép gửi ở constant rate kể cả khi mạng congested.  
C. UDP có built-in reliability tốt hơn TCP cho multimedia.  
D. UDP hỗ trợ multicast còn TCP thì không hỗ trợ.

**Đáp án: B**  
*Giải thích: TCP congestion control giảm throughput khi network congested. Multimedia apps (streaming, VoIP) prefer constant rate với occasional loss hơn là variable rate với no loss. UDP cho phép app tự quản lý rate mà không bị TCP throttle.*

---

**Câu 70.** Vấn đề fairness nào vẫn tồn tại dù có thể ép UDP phải "fair"?

A. TCP connections không thể phân biệt với UDP connections.  
B. Ứng dụng có thể mở nhiều parallel TCP connections, mỗi connection nhận share bằng nhau → tổng share lớn hơn.  
C. MTU khác nhau trên các links gây ra bất công bằng.  
D. Server có thể cấp ưu tiên cho kết nối trả phí.

**Đáp án: B**  
*Giải thích: Một app dùng 11 parallel connections chia sẻ link với 9 apps mỗi app dùng 1 connection → app đó nhận 11/(11+9) = 55% bandwidth. Web browsers thường dùng multiple parallel connections để tải nhanh hơn.*

---

