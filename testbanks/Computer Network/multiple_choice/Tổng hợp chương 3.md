# Quiz: Chapter 3 — Transport Layer (Sections 3.5 – 3.8)
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

## Tóm tắt phân bổ câu hỏi

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
