# Chương 4: Network Layer — Bộ câu hỏi ôn tập

## Câu hỏi tổng hợp và so sánh

**Câu 61.** Điều nào sau đây đúng về sự khác biệt giữa forwarding và routing?

A. Forwarding là chức năng network-wide; routing là chức năng local tại mỗi router
B. Forwarding là chức năng local tại mỗi router (data plane); routing là chức năng network-wide xác định end-to-end paths (control plane)
C. Cả hai đều là chức năng local tại từng router
D. Cả hai đều là chức năng network-wide

**Đáp án: B**
*Giải thích: Đây là phân biệt quan trọng: forwarding = chuyển packet từ input sang output trong một router đơn (data plane, hardware, nanosecond); routing = xác định path từ source đến destination qua toàn mạng (control plane, software, millisecond–second).*

---

**Câu 62.** Trong VC network, nếu router R1 có entry: Incoming Interface=1, Incoming VC#=12, Outgoing Interface=2, Outgoing VC#=22. Packet đến interface 1 với VC#=12 sẽ được xử lý thế nào?

A. Packet bị drop vì VC# không hợp lệ
B. Packet được forward ra interface 2 với VC# được thay thành 22
C. Packet được forward ra interface 2 với VC# giữ nguyên là 12
D. Packet được gửi đến routing processor để xử lý

**Đáp án: B**
*Giải thích: Router tra cứu forwarding table với (incoming interface=1, incoming VC#=12) → tìm thấy entry → forward packet ra outgoing interface=2 và thay thế VC# thành 22.*

---

**Câu 63.** Tại sao Internet chọn datagram model thay vì VC model?

A. Datagram model nhanh hơn VC model trong mọi trường hợp
B. Datagram model đơn giản hơn cho network, phù hợp với end systems thông minh có thể tự xử lý reliability và ordering
C. Datagram model đảm bảo QoS tốt hơn
D. VC model không thể scale cho internet-scale networks

**Đáp án: B**
*Giải thích: Internet architects muốn kết nối computers (end systems thông minh), không phải dumb phones. Network layer đơn giản tối đa (best-effort) → dễ liên kết diverse technologies; các tính năng phức tạp như reliability được xử lý ở end systems.*

---

**Câu 64.** Khi nói "packet được dropped tại router," điều này thực sự xảy ra ở đâu trong kiến trúc router?

A. Tại routing processor khi không tìm thấy route
B. Tại các queues (hàng đợi) ở input ports hoặc output ports khi memory bị cạn kiệt
C. Tại switching fabric khi có contention
D. Tại forwarding table khi không có matching entry

**Đáp án: B**
*Giải thích: Packets bị "lost within the network" hoặc "dropped at a router" thực sự xảy ra tại các queues trong router — khi queue đầy (memory exhausted), arriving packets phải bị drop.*

---

**Câu 65.** So sánh: trong VC network, routers cần duy trì loại state nào mà datagram network không cần?

A. Forwarding table state
B. Connection state — thông tin về mỗi ongoing VC (VC numbers, interfaces)
C. Routing table state
D. ARP cache state

**Đáp án: B**
*Giải thích: VC networks yêu cầu routers duy trì connection state cho mỗi VC đang hoạt động. Datagram networks không có VCs, nên không cần connection state — chỉ cần forwarding state (destination prefix → interface) thay đổi chậm.*

---

**Câu 66.** Loại switching nào trong router hỗ trợ multiple parallel forwarding tốt nhất?

A. Switching via memory
B. Switching via a bus
C. Switching via interconnection network (crossbar)
D. Cả ba đều hỗ trợ như nhau

**Đáp án: C**
*Giải thích: Crossbar switch cho phép forward nhiều packets song song — ví dụ A→Y và B→X đồng thời — miễn là không cùng output port. Memory switching và bus switching đều chỉ xử lý một packet tại một thời điểm.*

---

**Câu 67.** Điều nào sau đây KHÔNG phải là dịch vụ được cung cấp bởi Internet network layer?

A. Best-effort delivery
B. Chuyển packets từ sending host đến receiving host
C. Guaranteed in-order packet delivery
D. Host-to-host communication

**Đáp án: C**
*Giải thích: Internet's best-effort service không đảm bảo in-order delivery, timing, hay delivery. Guaranteed in-order delivery là tính năng của TCP (transport layer), không phải network layer.*

---

**Câu 68.** Tại sao "packet switch" là thuật ngữ tổng quát hơn "router"?

A. Packet switch chỉ hoạt động ở layer 2; router hoạt động ở layer 3
B. Packet switch là thiết bị chuyển tiếp packet dựa trên header value — bao gồm cả link-layer switches (layer 2) và routers (layer 3)
C. Router là thiết bị mạnh hơn packet switch
D. Packet switch chỉ dùng trong LAN; router dùng trong WAN

**Đáp án: B**
*Giải thích: Packet switch là thuật ngữ tổng quát cho bất kỳ thiết bị nào chuyển tiếp packet dựa trên header value. Link-layer switches (layer 2 devices) dùng MAC address; routers (layer 3 devices) dùng IP address.*

---

**Câu 69.** Trong forwarding table sau, packet với destination address bắt đầu bằng `11001000 00010111 00011000` sẽ được forward ra interface nào?

```
11001000 00010111 00010   → interface 0
11001000 00010111 00011000 → interface 1
11001000 00010111 00011   → interface 2
otherwise                  → interface 3
```

A. Interface 0
B. Interface 1
C. Interface 2
D. Interface 3

**Đáp án: B**
*Giải thích: Longest prefix matching: prefix `11001000 00010111 00011000` (24 bits, interface 1) dài hơn `11001000 00010111 00011` (21 bits, interface 2). Router chọn longest match → interface 1.*

---

**Câu 70.** Điều gì xảy ra với packet loss nếu switch fabric không đủ nhanh so với line speed (Rswitch < N × Rline)?

A. Packets được gửi lại tự động
B. Queuing xảy ra ở input ports — nếu hàng đợi đầy thì packet loss xảy ra tại đây
C. Routing processor xử lý overflow
D. Packets bị fragmentation để giảm kích thước

**Đáp án: B**
*Giải thích: Nếu switch fabric không đủ nhanh, packets phải queue tại input ports chờ đến lượt. Khi input port queue đầy → packet bị drop. Đây là một trong các nguyên nhân packet loss trong router.*

---

**Câu 71.** Xét một router với 4 input ports và 4 output ports. Switch fabric có tốc độ Rswitch = 4 × Rline. Trong trường hợp xấu nhất (worst case), có thể có queuing tại input ports không?

A. Không bao giờ — switch fabric đủ nhanh nên không bao giờ có queuing
B. Có thể có do HOL blocking, ngay cả khi switch fabric đủ nhanh
C. Chỉ khi tất cả 4 input ports đang nhận packet đồng thời
D. Chỉ khi routing processor bận

**Đáp án: B**
*Giải thích: Dù Rswitch = N × Rline (đủ nhanh về mặt lý thuyết), HOL blocking vẫn có thể gây queuing tại input ports. Một packet ở vị trí thứ hai bị chặn bởi packet đầu hàng đang chờ output port bận.*

---

**Câu 72.** Trong kiến trúc router, "line card" là gì?

A. Thẻ ghi nhận thông tin về routing protocols
B. Printed circuit board chứa một hoặc nhiều input/output ports, kết nối với switching fabric
C. Card quản lý routing processor
D. Bộ nhớ lưu trữ forwarding table

**Đáp án: B**
*Giải thích: Line card là printed circuit board chứa các ports (input và/hoặc output) và kết nối với switching fabric. Forwarding table shadow copy được lưu trên line card để thực hiện local lookup.*

---

**Câu 73.** ATM ABR service có thể bị mất cell không, và có cho phép reorder cell không?

A. Không thể mất, không reorder
B. Có thể mất cell, nhưng không reorder
C. Có thể mất và reorder
D. Không thể mất, có thể reorder

**Đáp án: B**
*Giải thích: ATM ABR: cells có thể bị mất (như Internet best-effort), nhưng không được reorder (khác Internet). ABR cũng đảm bảo MCR tối thiểu và cung cấp congestion feedback.*

---

**Câu 74.** Tại sao việc router duy trì "connection state" trong VC network được coi là một vấn đề quan trọng?

A. Vì nó tiêu tốn CPU của routing processor
B. Vì mỗi kết nối mới/kết thúc đều cần update, tạo overhead lớn ở backbone routers — có thể ở microsecond timescale
C. Vì connection state khó mã hóa để bảo mật
D. Vì connection state dễ bị tấn công bởi DDoS

**Đáp án: B**
*Giải thích: Trong VC network, mỗi khi có kết nối mới hoặc kết thúc, forwarding table phải được cập nhật ở tất cả routers trên path. Ở backbone router, điều này có thể xảy ra ở microsecond timescale — tạo burden lớn.*

---

**Câu 75.** Xét packet scheduler, WFQ (Weighted Fair Queuing) khác FCFS như thế nào?

A. WFQ drop packets ngẫu nhiên; FCFS không bao giờ drop
B. WFQ chia sẻ outgoing link công bằng (theo trọng số) giữa các end-to-end connections; FCFS đơn giản truyền packet theo thứ tự đến
C. WFQ ưu tiên tất cả packets như nhau; FCFS ưu tiên theo priority
D. WFQ chậm hơn nhưng đảm bảo delivery; FCFS nhanh hơn nhưng có thể mất packet

**Đáp án: B**
*Giải thích: FCFS (First-Come-First-Served) đơn giản: packet đến trước được truyền trước. WFQ chia sẻ bandwidth theo trọng số giữa các flows/connections khác nhau — quan trọng cho QoS guarantees.*

---

**Câu 76.** Khi nói network layer cung cấp "connection service" ở network layer vs transport layer, điểm nào sau đây đúng?

A. Cả hai đều được triển khai chỉ ở end systems
B. Network-layer connection service cần sự tham gia của routers trong network core; transport-layer connection chỉ cần hai end systems
C. Transport-layer connection cần sự tham gia của routers; network-layer không cần
D. Cả hai đều cần sự tham gia của routers trong network core

**Đáp án: B**
*Giải thích: Đây là sự khác biệt cơ bản: TCP connection setup chỉ ở end systems (routers không biết). VC setup ở network layer cần các routers trên path tham gia — mỗi router biết và duy trì trạng thái của VC.*

---

**Câu 77.** Điều nào sau đây là đặc điểm của datagram networks?

A. Mỗi packet của cùng một connection luôn đi theo cùng một path
B. Routers duy trì connection state cho mỗi active connection
C. Các packet của cùng một connection có thể đi theo các paths khác nhau và đến không đúng thứ tự
D. Cần handshake trước khi gửi data

**Đáp án: C**
*Giải thích: Trong datagram networks, không có VCs và forwarding tables có thể thay đổi. Do đó, các packets của cùng một connection có thể được routed qua các paths khác nhau và có thể đến không đúng thứ tự.*

---

**Câu 78.** Trong router architecture, "data plane" và "control plane" tương ứng với những gì?

A. Data plane = routing protocols; Control plane = packet forwarding
B. Data plane = forwarding (input ports, switching fabric, output ports — hardware); Control plane = routing (routing processor — software)
C. Data plane = physical layer; Control plane = network layer
D. Data plane và control plane đều nằm trong routing processor

**Đáp án: B**
*Giải thích: Data plane (forwarding plane) = input ports + switching fabric + output ports — implemented in hardware, nanosecond timescale. Control plane = routing processor — implemented in software, millisecond–second timescale.*

---

**Câu 79.** Tại sao Internet network-layer service model tối giản lại tốt cho việc kết nối các mạng khác nhau?

A. Vì nó đảm bảo QoS cho tất cả ứng dụng
B. Vì nó đặt ít yêu cầu lên network layer → dễ dàng kết nối các mạng với link technologies rất khác nhau (satellite, Ethernet, fiber, radio, các đặc tính loss và speed khác nhau)
C. Vì nó tương thích với tất cả routing protocols
D. Vì nó cung cấp in-order delivery miễn phí

**Đáp án: B**
*Giải thích: Minimal service model = minimal requirements → dễ kết nối diverse link technologies. Không cần lo về guaranteed bandwidth, jitter hay in-order delivery ở network layer — các tính năng đó được xử lý ở transport layer nếu cần.*

---

**Câu 80.** Điều nào sau đây MÔ TẢ ĐÚNG nhất về packet scheduler và AQM?

A. Packet scheduler và AQM đều quyết định packet nào bị drop khi buffer đầy
B. Packet scheduler chọn packet tiếp theo để truyền; AQM quyết định khi nào drop/mark packets (có thể trước khi buffer đầy)
C. Packet scheduler và AQM đều chỉ hoạt động ở input ports
D. AQM thay thế hoàn toàn packet scheduler trong modern routers

**Đáp án: B**
*Giải thích: Packet scheduler (WFQ, FCFS...) quyết định thứ tự truyền trong output queue. AQM (RED...) quyết định chính sách drop/mark — có thể chủ động drop trước khi buffer đầy để gửi congestion signal sớm cho sender.*

---

**Câu 81.** Nếu một mạng chỉ sử dụng best-effort service, transport layer cần đảm nhận những chức năng gì mà network layer không cung cấp?

A. Không cần gì thêm — best-effort là đủ
B. Reliable delivery, in-order delivery, flow control, congestion control — nếu ứng dụng cần (như TCP)
C. Chỉ cần congestion control
D. Chỉ cần in-order delivery

**Đáp án: B**
*Giải thích: Internet best-effort không đảm bảo gì. TCP ở transport layer bổ sung: reliable delivery (ACK, retransmission), in-order delivery, flow control, và congestion control. UDP không cung cấp những thứ này — ứng dụng tự xử lý nếu cần.*

---

**Câu 82.** Xét scenario: Rswitch = N × Rline, tất cả N input ports nhận packets, tất cả đều muốn ra cùng một output port. Điều gì xảy ra?

A. Không có queuing vì switch fabric đủ nhanh
B. Queuing xảy ra tại output port — N packets đến trong thời gian truyền 1 packet
C. Queuing xảy ra tại switching fabric
D. Packets được drop ngay tại input ports

**Đáp án: B**
*Giải thích: Dù switch fabric N lần nhanh hơn line speed, output port chỉ có thể truyền 1 packet mỗi time unit. Nếu N packets đến cùng lúc muốn ra một output port → N-1 packets phải queue → output port queuing xảy ra.*

---

**Câu 83.** Điều nào phân biệt "packet switch" từ góc độ layer mà nó hoạt động?

A. Packet switch chỉ là thuật ngữ khác của router
B. Link-layer switches base forwarding decision trên layer-2 fields (MAC address); routers base forwarding decision trên layer-3 fields (IP address)
C. Packet switches chỉ forward broadcast traffic
D. Routers chậm hơn link-layer switches

**Đáp án: B**
*Giải thích: Packet switch là generic term. Link-layer switches (layer 2 devices) dùng MAC address để forward. Routers (layer 3 devices) dùng IP address. Routers cũng cần implement layer-2 protocols vì cần dịch vụ của layer 2.*

---

**Câu 84.** Trong context của datagram networks, "longest prefix matching" quan trọng vì lý do gì?

A. Đảm bảo packets đến đúng thứ tự
B. Cho phép aggregation địa chỉ IP — một entry trong forwarding table có thể đại diện cho nhiều địa chỉ, giảm kích thước bảng
C. Tăng tốc độ switching fabric
D. Giảm packet loss

**Đáp án: B**
*Giải thích: Longest prefix matching cho phép hierarchical addressing — một prefix entry đại diện cho một dải địa chỉ. Điều này cho phép "route aggregation" (gộp nhiều routes), giảm kích thước forwarding table từ 4+ tỷ entries xuống còn manageable.*

---

**Câu 85.** Trong router architecture, tại sao input port cần lưu "shadow copy" của forwarding table thay vì query routing processor mỗi lần?

A. Routing processor thường bị lỗi
B. Routing processor hoạt động ở millisecond timescale; forwarding cần nanosecond timescale — không thể chờ routing processor mỗi packet
C. Routing processor không có đủ interfaces để connect với tất cả input ports
D. Shadow copy giúp giảm cost của router

**Đáp án: B**
*Giải thích: Routing processor (software, CPU) rất chậm so với yêu cầu forwarding. Với link 10 Gbps, chỉ có 51.2 ns per packet — không thể query routing processor mỗi lần. Shadow copy tại input port cho phép local lookup trong nanoseconds.*

---

**Câu 86.** Điều nào sau đây là đúng về network-layer services trong major architectures hiện nay?

A. Tất cả major architectures cung cấp cả connection và connectionless service
B. Major architectures cung cấp HOẶC connectionless service (datagram) HOẶC connection service (VC), không phải cả hai
C. Major architectures chỉ cung cấp connectionless service
D. Major architectures đều đang chuyển sang VC model

**Đáp án: B**
*Giải thích: Trong tất cả major computer network architectures hiện nay (Internet, ATM, frame relay...), network layer cung cấp hoặc host-to-host connectionless service hoặc connection service — không phải cả hai trong cùng một network.*

---

**Câu 87.** Xét một router đang xử lý packet với destination address: `11001000 00010111 00011000 10101010`. Với forwarding table từ câu 69, interface nào được chọn và tại sao?

A. Interface 0 — prefix 21-bit match
B. Interface 1 — prefix 24-bit là longest match (khớp hoàn toàn 24 bits đầu)
C. Interface 2 — prefix 21-bit match
D. Interface 3 — otherwise

**Đáp án: B**
*Giải thích: Kiểm tra: 24-bit prefix `11001000 00010111 00011000` khớp với địa chỉ (interface 1). 21-bit prefix `11001000 00010111 00011` cũng khớp (interface 2). Longest prefix = 24 bits → interface 1 được chọn.*

---

**Câu 88.** Trong context network layer, tại sao Internet lại đặt congestion control ở transport layer (TCP) thay vì network layer?

A. Transport layer nhanh hơn network layer
B. Phù hợp với triết lý Internet: network layer tối giản (best-effort), các tính năng phức tạp ở end systems — congestion control ở TCP chạy trong end systems
C. Network layer không đủ thông tin để làm congestion control
D. Congestion control ở transport layer được chuẩn hóa trước

**Đáp án: B**
*Giải thích: Internet's design philosophy: "smart edge, dumb core." Network layer (routers) giữ đơn giản tối đa. Congestion control, reliability, ordering đều được đẩy lên end systems (TCP). Điều này làm network dễ scale và dễ đổi mới.*

---

**Câu 89.** Một router đang chạy routing algorithm để cập nhật forwarding table. Đây là hoạt động của plane nào, và chạy ở timescale nào?

A. Data plane, nanosecond timescale
B. Control plane (routing processor, software), millisecond đến second timescale
C. Data plane (switching fabric), microsecond timescale
D. Control plane (hardware), nanosecond timescale

**Đáp án: B**
*Giải thích: Routing algorithm là control plane function — chạy trên routing processor (traditional CPU, software). Timescale: millisecond đến second. Không phải data plane (forwarding) vốn là hardware ở nanosecond.*

---

**Câu 90.** Điều nào sau đây là ví dụ về "connection setup" ở network layer?

A. TCP 3-way handshake
B. DNS lookup
C. ATM signaling để thiết lập virtual circuit trước khi truyền data
D. ARP để tìm MAC address

**Đáp án: C**
*Giải thích: Connection setup ở network layer = thiết lập VC. ATM dùng signaling protocols (như Q.2931) để thiết lập virtual circuit — các routers trên path bắt tay với nhau. TCP handshake là transport-layer, không phải network-layer.*

---

**Câu 91.** So sánh: ATM CBR, ATM ABR, và Internet best-effort — cái nào cung cấp congestion indication cho sender?

A. Chỉ ATM CBR
B. Chỉ Internet best-effort
C. Chỉ ATM ABR
D. Cả ba đều không

**Đáp án: C**
*Giải thích: Theo Table 4.1: Internet best-effort = None (no congestion indication); ATM CBR = congestion sẽ không xảy ra (guaranteed); ATM ABR = congestion indication provided (feedback mechanism).*

---

**Câu 92.** Điều nào sau đây MÔ TẢ SAI về switching via memory trong modern routers?

A. Lookup và storing packet thực hiện bởi processing trên input line cards
B. Hai packets không thể được forward đồng thời ngay cả khi đến các destination ports khác nhau (do shared system bus)
C. Modern routers switch via memory hoàn toàn giống early routers — CPU kiểm soát mọi thứ
D. Cisco Catalyst 8500 series sử dụng shared memory

**Đáp án: C**
*Giải thích: Modern routers switch via memory KHÁC early routers ở điểm quan trọng: lookup và packet storage được thực hiện bởi processing trên input line cards (không phải central CPU). Điều này phân tán xử lý, tăng hiệu suất.*

---

**Câu 93.** Tại sao HOL blocking là vấn đề nghiêm trọng trong input-queued switch?

A. Nó chỉ ảnh hưởng đến tốc độ forward của một vài packets
B. Nó giới hạn throughput của switch xuống chỉ ~58% capacity ngay cả khi switch fabric có thể nhanh hơn
C. Nó gây ra packet corruption
D. Nó chỉ xảy ra khi routing table bị lỗi

**Đáp án: B**
*Giải thích: Karol 1987 chỉ ra rằng do HOL blocking, input queue tăng không giới hạn (significant packet loss) khi arrival rate chỉ đạt 58% capacity. Đây là fundamental limitation của input-queued switch với FCFS scheduling.*

---

**Câu 94.** Trong context của datagram network, forwarding table khác routing table như thế nào?

A. Chúng hoàn toàn giống nhau
B. Forwarding table được tối ưu cho fast hardware lookup (nanosecond); routing table là data structure phức tạp hơn dùng bởi routing algorithm, thường được tổng hợp để tạo ra forwarding table
C. Routing table chỉ dùng ở backbone routers; forwarding table ở edge routers
D. Forwarding table dùng cho IPv6; routing table dùng cho IPv4

**Đáp án: B**
*Giải thích: Routing table dùng bởi routing processor để chạy routing algorithm và lưu thông tin phức tạp hơn. Forwarding table là bảng được tối ưu cho hardware lookup — thường là subset/compressed version của routing table, được routing processor tính toán và push xuống line cards.*

---

**Câu 95.** Dựa trên triết lý thiết kế của Internet, điều gì làm cho việc deploy ứng dụng mới (như Web) trở nên nhanh chóng?

A. ISPs cung cấp dedicated bandwidth cho mỗi ứng dụng mới
B. Chỉ cần attach một server mới và định nghĩa application-layer protocol mới — không cần thay đổi network core (routers)
C. IP protocol được thiết kế để tự động hỗ trợ mọi ứng dụng mới
D. Routers có thể được cập nhật firmware để hỗ trợ ứng dụng mới

**Đáp án: B**
*Giải thích: Vì Internet network layer đơn giản (best-effort, không application-specific), thêm dịch vụ mới (Web, email, streaming...) chỉ cần attach server mới và tạo application-layer protocol. Không cần thay đổi bất kỳ router nào trong network core.*

---

**Câu 96.** Điều nào sau đây là ví dụ về "match plus action" trong network devices NGOÀI routers?

A. Router lookup IP prefix → forward to output port
B. Firewall: match incoming packet header với criteria → drop packet; NAT: match port number → rewrite port; Link-layer switch: match MAC address → forward
C. DNS server: match domain name → IP address
D. Application server: match URL path → serve file

**Đáp án: B**
*Giải thích: "Match plus action" xuất hiện rộng rãi: Firewalls (match header criteria, action = drop/allow), NAT (match port number, action = rewrite), link-layer switches (match MAC address, action = forward/flood). Đây là abstraction tổng quát và mạnh mẽ.*

---

**Câu 97.** Khi routing algorithm centralized (chạy trên central site) vs decentralized (chạy phân tán trong routers), điểm chung là gì?

A. Cả hai đều không cần forwarding tables
B. Dù centralized hay decentralized, router đều nhận routing protocol messages để configure forwarding table của mình
C. Centralized routing không cần routers nhận messages
D. Decentralized routing không cần forwarding tables

**Đáp án: B**
*Giải thích: Dù routing algorithm chạy ở đâu (central server hay distributed trong routers), kết quả cuối cùng vẫn là: routers nhận routing protocol messages → configure forwarding tables. Điểm khác nhau là nơi tính toán diễn ra.*

---

**Câu 98.** Hãy giải thích tại sao packet trong datagram network có thể đến đích không đúng thứ tự.

A. Vì datagram network không hỗ trợ sequencing
B. Vì forwarding tables có thể thay đổi trong quá trình transmission — các packets liên tiếp có thể được routed qua các paths khác nhau với delays khác nhau
C. Vì routers trong datagram network cố ý shuffle packets
D. Vì best-effort service yêu cầu random ordering

**Đáp án: B**
*Giải thích: Trong datagram network, forwarding tables được cập nhật bởi routing algorithms (mỗi 1–5 phút). Các packets liên tiếp của cùng một connection có thể được routed qua paths khác nhau (nếu forwarding table thay đổi hoặc có load balancing) → đến theo thứ tự khác nhau.*

---

**Câu 99.** Điều nào sau đây ĐÚNG về ATM network service models?

A. ATM chỉ cung cấp một loại service model duy nhất
B. ATM cung cấp multiple service models — các connections khác nhau có thể được cung cấp các classes of service khác nhau trong cùng một mạng
C. ATM không hỗ trợ variable bit rate traffic
D. ATM CBR và ABR đều đảm bảo zero packet loss

**Đáp án: B**
*Giải thích: ATM đặc biệt ở chỗ cung cấp multiple service models (CBR, ABR, và khác) — các kết nối khác nhau trong cùng một ATM network có thể nhận các mức đảm bảo dịch vụ khác nhau. Điều này trái với Internet chỉ có best-effort.*

---

**Câu 100.** Tóm tắt: ba chức năng chính của network layer trong các kiến trúc hỗ trợ connection là gì?

A. Encapsulation, forwarding, decapsulation
B. Forwarding, routing, connection setup
C. Addressing, routing, error detection
D. Multiplexing, forwarding, demultiplexing

**Đáp án: B**
*Giải thích: Trong các kiến trúc như ATM hỗ trợ connection ở network layer, có ba chức năng: (1) Forwarding — chuyển packet trong router; (2) Routing — xác định path qua mạng; (3) Connection setup — thiết lập trạng thái trước khi gửi data.*

