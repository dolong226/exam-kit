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
