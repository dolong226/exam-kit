# Bộ Câu Hỏi Trắc Nghiệm: Network Layer (Chương 4)
## Phạm vi: IP Protocol, Routing Algorithms, Routing in the Internet, Broadcast & Multicast

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
