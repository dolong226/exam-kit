# Bộ Câu Hỏi Trắc Nghiệm: Network Layer (Chương 4)
## Phạm vi: IP Protocol, Routing Algorithms, Routing in the Internet, Broadcast & Multicast

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
