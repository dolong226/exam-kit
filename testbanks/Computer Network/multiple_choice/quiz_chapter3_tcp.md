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
