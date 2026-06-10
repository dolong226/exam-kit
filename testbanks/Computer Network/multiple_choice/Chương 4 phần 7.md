# Bộ Câu Hỏi Trắc Nghiệm: Network Layer (Chương 4)
## Phạm vi: IP Protocol, Routing Algorithms, Routing in the Internet, Broadcast & Multicast


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

