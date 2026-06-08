# Quiz: Chapter 3 — Transport Layer (Sections 3.5 – 3.8) Phần I,II,III
# Computer Networking: A Top-Down Approach (Kurose & Ross)

---

## PHẦN I: TCP Connection & Segment Structure (Section 3.5.1 – 3.5.2)

**Câu 1.** TCP được gọi là "connection-oriented" vì lý do nào sau đây?

A. Nó yêu cầu mỗi router trên đường truyền phải lưu trạng thái kết nối.  
B. Hai process phải thực hiện "handshake" và thiết lập các thông số trước khi truyền dữ liệu.  
C. Nó sử dụng kênh truyền TDM hoặc FDM dành riêng giữa hai đầu cuối.  
D. Nó chỉ hỗ trợ kết nối một chiều từ client đến server.

**Đáp án: B**  
*Giải thích: TCP yêu cầu hai bên trao đổi các segment đặc biệt (three-way handshake) để khởi tạo state variables trước khi truyền data. Trạng thái kết nối chỉ nằm ở hai end system, không ở intermediate routers.*

---

**Câu 2.** Điều gì xảy ra với TCP connection state tại các intermediate routers?

A. Mỗi router duy trì một bản sao đầy đủ của TCP connection state.  
B. Routers chỉ lưu thông tin về sequence number của các segment đang chuyển tiếp.  
C. Routers không duy trì TCP connection state; chúng chỉ xử lý các IP datagrams.  
D. Routers lưu trạng thái kết nối để hỗ trợ flow control.

**Đáp án: C**  
*Giải thích: TCP là giao thức end-to-end. Intermediate routers hoàn toàn không biết đến TCP connections — chúng chỉ thấy và xử lý IP datagrams.*

---

**Câu 3.** TCP cung cấp dịch vụ nào trong số các dịch vụ sau?

A. Full-duplex, point-to-point, multicast.  
B. Full-duplex, point-to-point, unicast.  
C. Half-duplex, multipoint, reliable.  
D. Simplex, point-to-point, unreliable.

**Đáp án: B**  
*Giải thích: TCP là full-duplex (hai chiều đồng thời) và point-to-point (một sender, một receiver). TCP không hỗ trợ multicast.*

---

**Câu 4.** Maximum Segment Size (MSS) trong TCP được xác định dựa trên yếu tố nào?

A. Kích thước của receive buffer tại receiver.  
B. MTU (Maximum Transmission Unit) của link-layer frame tại sending host.  
C. Giá trị do server quyết định trong quá trình three-way handshake.  
D. Tốc độ đường truyền giữa sender và receiver.

**Đáp án: B**  
*Giải thích: MSS được đặt sao cho một TCP segment (cộng với TCP/IP header ~40 bytes) vừa khít một link-layer frame có kích thước MTU. MSS là kích thước tối đa của application-layer data trong segment, không phải toàn bộ segment.*

---

**Câu 5.** Trường "Sequence Number" trong TCP header biểu thị điều gì?

A. Số thứ tự của segment trong dòng các segment đã gửi.  
B. Byte-stream number của byte đầu tiên trong data field của segment đó.  
C. Tổng số byte đã được receiver xác nhận.  
D. Số lần segment đã được retransmit.

**Đáp án: B**  
*Giải thích: TCP xem data là một luồng byte liên tục. Sequence number của một segment là vị trí (byte-stream number) của byte đầu tiên trong data field của segment đó.*

---

**Câu 6.** Host A đã nhận tất cả các byte từ 0 đến 535 từ Host B. Giá trị nào Host A sẽ đặt trong trường Acknowledgment Number khi gửi segment tiếp theo?

A. 535  
B. 536  
C. 537  
D. 0

**Đáp án: B**  
*Giải thích: Acknowledgment Number = sequence number của byte tiếp theo mà host đang chờ nhận. Host A đã nhận đến byte 535, nên nó chờ byte 536, do đó ACK = 536.*

---

**Câu 7.** TCP sử dụng kiểu acknowledgment nào?

A. Individual acknowledgment — xác nhận từng segment riêng lẻ.  
B. Negative acknowledgment — báo segment bị lỗi.  
C. Cumulative acknowledgment — xác nhận tất cả byte cho đến byte đầu tiên bị thiếu.  
D. Selective acknowledgment — xác nhận chính xác từng byte đã nhận.

**Đáp án: C**  
*Giải thích: TCP dùng cumulative ACK: ACK value y nghĩa là "tôi đã nhận đúng tất cả byte cho đến byte y-1, tôi đang chờ byte y." Nếu có byte bị thiếu ở giữa, TCP vẫn chỉ ACK đến byte cuối cùng nhận được liên tục.*

---

**Câu 8.** Trong ví dụ Telnet, Host A (client) gửi ký tự 'C' với sequence number 42. Server trả về segment với sequence number 79, ACK = 43, và echoes lại 'C'. Segment thứ ba từ client sẽ có ACK bằng bao nhiêu?

A. 79  
B. 80  
C. 43  
D. 42

**Đáp án: B**  
*Giải thích: Client nhận được byte 79 từ server (1 byte ký tự 'C'). Byte tiếp theo client chờ là 80, nên ACK = 80.*

---

**Câu 9.** Trường "Receive Window" trong TCP segment header phục vụ mục đích gì?

A. Chỉ ra kích thước tối đa của một segment.  
B. Thông báo cho sender biết số byte receiver sẵn sàng chấp nhận (flow control).  
C. Giới hạn tốc độ gửi dựa trên tình trạng congestion.  
D. Xác định số segment tối đa có thể gửi mà chưa cần ACK.

**Đáp án: B**  
*Giải thích: Trường 16-bit receive window được dùng cho flow control, thông báo cho sender biết còn bao nhiêu không gian trong receive buffer của receiver.*

---

**Câu 10.** Tại sao cả hai phía của một TCP connection đều chọn Initial Sequence Number (ISN) ngẫu nhiên?

A. Để tránh xung đột với các TCP connection đang chạy song song trên cùng port.  
B. Để ngăn các segment còn sót từ kết nối cũ bị nhầm lẫn là segment hợp lệ của kết nối mới.  
C. Để tăng entropy và bảo mật dữ liệu truyền đi.  
D. Để đảm bảo sequence number không bao giờ bị overflow.

**Đáp án: B**  
*Giải thích: Nếu dùng ISN cố định (ví dụ luôn bắt đầu từ 0), một segment bị trễ từ kết nối trước (cùng port numbers) có thể được nhầm là segment hợp lệ của kết nối mới. ISN ngẫu nhiên giảm thiểu rủi ro này.*

---

**Câu 11.** Flag bit nào trong TCP header được dùng để thiết lập kết nối (connection setup)?

A. URG và PSH  
B. SYN và FIN  
C. RST và ACK  
D. SYN và ACK

**Đáp án: D**  
*Giải thích: Quá trình thiết lập kết nối dùng SYN (synchronize) và ACK (acknowledge). FIN dùng để đóng kết nối, RST để reset, URG/PSH cho dữ liệu khẩn cấp.*

---

**Câu 12.** Kích thước điển hình của TCP header là bao nhiêu byte?

A. 8 bytes  
B. 12 bytes  
C. 20 bytes  
D. 40 bytes

**Đáp án: C**  
*Giải thích: TCP header điển hình (không có options) là 20 bytes. Header length field là 4-bit, chỉ số 32-bit words. Để so sánh, UDP header chỉ có 8 bytes.*

---

## PHẦN II: RTT Estimation & Timeout (Section 3.5.3)

**Câu 13.** SampleRTT là gì trong ngữ cảnh TCP?

A. Giá trị RTT trung bình tính từ tất cả các segment đã gửi.  
B. Thời gian từ khi gửi segment đến khi nhận được ACK cho segment đó.  
C. Thời gian timeout được cấu hình thủ công.  
D. Độ lệch chuẩn của các giá trị RTT đo được.

**Đáp án: B**  
*Giải thích: SampleRTT là khoảng thời gian đo được cho một segment cụ thể: từ lúc pass segment xuống IP cho đến khi nhận được ACK tương ứng.*

---

**Câu 14.** Tại sao TCP không đo SampleRTT cho các segment đã bị retransmit?

A. Vì retransmitted segment không có sequence number hợp lệ.  
B. Vì không thể phân biệt ACK nhận được là cho bản gốc hay bản retransmit (ambiguity).  
C. Vì retransmitted segment luôn có RTT bằng 0.  
D. Vì receiver không gửi ACK cho retransmitted segment.

**Đáp án: B**  
*Giải thích: Đây là vấn đề được mô tả bởi Karn (1987). Nếu segment bị retransmit và ta nhận được ACK, không biết ACK đó cho bản gốc hay bản retransmit — dùng sample đó sẽ gây ra sai lệch trong EstimatedRTT.*

---

**Câu 15.** Công thức tính EstimatedRTT trong TCP là gì, với α = 0.125?

A. EstimatedRTT = 0.5 × EstimatedRTT + 0.5 × SampleRTT  
B. EstimatedRTT = 0.875 × EstimatedRTT + 0.125 × SampleRTT  
C. EstimatedRTT = SampleRTT  
D. EstimatedRTT = min(EstimatedRTT, SampleRTT)

**Đáp án: B**  
*Giải thích: Theo RFC 6298, α = 0.125 (1/8). Công thức EWMA: EstimatedRTT = (1-α)·EstimatedRTT + α·SampleRTT = 0.875·EstimatedRTT + 0.125·SampleRTT. Đây là Exponential Weighted Moving Average, cho phép sample gần đây có trọng số cao hơn.*

---

**Câu 16.** Tại sao EstimatedRTT được gọi là Exponential Weighted Moving Average (EWMA)?

A. Vì nó sử dụng hàm mũ để tính timeout.  
B. Vì trọng số của một SampleRTT giảm theo hàm mũ qua từng lần cập nhật.  
C. Vì giá trị RTT tăng theo hàm mũ khi có congestion.  
D. Vì nó được tính toán bằng thuật toán Exponential Backoff.

**Đáp án: B**  
*Giải thích: Nếu khai triển công thức đệ quy, SampleRTT đo được i lần trước có trọng số (1-α)^i · α. Trọng số này giảm theo hàm mũ khi i tăng, nghĩa là sample càng cũ càng ít ảnh hưởng.*

---

**Câu 17.** DevRTT trong TCP đo lường điều gì?

A. Giá trị RTT lớn nhất đo được trong toàn bộ kết nối.  
B. Độ biến động ước tính của SampleRTT so với EstimatedRTT (EWMA của |SampleRTT - EstimatedRTT|).  
C. Sự khác biệt giữa RTT gửi đi và RTT nhận về.  
D. Thời gian xử lý tại receiver.

**Đáp án: B**  
*Giải thích: DevRTT = (1-β)·DevRTT + β·|SampleRTT - EstimatedRTT|, với β = 0.25. Nó đo độ biến động của RTT, dùng để điều chỉnh margin trong TimeoutInterval.*

---

**Câu 18.** Công thức tính TimeoutInterval trong TCP là gì?

A. TimeoutInterval = EstimatedRTT  
B. TimeoutInterval = EstimatedRTT + DevRTT  
C. TimeoutInterval = EstimatedRTT + 4 × DevRTT  
D. TimeoutInterval = 2 × EstimatedRTT

**Đáp án: C**  
*Giải thích: Theo RFC 6298: TimeoutInterval = EstimatedRTT + 4·DevRTT. Hệ số 4 cho margin đủ lớn khi RTT biến động nhiều, nhưng không quá lớn để tránh trễ không cần thiết khi RTT ổn định.*

---

**Câu 19.** Khi xảy ra timeout, TCP xử lý TimeoutInterval như thế nào?

A. Giữ nguyên TimeoutInterval.  
B. Đặt TimeoutInterval về giá trị ban đầu là 1 giây.  
C. Nhân đôi TimeoutInterval (exponential backoff).  
D. Tính lại TimeoutInterval từ EstimatedRTT và DevRTT mới nhất.

**Đáp án: C**  
*Giải thích: Mỗi lần timeout, TCP nhân đôi TimeoutInterval (exponential backoff). Điều này tránh việc sender liên tục retransmit trong khi mạng đang tắc nghẽn. Khi nhận được ACK mới, TimeoutInterval được tính lại theo công thức EstimatedRTT + 4·DevRTT.*

---

**Câu 20.** Giá trị TimeoutInterval khởi tạo được khuyến nghị là bao nhiêu?

A. 0.5 giây  
B. 1 giây  
C. 2 giây  
D. RTT đầu tiên đo được

**Đáp án: B**  
*Giải thích: RFC 6298 khuyến nghị TimeoutInterval ban đầu là 1 giây trước khi có đủ dữ liệu để ước lượng EstimatedRTT và DevRTT.*

---

## PHẦN III: Reliable Data Transfer trong TCP (Section 3.5.4)

**Câu 21.** TCP xây dựng reliable data transfer trên nền tảng nào?

A. IP service, vốn đã đảm bảo delivery theo thứ tự.  
B. IP service "best-effort" không đảm bảo delivery, thứ tự, hay tính toàn vẹn.  
C. Link-layer protocol đảm bảo không mất gói.  
D. Physical layer với error correction code.

**Đáp án: B**  
*Giải thích: IP là unreliable best-effort service — không đảm bảo delivery, không đảm bảo thứ tự, không đảm bảo integrity. TCP tạo ra reliable data transfer "trên nền" IP không tin cậy này.*

---

**Câu 22.** Biến `SendBase` trong TCP sender biểu thị điều gì?

A. Sequence number của segment tiếp theo sẽ được gửi.  
B. Sequence number của byte unacknowledged cũ nhất (oldest unacknowledged byte).  
C. Kích thước của congestion window hiện tại.  
D. Số lượng segment đã được ACK.

**Đáp án: B**  
*Giải thích: SendBase là sequence number của byte unacknowledged cũ nhất. SendBase-1 là byte cuối cùng đã được ACK thành công. Khi nhận ACK y > SendBase, sender cập nhật SendBase = y.*

---

**Câu 23.** Trong TCP, nếu ACK cho segment n+1 đến trước khi timeout của segment n, TCP sẽ làm gì với segment n?

A. Retransmit segment n ngay lập tức.  
B. Không retransmit segment n vì cumulative ACK n+1 ngầm xác nhận n đã nhận được.  
C. Retransmit segment n sau một khoảng delay cố định.  
D. Đánh dấu segment n là lost và yêu cầu selective retransmit.

**Đáp án: B**  
*Giải thích: TCP dùng cumulative ACK. Nếu ACK=120 đến (xác nhận đến byte 119), điều này ngầm xác nhận tất cả byte trước 120 đã nhận được — kể cả nếu ACK=100 bị mất. Đây là "cơ chế che" của cumulative ACK.*

---

**Câu 24.** Fast Retransmit được kích hoạt khi nào?

A. Khi timeout xảy ra lần đầu tiên.  
B. Khi sender nhận được 3 duplicate ACKs cho cùng một segment.  
C. Khi receiver phát hiện checksum error.  
D. Khi congestion window đầy.

**Đáp án: B**  
*Giải thích: 3 duplicate ACKs là dấu hiệu ngầm (implicit NAK) cho biết segment ngay sau segment được ACK 3 lần đã bị mất. TCP thực hiện fast retransmit — retransmit ngay mà không chờ timeout.*

---

**Câu 25.** Tại sao TCP chờ 3 duplicate ACKs thay vì chỉ 1 trước khi fast retransmit?

A. Vì 1 hay 2 duplicate ACK có thể do packet reordering trong network, không nhất thiết là mất gói.  
B. Vì TCP cần thời gian để verify checksum của segment.  
C. Vì receiver cần gửi 3 lần để đảm bảo sender nhận được tín hiệu.  
D. Vì RFC 5681 quy định cứng nhắc con số 3.

**Đáp án: A**  
*Giải thích: Một hoặc hai duplicate ACK có thể xuất hiện do reordering — segment đến không đúng thứ tự nhưng không bị mất. 3 duplicate ACKs là dấu hiệu đủ mạnh để kết luận gói bị mất, không phải bị reorder.*

---

**Câu 26.** Theo policy của TCP receiver về ACK generation, khi nào receiver gửi "delayed ACK"?

A. Khi nhận được out-of-order segment.  
B. Khi nhận được in-order segment và không có segment nào đang chờ ACK — chờ tối đa 500ms cho segment tiếp theo.  
C. Khi receive buffer đầy.  
D. Khi phát hiện duplicate segment.

**Đáp án: B**  
*Giải thích: Theo RFC 5681, khi nhận in-order segment và data up to expected sequence number đã được ACK hết, receiver chờ tối đa 500ms. Nếu segment tiếp theo đến trong thời gian đó, gửi 1 cumulative ACK cho cả hai.*

---

**Câu 27.** Khi receiver nhận được out-of-order segment (higher than expected sequence number), TCP receiver làm gì?

A. Discard ngay lập tức và không gửi ACK.  
B. Lưu lại segment và gửi ngay một duplicate ACK chỉ sequence number của byte tiếp theo đang chờ.  
C. Gửi Negative ACK (NAK) cho segment bị thiếu.  
D. Chờ 500ms rồi mới gửi ACK.

**Đáp án: B**  
*Giải thích: Khi phát hiện gap (segment đến có sequence number cao hơn expected), receiver lưu out-of-order segment và ngay lập tức gửi duplicate ACK chỉ ra sequence number của byte đang còn thiếu (lower end of gap).*

---

**Câu 28.** TCP được phân loại gần nhất với giao thức nào trong số GBN và SR, và tại sao không phải hoàn toàn?

A. Hoàn toàn là GBN vì dùng cumulative ACK và retransmit từ segment bị mất.  
B. Hoàn toàn là SR vì lưu out-of-order segments và retransmit từng segment riêng lẻ.  
C. Hybrid của GBN và SR: dùng cumulative ACK như GBN nhưng buffer out-of-order segments và retransmit ít nhất như SR.  
D. Không phải GBN cũng không phải SR vì TCP dùng timer thay vì window.

**Đáp án: C**  
*Giải thích: TCP dùng cumulative ACK (như GBN) nhưng buffer out-of-order segments (như SR) và thường chỉ retransmit segment bị mất (không retransmit toàn bộ window như GBN thuần túy). SACK (selective acknowledgment, RFC 2018) làm TCP giống SR hơn.*

---

