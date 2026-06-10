# Chương 4: Network Layer — Bộ câu hỏi ôn tập

---

## Phần 4.1 — Introduction to the Network Layer

**Câu 1.** Chức năng chính của network layer là gì?

A. Cung cấp process-to-process communication giữa hai ứng dụng
B. Cung cấp host-to-host communication service
C. Truyền bit vật lý qua đường truyền
D. Quản lý địa chỉ MAC giữa các thiết bị

**Đáp án: B**
*Giải thích: Network layer có nhiệm vụ di chuyển packet từ sending host đến receiving host — đây là dịch vụ host-to-host. Transport layer mới cung cấp process-to-process communication.*

---

**Câu 2.** Điểm khác biệt quan trọng giữa transport layer và network layer là:

A. Network layer chỉ tồn tại ở end systems, transport layer tồn tại ở cả routers
B. Transport layer chỉ tồn tại ở end systems, network layer tồn tại ở cả end systems lẫn routers
C. Cả hai đều chỉ tồn tại ở end systems
D. Cả hai đều tồn tại ở mọi thiết bị trong mạng

**Đáp án: B**
*Giải thích: Mỗi host và router trong mạng đều có một phần của network layer. Transport layer và application layer chỉ chạy ở end systems (và các thiết bị edge), không chạy trong routers (trừ mục đích điều khiển).*

---

**Câu 3.** Forwarding trong network layer được định nghĩa là:

A. Quá trình xác định đường đi toàn mạng từ nguồn tới đích
B. Quá trình chuyển packet từ input link sang output link phù hợp trong một router đơn lẻ
C. Quá trình thiết lập kết nối giữa hai end systems
D. Quá trình mã hóa dữ liệu trước khi truyền qua mạng

**Đáp án: B**
*Giải thích: Forwarding là hành động cục bộ tại một router — nhìn vào header của packet và chuyển nó ra đúng output interface. Đây là chức năng data plane.*

---

**Câu 4.** Routing trong network layer được định nghĩa là:

A. Chuyển packet từ input port sang output port trong router
B. Xác định đường đi end-to-end mà packet sẽ đi từ source tới destination qua toàn mạng
C. Lưu trữ và truyền lại packet bị mất
D. Phân mảnh packet khi kích thước quá lớn

**Đáp án: B**
*Giải thích: Routing là quá trình toàn mạng (network-wide) — các routing algorithm tính toán đường đi tối ưu từ source đến destination. Đây là chức năng control plane.*

---

**Câu 5.** Dùng phép ẩn dụ lái xe, forwarding và routing tương ứng với điều gì?

A. Forwarding = lập kế hoạch chuyến đi; Routing = đi qua một ngã tư đơn lẻ
B. Forwarding = đi qua một ngã tư/interchange đơn lẻ; Routing = lập kế hoạch toàn bộ chuyến đi
C. Cả hai đều tương ứng với việc lập kế hoạch chuyến đi
D. Cả hai đều tương ứng với việc đi qua một ngã tư

**Đáp án: B**
*Giải thích: Forwarding giống như lái xe qua một interchange — quyết định ra ngả nào. Routing giống như lập kế hoạch cả chuyến đi từ Pennsylvania đến Florida trước khi khởi hành.*

---

**Câu 6.** Forwarding table trong router được sử dụng như thế nào?

A. Lưu trữ toàn bộ lịch sử packet đã đi qua router
B. Router tra cứu giá trị trong header packet để xác định output link interface
C. Lưu thông tin về trạng thái congestion của mạng
D. Quản lý hàng đợi packet tại các cổng đầu ra

**Đáp án: B**
*Giải thích: Router đọc một trường trong header của packet (ví dụ địa chỉ đích), dùng giá trị đó để index vào forwarding table, và forwarding table cho biết phải gửi packet ra interface nào.*

---

**Câu 7.** Ai/cái gì quyết định các giá trị được nạp vào forwarding table của router?

A. Network administrator nhập tay trực tiếp
B. Transport layer của router
C. Routing algorithm
D. End system gửi packet

**Đáp án: C**
*Giải thích: Routing algorithm — dù là centralized hay decentralized — tính toán và cập nhật các giá trị trong forwarding table. Router nhận routing protocol messages để cấu hình bảng này.*

---

**Câu 8.** Trong một mạng giả định mà forwarding tables được cấu hình hoàn toàn thủ công bởi con người, điều gì xảy ra?

A. Mạng hoạt động hiệu quả hơn vì có sự kiểm soát con người
B. Không cần routing protocols, nhưng dễ xảy ra lỗi và phản ứng chậm với thay đổi topology
C. Routing protocols vẫn cần thiết để đồng bộ thông tin
D. Forwarding table sẽ không cần thiết nữa

**Đáp án: B**
*Giải thích: Về mặt kỹ thuật có thể không cần routing protocols nếu con người cấu hình tay, nhưng điều này rất dễ lỗi và phản ứng rất chậm khi topology thay đổi.*

---

**Câu 9.** "Connection setup" là chức năng network-layer thứ ba xuất hiện trong loại mạng nào?

A. Datagram networks như Internet
B. Các kiến trúc như ATM, frame relay, MPLS
C. Chỉ trong wireless networks
D. Tất cả các mạng IP

**Đáp án: B**
*Giải thích: Một số kiến trúc mạng như ATM, frame relay, và MPLS yêu cầu các router dọc đường đi phải bắt tay với nhau (handshake) để thiết lập trạng thái trước khi data packets được gửi.*

---

**Câu 10.** "Best-effort service" của Internet có nghĩa là gì?

A. Đảm bảo delivery với delay tối thiểu
B. Không đảm bảo timing, thứ tự packet, hay delivery cuối cùng của packet
C. Đảm bảo packet được deliver theo đúng thứ tự gửi
D. Cung cấp bandwidth tối thiểu cho mỗi flow

**Đáp án: B**
*Giải thích: Best-effort service của Internet không đảm bảo: timing giữa các packet, thứ tự nhận packet, hay việc packet có đến đích hay không. Một mạng không deliver packet nào cũng thỏa mãn định nghĩa này.*

---

**Câu 11.** Dịch vụ network layer nào đảm bảo packet đến đích trong một khoảng thời gian xác định?

A. Best-effort service
B. Guaranteed delivery
C. Guaranteed delivery with bounded delay
D. In-order packet delivery

**Đáp án: C**
*Giải thích: "Guaranteed delivery with bounded delay" không chỉ đảm bảo packet đến nơi mà còn đảm bảo đến trong một khoảng thời gian cụ thể (ví dụ, trong vòng 100ms).*

---

**Câu 12.** "Guaranteed maximum jitter" trong network service model có nghĩa là gì?

A. Đảm bảo không có packet nào bị mất
B. Đảm bảo khoảng cách thời gian giữa việc gửi hai packet liên tiếp bằng (hoặc gần bằng) khoảng cách thời gian giữa việc nhận chúng
C. Đảm bảo bandwidth tối thiểu cho mỗi kết nối
D. Đảm bảo packet đến theo đúng thứ tự

**Đáp án: B**
*Giải thích: Jitter là sự biến động về delay. "Guaranteed maximum jitter" đảm bảo khoảng cách thời gian giữa hai packet liên tiếp không thay đổi quá một giá trị xác định từ sender đến receiver.*

---

**Câu 13.** ATM CBR (Constant Bit Rate) service được thiết kế chủ yếu cho loại traffic nào?

A. File transfer và email
B. Web browsing
C. Real-time audio và video với bit rate cố định
D. Database transactions

**Đáp án: C**
*Giải thích: CBR được chuẩn hóa đầu tiên do sự quan tâm của các công ty điện thoại — phù hợp cho real-time, constant bit rate audio và video traffic. Mục tiêu là tạo ra một "virtual pipe" cố định.*

---

**Câu 14.** ATM ABR (Available Bit Rate) service khác Internet best-effort ở điểm nào?

A. ABR đảm bảo không mất packet
B. ABR đảm bảo Minimum Cell Rate (MCR) và cung cấp congestion feedback cho sender
C. ABR đảm bảo packet đến đúng thứ tự và không có jitter
D. ABR không cho phép reordering packet

**Đáp án: B**
*Giải thích: ABR đảm bảo một MCR tối thiểu, cho phép gửi cao hơn nếu mạng có đủ tài nguyên, và cung cấp congestion notification (feedback) cho sender. Cells có thể bị mất nhưng không thể bị reorder.*

---

**Câu 15.** So sánh Internet best-effort với ATM CBR: điểm khác biệt về "Ordering" là gì?

A. Cả hai đều đảm bảo in-order delivery
B. Best-effort: bất kỳ thứ tự nào có thể xảy ra; CBR: đảm bảo in-order
C. Best-effort: in-order; CBR: không đảm bảo thứ tự
D. Cả hai đều không đảm bảo thứ tự

**Đáp án: B**
*Giải thích: Internet best-effort không đảm bảo thứ tự ("any order possible"), trong khi ATM CBR đảm bảo các cell đến theo đúng thứ tự đã gửi ("in order").*

---

## Phần 4.2 — Virtual Circuit and Datagram Networks

**Câu 16.** Điểm tương đồng giữa network-layer connection service và transport-layer connection-oriented service là gì?

A. Cả hai đều được triển khai trong routers lõi mạng
B. Cả hai đều bắt đầu bằng handshaking giữa source và destination
C. Cả hai đều chỉ chạy trên end systems
D. Cả hai đều không cần thiết lập trạng thái

**Đáp án: B**
*Giải thích: Cả network-layer connection service và transport-layer connection-oriented service đều bắt đầu bằng handshaking. Tuy nhiên, cách triển khai và phạm vi có sự khác biệt quan trọng.*

---

**Câu 17.** Điểm khác biệt quan trọng nhất giữa network-layer connection service và transport-layer connection service là:

A. Transport layer dùng TCP, network layer dùng UDP
B. Network-layer connection service được triển khai trong cả routers ở network core, không chỉ ở end systems
C. Network layer nhanh hơn transport layer
D. Transport layer hỗ trợ nhiều kết nối đồng thời hơn network layer

**Đáp án: B**
*Giải thích: Transport-layer connection (như TCP 3-way handshake) chỉ liên quan đến hai end systems. Network-layer connection (VC) liên quan đến cả các routers trong network core — mỗi router phải thiết lập và duy trì trạng thái kết nối.*

---

**Câu 18.** Virtual-circuit (VC) network và datagram network khác nhau như thế nào về việc cung cấp service?

A. VC network cung cấp cả connection và connectionless service; datagram network chỉ cung cấp connectionless
B. VC network chỉ cung cấp connection service; datagram network chỉ cung cấp connectionless service
C. Cả hai đều cung cấp connection service nhưng theo cách khác nhau
D. Datagram network cung cấp connection service; VC network cung cấp connectionless service

**Đáp án: B**
*Giải thích: Trong các kiến trúc mạng lớn hiện nay, network layer cung cấp hoặc connectionless (datagram) hoặc connection service (VC), không phải cả hai. Internet là datagram network; ATM, frame relay là VC networks.*

---

**Câu 19.** Một Virtual Circuit (VC) bao gồm những thành phần nào?

A. Chỉ một địa chỉ IP nguồn và đích
B. Một path giữa source và destination, các VC number trên mỗi link, và entries trong forwarding table của mỗi router trên path
C. Chỉ forwarding table entries trong các routers
D. Địa chỉ MAC của các thiết bị dọc đường đi

**Đáp án: B**
*Giải thích: VC gồm 3 thành phần: (1) path (loạt links và routers), (2) VC numbers — một số cho mỗi link trên path, và (3) entries trong forwarding table của mỗi router trên path.*

---

**Câu 20.** Tại sao VC number lại thay đổi trên mỗi link thay vì giữ nguyên một số duy nhất?

A. Để tăng bảo mật cho kết nối
B. Để giảm độ dài VC field trong header và đơn giản hóa VC setup — mỗi link có thể chọn VC number độc lập
C. Vì các router không thể lưu trữ VC number dài
D. Để tương thích với nhiều loại link layer khác nhau

**Đáp án: B**
*Giải thích: Hai lý do: (1) Giảm độ dài VC field trong packet header. (2) Quan trọng hơn, mỗi link chọn VC number độc lập, tránh phải trao đổi nhiều message để đồng ý về một số duy nhất không trùng với các VC khác.*

---

**Câu 21.** Forwarding table của một router trong VC network có những cột nào?

A. Destination IP address và output interface
B. Incoming interface, incoming VC#, outgoing interface, outgoing VC#
C. Source IP, destination IP, và next-hop router
D. VC number và bandwidth allocation

**Đáp án: B**
*Giải thích: Forwarding table trong VC network ánh xạ (incoming interface, incoming VC#) → (outgoing interface, outgoing VC#). Router thay thế VC number khi chuyển tiếp packet.*

---

**Câu 22.** Ba giai đoạn của một Virtual Circuit là:

A. Connection request, data transfer, acknowledgment
B. VC setup, data transfer, VC teardown
C. Handshake, routing, forwarding
D. Initialization, transmission, termination confirmation

**Đáp án: B**
*Giải thích: VC có 3 giai đoạn rõ ràng: (1) VC setup — thiết lập path và forwarding entries; (2) Data transfer — gửi packets theo VC đã thiết lập; (3) VC teardown — xóa entries và giải phóng tài nguyên.*

---

**Câu 23.** Trong giai đoạn VC setup, điều gì xảy ra ở các routers dọc đường?

A. Các router chỉ lưu địa chỉ IP đích, không cần thêm thông tin
B. Mỗi router thêm một entry vào forwarding table và có thể reserve bandwidth cho VC
C. Các router ghi nhớ toàn bộ nội dung packet sẽ được gửi
D. Các router chỉ cập nhật routing table, không phải forwarding table

**Đáp án: B**
*Giải thích: Trong VC setup, network layer xác định path, gán VC numbers cho từng link, và thêm entry vào forwarding table của mỗi router trên path. Network layer cũng có thể reserve tài nguyên (như bandwidth).*

---

**Câu 24.** "Signaling messages" và "signaling protocols" trong VC networks dùng để làm gì?

A. Gửi data payload giữa các end systems
B. Truyền thông tin về congestion cho sender
C. Khởi tạo hoặc kết thúc VC và thiết lập connection state trong router tables
D. Đồng bộ routing tables giữa các routers

**Đáp án: C**
*Giải thích: Signaling messages là các thông điệp mà end systems gửi vào mạng để khởi tạo/kết thúc VC, và các messages được truyền giữa routers để thiết lập/xóa connection state. Signaling protocols định nghĩa cách trao đổi chúng.*

---

**Câu 25.** VC setup khác TCP connection setup ở điểm gì?

A. TCP setup liên quan đến routers; VC setup chỉ liên quan đến end systems
B. VC setup liên quan đến các routers dọc đường (mỗi router biết và duy trì trạng thái VC); TCP setup chỉ liên quan đến hai end systems
C. Cả hai đều có cùng phạm vi, chỉ khác về giao thức sử dụng
D. VC setup nhanh hơn TCP setup vì không cần handshake

**Đáp án: B**
*Giải thích: TCP 3-way handshake chỉ liên quan đến hai end systems — các routers trong mạng hoàn toàn không biết về nó. VC setup ngược lại, yêu cầu mỗi router trên path phải tham gia và duy trì trạng thái.*

---

**Câu 26.** Trong datagram network, router sử dụng gì để quyết định forward packet ra output link nào?

A. VC number trong header của packet
B. Địa chỉ IP nguồn của packet
C. Destination address của packet
D. Port number của transport layer

**Đáp án: C**
*Giải thích: Trong datagram network, không có VC. Mỗi packet mang địa chỉ đích, và mỗi router dùng destination address để tra cứu forwarding table và xác định output interface.*

---

**Câu 27.** Tại sao không thể có một forwarding table entry cho mỗi địa chỉ 32-bit trong datagram network?

A. Vì router không đủ năng lượng xử lý
B. Vì có hơn 4 tỷ địa chỉ có thể — quá lớn để lưu trữ thực tế
C. Vì địa chỉ IP không được phép trùng lặp
D. Vì các routers chỉ xử lý địa chỉ IPv6

**Đáp án: B**
*Giải thích: Địa chỉ IPv4 là 32-bit, nghĩa là hơn 4 tỷ địa chỉ có thể. Lưu một entry cho mỗi địa chỉ là hoàn toàn không khả thi (brute-force approach).*

---

**Câu 28.** "Longest prefix matching rule" trong forwarding table của datagram network có nghĩa là gì?

A. Router chọn entry có prefix ngắn nhất khớp với địa chỉ đích
B. Router chọn entry có prefix dài nhất khớp với địa chỉ đích để forward packet
C. Router chọn entry đầu tiên trong bảng khớp với địa chỉ đích
D. Router broadcast packet đến tất cả output ports khi có nhiều matches

**Đáp án: B**
*Giải thích: Khi địa chỉ đích khớp với nhiều entries, router dùng longest prefix matching — chọn entry có số bit prefix dài nhất khớp. Điều này cho phép phân cấp địa chỉ và routing hiệu quả.*

---

**Câu 29.** Forwarding table trong datagram network thay đổi với tần suất như thế nào so với VC network?

A. Datagram network thay đổi nhanh hơn (microsecond) vì mỗi packet là độc lập
B. Datagram network thay đổi chậm hơn (vài phút); VC network thay đổi mỗi khi có kết nối mới/kết thúc (microsecond)
C. Cả hai thay đổi với tần suất như nhau
D. VC network không bao giờ thay đổi forwarding table

**Đáp án: B**
*Giải thích: Forwarding tables trong datagram network được cập nhật bởi routing algorithms, thường mỗi 1–5 phút. VC network thay đổi mỗi khi có kết nối mới thiết lập hoặc kết thúc — có thể ở microsecond timescale.*

---

**Câu 30.** Nguồn gốc của VC networks xuất phát từ đâu và datagram networks xuất phát từ đâu?

A. VC từ Internet; datagram từ telephony
B. VC từ telephony (điện thoại); datagram từ nhu cầu kết nối computers
C. Cả hai đều xuất phát từ quân sự
D. VC từ satellite communications; datagram từ cable networks

**Đáp án: B**
*Giải thích: VC networks có nguồn gốc từ telephony — điện thoại cần real circuits và per-call state. Internet datagram network phát triển từ nhu cầu kết nối computers, với end systems thông minh hơn cho phép network layer đơn giản hóa tối đa.*

---

**Câu 31.** Triết lý thiết kế của Internet datagram network là gì (so với VC telephone network)?

A. Đặt tất cả tính năng phức tạp vào trong network core
B. Tối giản hóa network layer, đặt các chức năng phức tạp (reliable delivery, ordering, congestion control) ở end systems
C. Tối đa hóa các đảm bảo dịch vụ của network layer
D. Sử dụng dedicated connections cho mỗi ứng dụng

**Đáp án: B**
*Giải thích: Internet "inverts" mô hình điện thoại — network layer đơn giản nhất có thể (best-effort), còn các tính năng như in-order delivery, reliable transfer, congestion control được triển khai ở higher layers trong end systems.*

---

**Câu 32.** Lợi ích của việc Internet có network-layer service model tối giản là gì?

A. Đảm bảo QoS tốt hơn cho tất cả ứng dụng
B. Dễ dàng kết nối nhiều loại link-layer technologies khác nhau (satellite, Ethernet, fiber, radio)
C. Giảm số lượng routers cần thiết trong mạng
D. Tăng tốc độ truyền dữ liệu tối đa

**Đáp án: B**
*Giải thích: Vì Internet không áp đặt yêu cầu gì lên network layer, nó dễ dàng liên kết các mạng với link-layer technologies rất khác nhau (satellite, Ethernet, fiber, radio) với đặc tính transmission rates và loss characteristics khác nhau.*

---

**Câu 33.** Tại sao việc thêm dịch vụ mới vào Internet lại dễ dàng hơn so với telephone network truyền thống?

A. Vì Internet có băng thông lớn hơn
B. Vì chỉ cần attach một host mới và định nghĩa một application-layer protocol mới, không cần thay đổi network core
C. Vì Internet sử dụng VC nên dễ cấu hình hơn
D. Vì các ISP luôn hỗ trợ mọi loại dịch vụ mới

**Đáp án: B**
*Giải thích: Trong Internet, các dịch vụ như email, Web, DNS đều được triển khai ở hosts (servers) ở network edge. Thêm dịch vụ mới chỉ cần attach một host và định nghĩa application-layer protocol mới — không cần thay đổi gì trong network core.*

---

## Phần 4.3 — What's Inside a Router?

**Câu 34.** Bốn thành phần chính của một router là gì?

A. CPU, RAM, ROM, và network interface
B. Input ports, switching fabric, output ports, và routing processor
C. Forwarding table, routing table, ARP cache, và packet buffer
D. Physical layer, data link layer, network layer, và transport layer

**Đáp án: B**
*Giải thích: Bốn thành phần chính của generic router architecture: (1) Input ports, (2) Switching fabric, (3) Output ports, (4) Routing processor.*

---

**Câu 35.** Input port của router thực hiện những chức năng nào?

A. Chỉ thực hiện chức năng physical layer
B. Kết thúc incoming physical link, xử lý link-layer, và thực hiện lookup để xác định output port
C. Chỉ thực hiện lookup trong forwarding table
D. Chỉ buffer packets chờ switching fabric

**Đáp án: B**
*Giải thích: Input port thực hiện: (1) physical layer termination, (2) link-layer functions, (3) lookup function — tra cứu forwarding table để xác định output port. Đây là chức năng quan trọng nhất.*

---

**Câu 36.** Switching fabric trong router có chức năng gì?

A. Thực hiện routing algorithm
B. Kết nối input ports với output ports của router
C. Quản lý forwarding table
D. Xử lý các routing protocol messages

**Đáp án: B**
*Giải thích: Switching fabric là "mạng bên trong router" — nó kết nối các input ports với các output ports, cho phép packets được chuyển từ input port sang output port phù hợp.*

---

**Câu 37.** Output port của router thực hiện chức năng gì?

A. Thực hiện routing algorithm và cập nhật forwarding table
B. Lưu trữ packets từ switching fabric và truyền chúng ra outgoing link
C. Nhận packets từ network và phân loại chúng
D. Quản lý kết nối với các routers láng giềng

**Đáp án: B**
*Giải thích: Output port lưu trữ packets nhận được từ switching fabric và truyền chúng ra outgoing link, thực hiện các chức năng link-layer và physical-layer cần thiết.*

---

**Câu 38.** Routing processor trong router đảm nhiệm những gì?

A. Chuyển tiếp packets từ input đến output ports
B. Thực thi routing protocols, duy trì routing tables, tính toán forwarding table, và thực hiện network management
C. Chỉ thực hiện switching giữa các ports
D. Quản lý buffer tại input và output ports

**Đáp án: B**
*Giải thích: Routing processor (thường là traditional CPU) thực thi routing protocols, duy trì routing tables và link state information, tính toán forwarding table, và thực hiện network management functions.*

---

**Câu 39.** Tại sao forwarding plane phải được triển khai bằng hardware thay vì software?

A. Vì hardware rẻ hơn software
B. Vì tốc độ yêu cầu quá cao — ví dụ với link 10 Gbps và datagram 64 byte, chỉ có 51.2 ns để xử lý mỗi datagram
C. Vì software không thể đọc IP headers
D. Vì routing protocols yêu cầu hardware acceleration

**Đáp án: B**
*Giải thích: Với link 10 Gbps và datagram 64-byte, input port chỉ có 51.2 ns để xử lý trước khi datagram tiếp theo đến. Tốc độ này đòi hỏi hardware implementation — software quá chậm.*

---

**Câu 40.** Sự khác biệt về timescale giữa forwarding plane và control plane là gì?

A. Cả hai đều hoạt động ở nanosecond timescale
B. Forwarding plane: nanosecond; Control plane: millisecond đến second
C. Forwarding plane: millisecond; Control plane: nanosecond
D. Cả hai đều hoạt động ở millisecond timescale

**Đáp án: B**
*Giải thích: Forwarding plane (hardware) hoạt động ở nanosecond timescale. Control plane (routing protocols, management — chạy trên routing processor/CPU) hoạt động ở millisecond hoặc second timescale.*

---

**Câu 41.** Tại sao forwarding table thường được lưu một "shadow copy" tại mỗi input port?

A. Để backup khi routing processor hỏng
B. Để forwarding decisions có thể được thực hiện locally tại mỗi input port mà không cần invoke centralized routing processor cho mỗi packet
C. Để tăng dung lượng lưu trữ của router
D. Để đồng bộ hóa giữa các routers láng giềng

**Đáp án: B**
*Giải thích: Với shadow copy tại mỗi input port, lookup có thể được thực hiện locally — tránh được bottleneck của việc gọi centralized routing processor cho mỗi packet. Forwarding table gốc được sao chép từ routing processor qua một bus riêng.*

---

**Câu 42.** TCAM (Ternary Content Addressable Memory) được sử dụng trong router để làm gì?

A. Lưu trữ routing protocols
B. Thực hiện IP address lookup trong forwarding table với thời gian constant
C. Quản lý buffer tại output ports
D. Tăng tốc switching fabric

**Đáp án: B**
*Giải thích: TCAM nhận một 32-bit IP address và trả về nội dung của forwarding table entry tương ứng trong essentially constant time — rất hiệu quả cho lookup operation.*

---

**Câu 43.** "Match plus action" abstraction trong input port processing là gì và có xuất hiện ở đâu ngoài routers?

A. Chỉ xuất hiện trong routers, không có ở thiết bị khác
B. Match = lookup địa chỉ IP, action = gửi vào switching fabric; cũng xuất hiện trong firewalls, NAT, link-layer switches
C. Chỉ xuất hiện trong link-layer switches
D. Match = kiểm tra port number, action = truyền qua physical layer

**Đáp án: B**
*Giải thích: "Match plus action" là abstraction tổng quát: routers (match IP, forward), link-layer switches (match MAC address), firewalls (match header criteria, drop/allow), NAT (match port number, rewrite). Đây là abstraction phổ biến và mạnh mẽ.*

---

**Câu 44.** Switching via memory (trong routers thế hệ đầu) hoạt động như thế nào?

A. Packet được chuyển trực tiếp từ input port đến output port qua hardware bus
B. CPU kiểm soát việc copy packet từ input port vào processor memory, tra cứu output port, rồi copy sang output port buffers
C. Một crossbar switch điều hướng packet đến output port
D. Packet được broadcast đến tất cả output ports rồi lọc

**Đáp án: B**
*Giải thích: Trong early memory-based switching: packet đến input port → interrupt CPU → CPU copy vào processor memory → tra cứu forwarding table → copy đến output port buffer. Throughput bị giới hạn bởi memory bandwidth (< B/2).*

---

**Câu 45.** Hạn chế của switching via memory là gì?

A. Không thể xử lý nhiều loại packet
B. Throughput bị giới hạn bởi memory bandwidth — chỉ một memory read/write trên shared bus tại một thời điểm, nên tối đa B/2 packets/second
C. Không hỗ trợ nhiều output ports
D. Yêu cầu quá nhiều năng lượng

**Đáp án: B**
*Giải thích: Với memory bandwidth B packets/second, overall forwarding throughput phải nhỏ hơn B/2 (vì mỗi packet cần cả read và write). Hai packets không thể được forward đồng thời dù đến các destination ports khác nhau.*

---

**Câu 46.** Switching via a bus hoạt động như thế nào?

A. CPU copy packet từ input port sang output port qua processor memory
B. Input port gắn label chỉ output port, truyền packet lên shared bus; tất cả output ports nhận nhưng chỉ port có label đúng mới giữ packet
C. Một crossbar switch điều hướng packet trực tiếp
D. Packets được chia nhỏ và truyền song song qua nhiều buses

**Đáp án: B**
*Giải thích: Input port prepend một internal label (chỉ định output port đích) vào packet, truyền lên shared bus. Tất cả output ports nhận packet, nhưng chỉ port match label mới giữ lại. Label được xóa ở output port.*

---

**Câu 47.** Hạn chế chính của switching via a bus là gì?

A. Không thể xử lý các packet có kích thước khác nhau
B. Switching speed bị giới hạn bởi bus speed — chỉ một packet có thể cross bus tại một thời điểm
C. Không hỗ trợ multicast
D. Yêu cầu nhiều CPU cores

**Đáp án: B**
*Giải thích: Vì tất cả packets phải cross single shared bus, switching speed bị giới hạn bởi bus speed. Đây là bottleneck cho các routers cần throughput cao, nhưng đủ dùng cho small LAN/enterprise networks.*

---

**Câu 48.** Crossbar switch (switching via interconnection network) khác switching via bus như thế nào?

A. Crossbar switch chậm hơn nhưng đơn giản hơn
B. Crossbar switch có thể forward nhiều packets song song (miễn là output ports khác nhau), vượt qua giới hạn bandwidth của single bus
C. Crossbar switch yêu cầu nhiều memory hơn
D. Crossbar switch không hỗ trợ large-scale networks

**Đáp án: B**
*Giải thích: Crossbar switch gồm 2N buses kết nối N input với N output ports. Nhiều packets có thể được forward song song — ví dụ A→Y và B→X đồng thời — miễn là không cùng output port. Đây là lợi thế lớn so với single shared bus.*

---

**Câu 49.** Trong crossbar switch, khi nào một packet phải chờ tại input port?

A. Khi forwarding table chưa được cập nhật
B. Khi hai packets từ hai input ports khác nhau cùng muốn đến cùng một output port
C. Khi packet quá lớn để fit vào bus
D. Khi routing processor đang bận

**Đáp án: B**
*Giải thích: Trong crossbar, nếu hai packets từ hai input ports khác nhau đều muốn đến cùng một output port, một trong hai phải chờ — chỉ một packet có thể được gửi qua một bus bất kỳ tại một thời điểm.*

---

**Câu 50.** HOL (Head-of-the-Line) blocking là gì?

A. Router bị tắc nghẽn vì quá nhiều routing protocol messages
B. Một packet trong input queue phải chờ chuyển qua fabric (dù output port của nó rảnh) vì bị chặn bởi packet ở đầu hàng đợi đang contend output port khác
C. Output port buffer đầy và không nhận thêm packets
D. Routing processor không thể tính toán forwarding table kịp thời

**Đáp án: B**
*Giải thích: HOL blocking: một packet ở vị trí thứ hai trong input queue không thể được chuyển đến output port của nó (dù output port rảnh!) vì packet đứng đầu hàng đợi đang bị blocked. Nghiên cứu cho thấy HOL blocking giới hạn throughput ở ~58% capacity.*

---

**Câu 51.** HOL blocking gây ra hậu quả gì về mặt performance?

A. Tăng delay nhưng không ảnh hưởng throughput
B. Input queue tăng đến unbounded length — packet loss đáng kể xảy ra khi packet arrival rate đạt ~58% capacity
C. Chỉ ảnh hưởng đến high-priority packets
D. Không ảnh hưởng nếu switch fabric đủ nhanh

**Đáp án: B**
*Giải thích: Theo Karol 1987, do HOL blocking, input queue tăng không giới hạn (tức là significant packet loss) khi arrival rate chỉ đạt 58% capacity — ngay cả khi switch fabric được giả định đủ nhanh.*

---

**Câu 52.** Output port queuing xảy ra khi nào?

A. Khi routing processor bận xử lý routing protocols
B. Khi nhiều packets cùng lúc đến từ N input ports và cùng muốn ra một output port — output port chỉ có thể truyền một packet mỗi time unit
C. Khi forwarding table chứa quá nhiều entries
D. Khi switch fabric không đủ nhanh hơn line speed

**Đáp án: B**
*Giải thích: Nếu switch fabric N lần nhanh hơn line speed và N packets từ N input ports đều muốn ra một output port, N packets mới đến trong thời gian truyền 1 packet → phải queue. Nếu hàng đợi đầy → packet loss.*

---

**Câu 53.** Rule of thumb cổ điển về kích thước buffer cho router là gì?

A. Buffer = Link capacity × 1 second
B. Buffer B = RTT × C (Round-trip time × Link capacity)
C. Buffer = số lượng flows × 1 packet
D. Buffer = Link speed / 10

**Đáp án: B**
*Giải thích: Rule of thumb cổ điển (RFC 3439): B = RTT × C. Ví dụ: 10 Gbps link với RTT = 250ms → cần B = 2.5 Gbits. Tuy nhiên nghiên cứu gần đây đề xuất B = RTT × C / √N cho N TCP flows lớn.*

---

**Câu 54.** Công thức buffer sizing cải tiến cho large backbone links với N TCP flows là gì?

A. B = RTT × C × N
B. B = RTT × C / √N
C. B = RTT × C / N
D. B = RTT / C × √N

**Đáp án: B**
*Giải thích: Nghiên cứu [Appenzeller 2004] đề xuất B = RTT × C / √N. Với N lớn (nhiều TCP flows qua backbone), lượng buffer cần thiết giảm đáng kể so với rule of thumb cổ điển.*

---

**Câu 55.** AQM (Active Queue Management) và thuật toán RED (Random Early Detection) hoạt động như thế nào?

A. RED drop tất cả packets khi queue đầy
B. RED duy trì weighted average queue length: admit nếu < minth, drop/mark nếu > maxth hoặc queue đầy, drop/mark theo xác suất nếu trong [minth, maxth]
C. RED ưu tiên drop packets có priority thấp nhất
D. RED chỉ hoạt động với UDP traffic

**Đáp án: B**
*Giải thích: RED dùng weighted average queue length. Ba trường hợp: (1) avg < minth → admit, (2) queue full hoặc avg > maxth → drop/mark, (3) avg ∈ [minth, maxth] → drop/mark theo probability. Mục tiêu: gửi congestion signal sớm cho sender.*

---

**Câu 56.** "Drop-tail" policy trong router là gì?

A. Drop packets có TTL thấp nhất khi buffer đầy
B. Drop arriving packet khi không còn memory để buffer — đây là policy đơn giản nhất
C. Drop oldest packet trong queue để nhường chỗ cho packet mới
D. Drop packets khi CPU của routing processor quá tải

**Đáp án: B**
*Giải thích: Drop-tail là policy đơn giản nhất: khi buffer đầy, drop arriving packet. Ngược lại, một số policies chủ động drop hoặc đánh dấu packets trước khi buffer đầy (AQM) để cung cấp congestion signal sớm hơn.*

---

**Câu 57.** Packet scheduler tại output port quyết định điều gì?

A. Quyết định packet nào sẽ bị drop khi buffer đầy
B. Chọn một packet trong số các packets đang chờ để truyền tiếp theo — ví dụ FCFS hoặc WFQ
C. Quyết định routing path cho packet
D. Xác định TTL của packet

**Đáp án: B**
*Giải thích: Packet scheduler chọn packet tiếp theo để truyền từ output queue. FCFS (First-Come-First-Served) là đơn giản nhất. WFQ (Weighted Fair Queuing) chia sẻ bandwidth công bằng giữa các flows. Scheduling đóng vai trò quan trọng trong QoS.*

---

**Câu 58.** Trong kiến trúc routing control plane truyền thống, control plane nằm ở đâu?

A. Trong một centralized server bên ngoài router
B. Hoàn toàn trong routing processor của mỗi router — decentralized, các routers tương tác qua routing protocol messages
C. Trong cloud infrastructure do ISP quản lý
D. Trong end systems của users

**Đáp án: B**
*Giải thích: Trong kiến trúc truyền thống, routing control plane hoàn toàn nằm trong routing processor của mỗi router. Network-wide control plane là decentralized — các routers chạy routing algorithms và trao đổi control messages.*

---

**Câu 59.** Xu hướng nghiên cứu mới về router control plane là gì?

A. Tăng tốc control plane bằng cách dùng FPGA
B. Tách biệt software control plane khỏi hardware data plane — một phần control plane ở router, phần khác ở external centralized server — với well-defined API
C. Loại bỏ hoàn toàn control plane trong router
D. Merge control plane và data plane thành một hardware component

**Đáp án: B**
*Giải thích: Các nhà nghiên cứu đề xuất tách data plane (hardware) khỏi control plane (software), với một phần control plane trong router (local measurement, forwarding table install) và phần khác trong centralized server (route calculation). Điều này đơn giản hóa routing và cho phép network innovation.*

---

## Phần 4.4 — The Internet Protocol (IP): Introduction

**Câu 60.** IP có bao nhiêu phiên bản đang được sử dụng và phiên bản nào phổ biến nhất?

A. Chỉ một phiên bản — IPv4
B. Hai phiên bản — IPv4 (widely deployed) và IPv6
C. Ba phiên bản — IPv4, IPv5, IPv6
D. Bốn phiên bản — IPv4, IPv5, IPv6, IPv7

**Đáp án: B**
*Giải thích: Hiện có hai phiên bản IP đang được sử dụng: IPv4 (phổ biến nhất, còn gọi là IP) và IPv6. IPv4 dùng địa chỉ 32-bit; IPv6 dùng địa chỉ 128-bit.*

---

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

---

## Câu hỏi nâng cao và phân tích

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



# Bộ Câu Hỏi Trắc Nghiệm: Network Layer (Chương 4)
## Phạm vi: IP Protocol, Routing Algorithms, Routing in the Internet, Broadcast & Multicast

---

## PHẦN 1: IP PROTOCOL (4.4)

**Câu 1.** Ba thành phần chính của network layer trong Internet là gì?

A. TCP, UDP, và IP  
B. IP protocol, routing protocols, và ICMP  
C. DNS, HTTP, và IP  
D. Ethernet, Wi-Fi, và IP  

**Đáp án: B**  
*Giải thích: Network layer của Internet gồm IP protocol (addressing, datagram format, packet handling), routing protocols (RIP, OSPF, BGP để tính forwarding table), và ICMP (error reporting, router signaling).*

---

**Câu 2.** Trường "Version" trong IPv4 datagram có độ dài bao nhiêu bit?

A. 8 bit  
B. 16 bit  
C. 4 bit  
D. 32 bit  

**Đáp án: C**  
*Giải thích: Trường Version có 4 bit, xác định phiên bản IP (4 cho IPv4, 6 cho IPv6) để router biết cách diễn giải phần còn lại của datagram.*

---

**Câu 3.** Kích thước tối đa lý thuyết của một IPv4 datagram là bao nhiêu?

A. 1500 bytes  
B. 576 bytes  
C. 65,535 bytes  
D. 32,768 bytes  

**Đáp án: C**  
*Giải thích: Trường Datagram length có 16 bit nên giá trị tối đa là 2^16 - 1 = 65,535 bytes. Tuy nhiên, trên thực tế datagram hiếm khi vượt quá 1,500 bytes.*

---

**Câu 4.** Mục đích của trường TTL (Time-to-Live) trong IPv4 datagram là gì?

A. Xác định thời gian datagram được tạo ra  
B. Ngăn datagram lưu hành mãi mãi trong mạng do routing loop  
C. Chỉ định thời gian timeout cho kết nối TCP  
D. Đo độ trễ của datagram trên đường truyền  

**Đáp án: B**  
*Giải thích: TTL được giảm 1 mỗi khi qua một router. Khi TTL = 0, datagram bị hủy. Điều này ngăn datagram bị kẹt vĩnh viễn trong mạng do routing loop.*

---

**Câu 5.** Trường "Protocol" trong IPv4 datagram đóng vai trò gì?

A. Xác định phiên bản IP được sử dụng  
B. Chỉ định transport-layer protocol (TCP=6, UDP=17) để demultiplex tại đích  
C. Xác định loại link-layer frame  
D. Chỉ định phương thức mã hóa dữ liệu  

**Đáp án: B**  
*Giải thích: Trường Protocol là "keo dán" giữa network và transport layer, tương tự như port number là keo dán giữa transport và application layer. Giá trị 6 = TCP, 17 = UDP.*

---

**Câu 6.** Tại sao header checksum phải được tính lại tại mỗi router?

A. Vì dữ liệu payload thay đổi  
B. Vì TTL field thay đổi tại mỗi router  
C. Vì source IP address thay đổi  
D. Vì destination IP address thay đổi  

**Đáp án: B**  
*Giải thích: TTL bị giảm 1 tại mỗi router, làm thay đổi nội dung header, do đó checksum phải được tính lại. Options field cũng có thể thay đổi.*

---

**Câu 7.** IP Fragmentation xảy ra khi nào?

A. Khi datagram quá nhỏ so với MTU của link  
B. Khi datagram lớn hơn MTU (Maximum Transmission Unit) của outgoing link  
C. Khi có quá nhiều datagram trong mạng  
D. Khi TTL của datagram bằng 0  

**Đáp án: B**  
*Giải thích: MTU giới hạn kích thước tối đa của dữ liệu trong một link-layer frame. Khi IP datagram lớn hơn MTU, router phải phân mảnh (fragment) datagram thành các phần nhỏ hơn.*

---

**Câu 8.** Trong IP fragmentation, quá trình reassembly diễn ra ở đâu?

A. Tại mỗi router trung gian  
B. Tại router đầu tiên nhận được fragment  
C. Tại end system (destination host)  
D. Tại gateway router của AS đích  

**Đáp án: C**  
*Giải thích: Các nhà thiết kế IPv4 quyết định đặt việc reassembly ở end system thay vì router để giữ cho network core đơn giản và tránh làm phức tạp hoặc giảm hiệu năng router.*

---

**Câu 9.** Một datagram 4,000 bytes đến router với MTU 1,500 bytes. Datagram gốc có 20 bytes IP header. Dữ liệu payload của fragment đầu tiên có kích thước bao nhiêu?

A. 1,500 bytes  
B. 1,480 bytes  
C. 1,460 bytes  
D. 1,020 bytes  

**Đáp án: B**  
*Giải thích: MTU = 1,500 bytes, trừ đi 20 bytes IP header = 1,480 bytes dữ liệu. Lượng payload trong mỗi fragment (trừ fragment cuối) phải là bội số của 8 bytes.*

---

**Câu 10.** Fragment cuối cùng của một datagram bị phân mảnh có flag bit như thế nào?

A. Flag = 1 (còn fragment tiếp theo)  
B. Flag = 0 (đây là fragment cuối)  
C. Flag = 2 (fragment đặc biệt)  
D. Flag không thay đổi  

**Đáp án: B**  
*Giải thích: Flag = 1 có nghĩa là "còn more fragments" (chưa phải cuối). Flag = 0 báo hiệu đây là fragment cuối cùng, giúp destination host xác nhận đã nhận đủ.*

---

**Câu 11.** Trường "Fragmentation offset" trong IP header đơn vị là gì?

A. Bytes  
B. 8-byte chunks (đơn vị 8 bytes)  
C. 16-byte chunks  
D. Bits  

**Đáp án: B**  
*Giải thích: Offset được tính theo đơn vị 8-byte chunks. Ví dụ offset = 185 nghĩa là dữ liệu bắt đầu tại byte 185 × 8 = 1,480 của datagram gốc.*

---

**Câu 12.** Tấn công DoS "Jolt2" liên quan đến fragmentation như thế nào?

A. Gửi datagram quá lớn để làm tràn bộ nhớ router  
B. Gửi hàng loạt fragment nhỏ không có fragment nào có offset = 0  
C. Gửi fragment trùng lặp để làm chậm mạng  
D. Gửi fragment với TTL = 0  

**Đáp án: B**  
*Giải thích: Jolt2 attack gửi stream các fragment nhỏ, không có fragment nào có offset = 0, khiến target host bị collapse khi cố gắng tái tạo datagram từ các packet dị dạng.*

---

**Câu 13.** Một IP address trong IPv4 có độ dài bao nhiêu bit?

A. 16 bit  
B. 64 bit  
C. 128 bit  
D. 32 bit  

**Đáp án: D**  
*Giải thích: IPv4 address có 32 bit (4 bytes), cho phép khoảng 4 tỷ địa chỉ khác nhau. Được viết dưới dạng dotted-decimal notation (ví dụ: 193.32.216.9).*

---

**Câu 14.** Trong IP addressing, một "interface" là gì?

A. Phần mềm kết nối giữa hai protocol  
B. Ranh giới giữa host/router và physical link  
C. Địa chỉ IP dùng để nhận dạng mạng  
D. Giao thức kết nối giữa hai AS  

**Đáp án: B**  
*Giải thích: Interface là ranh giới giữa host hoặc router và physical link của nó. IP address được gắn với interface, không phải với host hoặc router. Router có nhiều interface (một cho mỗi link).*

---

**Câu 15.** Subnet mask /24 có nghĩa là gì?

A. Subnet có tối đa 24 host  
B. 24 bit đầu tiên của IP address xác định subnet address  
C. Subnet sử dụng 24 router  
D. Datagram có thể qua tối đa 24 router  

**Đáp án: B**  
*Giải thích: /24 (CIDR notation) nghĩa là 24 bit đầu (leftmost) là network portion. Ví dụ: 223.1.1.0/24 bao gồm tất cả địa chỉ có dạng 223.1.1.xxx.*

---

**Câu 16.** Phương pháp xác định subnet trong một mạng là gì?

A. Đếm số router trong mạng  
B. Tách mỗi interface khỏi host/router, mỗi mạng isolated là một subnet  
C. Đếm số switch trong mạng  
D. Xem số VLAN được cấu hình  

**Đáp án: B**  
*Giải thích: Để xác định subnet, tách (detach) mỗi interface khỏi host/router, tạo ra các "islands" mạng cô lập. Mỗi island đó là một subnet.*

---

**Câu 17.** CIDR (Classless Interdomain Routing) khắc phục hạn chế gì của classful addressing?

A. CIDR cho phép địa chỉ IP dài hơn  
B. CIDR cho phép subnet mask linh hoạt, không bị giới hạn ở 8, 16, 24 bit  
C. CIDR tăng tốc độ routing  
D. CIDR bảo mật địa chỉ IP tốt hơn  

**Đáp án: B**  
*Giải thích: Classful addressing chỉ cho phép subnet 8-bit (Class A), 16-bit (Class B), 24-bit (Class C). CIDR generalize thành a.b.c.d/x với x bất kỳ, phân bổ địa chỉ hiệu quả hơn.*

---

**Câu 18.** "Address aggregation" (hay route aggregation) là gì?

A. Việc gộp nhiều địa chỉ IP thành một địa chỉ duy nhất  
B. Dùng một prefix duy nhất để advertise nhiều mạng con bên trong  
C. Tự động phân bổ địa chỉ IP cho các host  
D. Chuyển đổi địa chỉ private thành public  

**Đáp án: B**  
*Giải thích: Address aggregation cho phép ISP advertise một prefix duy nhất (ví dụ /20) thay vì nhiều prefix nhỏ hơn của các tổ chức bên trong. Giúp giảm kích thước routing table.*

---

**Câu 19.** Khi hai ISP cùng advertise prefix cho một tổ chức (một /20 và một /23), router sẽ chọn path nào?

A. Path qua ISP advertise prefix /20 (ngắn hơn)  
B. Path qua ISP advertise prefix /23 (dài hơn, cụ thể hơn) — longest prefix matching  
C. Router chọn ngẫu nhiên  
D. Router chọn path có chi phí thấp hơn  

**Đáp án: B**  
*Giải thích: Longest prefix matching: router chọn entry trong forwarding table có prefix dài nhất (cụ thể nhất) match với destination address. /23 cụ thể hơn /20.*

---

**Câu 20.** DHCP là giao thức gì và hoạt động theo mô hình nào?

A. Giao thức routing, mô hình peer-to-peer  
B. Giao thức tự động cấp phát IP address, mô hình client-server  
C. Giao thức bảo mật, mô hình request-response  
D. Giao thức multicast, mô hình broadcast  

**Đáp án: B**  
*Giải thích: DHCP (Dynamic Host Configuration Protocol) tự động cấp phát IP address cho host khi kết nối vào mạng. Hoạt động theo mô hình client-server với 4 bước: Discover, Offer, Request, ACK.*

---

**Câu 21.** Bốn bước của quá trình DHCP theo thứ tự đúng là gì?

A. Request → Discover → Offer → ACK  
B. Discover → Offer → Request → ACK  
C. Offer → Discover → ACK → Request  
D. Discover → Request → Offer → ACK  

**Đáp án: B**  
*Giải thích: (1) DHCP Discover: client broadcast tìm server; (2) DHCP Offer: server đề xuất địa chỉ IP; (3) DHCP Request: client chọn offer và xác nhận; (4) DHCP ACK: server xác nhận cấp phát.*

---

**Câu 22.** Trong bước DHCP Discover, client sử dụng destination IP address nào?

A. Địa chỉ IP của DHCP server  
B. Địa chỉ IP của default gateway  
C. 255.255.255.255 (broadcast address)  
D. 127.0.0.1 (loopback)  

**Đáp án: C**  
*Giải thích: Client chưa biết địa chỉ DHCP server nên gửi broadcast đến 255.255.255.255 với source address 0.0.0.0 ("this host"). Tất cả nodes trên subnet đều nhận được.*

---

**Câu 23.** Ngoài IP address, DHCP còn cung cấp thông tin gì cho host?

A. Chỉ địa chỉ IP và subnet mask  
B. Subnet mask, địa chỉ default gateway, và địa chỉ DNS server  
C. Địa chỉ IP, MAC address, và routing table  
D. Chỉ địa chỉ IP  

**Đáp án: B**  
*Giải thích: DHCP cung cấp: (1) IP address, (2) subnet mask, (3) địa chỉ first-hop router (default gateway), và (4) địa chỉ DNS server cục bộ.*

---

**Câu 24.** Vì sao DHCP được gọi là "plug-and-play" protocol?

A. Vì nó sử dụng USB để kết nối  
B. Vì tự động cấu hình network, không cần administrator can thiệp thủ công  
C. Vì hoạt động trên mọi loại hardware  
D. Vì có thể cắm và rút cáp mạng tùy ý  

**Đáp án: B**  
*Giải thích: DHCP tự động hóa việc cấp phát IP address và cấu hình mạng, đặc biệt hữu ích khi host thường xuyên di chuyển giữa các subnet (như sinh viên dùng laptop).*

---

**Câu 25.** NAT (Network Address Translation) giải quyết vấn đề gì?

A. Tăng tốc độ routing  
B. Cho phép nhiều device trong mạng private dùng chung một public IP address  
C. Bảo mật dữ liệu bằng mã hóa  
D. Tăng độ tin cậy của kết nối  

**Đáp án: B**  
*Giải thích: NAT cho phép tất cả traffic từ home network ra Internet dùng một single IP address (IP của WAN-side interface của NAT router), ẩn cấu trúc mạng nội bộ.*

---

**Câu 26.** NAT sử dụng cơ chế gì để phân biệt các internal host khi nhận response từ Internet?

A. MAC address của mỗi device  
B. NAT translation table sử dụng cả IP address và port number  
C. Địa chỉ private IP của mỗi device  
D. Sequence number của TCP  

**Đáp án: B**  
*Giải thích: NAT translation table lưu mapping giữa (WAN IP, WAN port) và (LAN IP, LAN port). Vì port number 16-bit, NAT có thể hỗ trợ hơn 60,000 kết nối đồng thời với 1 WAN IP.*

---

**Câu 27.** Giới hạn nào của NAT ảnh hưởng đến P2P applications?

A. NAT giới hạn tốc độ download  
B. Host sau NAT không thể hoạt động như server vì không thể nhận incoming TCP connections từ ngoài  
C. NAT không hỗ trợ UDP  
D. NAT giới hạn số lượng download đồng thời  

**Đáp án: B**  
*Giải thích: Peer sau NAT không thể chấp nhận TCP connection khởi tạo từ bên ngoài. Giải pháp bao gồm connection reversal (qua peer trung gian) hoặc UPnP.*

---

**Câu 28.** UPnP (Universal Plug and Play) giải quyết vấn đề NAT như thế nào?

A. Loại bỏ hoàn toàn NAT khỏi mạng  
B. Cho phép application yêu cầu NAT tạo port mapping để nhận incoming connections  
C. Tự động cấp phát địa chỉ IP công cộng  
D. Mã hóa tất cả traffic đi qua NAT  

**Đáp án: B**  
*Giải thích: UPnP cho phép host request NAT tạo mapping (private IP, private port) → (public IP, public port), sau đó advertise public address để external host có thể kết nối vào.*

---

**Câu 29.** ICMP được sử dụng chủ yếu để làm gì?

A. Routing packets giữa các mạng  
B. Error reporting và thông báo network-layer information  
C. Mã hóa dữ liệu truyền tải  
D. Quản lý địa chỉ IP  

**Đáp án: B**  
*Giải thích: ICMP (Internet Control Message Protocol) dùng để báo lỗi (như "Destination network unreachable") và cung cấp thông tin network-layer. ICMP messages được mang trong IP datagrams.*

---

**Câu 30.** Lệnh `ping` sử dụng loại ICMP message nào?

A. Type 3 Code 0 (Destination unreachable)  
B. Type 11 Code 0 (TTL expired)  
C. Type 8 Code 0 (Echo request) và Type 0 Code 0 (Echo reply)  
D. Type 4 Code 0 (Source quench)  

**Đáp án: C**  
*Giải thích: `ping` gửi ICMP type 8 code 0 (echo request). Destination host phản hồi bằng type 0 code 0 (echo reply). Đây là cách kiểm tra kết nối cơ bản nhất.*

---

**Câu 31.** Traceroute hoạt động dựa trên cơ chế nào?

A. Gửi packet với destination address là mỗi router trên đường đi  
B. Gửi series UDP datagram với TTL tăng dần (1, 2, 3,...), thu thập ICMP TTL-expired responses  
C. Hỏi mỗi router về routing table của nó  
D. Sử dụng SNMP để lấy thông tin từ các router  

**Đáp án: B**  
*Giải thích: Traceroute gửi UDP datagram với TTL=1,2,3... Khi TTL hết tại router thứ n, router gửi ICMP type 11 code 0 (TTL expired) về. Source thu thập tên và địa chỉ của từng router.*

---

**Câu 32.** Traceroute biết khi nào cần dừng gửi probe packets?

A. Khi nhận được một số lượng nhất định responses  
B. Khi destination gửi ICMP type 3 code 3 (Port unreachable) vì datagram dùng unlikely port  
C. Khi TTL đạt giá trị tối đa 255  
D. Khi mất kết nối internet  

**Đáp án: B**  
*Giải thích: Destination nhận UDP datagram với unlikely port number sẽ gửi ICMP "port unreachable" (type 3, code 3). Source nhận được message này biết đã đến đích, dừng gửi.*

---

**Câu 33.** Lý do chính dẫn đến sự ra đời của IPv6 là gì?

A. IPv4 không hỗ trợ multicast  
B. IPv4 không có tính năng bảo mật  
C. Không gian địa chỉ 32-bit của IPv4 đang cạn kiệt  
D. IPv4 quá chậm cho các ứng dụng video  

**Đáp án: C**  
*Giải thích: Sự bùng nổ kết nối Internet khiến địa chỉ IPv4 cạn kiệt. IANA đã cấp hết pool địa chỉ IPv4 chưa phân bổ vào tháng 2/2011. IPv6 mở rộng địa chỉ lên 128 bit.*

---

**Câu 34.** IPv6 address có độ dài bao nhiêu bit?

A. 32 bit  
B. 64 bit  
C. 256 bit  
D. 128 bit  

**Đáp án: D**  
*Giải thích: IPv6 tăng kích thước địa chỉ từ 32 lên 128 bit, đủ để cấp địa chỉ cho mọi "hạt cát trên Trái Đất". Ngoài unicast và multicast, IPv6 còn thêm anycast address.*

---

**Câu 35.** IPv6 fixed header có kích thước bao nhiêu bytes?

A. 20 bytes  
B. 60 bytes  
C. 40 bytes  
D. 80 bytes  

**Đáp án: C**  
*Giải thích: IPv6 có fixed-length header 40 bytes (gấp đôi IPv4 minimum 20 bytes), cho phép xử lý nhanh hơn. Các trường ít dùng như options được loại khỏi header chuẩn.*

---

**Câu 36.** IPv6 đã loại bỏ những tính năng nào so với IPv4?

A. Routing và addressing  
B. Fragmentation tại router, header checksum, và options field trong header chuẩn  
C. TTL và source address  
D. UDP và TCP support  

**Đáp án: B**  
*Giải thích: IPv6 loại bỏ: (1) fragmentation tại router (chỉ ở end systems), (2) header checksum (tránh tính lại tại mỗi router do hop limit thay đổi), (3) options không còn trong header chuẩn.*

---

**Câu 37.** Trường "Flow label" trong IPv6 dùng để làm gì?

A. Xác định version của IP  
B. Nhận dạng một flow của datagram yêu cầu xử lý đặc biệt (QoS, real-time)  
C. Đếm số router mà datagram đã đi qua  
D. Xác định protocol của transport layer  

**Đáp án: B**  
*Giải thích: Flow label (20 bit) cho phép gán nhãn cho các packet thuộc cùng một flow (như audio/video) để xử lý với QoS đặc biệt. Định nghĩa chính xác của "flow" vẫn còn mở.*

---

**Câu 38.** Phương pháp "Dual-stack" trong chuyển đổi IPv4 → IPv6 là gì?

A. Chạy hai mạng hoàn toàn tách biệt  
B. Node có cả implementation IPv4 lẫn IPv6, dùng IPv6 với node IPv6, IPv4 với node IPv4  
C. Đặt hai router tại mỗi điểm kết nối  
D. Dùng NAT để chuyển đổi giữa IPv4 và IPv6  

**Đáp án: B**  
*Giải thích: Dual-stack node (IPv6/IPv4 node) có thể gửi và nhận cả hai loại datagram. Dùng DNS để xác định node đích hỗ trợ IPv6 hay chỉ IPv4. Hạn chế: có thể mất thông tin IPv6-specific khi convert.*

---

**Câu 39.** Tunneling trong chuyển đổi IPv6 giải quyết vấn đề gì?

A. Tăng tốc độ truyền IPv6 packet  
B. Cho phép IPv6 packet đi qua vùng mạng chỉ có IPv4 bằng cách đóng gói IPv6 vào IPv4  
C. Bảo mật IPv6 traffic  
D. Giảm kích thước IPv6 header  

**Đáp án: B**  
*Giải thích: Tunneling đóng gói toàn bộ IPv6 datagram vào data field của IPv4 datagram. IPv4 routers trung gian không biết bên trong là IPv6. Node đầu kia giải đóng gói và xử lý IPv6 datagram.*

---

**Câu 40.** IPsec cung cấp những dịch vụ bảo mật nào?

A. Chỉ mã hóa dữ liệu  
B. Cryptographic agreement, encryption, data integrity, và origin authentication  
C. Chỉ xác thực nguồn gốc  
D. Chỉ kiểm tra tính toàn vẹn dữ liệu  

**Đáp án: B**  
*Giải thích: IPsec (trong transport mode) cung cấp: (1) thỏa thuận thuật toán mã hóa và keys, (2) mã hóa payload, (3) kiểm tra tính toàn vẹn dữ liệu, (4) xác thực địa chỉ nguồn.*

---

## PHẦN 2: ROUTING ALGORITHMS (4.5)

**Câu 41.** Mục đích của routing algorithm là gì?

A. Mã hóa dữ liệu trước khi gửi  
B. Tìm "good path" (thường là least-cost path) từ source đến destination router  
C. Phân bổ địa chỉ IP cho các thiết bị  
D. Kiểm soát tốc độ truyền dữ liệu  

**Đáp án: B**  
*Giải thích: Routing algorithm xác định đường đi tốt (thường là ít tốn kém nhất) từ source router đến destination router. Kết quả được lưu vào forwarding table.*

---

**Câu 42.** Sự khác biệt giữa "global routing algorithm" và "decentralized routing algorithm" là gì?

A. Global dùng nhiều router hơn  
B. Global có complete knowledge về network; decentralized chỉ biết local information và trao đổi với neighbors  
C. Global chạy nhanh hơn  
D. Global chỉ dùng trong Internet, decentralized dùng trong LAN  

**Đáp án: B**  
*Giải thích: Global (link-state) algorithm có complete map của network. Decentralized (distance-vector) algorithm: mỗi node chỉ biết chi phí link trực tiếp, trao đổi thông tin dần dần với neighbors.*

---

**Câu 43.** Link-State (LS) algorithm còn được gọi là gì và vì sao?

A. Distance-vector, vì dùng vector khoảng cách  
B. Link-state, vì mỗi node phải biết chi phí (state) của mọi link trong mạng  
C. Path-vector, vì lưu toàn bộ đường đi  
D. Flooding algorithm, vì broadcast thông tin  

**Đáp án: B**  
*Giải thích: LS algorithm yêu cầu mỗi node biết "state" (chi phí) của tất cả link trong mạng. Thông tin này được thu thập qua link-state broadcast từ tất cả nodes.*

---

**Câu 44.** Dijkstra's algorithm có độ phức tạp tính toán worst-case là bao nhiêu?

A. O(n)  
B. O(n log n)  
C. O(n²)  
D. O(n³)  

**Đáp án: C**  
*Giải thích: Với n nodes, tổng số lần tìm kiếm qua các iterations là n(n+1)/2 = O(n²). Dùng heap data structure có thể giảm xuống O(n log n).*

---

**Câu 45.** Trong Dijkstra's algorithm, tập N' (hay N') đại diện cho điều gì?

A. Tập tất cả nodes trong mạng  
B. Tập nodes mà least-cost path từ source đã được xác định chắc chắn  
C. Tập neighbors của source node  
D. Tập nodes chưa được thăm  

**Đáp án: B**  
*Giải thích: N' là tập các nodes mà shortest path từ source node u đã được tính toán xong và chính xác. Mỗi iteration thêm một node vào N' (node có D(v) nhỏ nhất ngoài N').*

---

**Câu 46.** Vấn đề "oscillation" trong LS routing xảy ra khi nào?

A. Khi mạng bị chia cắt  
B. Khi link costs dựa trên lưu lượng traffic, khiến routers đồng thời chuyển route theo cùng một hướng  
C. Khi router bị lỗi  
D. Khi có quá nhiều routers trong mạng  

**Đáp án: B**  
*Giải thích: Nếu link cost phản ánh congestion, tất cả routers có thể cùng chuyển traffic sang một route "tốt hơn", tạo congestion ở đó, rồi lại chuyển ngược lại. Giải pháp: randomize thời điểm chạy LS algorithm.*

---

**Câu 47.** Bellman-Ford equation trong DV algorithm là gì?

A. dx(y) = max_v{c(x,v) + dv(y)}  
B. dx(y) = min_v{c(x,v) + dv(y)}  
C. dx(y) = sum_v{c(x,v) + dv(y)}  
D. dx(y) = c(x,y) × hop_count  

**Đáp án: B**  
*Giải thích: Chi phí least-cost path từ x đến y bằng minimum (qua tất cả neighbors v) của tổng chi phí link x→v cộng chi phí v→y. Đây là nền tảng của DV algorithm.*

---

**Câu 48.** Distance-Vector algorithm có ba đặc tính chính là gì?

A. Fast, reliable, và secure  
B. Iterative, asynchronous, và distributed  
C. Global, centralized, và synchronized  
D. Static, deterministic, và centralized  

**Đáp án: B**  
*Giải thích: DV là: (1) iterative — tiếp tục đến khi không còn thay đổi; (2) asynchronous — không cần tất cả nodes hoạt động đồng thời; (3) distributed — mỗi node tính toán và chia sẻ với neighbors.*

---

**Câu 49.** Trong DV algorithm, khi nào một node gửi distance vector update cho neighbors?

A. Mỗi giây một lần  
B. Khi distance vector của node đó thay đổi (do link cost thay đổi hoặc nhận update từ neighbor)  
C. Khi router khởi động lại  
D. Chỉ khi được yêu cầu  

**Đáp án: B**  
*Giải thích: Node x gửi updated distance vector cho tất cả neighbors khi Dx(y) thay đổi cho bất kỳ destination y nào. Điều này xảy ra sau khi nhận update từ neighbor hoặc khi link cost thay đổi.*

---

**Câu 50.** "Count-to-infinity problem" trong DV algorithm là gì?

A. Router đếm vô hạn gói tin trong queue  
B. Khi link cost tăng, bad news lan chậm qua mạng — nodes liên tục tăng cost estimate lên vô cùng  
C. Routing table lớn vô hạn  
D. Vòng lặp đếm không bao giờ kết thúc trong thuật toán  

**Đáp án: B**  
*Giải thích: Khi link X-Y cost tăng từ 4 lên 60, Y nghĩ vẫn có thể đi qua Z (vì Z trước đó báo cost=5 qua Y). Y và Z tăng cost estimate lần lượt (6, 7, 8...) cho đến khi vượt 50. Rất chậm.*

---

**Câu 51.** "Poisoned reverse" giải quyết vấn đề gì trong DV algorithm?

A. Tránh routing loop giữa tất cả các cặp nodes  
B. Tránh routing loop giữa hai neighboring nodes — node quảng bá cost = ∞ cho neighbor mà nó đang route qua  
C. Tăng tốc convergence của DV algorithm  
D. Giảm kích thước routing table  

**Đáp án: B**  
*Giải thích: Nếu Z route đến X qua Y, Z quảng bá Dz(X) = ∞ cho Y. Y không bao giờ route đến X qua Z (tránh loop 2 node). Nhưng poisoned reverse không giải quyết được loop 3+ nodes.*

---

**Câu 52.** So sánh LS và DV algorithm về "robustness" (khả năng chịu lỗi)?

A. LS và DV đều không bị ảnh hưởng bởi router lỗi  
B. LS tốt hơn: node chỉ tính forwarding table riêng, lỗi không lan rộng; DV: lỗi có thể lan sang toàn mạng  
C. DV tốt hơn: phân tán nên không có điểm lỗi đơn  
D. Cả hai đều có cùng mức độ robustness  

**Đáp án: B**  
*Giải thích: LS: mỗi node tính forwarding table độc lập, router lỗi chỉ có thể broadcast incorrect link cost (giới hạn). DV: node lỗi có thể advertise incorrect cost đến mọi destination, lan toàn mạng.*

---

**Câu 53.** Hierarchical routing được thực hiện thông qua cơ chế gì?

A. Phân cấp địa chỉ IP  
B. Tổ chức routers thành Autonomous Systems (ASs)  
C. Sử dụng nhiều level của routing tables  
D. Phân chia mạng theo địa lý  

**Đáp án: B**  
*Giải thích: Routers được nhóm thành AS (Autonomous Systems). Mỗi AS chạy intra-AS routing protocol riêng. Các AS kết nối với nhau qua inter-AS routing protocol (BGP).*

---

**Câu 54.** "Gateway router" trong một AS có vai trò gì?

A. Cấp phát địa chỉ IP cho các host trong AS  
B. Forward packets đến destinations ngoài AS và trao đổi routing info với routers AS khác  
C. Chạy DHCP server cho toàn bộ AS  
D. Theo dõi và ghi lại toàn bộ traffic trong AS  

**Đáp án: B**  
*Giải thích: Gateway router là router ở biên của AS, chịu trách nhiệm: forward packets ra ngoài AS, và trao đổi routing information với gateway routers của AS khác qua inter-AS protocol.*

---

**Câu 55.** "Hot-potato routing" là chiến lược gì?

A. Ưu tiên route qua đường đắt nhất  
B. AS chuyển packet ra khỏi mình càng nhanh càng tốt — chọn gateway có least cost từ nội bộ  
C. Route packet qua đường ngắn nhất về số hop  
D. Route packet qua đường có băng thông cao nhất  

**Đáp án: B**  
*Giải thích: Hot-potato routing: AS "tống khứ" packet càng nhanh càng tốt bằng cách chọn gateway router mà chi phí nội bộ (intra-AS) đến đó là nhỏ nhất, bất kể chi phí bên ngoài.*

---

**Câu 56.** Hai lý do chính cần hierarchical routing là gì?

A. Bảo mật và hiệu suất  
B. Scale (quy mô) và administrative autonomy (tự chủ quản trị)  
C. Tốc độ và độ tin cậy  
D. Chi phí và địa lý  

**Đáp án: B**  
*Giải thích: (1) Scale: mạng Internet có hàng triệu router, không thể dùng LS/DV toàn cầu; (2) Administrative autonomy: mỗi tổ chức muốn tự chọn routing protocol và ẩn cấu trúc nội bộ.*

---

## PHẦN 3: ROUTING IN THE INTERNET (4.6)

**Câu 57.** RIP (Routing Information Protocol) sử dụng metric nào để đo chi phí?

A. Bandwidth của link  
B. Delay của link  
C. Hop count (số subnet phải đi qua)  
D. Monetary cost của link  

**Đáp án: C**  
*Giải thích: RIP dùng hop count làm metric — mỗi link có cost = 1. "Hop" là số subnet traversed từ source router đến destination subnet, bao gồm cả destination subnet.*

---

**Câu 58.** RIP giới hạn maximum path cost là bao nhiêu và tại sao?

A. 255, vì field lưu giá trị 8-bit  
B. 16, để ngăn counting problem nghiêm trọng  
C. 15, giới hạn phạm vi hoạt động của RIP  
D. 100, theo quy ước kỹ thuật  

**Đáp án: C**  
*Giải thích: Maximum hop count trong RIP là 15. Cost = 16 được coi là ∞ (unreachable). Điều này giới hạn RIP chỉ dùng trong AS có đường kính dưới 15 hops.*

---

**Câu 59.** RIP routers trao đổi routing update như thế nào và bao lâu một lần?

A. Unicast mỗi 5 giây qua TCP  
B. Broadcast RIP response message mỗi 30 giây qua UDP  
C. Multicast mỗi 60 giây qua IP  
D. Anycast mỗi 10 giây qua ICMP  

**Đáp án: B**  
*Giải thích: RIP routers gửi RIP response message (advertisement) khoảng mỗi 30 giây. Dùng UDP port 520. Nếu không nhận được update từ neighbor trong 180 giây, coi neighbor đã down.*

---

**Câu 60.** Khi router D nhận advertisement từ router A với subnet z có cost 4 (thay vì 7 qua router B), router D cập nhật routing table như thế nào?

A. Giữ nguyên đường cũ qua B  
B. Cập nhật: đường đến z qua A với cost = 4 + 1 = 5 (thay vì 7 qua B)  
C. Xóa entry cho subnet z  
D. Tạo route mới song song với đường cũ  

**Đáp án: B**  
*Giải thích: D nhận được: z cách A 4 hops. D đến A là 1 hop. Vậy D đến z qua A = 5 hops, tốt hơn 7 hops qua B. D cập nhật: next router = A, hops = 5.*

---

**Câu 61.** RIP được implement như thế nào trong hệ thống Unix?

A. Trực tiếp trong kernel  
B. Là application-layer process gọi là "routed" chạy trên UDP  
C. Là driver trong network stack  
D. Là hardware firmware của router  

**Đáp án: B**  
*Giải thích: RIP chạy như application-layer process "routed" (route daemon), giao tiếp qua standard socket với UDP. Dù là application-layer, nó có quyền truy cập đặc biệt để chỉnh sửa routing table trong kernel.*

---

**Câu 62.** Sự khác biệt chính giữa OSPF và RIP về kiểu algorithm là gì?

A. OSPF dùng DV algorithm, RIP dùng LS algorithm  
B. OSPF dùng LS algorithm (Dijkstra), RIP dùng DV algorithm (Bellman-Ford)  
C. Cả hai đều dùng DV algorithm nhưng metric khác nhau  
D. Cả hai đều dùng LS algorithm nhưng OSPF chính xác hơn  

**Đáp án: B**  
*Giải thích: OSPF (Open Shortest Path First) là link-state protocol dùng Dijkstra algorithm. RIP là distance-vector protocol dùng Bellman-Ford. OSPF phổ biến ở upper-tier ISPs, RIP ở lower-tier.*

---

**Câu 63.** OSPF broadcasts routing information như thế nào và với tần suất bao nhiêu?

A. Unicast đến mỗi neighbor mỗi 30 giây  
B. Broadcast đến tất cả routers trong AS khi link thay đổi, và ít nhất mỗi 30 phút  
C. Multicast đến nhóm OSPF mỗi 5 phút  
D. Chỉ broadcast khi router khởi động  

**Đáp án: B**  
*Giải thích: OSPF broadcast link-state info đến tất cả routers trong AS khi có thay đổi link state, và định kỳ ít nhất mỗi 30 phút dù không có thay đổi (để tăng độ tin cậy). Dùng trực tiếp IP (protocol 89).*

---

**Câu 64.** OSPF hỗ trợ tính năng nào mà RIP không có?

A. Distance-vector routing  
B. Hierarchical routing trong AS (phân chia thành areas), multiple same-cost paths, authentication  
C. Hop count metric  
D. UDP transport  

**Đáp án: B**  
*Giải thích: OSPF có nhiều tính năng nâng cao: (1) authentication, (2) multiple equal-cost paths, (3) integrated unicast/multicast support, (4) hierarchical routing với areas và backbone area.*

---

**Câu 65.** Trong OSPF hierarchical routing, "backbone area" có vai trò gì?

A. Chạy tất cả routing computation  
B. Route traffic giữa các areas trong AS  
C. Kết nối với các AS khác  
D. Cấp phát địa chỉ IP cho toàn AS  

**Đáp án: B**  
*Giải thích: Backbone area là area đặc biệt trong OSPF AS, chứa tất cả area border routers. Nhiệm vụ chính: route traffic giữa các non-backbone areas. Packet phải đi: intra-area → backbone → intra-area đích.*

---

**Câu 66.** BGP (Border Gateway Protocol) là giao thức gì và chạy ở level nào?

A. Intra-AS routing protocol, chạy trong một AS  
B. Inter-AS routing protocol, kết nối các AS với nhau qua TCP connections  
C. Link-layer protocol, kết nối routers trong cùng subnet  
D. Transport protocol thay thế TCP  

**Đáp án: B**  
*Giải thích: BGP4 là de facto standard inter-AS routing protocol. BGP peers trao đổi routing information qua semi-permanent TCP connections (port 179). Là "keo dán" giúp Internet hoạt động thống nhất.*

---

**Câu 67.** Sự khác biệt giữa eBGP và iBGP session là gì?

A. eBGP dùng TCP, iBGP dùng UDP  
B. eBGP session span giữa hai AS khác nhau; iBGP session giữa routers trong cùng AS  
C. eBGP nhanh hơn iBGP  
D. eBGP dùng port 80, iBGP dùng port 443  

**Đáp án: B**  
*Giải thích: eBGP (external BGP) kết nối gateway routers của hai AS khác nhau. iBGP (internal BGP) kết nối các routers trong cùng một AS, tạo mesh để phân phối routing info nội bộ.*

---

**Câu 68.** Trong BGP, "AS-PATH" attribute chứa thông tin gì?

A. Chi phí của mỗi link trên đường đi  
B. Danh sách các AS mà advertisement cho prefix đó đã đi qua  
C. Địa chỉ IP của mỗi router trên đường đi  
D. Thời gian packet đi qua mỗi AS  

**Đáp án: B**  
*Giải thích: AS-PATH là list các ASN (Autonomous System Numbers) mà route advertisement đã đi qua. Dùng để: (1) phát hiện và tránh loop (nếu ASN của mình xuất hiện trong path, từ chối); (2) chọn giữa các routes.*

---

**Câu 69.** "NEXT-HOP" attribute trong BGP dùng để làm gì?

A. Xác định destination address của packet  
B. Là địa chỉ IP của router interface đầu tiên bắt đầu AS-PATH — giúp router xác định interface đầu ra  
C. Xác định protocol tiếp theo trong stack  
D. Chỉ định router tiếp theo sau khi ra khỏi AS  

**Đáp án: B**  
*Giải thích: NEXT-HOP là IP address của router interface bắt đầu AS-PATH. Router nội bộ dùng NEXT-HOP + intra-AS routing (OSPF) để tìm shortest path đến NEXT-HOP, xác định output interface.*

---

**Câu 70.** BGP route selection sử dụng các tiêu chí theo thứ tự ưu tiên nào?

A. AS-PATH length → local preference → NEXT-HOP → BGP identifier  
B. Local preference → AS-PATH length (shortest) → closest NEXT-HOP (hot-potato) → BGP identifier  
C. NEXT-HOP → local preference → AS-PATH length → BGP identifier  
D. Bandwidth → delay → hop count → local preference  

**Đáp án: B**  
*Giải thích: Thứ tự: (1) Cao nhất local preference; (2) Nếu bằng nhau: shortest AS-PATH; (3) Nếu bằng nhau: closest NEXT-HOP (hot-potato routing); (4) Nếu vẫn bằng nhau: dùng BGP identifiers.*

---

**Câu 71.** "Stub network" trong BGP routing policy là gì?

A. Mạng không kết nối với Internet  
B. AS chỉ là source/destination của traffic, không forward traffic transit giữa các AS khác  
C. Mạng chỉ có một router  
D. AS không chạy BGP  

**Đáp án: B**  
*Giải thích: Stub AS (như W, X, Y trong ví dụ) chỉ nhận/gửi traffic cho chính mình. Đảm bảo tính chất này bằng cách chỉ advertise routes đến chính nó, không advertise routes transit đến AS khác.*

---

**Câu 72.** Tại sao Internet dùng hai loại routing protocol khác nhau (intra-AS và inter-AS)?

A. Do lịch sử phát triển ngẫu nhiên  
B. Intra-AS ưu tiên performance; inter-AS ưu tiên policy và scale — hai mục tiêu khác nhau  
C. Do giới hạn phần cứng của router  
D. Để tương thích với nhiều nhà sản xuất thiết bị  

**Đáp án: B**  
*Giải thích: Intra-AS: tất cả dưới cùng quản trị, ưu tiên performance. Inter-AS: policy là chủ đạo (AS nào có thể forward traffic của ai?), cần BGP với AS-PATH để kiểm soát routing policy.*

---

## PHẦN 4: BROADCAST AND MULTICAST ROUTING (4.7)

**Câu 73.** Broadcast routing cung cấp dịch vụ gì?

A. Gửi packet từ source đến một destination duy nhất  
B. Gửi packet từ source đến tất cả nodes khác trong mạng  
C. Gửi packet đến một nhóm nodes đã đăng ký  
D. Gửi packet đến node gần nhất trong nhóm  

**Đáp án: B**  
*Giải thích: Broadcast routing: source gửi một packet đến tất cả (all) nodes trong mạng. Khác với unicast (một đến một) và multicast (một đến nhiều trong group).*

---

**Câu 74.** Nhược điểm của N-way-unicast approach cho broadcast là gì?

A. Quá phức tạp để implement  
B. Không hiệu quả (N copies trên first hop), cần biết địa chỉ tất cả recipients, không dùng được khi broadcast cần thiết cho routing  
C. Chỉ hoạt động được với TCP  
D. Không hỗ trợ IPv6  

**Đáp án: B**  
*Giải thích: N-way-unicast gửi N copies riêng biệt: (1) N copies qua first hop link; (2) cần biết địa chỉ mọi recipient (cần thêm protocol); (3) link-state routing dùng broadcast để build unicast routes — circular dependency.*

---

**Câu 75.** "Broadcast storm" trong uncontrolled flooding là gì?

A. Một packet broadcast đến toàn bộ Internet  
B. Sự nhân bản không kiểm soát của broadcast packet, tạo ra vô số copies làm tê liệt mạng  
C. Cơn bão thực sự làm đứt cáp mạng  
D. Quá nhiều routers cùng broadcast routing update  

**Đáp án: B**  
*Giải thích: Trong uncontrolled flooding, nếu graph có cycles, broadcast packets sẽ vòng mãi và nhân bản. Mỗi node có nhiều neighbors tạo nhiều copies, tạo ra broadcast storm làm mạng tê liệt.*

---

**Câu 76.** Cơ chế "Sequence-number-controlled flooding" ngăn broadcast storm như thế nào?

A. Giới hạn số lượng flood packet mỗi giây  
B. Node lưu (source address, sequence number) của packet đã nhận — nếu trùng thì drop, không forward  
C. Chỉ forward đến một subset neighbors  
D. Giảm TTL mỗi lần forward  

**Đáp án: B**  
*Giải thích: Source đặt unique ID (source address + sequence number) vào packet. Mỗi node duy trì danh sách packets đã forward. Nếu nhận packet có ID đã thấy → drop. Gnutella dùng cơ chế này.*

---

**Câu 77.** RPF (Reverse Path Forwarding) hoạt động theo nguyên tắc gì?

A. Forward packet đến tất cả neighbors trừ nơi nhận  
B. Chỉ forward packet nếu nó đến từ link nằm trên shortest unicast path của router đó về phía source  
C. Forward packet theo chiều ngược với unicast routing  
D. Chỉ forward packet đến router có ID số lẻ  

**Đáp án: B**  
*Giải thích: RPF: router chỉ forward broadcast packet nếu packet đến từ link mà là shortest path của router đó quay ngược về source. Ngược lại, drop. Không cần biết toàn bộ path, chỉ cần next-hop về phía source.*

---

**Câu 78.** So với RPF, spanning-tree broadcast cải thiện điều gì?

A. Giảm overhead tính toán  
B. Loại bỏ hoàn toàn redundant packets — mỗi node nhận đúng một bản copy  
C. Cho phép multicast trong spanning tree  
D. Tự động phục hồi khi link bị lỗi  

**Đáp án: B**  
*Giải thích: RPF vẫn tạo ra một số redundant packet. Spanning tree broadcast: forward packet chỉ trên các links trong spanning tree. Mỗi node nhận đúng một copy. Nhưng cần xây dựng và duy trì spanning tree.*

---

**Câu 79.** "Center-based" approach để xây dựng spanning tree hoạt động như thế nào?

A. Chọn node có nhiều links nhất làm center  
B. Mỗi node gửi tree-join message unicast đến center node — path của message tạo nên nhánh của spanning tree  
C. Tất cả nodes broadcast đồng thời để tìm center  
D. Router có ID nhỏ nhất tự động trở thành center  

**Đáp án: B**  
*Giải thích: Center (rendezvous point) được xác định trước. Nodes muốn join gửi unicast tree-join message đến center. Path của message đến center (hoặc đến một node đã trong tree) được "ghép" vào spanning tree.*

---

**Câu 80.** OSPF sử dụng loại broadcast nào để phổ biến link-state advertisements?

A. Sequence-number-controlled flooding  
B. RPF broadcast  
C. Center-based spanning tree  
D. N-way unicast  

**Đáp án: A**  
*Giải thích: OSPF dùng sequence number (32-bit) và age field trong LSA để phát hiện và loại bỏ duplicate. Đây là dạng sequence-number-controlled flooding để broadcast LSA đến tất cả routers trong AS.*

---

**Câu 81.** Multicast routing khác broadcast routing ở điểm gì?

A. Multicast nhanh hơn broadcast  
B. Multicast gửi đến subset of nodes (multicast group), broadcast gửi đến tất cả nodes  
C. Multicast dùng TCP, broadcast dùng UDP  
D. Multicast chỉ hoạt động trong một AS  

**Đáp án: B**  
*Giải thích: Broadcast: tất cả nodes nhận packet. Multicast: chỉ nodes thuộc multicast group nhận packet. Multicast hữu ích cho streaming, conferencing, phân phối nội dung đến nhóm subscribers.*

---

**Câu 82.** Class D IP address được dùng để làm gì?

A. Địa chỉ private cho mạng nội bộ  
B. Định danh một multicast group trong Internet  
C. Địa chỉ dùng riêng cho routers  
D. Địa chỉ broadcast trong subnet  

**Đáp án: B**  
*Giải thích: Class D địa chỉ (224.0.0.0 đến 239.255.255.255) là multicast group address. Mỗi host có unique unicast IP, nhưng có thể join multicast group và nhận packets gửi đến class D address đó.*

---

**Câu 83.** IGMP (Internet Group Management Protocol) hoạt động giữa ai?

A. Giữa các routers trong Internet  
B. Giữa host và first-hop (directly attached) router của nó  
C. Giữa các multicast sources  
D. Giữa AS gateway routers  

**Đáp án: B**  
*Giải thích: IGMP operate giữa host và router kết nối trực tiếp với nó. Host dùng IGMP để thông báo cho router về việc join/leave multicast group. Sau đó multicast routing protocols xử lý phần còn lại.*

---

**Câu 84.** Ba loại IGMP message là gì?

A. Join, Leave, và Update  
B. membership_query, membership_report, và leave_group  
C. Subscribe, Unsubscribe, và Ping  
D. Discover, Offer, và Request  

**Đáp án: B**  
*Giải thích: (1) membership_query: router hỏi hosts về groups đã join; (2) membership_report: host báo cáo groups đã join (phản hồi query hoặc tự động khi join mới); (3) leave_group: optional, báo rời group.*

---

**Câu 85.** "Soft state" trong IGMP có nghĩa là gì?

A. State được lưu vĩnh viễn trong memory  
B. State bị xóa tự động qua timeout nếu không được refresh — không cần explicit deletion  
C. State được backup sang server  
D. State chỉ tồn tại trong một session  

**Đáp án: B**  
*Giải thích: Soft state: router biết có hosts trong multicast group thông qua membership_report. Nếu host không phản hồi membership_query trong một thời gian, router tự động xóa state đó (timeout).*

---

**Câu 86.** Hai cách tiếp cận để xây dựng multicast routing tree là gì?

A. Unicast tree và broadcast tree  
B. Group-shared tree (một cây cho cả nhóm) và source-based tree (cây riêng cho mỗi sender)  
C. Static tree và dynamic tree  
D. Spanning tree và minimum spanning tree  

**Đáp án: B**  
*Giải thích: (1) Group-shared tree: một cây chung cho tất cả senders trong group, dùng center-based approach; (2) Source-based tree: mỗi source có cây riêng, dùng RPF với pruning.*

---

**Câu 87.** "Pruning" trong source-based multicast routing giải quyết vấn đề gì?

A. Giảm kích thước routing table  
B. Ngăn multicast packet đến routers không có attached hosts trong multicast group  
C. Loại bỏ các routers chạm chậm khỏi multicast tree  
D. Cắt bớt số lượng multicast groups  

**Đáp án: B**  
*Giải thích: RPF broadcast gửi packet đến mọi router, kể cả không có host nào trong group. Router không có members trong group gửi "prune message" upstream, router upstream stop forward đến nhánh đó.*

---

**Câu 88.** PIM (Protocol-Independent Multicast) có hai mode chính là gì?

A. IPv4 mode và IPv6 mode  
B. Dense mode (group members đông/tập trung) và Sparse mode (group members thưa/phân tán)  
C. Intra-AS mode và inter-AS mode  
D. Source mode và receiver mode  

**Đáp án: B**  
*Giải thích: PIM Dense mode: dùng flood-and-prune RPF (group members chiếm phần lớn mạng). PIM Sparse mode: dùng rendezvous points để xây dựng shared tree (group members thưa thớt).*

---

## PHẦN 5: CÂU HỎI TỔNG HỢP VÀ NÂNG CAO

**Câu 89.** Tại sao IPv6 loại bỏ tính năng fragmentation tại routers?

A. Vì IPv6 có địa chỉ dài hơn nên packet nhỏ hơn  
B. Fragmentation tốn time xử lý; IPv6 đặt trách nhiệm ở end systems, router dùng "Packet Too Big" ICMP để báo  
C. Vì không có router nào hỗ trợ IPv6 fragmentation  
D. Vì IPv6 packet không bao giờ cần fragmentation  

**Đáp án: B**  
*Giải thích: Fragmentation và reassembly tại router tốn nhiều tài nguyên. IPv6 giao trách nhiệm cho source/destination. Khi packet quá lớn, router drop và gửi "Packet Too Big" ICMPv6 về source. Source resend với size nhỏ hơn.*

---

**Câu 90.** Điểm khác biệt nào của NAT vi phạm nguyên tắc "end-to-end argument"?

A. NAT làm chậm kết nối  
B. NAT thay đổi IP address và port number — các host không nói chuyện trực tiếp mà qua trung gian can thiệp  
C. NAT không hỗ trợ IPv6  
D. NAT tiêu tốn quá nhiều băng thông  

**Đáp án: B**  
*Giải thích: End-to-end argument: hosts nên giao tiếp trực tiếp. NAT là "interfering node" sửa đổi IP address và port number, vi phạm nguyên tắc này. Port number cũng bị dùng sai mục đích (cho host thay vì process).*

---

**Câu 91.** Khi DV algorithm "converge", điều gì xảy ra?

A. Tất cả routers tắt và khởi động lại  
B. Tất cả routers có distance vector chính xác phản ánh topology thực; không còn update messages được gửi  
C. Router trung tâm tổng hợp tất cả routing tables  
D. Mỗi router chọn một path cố định và không bao giờ thay đổi  

**Đáp án: B**  
*Giải thích: Convergence: mọi Dx(y) estimate đã hội tụ đến giá trị thực dx(y). Không có node nào gửi update vì distance vector không thay đổi. Algorithm ở trạng thái quiescent — chờ event tiếp theo.*

---

**Câu 92.** Gói tin DHCP Discover được gửi đến port nào?

A. Port 80 (HTTP)  
B. Port 443 (HTTPS)  
C. Port 67 (DHCP server), gửi từ port 68 (DHCP client)  
D. Port 53 (DNS)  

**Đáp án: C**  
*Giải thích: DHCP sử dụng UDP. Client gửi từ port 68 đến port 67 (server). DHCP reply từ server port 67 đến client port 68. Điều này theo RFC 2131.*

---

**Câu 93.** Tại sao phải có cả intra-AS và inter-AS routing protocol, không thể chỉ dùng một loại?

A. Do giới hạn về phần cứng  
B. Policy chiếm ưu thế ở inter-AS (kiểm soát traffic), còn intra-AS ưu tiên performance; scale cũng khác nhau  
C. Do lịch sử phát triển tình cờ  
D. Vì các nước khác nhau có luật khác nhau về internet  

**Đáp án: B**  
*Giải thích: Intra-AS: cùng quản trị → ưu tiên performance/efficiency. Inter-AS: khác tổ chức → policy là ưu tiên (ai được transit traffic của ai?). Scale: inter-AS phải handle hàng triệu prefix, khác với intra-AS.*

---

**Câu 94.** Trong ví dụ fragmentation với datagram 4000 bytes, MTU 1500 bytes: fragment thứ 3 có offset bao nhiêu và flag bằng bao nhiêu?

A. Offset = 185, Flag = 1  
B. Offset = 370, Flag = 0  
C. Offset = 370, Flag = 1  
D. Offset = 185, Flag = 0  

**Đáp án: B**  
*Giải thích: Fragment 3 bắt đầu tại byte 2960 của payload gốc. Offset = 2960/8 = 370. Đây là fragment cuối (flag = 0 = no more fragments). Fragment 1: offset=0,flag=1; Fragment 2: offset=185,flag=1.*

---

**Câu 95.** Trường "Options" trong IPv4 bị loại bỏ trong IPv6 vì lý do gì?

A. Không ai sử dụng options trong IPv4  
B. Options làm header có kích thước variable, gây khó xử lý nhanh; IPv6 dùng "next header" chain để xử lý linh hoạt hơn  
C. IPv6 không cần options vì đã có tính năng đầy đủ  
D. Options trong IPv4 không hoạt động đúng  

**Đáp án: B**  
*Giải thích: Variable-length header do options làm router không biết data bắt đầu ở đâu, xử lý chậm. IPv6: fixed 40-byte header, options là "next headers" được chain — router có thể skip nếu không cần xử lý.*

---

**Câu 96.** Một tổ chức có 2000 hosts được cấp class B (/16) trong classful addressing. Bao nhiêu địa chỉ bị lãng phí?

A. Khoảng 2000 địa chỉ  
B. Khoảng 63,534 địa chỉ (65,534 - 2,000)  
C. Khoảng 30,000 địa chỉ  
D. Không có địa chỉ nào bị lãng phí  

**Đáp án: B**  
*Giải thích: Class B (/16) hỗ trợ 2^16 - 2 = 65,534 hosts. Tổ chức chỉ dùng 2,000. Lãng phí: 65,534 - 2,000 = 63,534 địa chỉ. Đây là vấn đề của classful addressing, CIDR giải quyết bằng /21 (~2,046 hosts).*

---

**Câu 97.** Trong Dijkstra's algorithm, sau initialization step, giá trị D(w) từ node u là bao nhiêu nếu có direct link u-w với cost 5?

A. ∞  
B. 0  
C. 5  
D. 1  

**Đáp án: C**  
*Giải thích: Trong initialization, D(v) = c(u,v) nếu v là neighbor trực tiếp của u, ngược lại D(v) = ∞. Nếu u-w có direct link với cost 5 thì D(w) = 5 (dù sau đó có thể tìm được path tốt hơn qua node khác).*

---

**Câu 98.** Tại sao BGP dùng TCP thay vì UDP cho BGP sessions?

A. TCP nhanh hơn UDP  
B. BGP cần reliable, ordered delivery của routing messages — TCP đảm bảo điều này  
C. UDP không hỗ trợ port numbers  
D. TCP tự động mã hóa dữ liệu  

**Đáp án: B**  
*Giải thích: BGP routing information rất quan trọng và cần được deliver đáng tin cậy. TCP (port 179) đảm bảo reliable, in-order delivery. Mất một BGP update có thể gây routing inconsistency nghiêm trọng.*

---

**Câu 99.** "Address aggregation" trong CIDR giúp gì cho Internet routing?

A. Tăng số lượng địa chỉ IP có thể dùng  
B. Giảm kích thước routing table của routers bên ngoài AS — một prefix đại diện cho nhiều subnets  
C. Tăng tốc độ routing  
D. Giúp phân bổ địa chỉ IP công bằng hơn  

**Đáp án: B**  
*Giải thích: Thay vì routers toàn cầu phải biết hàng nghìn prefix nhỏ, ISP advertise một prefix tổng hợp. Ví dụ: 8 tổ chức /23 được gộp thành một /20. Routers ngoài chỉ cần một entry thay vì 8.*

---

**Câu 100.** Sự khác biệt giữa "anycast" (IPv6) và "multicast" là gì?

A. Anycast và multicast giống nhau hoàn toàn  
B. Anycast: packet delivered đến MỘT trong group (node gần nhất); multicast: delivered đến TẤT CẢ trong group  
C. Anycast chỉ dùng trong IPv4, multicast chỉ trong IPv6  
D. Anycast nhanh hơn multicast  

**Đáp án: B**  
*Giải thích: Anycast (IPv6): gửi đến một trong số nodes nhận (thường là gần nhất) — hữu ích cho CDN (chọn mirror gần nhất). Multicast: gửi đến tất cả members của group. Unicast: một destination cố định.*

---

**Câu 101.** Tại sao ICMP được coi là nằm "above IP" trong kiến trúc mạng?

A. Vì ICMP xử lý data ở application layer  
B. Vì ICMP messages được mang trong IP datagrams như payload, tương tự TCP/UDP segments  
C. Vì ICMP chạy trên transport layer  
D. Vì ICMP được xử lý sau khi IP xử lý xong  

**Đáp án: B**  
*Giải thích: ICMP messages là IP payload (protocol number chỉ định ICMP). Khi host nhận IP datagram có ICMP protocol number, nó demultiplex content đến ICMP — giống như demultiplex đến TCP/UDP.*

---

**Câu 102.** Khi một router trong OSPF phát hiện link down, nó làm gì?

A. Chờ 30 phút rồi mới broadcast  
B. Ngay lập tức broadcast link-state advertisement mới đến tất cả routers trong AS  
C. Chỉ thông báo cho neighboring routers  
D. Gửi request đến area border router  

**Đáp án: B**  
*Giải thích: OSPF broadcast link-state info ngay khi có thay đổi link state (cost change, link up/down), không cần đợi. Ngoài ra còn broadcast định kỳ mỗi 30 phút dù không có thay đổi.*

---

**Câu 103.** Giá trị IP broadcast address là bao nhiêu và ý nghĩa của nó?

A. 0.0.0.0 — địa chỉ mặc định  
B. 255.255.255.255 — gửi đến tất cả hosts trong cùng subnet  
C. 127.0.0.1 — loopback address  
D. 224.0.0.1 — all-hosts multicast  

**Đáp án: B**  
*Giải thích: 255.255.255.255 là limited broadcast address. Datagram gửi đến địa chỉ này được deliver đến tất cả hosts trong cùng subnet. Routers optionally có thể forward đến neighboring subnets (thường không).*

---

**Câu 104.** OSPF authentication MD5 hoạt động như thế nào?

A. Mã hóa toàn bộ OSPF packet bằng key chung  
B. Tính MD5 hash của packet + secret key, đính kèm hash để receiver verify; dùng sequence number chống replay  
C. Yêu cầu password trong cleartext trong mỗi packet  
D. Dùng certificate từ CA để ký mỗi packet  

**Đáp án: B**  
*Giải thích: MD5 auth: router tính MD5(packet content + secret key), đặt kết quả vào packet. Receiver tính lại hash và so sánh. Sequence number ngăn replay attack (dùng lại packet cũ đã bắt được).*

---

**Câu 105.** Trong RIP, nếu router không nhận được update từ neighbor trong bao lâu thì coi là neighbor down?

A. 30 giây  
B. 60 giây  
C. 180 giây  
D. 300 giây  

**Đáp án: C**  
*Giải thích: RIP gửi update mỗi 30 giây. Nếu sau 180 giây (6 lần chu kỳ) không nhận được update từ neighbor, neighbor được coi là unreachable. RIP update routing table và propagate thông tin này.*

---

**Câu 106.** "Source quench" ICMP message (type 4) được dùng để làm gì?

A. Báo lỗi destination unreachable  
B. Yêu cầu source giảm tốc độ truyền khi router bị congested  
C. Reset kết nối TCP  
D. Xác nhận nhận được packet  

**Đáp án: B**  
*Giải thích: Source quench message: router congested gửi về source để yêu cầu giảm transmission rate. Tuy nhiên ít dùng trong thực tế vì TCP đã có congestion control riêng ở transport layer.*

---

**Câu 107.** Subnet 10.0.0.0/8 được dành cho mục đích gì?

A. Địa chỉ của routers backbone Internet  
B. Private network address — chỉ có ý nghĩa trong mạng nội bộ, không routable trên Internet  
C. Địa chỉ dành cho các nhà cung cấp dịch vụ  
D. Địa chỉ experimental không được sử dụng  

**Đáp án: B**  
*Giải thích: RFC 1918 dành 10.0.0.0/8, 172.16.0.0/12, và 192.168.0.0/16 cho private networks. Packets với địa chỉ này không được route trên Internet công cộng. Dùng phổ biến trong home/office networks với NAT.*

---

**Câu 108.** Khi nói "routing algorithm computes forwarding table", forwarding table dùng để làm gì?

A. Lưu toàn bộ topology của mạng  
B. Mapping destination address (hoặc prefix) → outgoing interface/next-hop để forward packet  
C. Lưu lịch sử routing  
D. Kiểm soát access vào mạng  

**Đáp án: B**  
*Giải thích: Forwarding table: mỗi entry là (destination prefix, outgoing interface hoặc next-hop address). Khi packet đến, router tra forwarding table bằng longest prefix match để quyết định nơi gửi tiếp.*

---

**Câu 109.** Điều gì xảy ra với IPv6 datagram quá lớn khi đến router IPv6?

A. Router tự động fragment datagram  
B. Router drop datagram và gửi "Packet Too Big" ICMPv6 về source  
C. Router giữ datagram cho đến khi tìm được MTU phù hợp  
D. Router chuyển đổi sang IPv4 để xử lý  

**Đáp án: B**  
*Giải thích: IPv6 không cho phép fragmentation tại routers. Khi packet quá lớn, router drop và gửi ICMPv6 "Packet Too Big" về source. Source resend với kích thước nhỏ hơn (path MTU discovery).*

---

**Câu 110.** Tại sao "flag day" để chuyển đổi toàn bộ Internet từ IPv4 sang IPv6 không khả thi?

A. Vì không có đủ IPv6 addresses  
B. Vì hàng triệu thiết bị và admin không thể đồng thời nâng cấp, ngay cả khi Internet còn nhỏ điều này đã là bất khả thi  
C. Vì IPv6 không tương thích với các ứng dụng hiện tại  
D. Vì IPv6 quá đắt để triển khai  

**Đáp án: B**  
*Giải thích: Internet hiện có hàng trăm triệu hosts và hàng triệu admins. Kể cả khi Internet còn nhỏ (những năm 1980, chuyển NCP→TCP), flag day đã không khả thi. Giải pháp: dual-stack và tunneling.*

---

**Câu 111.** "Autonomous System Number" (ASN) do ai cấp phát?

A. Các ISP lớn tự phân công  
B. ICANN và các regional Internet registries (ARIN, RIPE, APNIC, LACNIC)  
C. IETF qua RFC  
D. ITU (International Telecommunication Union)  

**Đáp án: B**  
*Giải thích: ASN được quản lý bởi ICANN và cấp phát qua các regional Internet registries (RIRs): ARIN (Bắc Mỹ), RIPE (Châu Âu), APNIC (Châu Á-Thái Bình Dương), LACNIC (Mỹ Latinh).*

---

**Câu 112.** Trong DV algorithm, node x biết thông tin gì về mạng?

A. Toàn bộ topology  
B. Chi phí link trực tiếp đến neighbors, distance vector của mình, và distance vectors của các neighbors  
C. Chỉ chi phí link trực tiếp  
D. Routing table của tất cả nodes trong mạng  

**Đáp án: B**  
*Giải thích: Mỗi node x duy trì: (1) c(x,v) — cost đến mỗi neighbor v trực tiếp; (2) Dx = [Dx(y)] — distance vector của x đến mọi node y; (3) Dv = [Dv(y)] — distance vector của mỗi neighbor v.*

---

**Câu 113.** Trong BGP, khi nào một router "filter" (từ chối) một route advertisement?

A. Khi AS-PATH rỗng  
B. Khi ASN của router xuất hiện trong AS-PATH (phát hiện loop), hoặc theo import policy  
C. Khi route có cost quá cao  
D. Khi route đến từ iBGP session  

**Đáp án: B**  
*Giải thích: Router từ chối route nếu: (1) ASN của mình trong AS-PATH (ngăn routing loop); (2) import policy quyết định không chấp nhận (policy-based filtering); (3) đã biết route tốt hơn đến cùng prefix.*

---

**Câu 114.** Khi router xử lý IP datagram, thứ tự kiểm tra nào đúng?

A. Kiểm tra destination address → tra forwarding table → forward  
B. Kiểm tra checksum → kiểm tra TTL → tra forwarding table → decrement TTL → recompute checksum → forward  
C. Decrement TTL → kiểm tra checksum → tra forwarding table → forward  
D. Tra forwarding table → kiểm tra checksum → kiểm tra TTL → forward  

**Đáp án: B**  
*Giải thích: Router: (1) verify header checksum; (2) check TTL (nếu = 0, drop + ICMP TTL expired); (3) tra forwarding table bằng destination address; (4) decrement TTL; (5) recompute checksum; (6) forward.*

---

**Câu 115.** Trong OSPF, "area border router" có chức năng gì?

A. Kết nối OSPF với BGP  
B. Route packets đến destinations ngoài area của nó, kết nối area với backbone  
C. Cấp phát địa chỉ IP trong area  
D. Theo dõi trạng thái của tất cả links trong area  

**Đáp án: B**  
*Giải thích: Area border router: có interfaces trong cả area và backbone. Routing inter-area: packet đi intra-area → area border router → backbone → area border router đích → intra-area đích.*

---

**Câu 116.** Mục đích của "DHCP relay agent" là gì?

A. Caching DHCP responses để tăng tốc  
B. Cho phép DHCP client trên subnet không có DHCP server tìm được DHCP server trên subnet khác  
C. Backup cho DHCP server chính  
D. Bảo mật DHCP traffic  

**Đáp án: B**  
*Giải thích: Nếu subnet không có DHCP server, router (relay agent) forward DHCP Discover broadcast từ client đến DHCP server trên subnet khác. Giúp dùng một DHCP server cho nhiều subnets.*

---

**Câu 117.** Sự khác biệt giữa "static routing" và "dynamic routing algorithm" là gì?

A. Static dùng IPv4, dynamic dùng IPv6  
B. Static: routes thay đổi rất chậm (thường do human); dynamic: routes tự động thay đổi theo topology/traffic  
C. Static nhanh hơn, dynamic chính xác hơn  
D. Static dùng LS, dynamic dùng DV  

**Đáp án: B**  
*Giải thích: Static routing: admin cấu hình thủ công, ít thay đổi. Dynamic routing: algorithm tự tính và cập nhật routes khi topology hoặc link cost thay đổi — responsive hơn nhưng dễ bị oscillation và routing loop hơn.*

---

**Câu 118.** Tại sao Internet chưa hoàn toàn chuyển sang IPv6 dù đã được phát triển từ những năm 1990?

A. IPv6 có lỗi kỹ thuật chưa được sửa  
B. Chi phí chuyển đổi cao, thiếu backward compatibility hoàn toàn, và network-layer changes rất khó thực hiện  
C. IPv4 đã đủ địa chỉ nhờ NAT  
D. Chính phủ các nước cấm dùng IPv6  

**Đáp án: B**  
*Giải thích: "Thay đổi network-layer protocol giống như thay nền móng nhà." NAT giúp gia hạn IPv4. Dual-stack và tunneling là giải pháp trung gian. Thay đổi application layer dễ hơn nhiều (Web, messaging ra đời nhanh).*

---

**Câu 119.** Trong "limited-scope flooding" của Gnutella, TTL field được dùng như thế nào?

A. Để xác định thứ tự ưu tiên của query  
B. Để giới hạn số hops mà flooded query sẽ được forward — TTL giảm mỗi hop, đến 0 thì stop  
C. Để timestamp query  
D. Để nhận dạng loại query  

**Đáp án: B**  
*Giải thích: Gnutella dùng TTL giống IP TTL. Mỗi peer khi forward query sẽ decrement TTL. Khi TTL = 0, query bị drop. Điều này giới hạn flood chỉ trong một số hops nhất định quanh initiator.*

---

**Câu 120.** Trong multicast, tại sao không thể đặt địa chỉ của tất cả receivers trong mỗi multicast packet?

A. Vì router không đọc được nhiều địa chỉ  
B. Với hàng trăm/nghìn receivers, overhead địa chỉ sẽ lớn hơn data; và sender cần biết địa chỉ tất cả receivers  
C. Vì IP header chỉ có 1 địa chỉ nguồn và 1 đích  
D. Vì địa chỉ receivers thay đổi liên tục  

**Đáp án: B**  
*Giải thích: Giải pháp: address indirection — dùng một Class D multicast group address thay cho danh sách receivers. Packet gửi đến group address được deliver đến tất cả members. Giải quyết cả scalability lẫn privacy.*

---

**Câu 121.** Hệ thống IDS (Intrusion Detection System) khác firewall ở điểm gì?

A. IDS chặn traffic, firewall chỉ theo dõi  
B. IDS thực hiện "deep packet inspection" — kiểm tra cả payload, dùng signature database; firewall chỉ kiểm tra header  
C. IDS hoạt động ở link layer, firewall ở network layer  
D. IDS và firewall hoàn toàn giống nhau  

**Đáp án: B**  
*Giải thích: Firewall: kiểm tra header fields (IP, port), block suspicious packets. IDS: "deep packet inspection" — kiểm tra cả application-layer payload, so sánh với attack signature database, tạo alert (không block). IPS = IDS + blocking.*

---

**Câu 122.** Trong OSPF, link weights do ai quyết định và theo tiêu chí gì?

A. Tự động tính theo bandwidth  
B. Network administrator cấu hình — có thể dựa trên link capacity, delay, cost, hoặc traffic engineering goals  
C. OSPF protocol tự tính theo RTT  
D. BGP cung cấp cho OSPF  

**Đáp án: B**  
*Giải thích: OSPF không mandate cách đặt link weights. Admin có thể đặt: tất cả bằng 1 (minimum hop), tỷ lệ nghịch với bandwidth (ưu tiên link nhanh), hoặc reverse-engineer weights để đạt traffic engineering goal.*

---

**Câu 123.** Khi một host muốn join multicast group, trình tự IGMP diễn ra như thế nào?

A. Host gửi join request đến multicast server  
B. Host gửi membership_report đến first-hop router (có thể tự phát hoặc sau membership_query)  
C. Host broadcast đến toàn mạng  
D. Host liên hệ ICANN để đăng ký  

**Đáp án: B**  
*Giải thích: Host muốn join group: gửi IGMP membership_report đến first-hop router (không cần đợi query). Router biết có host trong group, bắt đầu tham gia multicast routing cho group đó.*

---

**Câu 124.** Graph abstraction trong routing: nodes đại diện cho gì và edges đại diện cho gì?

A. Nodes = hosts, edges = switches  
B. Nodes = routers, edges = physical links giữa các routers  
C. Nodes = subnets, edges = routers  
D. Nodes = AS, edges = BGP sessions  

**Đáp án: B**  
*Giải thích: Trong mô hình graph để formulate routing problem: nodes N = routers (điểm quyết định forward), edges E = physical links giữa routers. Edge có cost (phản ánh length, speed, monetary cost).*

---

**Câu 125.** Khi BGP advertise một prefix, thông tin gì được truyền đi cùng với prefix đó?

A. Chỉ prefix address  
B. Prefix cùng với BGP attributes (AS-PATH, NEXT-HOP, local preference, và các attributes khác) — gọi là "route"  
C. Prefix và full routing table  
D. Prefix và danh sách tất cả hosts trong subnet đó  

**Đáp án: B**  
*Giải thích: Trong BGP, "route" = prefix + attributes. Hai attributes quan trọng nhất: AS-PATH (các AS đã đi qua) và NEXT-HOP (router interface bắt đầu AS-PATH). Router dùng attributes để chọn best route.*

---

**Câu 126.** Spanning tree trong broadcast routing: điều kiện để một graph G' = (N, E') là spanning tree của G = (N, E) là gì?

A. E' phải bằng E và G' connected  
B. E' ⊆ E, G' connected, G' không có cycle, và G' chứa tất cả nodes của G  
C. G' phải là minimum spanning tree  
D. E' phải chứa tất cả edges của E  

**Đáp án: B**  
*Giải thích: Spanning tree G' = (N, E'): (1) E' là subset của E; (2) connected — có path giữa mọi cặp nodes; (3) acyclic — không có cycle; (4) chứa tất cả nodes N. Minimum spanning tree: spanning tree có tổng edge cost nhỏ nhất.*

---

**Câu 127.** Điểm yếu của poisoned reverse trong giải quyết count-to-infinity problem là gì?

A. Poisoned reverse hoàn toàn không hiệu quả  
B. Chỉ ngăn được loop giữa 2 neighboring nodes; loop 3+ nodes vẫn không bị phát hiện  
C. Poisoned reverse tạo ra quá nhiều control traffic  
D. Chỉ hoạt động với RIP, không với OSPF  

**Đáp án: B**  
*Giải thích: Poisoned reverse hiệu quả với loop 2 nodes (Z route đến X qua Y, quảng bá Dz(X)=∞ cho Y). Nhưng với loop 3+ nodes (A→B→C→A), không node nào nhận ra toàn bộ vòng lặp.*

---

**Câu 128.** DVMRP (Distance-Vector Multicast Routing Protocol) sử dụng kỹ thuật gì?

A. Center-based shared tree  
B. Source-based trees với reverse path forwarding và pruning  
C. Spanning tree broadcast  
D. Sequence-number-controlled flooding  

**Đáp án: B**  
*Giải thích: DVMRP là multicast protocol đầu tiên trong Internet, dùng source-based trees với RPF (Reverse Path Forwarding) và pruning để loại bỏ các nhánh không có group members.*

---

**Câu 129.** Tại sao trong OSPF, một router cần periodic re-broadcast LSA (mỗi 30 phút) dù không có thay đổi?

A. Để sync với router neighbors  
B. Để tăng robustness — ngăn LSA cũ bị xóa do timeout, đảm bảo mọi router đều có state mới nhất  
C. Vì RFC yêu cầu như vậy  
D. Để reset sequence numbers  

**Đáp án: B**  
*Giải thích: LSA có age field — tăng dần theo thời gian. Periodic re-broadcast ngăn LSA bị coi là "too old" và bị xóa. RFC 2328 ghi rõ: "periodic updating adds robustness to the link state algorithm."*

---

**Câu 130.** Khi hai BGP routes có cùng local preference và cùng AS-PATH length, tiêu chí nào được áp dụng tiếp theo?

A. Chọn route có AS-PATH string nhỏ hơn về mặt alphabetical  
B. Hot-potato routing: chọn route có NEXT-HOP gần nhất (chi phí intra-AS nhỏ nhất)  
C. Chọn route đến từ eBGP session (ưu tiên hơn iBGP)  
D. Chọn ngẫu nhiên  

**Đáp án: B**  
*Giải thích: Tiebreaker thứ 3 trong BGP route selection: hot-potato routing — chọn route có NEXT-HOP router mà chi phí intra-AS (theo OSPF) là nhỏ nhất. AS muốn "tống khứ" traffic càng sớm càng tốt.*

---

**Câu 131.** Trong mạng point-to-point giữa hai routers, subnet này có bao nhiêu host addresses?

A. 0 — chỉ có router interfaces  
B. Tùy thuộc subnet mask  
C. 2 — hai router interfaces đó là 2 "hosts"  
D. 254 — standard subnet  

**Đáp án: A**  
*Giải thích: Subnet giữa hai router interfaces trên point-to-point link chỉ có 2 địa chỉ (2 router interfaces), không có host nào khác. Tuy nhiên, theo định nghĩa IP, đây vẫn là một subnet riêng.*

---

**Câu 132.** "Load-sensitive" routing algorithm có ưu và nhược điểm gì?

A. Ưu: đơn giản; Nhược: không tối ưu  
B. Ưu: tránh congested links; Nhược: dễ bị oscillation, routers có thể đồng loạt thay đổi route  
C. Ưu: tốc độ; Nhược: tốn bộ nhớ  
D. Ưu: bảo mật; Nhược: chậm  

**Đáp án: B**  
*Giải thích: Load-sensitive: link cost phản ánh congestion. Ưu: traffic tránh link tắc nghẽn. Nhược: tất cả routers cùng thấy congestion → đồng loạt chuyển route → congestion nơi mới → oscillation. RIP, OSPF, BGP là load-insensitive.*

---

**Câu 133.** Một router trong DV algorithm nhận distance vector update từ neighbor. Khi nào nó sẽ gửi update cho các neighbors của mình?

A. Luôn luôn gửi sau mỗi lần nhận update  
B. Chỉ khi distance vector của chính nó thay đổi sau khi tính lại  
C. Sau mỗi 30 giây  
D. Khi có người dùng yêu cầu  

**Đáp án: B**  
*Giải thích: Node x gửi updated Dx cho neighbors chỉ khi Dx(y) thay đổi cho ít nhất một destination y. Nếu không có thay đổi (update từ neighbor không ảnh hưởng), node không gửi gì — giảm overhead.*

---

**Câu 134.** Trong ví dụ NAT, host 10.0.0.1 gửi request từ port 3345, NAT thay đổi gì khi gửi ra Internet?

A. Chỉ thay đổi source IP address  
B. Thay source IP (10.0.0.1 → 138.76.29.7) và source port (3345 → 5001 mới), lưu mapping vào NAT table  
C. Thay đổi destination port  
D. Thay cả source và destination IP  

**Đáp án: B**  
*Giải thích: NAT thay: source IP = WAN IP của NAT router, source port = new port (NAT chọn). Lưu mapping: (WAN IP 138.76.29.7, port 5001) ↔ (LAN IP 10.0.0.1, port 3345). Web server chỉ thấy WAN IP.*

---

**Câu 135.** Hạn chế của "N-way-unicast" cho broadcast phát sinh vấn đề gì với link-state routing?

A. N-way-unicast quá phức tạp cho link-state  
B. Circular dependency: link-state dùng broadcast để build unicast routes, nhưng N-way-unicast cần unicast routes có sẵn  
C. N-way-unicast không hỗ trợ link-state metrics  
D. Link-state cần broadcast faster hơn N-way-unicast có thể cung cấp  

**Đáp án: B**  
*Giải thích: N-way-unicast cần unicast routing infrastructure sẵn có. Nhưng link-state routing dùng broadcast để phổ biến LSA để tính unicast routes — vòng tròn phụ thuộc. Phải dùng các cơ chế broadcast khác (RPF, spanning tree).*

---

**Câu 136.** Khi Internet routing table của một router có entry (138.16.64/22, port 7), điều đó có nghĩa là gì?

A. Gửi packet đến 138.16.64/22 qua port 7  
B. Mọi packet có destination address match prefix 138.16.64/22 được forward ra interface (port) 7  
C. 138.16.64/22 là địa chỉ của router connected ở port 7  
D. Port 7 là reserved cho subnet 138.16.64/22  

**Đáp án: B**  
*Giải thích: Forwarding table entry (prefix, output port): khi packet đến với destination IP match prefix 138.16.64/22, router forward ra output interface 7. Dùng longest prefix match nếu nhiều entries match.*

---

**Câu 137.** Source quench ICMP message ít được dùng trong thực tế vì lý do gì?

A. Vì nó không hoạt động đúng về mặt kỹ thuật  
B. Vì TCP đã có congestion control riêng ở transport layer, không cần network-layer feedback  
C. Vì routers không đủ memory để gửi source quench  
D. Vì source quench không được hỗ trợ trong IPv6  

**Đáp án: B**  
*Giải thích: TCP có congestion control (slow start, congestion avoidance) hoạt động ở transport layer mà không cần ICMP source quench. Thêm vào đó, source quench có thể bị lợi dụng để tấn công.*

---

**Câu 138.** Tại sao "administrative autonomy" là một trong những lý do cần Autonomous Systems?

A. Vì mỗi quốc gia có luật internet khác nhau  
B. Tổ chức muốn tự chọn routing protocol nội bộ và ẩn cấu trúc mạng nội bộ khỏi thế giới bên ngoài  
C. Vì không có routing protocol nào đủ mạnh cho toàn Internet  
D. Vì giới hạn phần cứng của router  

**Đáp án: B**  
*Giải thích: Administrative autonomy: công ty/ISP muốn (1) tự chọn routing protocol nội bộ, (2) ẩn topology nội bộ, (3) tự quyết định traffic policy, trong khi vẫn kết nối với Internet qua inter-AS protocol (BGP).*

---

**Câu 139.** Khi nói về LS algorithm, "link-state broadcast" là gì và tại sao cần thiết?

A. Broadcast quảng cáo địa chỉ IP mới  
B. Mỗi node broadcast thông tin về các links trực tiếp của mình đến mọi node khác, để mọi node có complete map  
C. Broadcast routing table toàn bộ  
D. Broadcast để tìm neighbor nodes  

**Đáp án: B**  
*Giải thích: LS algorithm cần complete, global knowledge. Cách thu thập: mỗi node broadcast "link-state packet" chứa danh sách và chi phí các links trực tiếp của nó. Sau broadcast, tất cả nodes có identical, complete network map.*

---

**Câu 140.** Trong multicast RPF với pruning, "prune message" được gửi khi nào và đi theo chiều nào?

A. Khi router join group, gửi downstream  
B. Khi router nhận multicast packet nhưng không có host nào trong group, gửi upstream  
C. Khi router bị tắt, gửi broadcast  
D. Khi link down, gửi đến tất cả neighbors  

**Đáp án: B**  
*Giải thích: Multicast router nhận packet nhưng không có attached hosts trong group → gửi prune message upstream (về phía source). Upstream router nhận prune từ tất cả downstream → gửi prune tiếp upstream, stop forward đến nhánh đó.*

---

**Câu 141.** Tại sao OSPF được gọi là "Open" Shortest Path First?

A. Vì thuật toán routing hoàn toàn mở (open-source)  
B. Vì routing protocol specification được công bố công khai (không phải proprietary)  
C. Vì OSPF cho phép mọi traffic đi qua  
D. Vì OSPF không yêu cầu authentication  

**Đáp án: B**  
*Giải thích: "Open" trong OSPF nghĩa là protocol specification được công bố công khai (RFC 2328), không phải proprietary (ví dụ: Cisco's EIGRP là proprietary). Bất kỳ ai cũng có thể implement OSPF.*

---

**Câu 142.** Một datagram có identification number 777, offset 185, flag 1. Đây là loại fragment nào?

A. Fragment đầu tiên  
B. Fragment cuối cùng  
C. Fragment ở giữa (không phải đầu, không phải cuối)  
D. Datagram không bị fragment  

**Đáp án: C**  
*Giải thích: offset ≠ 0 (không phải fragment đầu); flag = 1 (còn fragment tiếp, chưa phải cuối). Vậy đây là fragment ở giữa. offset = 185 → dữ liệu bắt đầu tại byte 185×8 = 1480.*

---

**Câu 143.** Khi host kết nối mạng mới, DHCP cấp IP "lease" thay vì permanent. Điều này có lợi gì?

A. Giảm tải cho DHCP server  
B. Cho phép tái sử dụng địa chỉ IP — khi host rời mạng, IP được trả lại pool và cấp cho host khác  
C. Tăng bảo mật  
D. Giảm traffic trên mạng  

**Đáp án: B**  
*Giải thích: DHCP lease với expiration time cho phép ISP/tổ chức quản lý pool nhỏ hơn tổng số users. Ví dụ: ISP với 2000 customers nhưng tối đa 400 online cùng lúc → cần pool khoảng 512 địa chỉ thay vì 2048.*

---

**Câu 144.** Tại sao IPv6 thêm "anycast" address type không có trong IPv4?

A. Để thay thế multicast  
B. Để hỗ trợ use case gửi đến một trong nhiều servers (server gần nhất) — hữu ích cho CDN và load balancing  
C. Vì IPv4 address space đã hết  
D. Để tương thích với IPv4 broadcast  

**Đáp án: B**  
*Giải thích: Anycast: packet delivered đến bất kỳ một node nào trong nhóm anycast (thường là gần nhất). Use case điển hình: HTTP GET đến mirror server gần nhất trong CDN. IPv4 không có native anycast.*

---

**Câu 145.** Sự khác biệt về cách tính checksum giữa IPv4 header checksum và TCP/UDP checksum là gì?

A. Không có sự khác biệt  
B. IPv4 checksum chỉ bao phủ IP header; TCP/UDP checksum bao phủ toàn bộ segment  
C. IPv4 dùng CRC, TCP/UDP dùng 1s complement  
D. IPv4 dùng MD5, TCP/UDP dùng SHA  

**Đáp án: B**  
*Giải thích: IP header checksum: chỉ bảo vệ header (không có data). TCP/UDP checksum: bảo phủ cả header lẫn data của segment. Đây là một lý do có redundancy — cả hai layer đều check errors.*

---

**Câu 146.** Khi xem xét "message complexity" của LS vs DV algorithm, LS cần bao nhiêu messages?

A. O(|N|) messages  
B. O(|N| × |E|) messages (mỗi node broadcast cost của mỗi link đến tất cả nodes)  
C. O(|E|) messages  
D. O(|N|²) messages  

**Đáp án: B**  
*Giải thích: LS: mỗi node broadcast link costs cho tất cả nodes. Mỗi node có nhiều links, tổng O(|N| × |E|) messages. DV: chỉ trao đổi với directly connected neighbors, nhưng convergence time phụ thuộc vào topology.*

---

**Câu 147.** Trong RIP, "hop" được định nghĩa là gì cụ thể?

A. Số routers phải đi qua  
B. Số subnets phải traverse từ source router đến destination subnet (bao gồm destination subnet)  
C. Số links phải đi qua  
D. Số AS phải đi qua  

**Đáp án: B**  
*Giải thích: RIP "hop" = số subnets traversed từ source router đến destination subnet, bao gồm cả destination subnet. Khác với "hop" theo nghĩa thông thường (số routers). Max RIP hops = 15; cost = 16 là ∞.*

---

**Câu 148.** Khi một IDS phát hiện attack signature trong packet payload, nó làm gì? Và IPS khác IDS thế nào?

A. IDS và IPS cùng block packet ngay lập tức  
B. IDS tạo alert (không block); IPS = IDS + blocking packets  
C. IDS forward packet đến security team; IPS drop packet  
D. IDS và IPS giống nhau hoàn toàn  

**Đáp án: B**  
*Giải thích: IDS: deep packet inspection, so sánh với signature database, tạo alert khi match. Không tự block. IPS (Intrusion Prevention System): như IDS nhưng còn actively block packets khi phát hiện attack.*

---

**Câu 149.** Tại sao BGP peers cần "semi-permanent" TCP connections thay vì tạo connection mới cho mỗi update?

A. Vì TCP khởi tạo connection rất chậm  
B. BGP sessions kéo dài liên tục; semi-permanent connection tránh overhead setup mới, giữ state về BGP neighbors  
C. Vì BGP chỉ hỗ trợ một kết nối tại một thời điểm  
D. Vì firewall không cho phép BGP tạo nhiều connections  

**Đáp án: B**  
*Giải thích: BGP cần liên tục trao đổi routing updates. Semi-permanent TCP connection (BGP session) hoạt động liên tục, giữ state giữa peers. Nếu connection down, routers ngừng nhận updates từ peer đó — ảnh hưởng routing.*

---

**Câu 150.** Nhìn tổng thể, lesson nào có thể rút ra từ quá trình triển khai IPv6?

A. Các tiêu chuẩn kỹ thuật mới được adopt rất nhanh  
B. Thay đổi network-layer protocol cực kỳ khó khăn; application-layer innovations (Web, P2P) triển khai nhanh hơn nhiều  
C. Internet cần được thiết kế lại hoàn toàn  
D. Chính phủ nên kiểm soát việc triển khai protocol mới  

**Đáp án: B**  
*Giải thích: IPv6 phát triển từ đầu những năm 1990 nhưng đến nay vẫn chưa hoàn toàn thay thế IPv4. Ngược lại: Web, instant messaging, P2P, streaming được triển khai rất nhanh. "Thay network-layer protocol = thay nền móng nhà; thay application-layer = sơn lại tường."*

---

*Hết bộ câu hỏi — 150 câu bao phủ: IP Protocol (4.4), Routing Algorithms (4.5), Routing in the Internet (4.6), Broadcast & Multicast Routing (4.7)*
