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
