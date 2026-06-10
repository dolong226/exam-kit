# Chương 4: Network Layer — Bộ câu hỏi ôn tập

-
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
