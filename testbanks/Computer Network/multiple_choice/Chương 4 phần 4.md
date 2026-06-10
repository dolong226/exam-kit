# Chương 4: Network Layer — Bộ câu hỏi ôn tập


**Câu 101.** Tại sao forwarding table entry trong datagram network dùng prefix thay vì địa chỉ đầy đủ?

A. Vì routers không đủ bộ nhớ để lưu địa chỉ 32-bit
B. Prefix-based aggregation giảm kích thước forwarding table từ 4+ tỷ entries xuống còn manageable — một prefix đại diện cho một dải địa chỉ được route cùng nhau
C. Vì địa chỉ IP ngắn hơn 32 bits
D. Vì prefix lookup nhanh hơn exact match

**Đáp án: B**
*Giải thích: Lý do chính là scalability: 4 tỷ entries cho IPv4 là không thực tế. Prefix-based forwarding (với longest prefix matching) cho phép hierarchical address aggregation — ISPs và networks sở hữu các address blocks, một prefix entry đại diện cho toàn bộ block.*

---

**Câu 102.** Tại sao "separation of data plane and control plane" được các nhà nghiên cứu đề xuất là có lợi?

A. Vì hardware data plane và software control plane không thể tích hợp
B. Vì tách biệt cho phép: thay thế centralized routing calculation (đơn giản hơn distributed), và enable network innovation (different control planes over fast hardware)
C. Vì nó giảm chi phí hardware của router
D. Vì nó cho phép loại bỏ forwarding tables

**Đáp án: B**
*Giải thích: Tách data plane (fast hardware) khỏi control plane (flexible software) có lợi: (1) Centralized route calculation đơn giản hơn distributed; (2) Các control plane khác nhau có thể chạy trên cùng hardware; (3) Well-defined API giữa hai plane. Đây là nền tảng của SDN (Software-Defined Networking).*

---

**Câu 103.** Một packet cần đi từ H1 đến H2. Tại router R1, input port nhận packet. Liệt kê đúng thứ tự các bước xử lý tại input port:

A. Forwarding table lookup → Physical layer processing → Link-layer processing → Switching fabric
B. Physical layer termination → Link-layer processing → Forwarding table lookup → Switching fabric
C. Switching fabric → Lookup → Physical layer → Link-layer
D. Link-layer → Physical layer → Lookup → Switching fabric

**Đáp án: B**
*Giải thích: Thứ tự đúng tại input port: (1) Physical layer termination (kết thúc physical link), (2) Link-layer processing (decapsulation, protocol handling), (3) Lookup trong forwarding table (xác định output port), sau đó gửi vào switching fabric.*

---

**Câu 104.** Xét buffer sizing rule mới B = RTT × C / √N: nếu N tăng lên 4 lần, buffer cần thiết thay đổi thế nào?

A. Tăng 4 lần
B. Giảm 4 lần (chia 4)
C. Giảm 2 lần (chia √4 = 2)
D. Không thay đổi

**Đáp án: C**
*Giải thích: B = RTT × C / √N. Nếu N tăng 4 lần → √N tăng 2 lần → B giảm 2 lần. Điều này có nghĩa là khi có nhiều TCP flows hơn, mỗi flow "smooths out" fluctuations, cần ít buffer hơn.*

---

**Câu 105.** Điều nào sau đây giải thích tại sao VC networks "arguably more complex" hơn datagram networks?

A. VC cần nhiều hardware hơn
B. VC cần call setup, per-call state maintenance ở routers, và signaling protocols — phức tạp hơn stateless datagram forwarding
C. VC xử lý nhiều loại packets hơn
D. VC cần routing algorithms phức tạp hơn

**Đáp án: B**
*Giải thích: VC networks cần: (1) signaling protocols để setup/teardown VCs, (2) mỗi router maintain connection state cho mỗi active VC, (3) coordination giữa các routers. Datagram network đơn giản hơn — chỉ cần forwarding table và routing algorithm.*

---

**Câu 106.** Trong RED algorithm, tại sao lại drop/mark packet với xác suất (probabilistic) thay vì drop tất cả khi queue vượt threshold?

A. Để tiết kiệm năng lượng xử lý
B. Probabilistic drop gửi congestion signal "sớm và nhẹ nhàng" cho một số senders, tránh synchronized drop của tất cả flows (global synchronization problem)
C. Để công bằng cho tất cả flows
D. Vì threshold không thể xác định chính xác

**Đáp án: B**
*Giải thích: Nếu drop tất cả khi queue đầy (drop-tail), tất cả TCP flows bị signal congestion đồng thời → tất cả giảm window đồng thời → throughput oscillation. RED's probabilistic early marking gửi signal sớm, tránh synchronization, giữ throughput stable.*

---

**Câu 107.** Giả sử một VC network có VC với path A-R1-R2-B, VC numbers là 12 (A-R1), 22 (R1-R2), 32 (R2-B). Khi VC teardown, điều gì phải xảy ra?

A. Chỉ end systems A và B cần được thông báo
B. Entries trong forwarding tables của R1 và R2 (và end systems) phải được xóa; tài nguyên đã reserve phải được giải phóng
C. Chỉ VC numbers cần được reset về 0
D. Forwarding tables không cần thay đổi — entries tự expire

**Đáp án: B**
*Giải thích: VC teardown: network layer thông báo cho end system phía kia, xóa entries tương ứng trong forwarding tables của tất cả routers trên path (R1, R2), và giải phóng tài nguyên đã reserve (bandwidth, buffers). Đây là overhead của VC model.*

---

**Câu 108.** Phát biểu nào ĐÚNG nhất về relationship giữa routing algorithm và forwarding table?

A. Forwarding table quyết định routing algorithm nào được sử dụng
B. Routing algorithm tính toán paths và outputs kết quả vào forwarding tables; forwarding tables được routers dùng để forward packets
C. Routing algorithm và forwarding table hoàn toàn độc lập
D. Forwarding table được tạo bởi end systems, không phải routers

**Đáp án: B**
*Giải thích: Đây là mối quan hệ một chiều: routing algorithm (control plane) tính toán optimal paths → insert values vào forwarding tables. Forwarding tables (data plane) được input ports dùng để quyết định forward packet ra đâu. Routing algorithm input vào forwarding table, không chiều ngược lại.*

---

**Câu 109.** Trong context network layer, tại sao "routers do not run application- and transport-layer protocols"?

A. Vì routers không đủ mạnh để chạy các protocols đó
B. Vì (trừ mục đích điều khiển) vai trò của routers là forward packets — không cần xử lý dữ liệu ở các layer cao hơn; điều này giúp routers đơn giản và nhanh hơn
C. Vì application protocols không tương thích với router hardware
D. Vì network layer protocol stack không include transport và application layers

**Đáp án: B**
*Giải thích: Routers chỉ cần đọc network-layer header để forward packet — không cần biết nội dung của TCP segment hay HTTP message. Điều này phù hợp với "dumb core, smart edge" và cho phép routers tập trung tối ưu cho forwarding.*

---

**Câu 110.** Điều nào phân biệt "congestion" ở output port và ở input port của router?

A. Congestion chỉ xảy ra ở output port, không bao giờ ở input port
B. Output port congestion: nhiều packets cùng muốn ra một link (output contention); Input port congestion: switch fabric không đủ nhanh hoặc HOL blocking ngăn packets vào switch fabric
C. Input port congestion không dẫn đến packet loss
D. Chúng hoàn toàn như nhau về nguyên nhân và hậu quả

**Đáp án: B**
*Giải thích: Output port queuing: khi Rswitch × N > Rline → nhiều packets đến output port nhanh hơn có thể truyền đi. Input port queuing: khi Rswitch < N × Rline (fabric không đủ nhanh) HOẶC HOL blocking. Cả hai đều dẫn đến packet loss nếu queue đầy.*

---

**Câu 111.** Tại sao địa chỉ đích trong datagram network phải được "stamped" bởi end system khi gửi packet?

A. Vì routers không thể đọc địa chỉ nguồn
B. Vì trong datagram network không có VC setup — không có pre-established path; mỗi packet phải tự mang đủ thông tin (địa chỉ đích) để các routers có thể forward độc lập
C. Vì địa chỉ đích cần để billing
D. Vì địa chỉ đích được dùng để tính checksum

**Đáp án: B**
*Giải thích: Datagram model: không có pre-established path, mỗi router forward độc lập dựa trên destination address. Mỗi packet mang destination address để mỗi router có thể tự quyết định forward như thế nào — không cần context về các packets trước đó.*

---

**Câu 112.** "Network service model defines the characteristics of end-to-end transport" — đây là trách nhiệm của layer nào và tại sao?

A. Transport layer — vì TCP/UDP quyết định service
B. Network layer — vì nó là layer thực sự chuyển packets giữa hosts, và transport layer dựa vào service của network layer
C. Application layer — vì applications quyết định QoS requirements
D. Link layer — vì link layer quyết định physical characteristics

**Đáp án: B**
*Giải thích: Network service model là trách nhiệm của network layer vì network layer là layer thực sự di chuyển packets từ host-to-host qua mạng. Transport layer nhận được dịch vụ từ network layer và build on top của đó để cung cấp process-to-process service.*

---

**Câu 113.** Trong ATM CBR, "virtual pipe" có nghĩa là gì thực tế?

A. Một physical cable dedicated cho mỗi connection
B. End-to-end delay, jitter, và cell loss rate đều được đảm bảo dưới giá trị tối đa được thỏa thuận khi setup kết nối
C. Một tunnel encrypted qua ATM network
D. Một reserved bandwidth channel không chia sẻ với connections khác

**Đáp án: B**
*Giải thích: "Virtual pipe" trong ATM CBR: mạng đảm bảo: (1) end-to-end delay < max specified, (2) jitter (delay variability) < max specified, (3) cell loss rate < max specified. Những thông số này được thỏa thuận khi CBR connection được thiết lập.*

---

**Câu 114.** Nếu bạn thiết kế một ứng dụng video conference real-time, tại sao bạn có thể KHÔNG dùng TCP mà vẫn hoạt động tốt trên Internet?

A. Vì TCP quá chậm cho video
B. Vì video conference có thể chịu được một ít packet loss (chất lượng giảm nhẹ) nhưng không chịu được high latency từ TCP retransmission — UDP phù hợp hơn vì application tự xử lý loss
C. Vì Internet không hỗ trợ TCP cho multimedia
D. Vì video conference yêu cầu multicast mà TCP không hỗ trợ

**Đáp án: B**
*Giải thích: Đây là trade-off: TCP retransmission gây delay — không chấp nhận được cho real-time. UDP + application-level loss concealment tốt hơn vì: một frame bị mất → chất lượng giảm nhẹ (chấp nhận được), không phải đợi retransmit (unacceptable delay cho real-time).*

---

**Câu 115.** Xét hai scenarios: (A) Routing algorithm centralized trên một server, (B) Routing algorithm decentralized trong mỗi router. Điểm GIỐNG NHAU giữa hai scenarios là gì?

A. Không có điểm gì giống nhau
B. Cả hai đều cuối cùng insert values vào forwarding tables trong routers; cả hai đều cần routers exchange thông tin
C. Cả hai chạy trên cùng hardware
D. Cả hai đều cần human operators cấu hình

**Đáp án: B**
*Giải thích: Dù routing computation ở đâu, kết quả phải là forwarding table values trong mỗi router. Centralized server vẫn cần thông tin về network topology (từ routers). Decentralized algorithms trực tiếp chạy trong routers và communicate với nhau. Đích đến giống nhau: forwarding tables được configured đúng.*

---

**Câu 116.** Điều gì xảy ra với "connection state" trong routers khi một VC bị teardown, và tại sao điều này quan trọng?

A. Connection state tự động expire sau một thời gian — không cần xử lý đặc biệt
B. Entries phải được xóa khỏi forwarding tables — quan trọng vì VC numbers có thể được tái sử dụng cho VCs mới; giữ stale entries có thể gây misrouting
C. Connection state được archive để audit
D. Routing processor giữ lại connection state để tối ưu future routing

**Đáp án: B**
*Giải thích: Khi VC teardown, entries phải được xóa. Quan trọng vì: (1) VC numbers có thể được tái sử dụng sau này — stale entries sẽ gây nhầm lẫn với VC numbers của connections mới, (2) Giải phóng tài nguyên (memory, bandwidth). Đây là một trong những reasons VC networks phức tạp hơn.*

---

**Câu 117.** Phân tích: tại sao Internet's best-effort model thực sự không tệ như nghe có vẻ?

A. Vì best-effort thực ra đảm bảo delivery trong hầu hết cases
B. Vì TCP ở transport layer cung cấp reliability/ordering; Internet tự nhiên ít mất packets; và end systems có thể implement bất kỳ service model nào cần — best-effort network đủ linh hoạt để support nhiều loại applications
C. Vì routers thực ra cố gắng deliver packets tốt nhất có thể
D. Vì modern hardware đủ nhanh để không có packet loss

**Đáp án: B**
*Giải thích: Best-effort không tệ vì: (1) TCP build on top để cung cấp reliable service khi cần; (2) Thực tế Internet ít mất packets; (3) Flexibility — applications chọn transport service phù hợp (TCP cho reliability, UDP cho low-latency); (4) Simple model → easy to build new services và connect new network technologies.*

---

**Câu 118.** Trong một crossbar switch với N=4 input và 4 output ports, trường hợp nào packets từ TẤT CẢ 4 input ports có thể được forward ĐỒNG THỜI?

A. Khi tất cả 4 packets muốn ra cùng một output port
B. Khi 4 packets muốn ra 4 output ports khác nhau — không có contention
C. Không bao giờ có thể forward 4 packets đồng thời
D. Chỉ khi switch fabric tốc độ gấp 4 lần line speed

**Đáp án: B**
*Giải thích: Crossbar switch có thể forward multiple packets song song miễn là các packets đến different output ports. Ví dụ: A→W, B→X, C→Y, D→Z — tất cả 4 có thể forward đồng thời. Chỉ bị blocking khi 2+ packets cùng muốn một output port.*

---

**Câu 119.** "Packet loss occurs here, at these queues within a router" — điều này có hàm ý gì về thiết kế network protocols?

A. Network protocols nên assume zero packet loss
B. Protocols cần assume packet loss là possible và handle nó appropriately — TCP dùng ACK/retransmission; UDP applications tự xử lý loss hoặc accept degradation
C. Router cần infinite buffer để tránh packet loss
D. Packet loss chỉ xảy ra ở edge routers, không ở backbone

**Đáp án: B**
*Giải thích: Biết rằng packet loss xảy ra tại router queues, protocols phải được thiết kế để handle: TCP dùng timeout + retransmission để detect và recover từ loss; UDP applications (video) dùng error concealment; congestion control (TCP, RED) để reduce loss rate. "Assume unreliable network" là design principle quan trọng.*

---

**Câu 120.** Kết luận quan trọng nhất từ việc so sánh VC vs datagram networks là gì?

A. VC networks hoàn toàn lỗi thời và không còn dùng nữa
B. Sự lựa chọn giữa VC (phức tạp nhưng có QoS guarantees) và datagram (đơn giản, flexible, best-effort) phản ánh sự đánh đổi cơ bản trong network design giữa performance guarantees và simplicity/flexibility
C. Datagram networks luôn tốt hơn VC networks
D. Sự khác biệt giữa chúng chỉ là về implementation, không phải fundamental design

**Đáp án: B**
*Giải thích: Đây là fundamental design trade-off: VC networks (ATM, frame relay) cung cấp QoS guarantees (bounded delay, guaranteed bandwidth) nhưng phức tạp hơn (connection state, signaling). Datagram networks (Internet) đơn giản, flexible, dễ scale nhưng chỉ best-effort. Mỗi loại phù hợp cho use cases khác nhau.*

---

**Câu 121.** Điểm nào sau đây là đúng về "packet switches" và "routers" theo định nghĩa chính xác trong sách?

A. Packet switch = router; chỉ là hai tên khác nhau cho cùng thiết bị
B. Packet switch là thuật ngữ tổng quát cho bất kỳ thiết bị nào forward packet dựa trên header; routers là packet switches hoạt động ở layer 3 (IP address); link-layer switches cũng là packet switches nhưng ở layer 2 (MAC address)
C. Router mạnh hơn packet switch vì xử lý nhiều layer hơn
D. Packet switch chỉ dùng trong LAN; router dùng trong WAN

**Đáp án: B**
*Giải thích: Chính xác theo text: "packet switch" = general device transferring packets based on header value. Routers = packet switches that forward based on network-layer fields. Link-layer switches = packet switches that forward based on link-layer frame fields.*

---

**Câu 122.** Nếu không có routing protocols và forwarding tables phải được cấu hình thủ công, vấn đề gì xảy ra khi network topology thay đổi (ví dụ, một link bị down)?

A. Mạng tự động tìm alternative paths
B. Packets tiếp tục được gửi ra failed link cho đến khi operators phát hiện và cập nhật tay tất cả affected forwarding tables — rất chậm và dễ lỗi
C. Routing algorithm tự động xử lý mà không cần protocols
D. End systems tự tìm alternative paths

**Đáp án: B**
*Giải thích: Không có routing protocols → không có automatic topology change detection và response. Operators phải thủ công phát hiện (có thể mất nhiều thời gian), xác định affected routes, và update tất cả forwarding tables — rất chậm và highly error-prone. Đây là lý do tại sao routing protocols quan trọng.*

---

**Câu 123.** "The Internet as a datagram network grew out of the need to connect computers together" — điều này ảnh hưởng đến design như thế nào?

A. Computers là dumb devices như điện thoại rotary, cần mạng thông minh để compensate
B. Computers là smart devices có thể xử lý phức tạp — cho phép network core đơn giản; end systems xử lý reliability, ordering, và other complex functions
C. Computers cần dedicated connections như telephone calls
D. Computers cần guaranteed bandwidth giống ATM CBR

**Đáp án: B**
*Giải thích: Điện thoại (rotary phones) = dumb devices → mạng PSTN phải smart (complex circuit switching, signaling). Computers = smart devices → Internet có thể đẩy complexity lên end systems; network core đơn giản (best-effort datagram). "Dumb core, smart edge" là fundamental Internet design principle.*

---

**Câu 124.** Thứ tự nào mô tả đúng "life of a packet" trong datagram network từ H1 đến H2?

A. H1 transport layer → H1 network layer → R1 → R2 → H2 network layer → H2 transport layer
B. H1 application layer → H1 transport layer → H1 network layer (encapsulate thành datagram) → R1 network layer (forward) → R2 network layer (forward) → H2 network layer (extract segment) → H2 transport layer
C. H1 physical layer → routers → H2 physical layer
D. H1 network layer → transport layer → application layer → H2

**Đáp án: B**
*Giải thích: Đúng theo Figure 4.1: H1 application → transport (create segment) → network (encapsulate vào datagram) → physical. Qua R1: network layer forward (không có transport/application processing). Qua R2: tương tự. H2: network layer (extract segment) → transport → application.*

---

**Câu 125.** Phát biểu nào MÔ TẢ ĐÚNG nhất về ATM ABR's Minimum Cell Rate (MCR)?

A. MCR là tốc độ tối đa được phép gửi
B. MCR là tốc độ tối thiểu được đảm bảo — sender luôn có thể gửi ít nhất ở rate MCR; có thể gửi cao hơn nếu mạng có đủ free resources
C. MCR là tốc độ trung bình phải duy trì
D. MCR là tốc độ được tính phí của connection

**Đáp án: B**
*Giải thích: MCR (Minimum Cell Rate) trong ATM ABR: đây là guaranteed floor — sender được đảm bảo có thể gửi ít nhất ở MCR. Nếu mạng có free resources, sender có thể burst lên Peak Cell Rate (PCR). Network cung cấp congestion feedback để điều chỉnh rate.*

---

**Câu 126.** Tại sao trong modern routers, lookup phải sử dụng TCAM hoặc các kỹ thuật đặc biệt thay vì linear search?

A. Vì forwarding tables quá lớn cho linear search
B. Vì với link 10 Gbps và 64-byte datagrams, chỉ có 51.2 ns per packet — linear search qua bảng lớn quá chậm; cần constant-time lookup (TCAM) hoặc efficient data structures
C. Vì TCAM rẻ hơn RAM thông thường
D. Vì linear search không hỗ trợ longest prefix matching

**Đáp án: B**
*Giải thích: Time constraint là driver: 10 Gbps / 64 bytes = 51.2 ns per packet. Linear search qua forwarding table (có thể hàng trăm nghìn entries) sẽ mất quá nhiều thời gian. TCAM cung cấp constant-time lookup; compressed trie và hardware pipelines cũng được dùng.*

---

**Câu 127.** Sự khác biệt về "where complexity lives" giữa telephone PSTN và Internet:

A. Cả hai đều đặt complexity trong network core
B. PSTN: complexity trong network core (circuit switching, signaling, per-call state); Internet: complexity ở edge/end systems (TCP, applications)
C. Cả hai đều đặt complexity ở end systems
D. PSTN: complexity ở end systems; Internet: complexity trong network core

**Đáp án: B**
*Giải thích: Fundamental contrast: PSTN thiết kế cho dumb end devices (rotary phones) → toàn bộ intelligence trong network core. Internet thiết kế cho smart computers → network core giữ simple (best-effort IP); intelligence (reliability, congestion control, applications) ở end systems.*

---

**Câu 128.** Trong context của virtual circuit, tại sao mỗi link có VC number riêng biệt thay vì một VC identifier toàn cục?

A. Vì global VC identifier gây bảo mật concerns
B. Hai lý do: (1) Giảm kích thước VC field trong packet header; (2) Đơn giản hóa VC setup — mỗi link independently chọn local VC number tránh coordination overhead để agree on globally unique number
C. Vì global VC identifier không thể fit vào IP header
D. Vì global VC identifier gây routing loops

**Đáp án: B**
*Giải thích: Lý do chính là (2): nếu yêu cầu cùng một VC number trên tất cả links, các routers phải trao đổi nhiều messages để thống nhất một số chưa được dùng bởi bất kỳ VC nào khác tại tất cả routers trên path — overhead lớn và phức tạp. Local VC numbers làm mỗi link độc lập.*

---

**Câu 129.** Điều nào sau đây là LÝ DO CHÍNH tại sao Internet không phải là VC network?

A. VC technology quá đắt để triển khai ở internet-scale
B. Các máy tính (end systems) có đủ intelligence để handle reliability/ordering; network core tối giản (best-effort) dễ scale, dễ liên kết diverse technologies, và dễ deploy new applications
C. IP protocol không compatible với VC
D. ATM (VC technology) quá chậm cho Internet speeds

**Đáp án: B**
*Giải thích: Đây là design choice, không phải technical limitation: Internet architects chọn datagram/best-effort vì: (1) Computers smart enough to handle reliability; (2) Simple network → easy to connect diverse link technologies; (3) Easy to add new applications (just add new servers/protocols); (4) Better fault tolerance — no per-connection state to lose.*

---

**Câu 130.** Tóm tắt: ba major parts của Chapter 4 là gì?

A. IP addressing, routing protocols, và network security
B. Sections 4.1–4.2 (network-layer functions và services), Sections 4.3–4.4 (forwarding), Sections 4.5–4.7 (routing)
C. Data plane, control plane, và management plane
D. IPv4, IPv6, và routing protocols

**Đáp án: B**
*Giải thích: Theo text: Chapter 4 có ba major parts: (1) Sections 4.1 và 4.2: network-layer functions và services; (2) Sections 4.3 và 4.4: forwarding; (3) Sections 4.5 đến 4.7: routing.*

---

**Câu 131.** Điều nào sau đây về Internet BEST MÔ TẢ lý do tại sao World Wide Web có thể được deploy nhanh chóng vào những năm 1990?

A. Vì Internet đã có guaranteed QoS cho HTTP traffic
B. Vì Web là ứng dụng chạy ở network edge (servers) — chỉ cần define HTTP protocol và attach web servers; không cần thay đổi bất kỳ router hay core network infrastructure nào
C. Vì routers được upgrade để hỗ trợ HTTP
D. Vì bandwidth tăng đủ nhanh để support Web traffic

**Đáp án: B**
*Giải thích: Đây là ví dụ điển hình của Internet's "dumb core, smart edge" philosophy: Web chỉ cần HTTP (application-layer protocol) chạy trên servers ở edge. Không cần thay đổi bất kỳ router nào, không cần signaling, không cần network-core support. Điều này contrast mạnh với telephone network nơi new services yêu cầu network upgrade.*

---

**Câu 132.** Giải thích tại sao trong Figure 4.10 (output port queuing), queuing xảy ra ngay cả khi Rswitch = N × Rline:

A. Vì switch fabric thực ra chậm hơn được tuyên bố
B. Vì tất cả N input ports gửi packets đến CÙNG một output port đồng thời — output link chỉ có thể truyền 1 packet/time unit, nhưng N packets đến trong 1 time unit → N-1 packets phải queue
C. Vì output port buffer quá nhỏ
D. Vì routing processor không đủ nhanh để update forwarding table

**Đáp án: B**
*Giải thích: Dù switch fabric N × Rline (nhanh gấp N lần), output link vẫn chỉ Rline. Worst case: N packets cùng muốn ra một output link → chỉ 1 được truyền → N-1 phải queue. Tiếp theo, trong thời gian truyền 1 packet, N packets mới có thể đến → queue tăng → eventual packet loss.*

---

**Câu 133.** Trong network management context, tại sao "counters used for network management must be updated" là một trong các actions tại input port?

A. Để tính toán shortest path
B. Để cung cấp visibility về network traffic — ví dụ số IP datagrams received, giúp operators monitor, troubleshoot, và plan capacity
C. Để tính phí người dùng
D. Để cập nhật forwarding table

**Đáp án: B**
*Giải thích: Network management counters (số datagrams received, bytes processed, errors...) tại input port cung cấp data cho: (1) Monitoring — phát hiện anomalies, (2) Troubleshooting, (3) Capacity planning, (4) Traffic engineering. SNMP và các network management protocols (Chapter 9) sử dụng data này.*

---

**Câu 134.** Điều nào sau đây ĐÚNG về sự khác biệt giữa host-to-host và process-to-process communication?

A. Cả hai đều do network layer cung cấp
B. Network layer cung cấp host-to-host (giữa hai máy); transport layer build trên đó để cung cấp process-to-process (giữa hai processes/applications cụ thể trên hai máy)
C. Transport layer cung cấp host-to-host; application layer cung cấp process-to-process
D. Process-to-process communication không liên quan đến network layer

**Đáp án: B**
*Giải thích: Phân cấp rõ ràng: Network layer: H1 ↔ H2 (host-level). Transport layer (dựa trên network layer service): Port 80 trên H1 ↔ Port 80 trên H2 (process-level, identified by port numbers). Application layer sử dụng transport service.*

---

**Câu 135.** Trong context của switching fabric, "switching via interconnection network" với multiple stages of switching elements có lợi ích gì so với single crossbar?

A. Đơn giản hơn để implement
B. Cho phép nhiều packets từ các input ports khác nhau cùng muốn một output port có thể proceed forward through fabric đồng thời (thay vì tất cả phải queue ngay tại input)
C. Rẻ hơn để sản xuất
D. Chậm hơn nhưng đáng tin cậy hơn

**Đáp án: B**
*Giải thích: Multi-stage interconnection networks (như Benes network) có thể route nhiều packets đến cùng một output port đồng thời qua các stages, giảm contention. Họ phức tạp hơn single crossbar nhưng cho phép higher throughput trong các scenarios có output port contention.*

---

**Câu 136.** Phát biểu nào về "security services" như một network-layer service là chính xác?

A. Internet hiện đang cung cấp built-in security services ở network layer
B. Security services (encryption, integrity, authentication) CÓ THỂ được cung cấp ở network layer — ví dụ IPsec — nhưng đây không phải là dịch vụ mà Internet's best-effort model cung cấp mặc định
C. Security services chỉ có thể được cung cấp ở application layer
D. Security ở network layer là không cần thiết vì transport layer đã có TLS

**Đáp án: B**
*Giải thích: Sách mô tả security services (encryption payload, integrity, authentication) là possible network-layer services. IPsec thực sự cung cấp điều này ở network layer. Tuy nhiên, Internet's default service model (best-effort) không include security — nó phải được thêm vào như một optional layer.*

---

**Câu 137.** Tại sao "packet switch" trong VC network vẫn được gọi là "router" trong context của Chapter 4?

A. Vì VC networks không còn tồn tại
B. Vì Chapter 4 focus vào network layer và trong context đó, tất cả packet-switching devices ở layer 3 đều được gọi chung là routers để đơn giản hóa discussion
C. Vì VC switches và IP routers có hardware giống hệt nhau
D. Vì thuật ngữ "router" được quy định bởi chuẩn quốc tế

**Đáp án: B**
*Giải thích: Text explicitly nói: "we'll even use the term router when talking about packet switches in virtual-circuit networks." Đây là simplification cho consistency trong Chapter 4 — focus vào network-layer functions, không phải implementation differences.*

---

**Câu 138.** Trong context forwarding, tại sao "the term port here is distinctly different from software ports"?

A. Router ports dùng số 32-bit; software ports dùng 16-bit
B. Router "ports" (input/output interfaces) là physical hardware interfaces; software "ports" (TCP/UDP) là logical identifiers cho processes/applications — hoàn toàn khác nhau về bản chất và layer
C. Router ports không thể bị numbered
D. Software ports chỉ tồn tại trong application layer

**Đáp án: B**
*Giải thích: Disambiguation quan trọng: Router input/output ports = physical hardware interfaces (plugs, cards) nhận và truyền packets. TCP/UDP ports = 16-bit numbers identifying processes/sockets. Cùng từ "port" nhưng ở hai layers hoàn toàn khác nhau.*

---

**Câu 139.** Điều nào ĐÚNG về việc routers trong datagram network "maintain forwarding state but not connection state"?

A. Datagram routers không maintain bất kỳ state nào
B. Datagram routers maintain forwarding state (destination prefix → interface, thay đổi chậm, minutes) nhưng KHÔNG maintain per-connection state — không biết về individual flows hay connections
C. Datagram routers maintain connection state giống VC routers
D. Connection state và forwarding state là cùng một thứ

**Đáp án: B**
*Giải thích: Sự phân biệt tinh tế: Datagram routers CÓ state (forwarding table — destination prefixes → interfaces, updated mỗi vài phút bởi routing algorithm). Nhưng họ KHÔNG có per-connection state — không biết "connection từ A đến B đang active" hay "packet này thuộc flow nào." Stateless về connections, stateful về routes.*

---

**Câu 140.** Kết luận tổng hợp: Network layer là "one of the most challenging layers" vì lý do gì?

A. Vì network layer dùng protocols phức tạp nhất
B. Vì network layer tồn tại trong EVERY host và router (không chỉ ở edge như transport/application layer) → network-layer protocols phải work ở scale của toàn Internet với billions of devices và countless link technologies
C. Vì network layer cần xử lý encryption và security
D. Vì network layer phải tương thích ngược với tất cả legacy systems

**Đáp án: B**
*Giải thích: Text explicitly: "there is a piece of the network layer in each and every host and router in the network. Because of this, network-layer protocols are among the most challenging." Scale là vấn đề cốt lõi — phải hoạt động ở billions of devices, diverse link technologies, và network-wide coordination cho routing.*

---

**Câu 141.** Theo kiến trúc router (Figure 4.6), điều nào sau đây được implement bằng HARDWARE?

A. Routing protocols (OSPF, BGP)
B. Input ports, switching fabric, output ports (forwarding plane)
C. Routing processor và control plane functions
D. Network management functions

**Đáp án: B**
*Giải thích: Forwarding plane (input ports + switching fabric + output ports) — implement in hardware vì yêu cầu nanosecond processing. Control plane (routing processor — execute routing protocols, management) — implement in software trên traditional CPU.*

---

**Câu 142.** Điều nào sau đây là ĐÚNG về "connection setup" so sánh ở network layer và transport layer?

A. Cả hai hoàn toàn giống nhau về cơ chế
B. Network-layer connection setup (VC): routers trên path FULLY AWARE và tham gia; Transport-layer (TCP): routers hoàn toàn OBLIVIOUS — chỉ end systems tham gia
C. Transport-layer connection setup liên quan đến routers; network-layer thì không
D. Cả hai đều chỉ liên quan đến end systems

**Đáp án: B**
*Giải thích: Contrast rõ ràng: TCP connection setup (SYN, SYN-ACK, ACK) — chỉ hai end systems biết, routers forward packets without knowledge of TCP connection. VC setup — mỗi router trên path tham gia, thêm entry vào forwarding table, fully aware của VC.*

---

**Câu 143.** Khi network có "a large number of TCP flows N passing through a link," buffer sizing rule mới B = RTT × C / √N có ý nghĩa gì về behavior của flows?

A. Nhiều flows = nhiều congestion = cần nhiều buffer hơn
B. Với N lớn, các flows "smooth out" lẫn nhau — peaks và valleys của individual flows tend to cancel out (statistical multiplexing), overall traffic smoother → cần ít buffer hơn
C. Nhiều flows làm buffer sizing phức tạp hơn, không thể predict
D. Buffer size không phụ thuộc vào số lượng flows

**Đáp án: B**
*Giải thích: Statistical multiplexing insight: khi N flows lớn, by law of large numbers, total traffic smoother hơn any individual flow. Một flow burst up khi flow khác backs off. Kết quả: peak-to-average ratio giảm → cần ít buffer hơn để absorb fluctuations. Đây là lý do buffer = RTT × C / √N thay vì RTT × C.*

---

**Câu 144.** Phát biểu nào sau đây tổng hợp đúng nhất lý do tại sao Internet chọn "best-effort" model?

A. Best-effort là model dễ implement nhất về mặt kỹ thuật
B. Best-effort maximizes flexibility: (1) Ít requirements lên link technologies → dễ kết nối diverse networks; (2) Applications chọn transport service phù hợp (TCP/UDP); (3) Dễ add new services ở edge; (4) Phù hợp với smart end systems
C. Best-effort đảm bảo performance tốt nhất cho tất cả applications
D. Best-effort là yêu cầu của ARPA khi thiết kế Internet ban đầu

**Đáp án: B**
*Giải thích: Comprehensive answer: best-effort không phải là limitation mà là deliberate design choice với multiple benefits: interoperability với diverse link technologies, flexibility cho applications, ease of service deployment, và alignment với smart-edge philosophy. Trade-off: no QoS guarantees, but application/transport layer fills in gaps.*

---

**Câu 145.** Điều nào sau đây KHÔNG ĐÚNG về ATM CBR service?

A. CBR cung cấp guaranteed constant bit rate
B. CBR đảm bảo end-to-end delay dưới một giá trị tối đa
C. CBR cho phép cells bị reorder nhưng không bị mất
D. CBR phù hợp cho real-time audio và video traffic

**Đáp án: C**
*Giải thích: Câu C sai: ATM CBR đảm bảo cells đến IN ORDER (không reorder) và cell loss rate dưới max specified value. CBR đảm bảo: (1) Constant bit rate (guaranteed bandwidth), (2) Bounded delay, (3) Bounded jitter, (4) In-order delivery, (5) Cell loss rate < specified value.*

---

**Câu 146.** Tổng hợp: Điều gì làm cho network layer "deceptively simple" theo sách?

A. Network layer chỉ có một chức năng đơn giản duy nhất
B. Phát biểu "move packets from a sending host to a receiving host" nghe đơn giản, nhưng thực tế đòi hỏi forwarding, routing, addressing, QoS, và nhiều mechanisms phức tạp khác — là layer phức tạp nhất trong stack
C. Network layer không có security concerns
D. Network layer chỉ cần một protocol là IP

**Đáp án: B**
*Giải thích: Text nói "the role of the network layer is thus deceptively simple — to move packets from a sending host to a receiving host." "Deceptively" vì statement này đơn giản nhưng implementation phức tạp cực kỳ: forwarding (hardware, nanosecond), routing (algorithms, protocols), addressing (IPv4, IPv6, NAT), fragmentation, QoS, etc.*

---

**Câu 147.** Trong context "match plus action," điều gì xảy ra trong NAT (Network Address Translation) tại input port?

A. NAT drop packets có destination address không hợp lệ
B. NAT match transport-layer port number trong incoming packet → action = rewrite port number (và thường cả IP address) trước khi forward
C. NAT duplicate packets đến nhiều servers
D. NAT add security headers cho packets

**Đáp án: B**
*Giải thích: NAT là ví dụ rõ ràng của "match plus action": Match = incoming packet có transport-layer port number match một giá trị trong NAT table; Action = rewrite port number (và/hoặc source/destination IP) để translate giữa private và public addresses. Chúng ta sẽ study NAT chi tiết hơn ở Section 4.4.*

---

**Câu 148.** Điều nào sau đây ĐÚNG về hai loại truyền thông tin routing: centralized vs decentralized?

A. Centralized routing không cần forwarding tables
B. Centralized: routing algorithm trên central site tính toán và download routing info đến mỗi router; Decentralized: routing algorithm chạy trong mỗi router, routers interact với nhau qua control messages
C. Decentralized routing không cần router communicate với nhau
D. Centralized routing là approach duy nhất được dùng trong Internet

**Đáp án: B**
*Giải thích: Hai approaches: (1) Centralized — một server tính toán paths, push routing info xuống routers (SDN concept); (2) Decentralized — mỗi router chạy routing algorithm, exchange control messages với neighbors (traditional approach: OSPF, BGP). Internet hiện tại dùng decentralized.*

---

**Câu 149.** Khi nói "routers implement layer 3 but must also implement layer 2 protocols," tại sao?

A. Vì router manufacturers muốn sell thêm features
B. Vì layer 3 (network layer) requires services from layer 2 (link layer) to actually transmit packets on physical links — không thể skip layers trong protocol stack
C. Vì IP protocol include layer 2 specifications
D. Vì hardware limitation của routers

**Đáp án: B**
*Giải thích: Fundamental layering principle: để forward một IP datagram ra một physical link, router phải: (1) Encapsulate datagram vào link-layer frame (layer 2, ví dụ Ethernet frame), (2) Transmit frame ra physical medium (layer 1). Router không thể "skip" layer 2 — cần nó để actually communicate trên physical links.*

---

**Câu 150.** Điều nào sau đây là ví dụ về "network service model defines characteristics of end-to-end transport" được thể hiện tốt nhất qua ATM CBR?

A. ATM CBR chỉ đảm bảo bandwidth, không đảm bảo gì khác
B. ATM CBR đồng thời định nghĩa AND đảm bảo: bounded delay, bounded jitter, guaranteed bandwidth, in-order delivery, và bounded loss rate — một complete set of end-to-end transport characteristics
C. ATM CBR chỉ đảm bảo loss rate
D. ATM CBR service model giống Internet best-effort

**Đáp án: B**
*Giải thích: ATM CBR là ví dụ perfect về comprehensive network service model: khi setup CBR connection, các thông số được thỏa thuận và đảm bảo — delay bound, jitter bound, bandwidth, in-order delivery, loss rate. Toàn bộ characteristics của "end-to-end virtual pipe" được specified và guaranteed. Contrast với Internet: không có gì được đảm bảo.*

