# Bộ câu hỏi trắc nghiệm — Chương 1: Computer Networks and the Internet

## Phần 10 — Lịch sử mạng máy tính

---

**Câu 77.** *(Dễ)* ARPAnet — tiền thân của Internet — được phát triển bởi cơ quan nào?

A. NASA  
B. IEEE  
C. ARPA (Advanced Research Projects Agency), Bộ Quốc phòng Mỹ  
D. AT&T Bell Labs  

> **Đáp án: C**  
> **ARPAnet** được phát triển dưới sự tài trợ của **DARPA** (Defense Advanced Research Projects Agency). Packet switch đầu tiên được lắp đặt tại UCLA năm 1969.

---

**Câu 78.** *(Dễ)* World Wide Web được phát minh bởi ai và ở đâu?

A. Bill Gates tại Microsoft  
B. Tim Berners-Lee tại CERN (1989-1991)  
C. Marc Andreessen tại UIUC  
D. Vint Cerf tại DARPA  

> **Đáp án: B**  
> **Tim Berners-Lee** tại **CERN** phát triển Web (1989-1991) — bao gồm HTML, HTTP, web server, và browser đầu tiên. Khác với việc phát minh Internet (ARPAnet).

---

**Câu 79.** *(Trung bình)* Ai được ghi nhận là người phát minh packet switching và đóng góp lý thuyết gì?

A. Vint Cerf — phát triển TCP/IP  
B. Leonard Kleinrock — dùng queuing theory chứng minh hiệu quả của packet switching cho bursty traffic  
C. Tim Berners-Lee — phát triển HTTP  
D. Robert Kahn — thiết kế ARPAnet  

> **Đáp án: B**  
> **Leonard Kleinrock** (MIT) là người đầu tiên công bố công trình về packet switching, dùng **queuing theory** để chứng minh hiệu quả cho bursty traffic. Packet switch đầu tiên lắp tại UCLA dưới sự giám sát của ông.

---

**Câu 80.** *(Trung bình)* TCP/IP trở thành giao thức chuẩn của ARPAnet vào ngày nào, và có gì đặc biệt về sự kiện này?

A. 1/1/1980 — chuyển đổi từng bước trong 5 năm  
B. 1/1/1983 — "flag day" event: tất cả hosts đồng loạt chuyển từ NCP sang TCP/IP  
C. 1/1/1990 — sau khi WWW được phát minh  
D. 1/1/1995 — khi NSFNET bị giải thể  

> **Đáp án: B**  
> Ngày **1/1/1983** là **"flag day"**: toàn bộ hosts trên ARPAnet buộc phải chuyển sang TCP/IP cùng một lúc — không có giai đoạn chuyển tiếp. Đây là cột mốc hình thành Internet hiện đại.

---

## Phần 11 — Câu hỏi tổng hợp & tư duy

---

**Câu 81.** *(Trung bình)* Tại sao Internet applications chạy trên **end systems** chứ không chạy trong **packet switches**?

A. Vì packet switches không đủ bộ nhớ để chạy ứng dụng  
B. Vì packet switches chỉ quan tâm đến việc chuyển tiếp packet — không biết và không cần biết ứng dụng là gì; intelligence được đặt ở rìa mạng  
C. Vì ứng dụng cần kết nối trực tiếp với người dùng  
D. Vì packet switches chạy một hệ điều hành khác  

> **Đáp án: B**  
> Đây là nguyên lý **end-to-end argument** của Internet: complexity nằm ở edges (end systems), không ở core (packet switches). Core chỉ làm forwarding đơn giản → linh hoạt và scalable hơn.

---

**Câu 82.** *(Trung bình)* Nếu traffic intensity La/R = 0 (gần không), queuing delay sẽ như thế nào?

A. Queuing delay rất lớn  
B. Queuing delay gần bằng 0, vì packets hiếm khi tìm thấy packet nào trong queue  
C. Queuing delay bằng transmission delay  
D. Queuing delay không xác định được  

> **Đáp án: B**  
> Khi La/R → 0: packet arrivals rất thưa, hầu như không bao giờ tìm thấy packet nào trong queue → **queuing delay ≈ 0**. Ngược lại khi La/R → 1, queuing delay → ∞.

---

**Câu 83.** *(Trung bình)* Trong ví dụ Traceroute, tại sao RTT đến Router 6 có thể lớn hơn RTT đến Router 7 (router xa hơn)?

A. Vì Router 7 nhanh hơn Router 6  
B. Vì queuing delay tại router biến thiên theo thời gian — packet đến Router 6 có thể gặp queue dài hơn packet sau đó đến Router 7  
C. Vì Traceroute đo sai  
D. Vì Router 6 ở xa hơn về mặt địa lý  

> **Đáp án: B**  
> Traceroute gửi các packet N theo thứ tự thời gian — **queuing delay** tại mỗi router thay đổi giữa các lần đo. Packet đến Router 6 gặp congestion nhiều hơn packet sau đó đến Router 7.

---

**Câu 84.** *(Trung bình)* Khi nhiều users cùng tải file từ cùng một server qua một **shared bottleneck link**, điều gì xảy ra với throughput của mỗi user?

A. Mỗi user vẫn nhận được throughput tối đa  
B. Throughput của mỗi user giảm xuống vì bandwidth bottleneck link bị chia sẻ cho nhiều flows  
C. Chỉ user kết nối đầu tiên nhận được throughput đầy đủ  
D. Throughput không thay đổi vì routers tự cân bằng  

> **Đáp án: B**  
> Bottleneck link với capacity R chia đều cho N downloads → mỗi user chỉ nhận **R/N** nếu R là ràng buộc hẹp nhất. Đây là lý do tại sao throughput thực tế thường thấp hơn tốc độ access link.

---

**Câu 85.** *(Khó)* Tại sao packet switching không phù hợp với **real-time applications** (như video call) theo lập luận của những người phản đối?

A. Vì packet switching không hỗ trợ video codec  
B. Vì queuing delay trong packet switching biến thiên và không dự đoán được (variable/unpredictable), gây jitter ảnh hưởng đến chất lượng real-time  
C. Vì packet switching có tốc độ thấp hơn circuit switching  
D. Vì packet switching không đảm bảo packet đến đúng thứ tự  

> **Đáp án: B**  
> Đối với real-time apps (VoIP, video conference), **jitter** (biến động delay) là vấn đề lớn hơn delay tuyệt đối. Circuit switching đảm bảo delay ổn định, nhưng packet switching có queuing delay biến thiên.

---

**Câu 86.** *(Khó)* Tại sao "botnet" lại đặc biệt nguy hiểm trong các cuộc tấn công mạng?

A. Vì botnet dùng mã hóa không thể bẻ phá  
B. Vì attacker kiểm soát hàng nghìn compromised hosts — aggregate traffic đủ để tấn công DDoS hiệu quả, đồng thời traffic đến từ nhiều địa chỉ IP khác nhau nên khó block  
C. Vì botnet tấn công tầng vật lý của mạng  
D. Vì botnet tự động vá lỗi của chính nó  

> **Đáp án: B**  
> **Botnet** kết hợp sức mạnh của hàng nghìn hosts → (1) **aggregate bandwidth** đủ lớn để flood target; (2) **phân tán nhiều IP** → khó filter; (3) khó truy tìm attacker thực sự.

---

**Câu 87.** *(Khó)* Bài tập: Gửi 3 packets, mỗi packet L bits, từ source qua 1 router đến destination, link rate R bps. Sử dụng store-and-forward. Tổng thời gian để destination nhận **cả 3 packets** là bao nhiêu?

A. 3L/R  
B. 4L/R  
C. 6L/R  
D. 2L/R  

> **Đáp án: B**  
> Phân tích theo pipeline: t=L/R: router nhận xong P1, bắt đầu forward P1 và source gửi P2. t=2L/R: destination nhận P1, router nhận xong P2. t=3L/R: destination nhận P2, router nhận xong P3. t=4L/R: destination nhận P3. Tổng = **4L/R**.

---

**Câu 88.** *(Khó)* Tại sao chi phí lao động lắp đặt (installation labor cost) thường quan trọng hơn chi phí vật liệu cáp (physical medium cost)?

A. Vì vật liệu cáp rất đắt  
B. Vì chi phí lao động lắp đặt có thể cao hơn gấp bậc (orders of magnitude) so với chi phí vật liệu — dẫn đến việc builders thường lắp cả nhiều loại cáp ngay từ đầu  
C. Vì vật liệu cáp không có giá trị tái sử dụng  
D. Vì labor cost cố định còn material cost biến thiên  

> **Đáp án: B**  
> Đây là lý giải thực tiễn: vì labor cost cao, nhiều builders lắp sẵn twisted pair + fiber + coaxial vào mọi phòng — dù hiện tại chỉ dùng một loại, khi cần upgrade không phải lắp lại dây.

---

## Phần 12 — Câu hỏi phân tích và so sánh

---

**Câu 89.** *(Trung bình)* So sánh: Đặc điểm nào phân biệt rõ nhất packet switching với circuit switching?

A. Packet switching nhanh hơn về tốc độ vật lý  
B. Packet switching phân bổ tài nguyên theo nhu cầu (on-demand), không dành riêng trước; circuit switching dành riêng tài nguyên cho toàn bộ thời gian connection  
C. Circuit switching không hỗ trợ digital data  
D. Packet switching không thể xử lý voice traffic  

> **Đáp án: B**  
> Sự khác biệt **cốt lõi**: packet switching = **statistical multiplexing** (dùng khi có nhu cầu); circuit switching = **dedicated resources** (dành sẵn dù không dùng). Đây là trade-off giữa efficiency và predictability.

---

**Câu 90.** *(Trung bình)* Tại sao **propagation delay** có thể là yếu tố dominant trong mạng WAN (Wide Area Network)?

A. Vì WAN có nhiều routers hơn LAN  
B. Vì khoảng cách địa lý lớn → d/s lớn, trong khi transmission delay nhỏ khi bandwidth cao và packet nhỏ  
C. Vì WAN dùng công nghệ cáp chậm hơn  
D. Vì propagation speed thấp hơn trong môi trường WAN  

> **Đáp án: B**  
> Trong WAN (nghìn km), d rất lớn → propagation delay hàng chục-trăm ms. Với link tốc độ cao (Gbps) và packet nhỏ, transmission delay chỉ microseconds → **propagation dominates**.

---

**Câu 91.** *(Trung bình)* Tại sao "access network" thường là **bottleneck** trong Internet ngày nay, chứ không phải network core?

A. Vì core routers xử lý chậm  
B. Vì core Internet được over-provisioned với high-speed links, trong khi access links (DSL, cable) có bandwidth thấp hơn nhiều  
C. Vì access network dùng công nghệ lỗi thời  
D. Vì core network không hỗ trợ packet switching  

> **Đáp án: B**  
> Core Internet dùng high-speed fiber links với bandwidth rất cao — được thiết kế dư thừa (over-provisioned). Bottleneck thường là **last-mile access link** (DSL, cable, 4G) giữa người dùng và ISP.

---

**Câu 92.** *(Khó)* Trong mô hình phân cấp ISP, quan hệ "customer-provider" hoạt động như thế nào về mặt tài chính?

A. Tier-1 ISPs trả tiền cho regional ISPs để có quyền truy cập  
B. ISP cấp thấp hơn (customer) trả tiền cho ISP cấp cao hơn (provider) để có kết nối Internet toàn cầu; tier-1 ISPs không trả tiền cho ai  
C. Mọi ISP đều trả phí ngang nhau cho IETF  
D. Chỉ end users trả tiền, các ISP kết nối miễn phí với nhau  

> **Đáp án: B**  
> **Customer pays provider**: access ISP → regional ISP → tier-1 ISP. Tier-1 ISPs không phải trả tiền cho ai (ở đỉnh hierarchy). Peering giữa cùng cấp thường settlement-free.

---

**Câu 93.** *(Khó)* Điểm mấu chốt nào giải thích tại sao Internet có thể scale đến hàng tỷ thiết bị?

A. Vì có đủ địa chỉ IPv4  
B. Vì kiến trúc phân tầng ISP, routing tự động, và nguyên lý packet switching cho phép mạng phát triển dần mà không cần thiết kế lại từ đầu  
C. Vì tất cả các routers đều được đồng bộ hóa tập trung  
D. Vì băng thông vật lý tăng đủ nhanh  

> **Đáp án: B**  
> Scalability của Internet đến từ: (1) **hierarchical ISP structure** — không cần full-mesh; (2) **distributed routing protocols** — tự động thích nghi; (3) **packet switching** — statistical multiplexing; (4) **standardized protocols** — interoperability.

---

**Câu 94.** *(Khó)* Nếu thiết kế một ứng dụng cần **đảm bảo độ trễ thấp và ổn định** (như điều khiển robot từ xa), bạn sẽ gặp thách thức gì với Internet hiện tại?

A. Internet không hỗ trợ kết nối real-time  
B. Queuing delay biến thiên (jitter) trong packet-switched Internet không đảm bảo được delay bound — Internet chỉ cung cấp best-effort service, không có guarantee  
C. Internet không đủ bandwidth cho ứng dụng real-time  
D. Routing protocols không đủ nhanh cho real-time  

> **Đáp án: B**  
> Internet là **best-effort network** — không có delay guarantee. Queuing delay biến thiên theo congestion. Đây là lý do các ứng dụng critical real-time phải dùng QoS mechanisms, edge computing, hoặc dedicated circuits.

---

**Câu 95.** *(Trung bình)* Sự kiện nào đánh dấu sự chuyển đổi Internet từ học thuật sang thương mại?

A. Sự ra đời của email năm 1972  
B. Năm 1991, NSFNET gỡ bỏ hạn chế sử dụng cho mục đích thương mại; năm 1995, NSFNET bị giải thể, backbone do commercial ISPs đảm nhận  
C. Sự ra đời của TCP/IP năm 1983  
D. Sự xuất hiện của browser Mosaic năm 1993  

> **Đáp án: B**  
> Hai sự kiện then chốt: **1991** — NSFNET mở cho thương mại; **1995** — NSFNET giải thể, backbone Internet chuyển hoàn toàn sang commercial ISPs. Đây là bước ngoặt commercialization.

---

**Câu 96.** *(Trung bình)* DNS (Domain Name System) thuộc tầng nào và có chức năng gì?

A. Transport layer — phân giải địa chỉ MAC  
B. Application layer — dịch hostname (như www.google.com) thành địa chỉ IP 32-bit  
C. Network layer — định tuyến gói tin đến đúng server  
D. Link layer — phân giải địa chỉ vật lý  

> **Đáp án: B**  
> **DNS** là application-layer protocol dịch **human-readable hostnames** → **IP addresses** (32-bit). Không có DNS, người dùng phải nhớ địa chỉ IP số để truy cập web.

---

**Câu 97.** *(Trung bình)* **VoIP** (Voice-over-IP) gặp thách thức gì liên quan đến **packetization delay**?

A. Không đủ băng thông để truyền audio  
B. Phía gửi phải tích lũy đủ một lượng encoded speech để fill một packet trước khi gửi — thời gian chờ này (packetization delay) ảnh hưởng đến chất lượng cảm nhận của người dùng  
C. IP không hỗ trợ real-time audio  
D. Mã hóa audio quá phức tạp cho end systems  

> **Đáp án: B**  
> **Packetization delay** trong VoIP: phải đợi đủ data để fill packet → gây độ trễ thêm. Kết hợp với queuing delay biến thiên → jitter → ảnh hưởng chất lượng thoại.

---

**Câu 98.** *(Khó)* Bài tập: Gửi file F = 32 Mb (megabits) từ server (Rs = 2 Mbps) đến client (Rc = 1 Mbps), core network rất nhanh. Thời gian download ước tính là bao nhiêu?

A. 16 giây  
B. 32 giây  
C. 64 giây  
D. 8 giây  

> **Đáp án: B**  
> Throughput = min{Rs, Rc} = min{2, 1} = **1 Mbps** (bottleneck là Rc). Thời gian = F/throughput = 32 Mb / 1 Mbps = **32 giây**. (Đây là ước tính, chưa tính store-and-forward và protocol overhead.)

---

**Câu 99.** *(Khó)* Tại sao end-to-end delay công thức là **N × (dproc + dtrans + dprop)** chứ không phải đơn giản là dtrans?

A. Vì dtrans chỉ tính được ở tầng Physical  
B. Vì packet phải đi qua N links với N-1 routers — tại mỗi hop đều có đủ 3 loại delay; chúng tích lũy (accumulate) qua mỗi node  
C. Vì công thức chỉ áp dụng cho WAN, không áp dụng cho LAN  
D. Vì N là số packet, không phải số link  

> **Đáp án: B**  
> Với N links, packet phải qua N-1 routers, mỗi router xử lý có processing delay, mỗi link có transmission và propagation delay. Tổng delay là **tổng tích lũy** của tất cả các thành phần qua N hops.

---

**Câu 100.** *(Khó)* Xem xét toàn bộ chương 1: Nguyên lý thiết kế nào giải thích **hầu hết** các quyết định kiến trúc của Internet?

A. Tốc độ tối đa là ưu tiên duy nhất  
B. Sự kết hợp của: packet switching để dùng tài nguyên hiệu quả, layered protocols để modularity, network of networks để scalability, và end-to-end principle để đặt intelligence ở edges — tất cả cùng tạo nên một hệ thống linh hoạt, scalable và open  
C. Bảo mật là ưu tiên hàng đầu từ đầu  
D. Centralized control để dễ quản lý  

> **Đáp án: B**  
> Internet được xây dựng trên tập hợp nguyên lý: **statistical multiplexing** (efficiency), **layering** (modularity và evolution), **hierarchical addressing** (scalability), **end-to-end argument** (simplicity at core). Không có một nguyên lý duy nhất mà là sự kết hợp hài hòa của nhiều nguyên lý.

---
