# Bộ câu hỏi trắc nghiệm — Chương 1: Computer Networks and the Internet

## Phần 1 — Tổng quan về Internet (What Is the Internet?)

---

**Câu 1.** *(Dễ)* Trong thuật ngữ mạng, tất cả các thiết bị kết nối vào Internet — từ máy tính đến điện thoại thông minh — được gọi chung là gì?

A. Routers  
B. Packet switches  
C. Hosts (end systems)  
D. ISPs  

> **Đáp án: C**  
> Tất cả các thiết bị kết nối Internet đều được gọi là **hosts** hoặc **end systems**. Đây là thuật ngữ được dùng thay thế cho nhau hoàn toàn.

---

**Câu 2.** *(Dễ)* Internet có thể được mô tả theo hai góc độ chính. Góc độ nào sau đây là KHÔNG đúng?

A. Mô tả theo phần cứng và phần mềm cấu thành (nuts-and-bolts)  
B. Mô tả như một hạ tầng cung cấp dịch vụ cho các ứng dụng phân tán  
C. Mô tả như một hệ thống truyền thông circuit-switched toàn cầu  
D. Cả A và B đều là cách mô tả đúng  

> **Đáp án: C**  
> Internet là mạng **packet-switched**, không phải circuit-switched toàn cầu. Hai cách mô tả chính xác là nuts-and-bolts (A) và infrastructure for distributed applications (B).

---

**Câu 3.** *(Dễ)* TCP/IP là gì?

A. Một loại phần cứng router  
B. Hai giao thức quan trọng nhất của Internet, quy định cách gói tin được gửi và nhận  
C. Một tiêu chuẩn dành riêng cho mạng không dây  
D. Một tổ chức quản lý tên miền Internet  

> **Đáp án: B**  
> **TCP** (Transmission Control Protocol) và **IP** (Internet Protocol) là hai giao thức cốt lõi của Internet — IP quy định định dạng gói tin, TCP đảm bảo truyền tải tin cậy.

---

**Câu 4.** *(Dễ)* Tổ chức nào chịu trách nhiệm phát triển các tiêu chuẩn Internet (Internet standards)?

A. IEEE  
B. ISO  
C. IETF (Internet Engineering Task Force)  
D. W3C  

> **Đáp án: C**  
> **IETF** phát triển các tiêu chuẩn Internet dưới dạng tài liệu gọi là **RFCs** (Requests for Comments). IEEE phụ trách tiêu chuẩn link-layer như Ethernet và WiFi.

---

**Câu 5.** *(Dễ)* RFC là viết tắt của gì và có vai trò gì?

A. Remote File Copy — dùng để sao chép file từ xa  
B. Requests for Comments — tài liệu định nghĩa các giao thức Internet  
C. Router Forwarding Control — điều khiển chuyển tiếp gói tin  
D. Reliable Frame Check — kiểm tra tính toàn vẹn của frame  

> **Đáp án: B**  
> **RFC** (Requests for Comments) là các tài liệu kỹ thuật chi tiết do IETF ban hành, định nghĩa các giao thức như TCP, IP, HTTP, SMTP. Hiện có hơn 6.000 RFC.

---

**Câu 6.** *(Dễ)* Ứng dụng phân tán (distributed application) là gì?

A. Ứng dụng chỉ chạy trên một máy chủ duy nhất  
B. Ứng dụng liên quan đến nhiều end systems trao đổi dữ liệu với nhau  
C. Ứng dụng chạy bên trong các packet switches  
D. Ứng dụng không cần kết nối Internet  

> **Đáp án: B**  
> **Distributed applications** như email, web, video streaming đều chạy trên các **end systems** và trao đổi dữ liệu qua mạng. Chúng không chạy trong packet switches.

---

**Câu 7.** *(Dễ)* API (Application Programming Interface) trong ngữ cảnh Internet có vai trò gì?

A. Tăng tốc độ truyền dữ liệu vật lý  
B. Quy định tập luật mà chương trình gửi phải tuân theo để Internet chuyển dữ liệu đến đích  
C. Mã hóa dữ liệu trước khi truyền  
D. Phân bổ địa chỉ IP cho các end systems  

> **Đáp án: B**  
> **Internet API** là tập hợp các quy tắc (rules) mà chương trình gửi phải tuân theo để yêu cầu hạ tầng Internet chuyển dữ liệu đến chương trình đích trên end system khác.

---

**Câu 8.** *(Trung bình)* Điều gì phân biệt **clients** và **servers** trong mạng?

A. Clients có tốc độ xử lý cao hơn servers  
B. Clients thường là thiết bị người dùng cuối (PC, smartphone), servers là máy lưu trữ và phân phối nội dung  
C. Servers chỉ tồn tại trong mạng doanh nghiệp, không có trong mạng gia đình  
D. Clients và servers là hai thuật ngữ hoàn toàn đồng nghĩa  

> **Đáp án: B**  
> **Clients** (desktop, laptop, smartphone) gửi yêu cầu và nhận dữ liệu. **Servers** (máy chủ web, email, video) là máy mạnh hơn, lưu trữ và phân phối nội dung — nhiều server ngày nay đặt trong các data centers lớn.

---

**Câu 9.** *(Trung bình)* Một **protocol** trong mạng máy tính định nghĩa những gì?

A. Chỉ định dạng của các gói tin  
B. Chỉ thứ tự gửi tin nhắn  
C. Định dạng, thứ tự của các message được trao đổi, và các hành động được thực hiện khi gửi/nhận message  
D. Chỉ cách mã hóa dữ liệu  

> **Đáp án: C**  
> Định nghĩa chính xác: *"A protocol defines the **format** and the **order** of messages exchanged between two or more communicating entities, as well as the **actions** taken on the transmission and/or receipt of a message or other event."*

---

**Câu 10.** *(Trung bình)* Tại sao việc có protocol standards (tiêu chuẩn giao thức) lại quan trọng?

A. Để tăng tốc độ truyền dữ liệu  
B. Để mọi người đồng ý về những gì mỗi protocol làm, cho phép tạo ra các hệ thống có thể tương tác (interoperate) với nhau  
C. Để giảm chi phí phần cứng  
D. Để hạn chế số lượng thiết bị kết nối Internet  

> **Đáp án: B**  
> Nếu không có tiêu chuẩn chung, các hệ thống sẽ không thể giao tiếp được với nhau — giống như hai người nói hai ngôn ngữ khác nhau. Standards đảm bảo **interoperability**.

---

## Phần 2 — Network Edge & Access Networks

---

**Câu 11.** *(Dễ)* **Access network** là gì?

A. Mạng kết nối các router lõi với nhau  
B. Mạng kết nối vật lý một end system với router đầu tiên trên đường đến đích  
C. Mạng nội bộ của các ISP cấp 1  
D. Mạng quản lý địa chỉ IP toàn cầu  

> **Đáp án: B**  
> **Access network** là phần mạng kết nối end system với **edge router** — cổng vào mạng lõi. Ví dụ: DSL, cable, WiFi, 4G.

---

**Câu 12.** *(Dễ)* DSL (Digital Subscriber Line) sử dụng hạ tầng nào để truyền dữ liệu?

A. Cáp đồng trục (coaxial cable)  
B. Cáp quang (fiber optic)  
C. Đường dây điện thoại đồng (twisted-pair copper wire)  
D. Sóng vô tuyến (radio spectrum)  

> **Đáp án: C**  
> DSL tận dụng hạ tầng **đường dây điện thoại** có sẵn — chính vì vậy nhà cung cấp DSL thường là công ty viễn thông (telco) đã có sẵn mạng dây đến từng nhà.

---

**Câu 13.** *(Dễ)* HFC (Hybrid Fiber Coax) là gì?

A. Công nghệ kết hợp DSL và WiFi  
B. Hệ thống kết hợp cáp quang từ trung tâm đến điểm phân phối khu phố, và cáp đồng trục đến từng hộ gia đình  
C. Giao thức truyền dữ liệu không dây thế hệ mới  
D. Tiêu chuẩn mã hóa dữ liệu trong mạng cable  

> **Đáp án: B**  
> **HFC** dùng **fiber optics** từ cable head end đến neighborhood junction, rồi **coaxial cable** từ đó đến từng nhà. Đây là nền tảng của cable Internet.

---

**Câu 14.** *(Trung bình)* Tại sao DSL được gọi là **asymmetric** (bất đối xứng)?

A. Vì DSL chỉ hỗ trợ một chiều truyền dữ liệu  
B. Vì tốc độ downstream và upstream khác nhau (downstream cao hơn upstream)  
C. Vì DSL hoạt động khác nhau tùy theo nhà cung cấp  
D. Vì DSL không đảm bảo băng thông cố định  

> **Đáp án: B**  
> DSL là **asymmetric** vì tốc độ **downstream** (từ mạng về nhà) cao hơn **upstream** (từ nhà lên mạng) — phù hợp với hành vi người dùng thường tải về nhiều hơn tải lên.

---

**Câu 15.** *(Trung bình)* Đặc điểm nào sau đây là của cable Internet access nhưng KHÔNG phải của DSL?

A. Dùng đường truyền vật lý có sẵn  
B. Tốc độ bị ảnh hưởng bởi khoảng cách đến trung tâm  
C. Là **shared broadcast medium** — nhiều hộ dùng chung băng thông  
D. Hỗ trợ truyền đồng thời dữ liệu và tín hiệu khác  

> **Đáp án: C**  
> Cable Internet là **shared broadcast medium**: mọi gói tin từ head end đều đến tất cả các hộ trong khu vực. Khi nhiều người cùng tải, băng thông bị chia sẻ — khác với DSL là dedicated per household.

---

**Câu 16.** *(Trung bình)* FTTH (Fiber to the Home) khác với DSL và cable ở điểm căn bản nào?

A. FTTH rẻ hơn nhưng chậm hơn  
B. FTTH cung cấp đường cáp quang trực tiếp từ CO đến tận nhà, cho tốc độ tiềm năng gigabit  
C. FTTH chỉ dùng cho doanh nghiệp, không dùng cho hộ gia đình  
D. FTTH không cần thiết bị đầu cuối tại nhà  

> **Đáp án: B**  
> **FTTH** kéo cáp quang trực tiếp đến nhà, loại bỏ hoàn toàn cáp đồng, cho phép tốc độ **gigabit** — vượt xa DSL và cable. Tuy nhiên chi phí triển khai cao hơn.

---

**Câu 17.** *(Trung bình)* Sự khác biệt cơ bản giữa WiFi (IEEE 802.11) và 3G/4G/LTE là gì?

A. WiFi nhanh hơn 3G/4G trong mọi trường hợp  
B. WiFi có phạm vi kết nối vài chục mét, còn 3G/4G phủ hàng chục km từ base station  
C. 3G/4G chỉ dùng cho voice, không dùng cho data  
D. WiFi và 3G/4G dùng cùng một tần số vô tuyến  

> **Đáp án: B**  
> **WiFi**: phạm vi vài chục mét, dùng access point. **3G/4G/LTE**: phạm vi hàng chục km từ base station — đây là **wide-area wireless** cho phép di chuyển tự do.

---

**Câu 18.** *(Trung bình)* Ethernet trong môi trường doanh nghiệp cung cấp tốc độ kết nối điển hình là bao nhiêu cho user?

A. 1 Mbps  
B. 10 Mbps  
C. 100 Mbps  
D. 1 Gbps  

> **Đáp án: C**  
> Người dùng thường có **100 Mbps** đến Ethernet switch. Servers có thể được kết nối với tốc độ **1 Gbps** hoặc **10 Gbps**.

---

**Câu 19.** *(Khó)* Tại sao khoảng cách giữa nhà và CO (Central Office) lại giới hạn hiệu quả của DSL?

A. Vì chi phí đường dây tăng theo khoảng cách  
B. Vì tín hiệu analog trên đường dây đồng bị suy giảm (attenuation) theo khoảng cách, làm giảm tốc độ khả dụng  
C. Vì DSLAM không thể xử lý tín hiệu từ xa  
D. Vì tần số được phân bổ thay đổi theo khoảng cách  

> **Đáp án: B**  
> Tín hiệu trên copper wire bị **suy giảm** (attenuation) khi truyền xa — càng xa CO, tín hiệu càng yếu, tốc độ DSL khả dụng càng thấp. Đây là giới hạn vật lý cố hữu của công nghệ này, thường giới hạn ở 5-10 dặm.

---

**Câu 20.** *(Khó)* Trong PON (Passive Optical Network) — kiến trúc FTTH — tại sao gọi là "passive"?

A. Vì không cần nguồn điện để vận hành  
B. Vì splitter quang không cần nguồn điện chủ động — nó chia tín hiệu quang theo cơ chế thụ động  
C. Vì dữ liệu chỉ truyền một chiều (từ CO về nhà)  
D. Vì PON không cần thiết bị tại nhà  

> **Đáp án: B**  
> **Passive** trong PON nghĩa là optical splitter không cần nguồn điện — nó chia ánh sáng theo cơ chế quang học thuần túy, khác với AON (Active Optical Network) dùng Ethernet switch chủ động.

---

## Phần 3 — Physical Media (Phương tiện vật lý)

---

**Câu 21.** *(Dễ)* Phương tiện vật lý được chia thành hai loại chính. Đó là:

A. Digital media và analog media  
B. Guided media và unguided media  
C. Wired media và wireless media  
D. Fast media và slow media  

> **Đáp án: B**  
> **Guided media**: sóng được dẫn qua môi trường rắn (cáp đồng, cáp quang). **Unguided media**: sóng lan truyền trong không gian (WiFi, vệ tinh). Đây là phân loại căn bản nhất.

---

**Câu 22.** *(Dễ)* Loại phương tiện vật lý nào phổ biến nhất và rẻ nhất trong mạng có dây?

A. Coaxial cable  
B. Fiber optic  
C. Twisted-pair copper wire  
D. Satellite link  

> **Đáp án: C**  
> **Twisted-pair copper wire** — dây đồng xoắn đôi — là phương tiện có dây phổ biến và rẻ nhất, được dùng trên 99% kết nối điện thoại cố định và phổ biến trong LAN.

---

**Câu 23.** *(Trung bình)* Vì sao dây đồng trong twisted pair được xoắn lại với nhau?

A. Để tăng độ bền cơ học  
B. Để giảm nhiễu điện từ (electromagnetic interference) từ các cặp dây gần đó  
C. Để tăng tốc độ truyền dữ liệu  
D. Để dễ nhận biết trong bó cáp  

> **Đáp án: B**  
> Cấu trúc **xoắn** giúp triệt tiêu nhiễu điện từ qua cơ chế đối pha (each twist cancels interference from adjacent twists) — đây là nguyên lý vật lý quan trọng của UTP/STP.

---

**Câu 24.** *(Trung bình)* Fiber optic có ưu điểm gì so với copper wire khi truyền dữ liệu đường dài?

A. Fiber rẻ hơn và dễ lắp đặt hơn  
B. Fiber có tốc độ cao hơn, không bị nhiễu điện từ, và suy giảm tín hiệu rất thấp trong khoảng cách tới 100 km  
C. Fiber nhẹ hơn và linh hoạt hơn  
D. Fiber hỗ trợ kết nối không dây  

> **Đáp án: B**  
> Fiber optic truyền **xung ánh sáng**, miễn nhiễm hoàn toàn với nhiễu điện từ, suy giảm rất thấp ở khoảng cách lớn. Đây là lý do fiber là lựa chọn cho **long-haul** và **backbone** Internet.

---

**Câu 25.** *(Trung bình)* Tại sao fiber optic chưa thay thế hoàn toàn copper wire trong mạng nội bộ (LAN)?

A. Fiber chậm hơn copper trong khoảng cách ngắn  
B. Chi phí thiết bị quang (transmitters, receivers, switches) vẫn còn cao cho short-haul deployment  
C. Fiber không tương thích với các thiết bị mạng hiện đại  
D. Fiber không thể truyền dữ liệu ở tốc độ LAN  

> **Đáp án: B**  
> Dù fiber nhanh hơn, **chi phí thiết bị đầu cuối quang** vẫn cao — đây là rào cản triển khai trong LAN và residential access, nơi cost-effectiveness là ưu tiên hàng đầu.

---

**Câu 26.** *(Khó)* Geostationary satellite (vệ tinh địa tĩnh) có propagation delay khoảng bao nhiêu và tại sao?

A. ~10 ms, vì vệ tinh ở gần Trái Đất  
B. ~280 ms, vì quỹ đạo ở độ cao ~36,000 km và sóng truyền với tốc độ ánh sáng  
C. ~1 ms, vì tín hiệu vệ tinh được khuếch đại nhiều lần  
D. ~500 ms, vì phải đi qua nhiều relay station  

> **Đáp án: B**  
> Vệ tinh địa tĩnh ở độ cao **36,000 km**. Sóng đi từ ground → satellite → ground = ~72,000 km ÷ tốc độ ánh sáng ≈ **280 ms**. Đây là hạn chế lớn cho các ứng dụng real-time.

---

## Phần 4 — Network Core: Packet Switching

---

**Câu 27.** *(Dễ)* Trong packet switching, dữ liệu được chia thành các đơn vị nhỏ gọi là gì?

A. Circuits  
B. Frames  
C. Packets  
D. Segments  

> **Đáp án: C**  
> Trong ngữ cảnh **network core**, các đơn vị dữ liệu được gọi là **packets**. (Lưu ý: ở các tầng khác có tên riêng: segment ở transport layer, frame ở link layer.)

---

**Câu 28.** *(Dễ)* **Store-and-forward transmission** có nghĩa là gì?

A. Router gửi ngay từng bit nhận được mà không cần đợi  
B. Router phải nhận toàn bộ packet trước khi bắt đầu truyền packet đó ra link tiếp theo  
C. Dữ liệu được lưu trữ vĩnh viễn tại router  
D. Router gửi packet theo từng half-packet một  

> **Đáp án: B**  
> **Store-and-forward**: router phải nhận **toàn bộ** packet → lưu vào buffer → mới bắt đầu truyền ra outbound link. Điều này tạo ra transmission delay tại mỗi hop.

---

**Câu 29.** *(Trung bình)* Cho một packet L bits truyền qua một link tốc độ R bps. Thời gian truyền packet (transmission delay) là bao nhiêu?

A. R/L  
B. L × R  
C. L/R  
D. R − L  

> **Đáp án: C**  
> **Transmission delay = L/R** (giây). Đây là thời gian để "đẩy" toàn bộ L bits vào link với tốc độ R bits/giây. Đây là công thức cơ bản nhất trong phân tích delay mạng.

---

**Câu 30.** *(Trung bình)* Nếu gửi 1 packet L bits từ source đến destination qua **N links**, mỗi link tốc độ R bps (store-and-forward), end-to-end delay (chỉ tính transmission) là bao nhiêu?

A. L/R  
B. N × L/R  
C. (N−1) × L/R  
D. L/(N×R)  

> **Đáp án: B**  
> Với store-and-forward và N links (N−1 routers), mỗi hop mất L/R giây, tổng = **N × L/R**. Công thức tổng quát: d_end-to-end = N(L/R) khi bỏ qua các delay khác.

---

**Câu 31.** *(Trung bình)* **Forwarding table** trong router dùng để làm gì?

A. Lưu trữ tạm thời các packet đang chờ truyền  
B. Ánh xạ địa chỉ đích của packet đến outbound link phù hợp  
C. Ghi lại lịch sử các packet đã truyền qua  
D. Quản lý băng thông của từng kết nối  

> **Đáp án: B**  
> **Forwarding table** map destination addresses → outbound links. Khi packet đến, router tra bảng này để biết phải gửi ra link nào — đây là cơ chế chuyển tiếp cơ bản của Internet.

---

**Câu 32.** *(Trung bình)* **Routing protocols** có vai trò gì liên quan đến forwarding tables?

A. Mã hóa nội dung forwarding table để bảo mật  
B. Tự động tính toán và cập nhật forwarding tables trong các routers  
C. Giám sát lưu lượng qua từng link  
D. Phân bổ địa chỉ IP cho các end systems  

> **Đáp án: B**  
> **Routing protocols** (như OSPF, BGP) tự động tính đường ngắn nhất và điền vào forwarding tables — thay vì người quản trị phải cấu hình thủ công từng router.

---

**Câu 33.** *(Trung bình)* Packet loss xảy ra trong hoàn cảnh nào?

A. Khi packet đi qua quá nhiều router  
B. Khi buffer (output queue) tại router bị đầy và packet mới đến không có chỗ để chờ  
C. Khi packet bị mã hóa sai  
D. Khi propagation delay quá lớn  

> **Đáp án: B**  
> **Packet loss** xảy ra khi output buffer đầy — router phải drop packet (hoặc packet đang đợi). Đây là hệ quả trực tiếp của congestion (tắc nghẽn mạng).

---

**Câu 34.** *(Khó)* Vì sao packet switching hiệu quả hơn circuit switching khi traffic là **bursty**?

A. Vì packet switching có tốc độ truyền vật lý cao hơn  
B. Vì packet switching phân bổ bandwidth theo nhu cầu thực tế, không lãng phí tài nguyên dành riêng cho connection khi không có data  
C. Vì packet switching không có queuing delay  
D. Vì packet switching luôn đảm bảo đúng thứ tự gói tin  

> **Đáp án: B**  
> Với traffic bursty (có lúc active, lúc idle), circuit switching lãng phí bandwidth dành riêng trong lúc idle. Packet switching **dùng tài nguyên theo nhu cầu** — nhiều user có thể chia sẻ hiệu quả hơn rất nhiều.

---

**Câu 35.** *(Khó)* Trong ví dụ sách: link 1 Mbps, mỗi user cần 100 kbps khi active, xác suất active = 10%. Circuit switching chỉ hỗ trợ tối đa bao nhiêu user đồng thời?

A. 100 users  
B. 35 users  
C. 10 users  
D. 1 user  

> **Đáp án: C**  
> Circuit switching: mỗi user cần 100 kbps dành riêng → 1 Mbps / 100 kbps = **10 users** tối đa. Với packet switching, 35 users có thể dùng chung link này với xác suất congestion rất thấp (~0.0004).

---

## Phần 5 — Circuit Switching

---

**Câu 36.** *(Dễ)* Trong circuit switching, tài nguyên mạng được xử lý như thế nào?

A. Chia sẻ theo yêu cầu giữa tất cả các kết nối  
B. Dành riêng (reserved) cho mỗi kết nối trong suốt thời gian phiên truyền  
C. Phân bổ ngẫu nhiên  
D. Không cần dự trữ, dùng khi nào có khi đó  

> **Đáp án: B**  
> **Circuit switching** dành riêng tài nguyên (bandwidth, buffers) cho một connection trong toàn bộ thời gian phiên — đảm bảo QoS nhưng lãng phí khi không dùng.

---

**Câu 37.** *(Dễ)* Mạng điện thoại truyền thống là ví dụ điển hình của loại switching nào?

A. Packet switching  
B. Circuit switching  
C. Message switching  
D. Label switching  

> **Đáp án: B**  
> Mạng điện thoại truyền thống dùng **circuit switching** — khi gọi điện, một mạch (circuit) được thiết lập và giữ nguyên cho đến khi kết thúc cuộc gọi.

---

**Câu 38.** *(Trung bình)* FDM (Frequency-Division Multiplexing) và TDM (Time-Division Multiplexing) khác nhau cơ bản ở điểm nào?

A. FDM chia theo thời gian, TDM chia theo tần số  
B. FDM chia spectrum tần số cho mỗi kết nối, TDM chia thời gian thành các slot cho mỗi kết nối  
C. FDM chỉ dùng cho analog, TDM chỉ dùng cho digital  
D. FDM và TDM đồng nghĩa với nhau  

> **Đáp án: B**  
> **FDM**: mỗi connection dùng một **dải tần** riêng biệt liên tục. **TDM**: mỗi connection được cấp một **time slot** trong frame, lặp lại định kỳ — hai cơ chế multiplexing cơ bản.

---

**Câu 39.** *(Trung bình)* Trong TDM với 24 slots/frame và link rate 1.536 Mbps, mỗi circuit có transmission rate là bao nhiêu?

A. 1.536 Mbps  
B. 128 kbps  
C. 64 kbps  
D. 24 kbps  

> **Đáp án: C**  
> Rate mỗi circuit = 1.536 Mbps ÷ 24 = **64 kbps**. Đây cũng chính là tốc độ chuẩn của một kênh thoại số (PCM voice channel) trong hệ thống T1.

---

**Câu 40.** *(Trung bình)* Nhược điểm chính của circuit switching là gì?

A. Không đảm bảo được chất lượng dịch vụ  
B. Lãng phí tài nguyên khi kết nối không truyền dữ liệu (idle periods)  
C. Không thể hỗ trợ nhiều kết nối cùng lúc  
D. Phức tạp hơn packet switching để triển khai  

> **Đáp án: B**  
> Khi connection idle (ví dụ: bác sĩ X-quang đang ngắm phim), tài nguyên đã dành riêng bị **lãng phí** — không ai khác dùng được. Đây là bất lợi cốt lõi của circuit switching.

---

**Câu 41.** *(Khó)* Bài tập: Gửi file 640,000 bits qua mạng circuit-switched TDM, 24 slots/frame, link rate 1.536 Mbps, circuit setup time 500 ms. Tổng thời gian gửi file là bao nhiêu?

A. 5 giây  
B. 10 giây  
C. 10.5 giây  
D. 11 giây  

> **Đáp án: C**  
> Rate mỗi circuit = 1.536/24 = 64 kbps. Thời gian truyền = 640,000/64,000 = **10 giây**. Cộng setup time 0.5 giây → tổng = **10.5 giây**. (Lưu ý: không phụ thuộc số link.)

---

## Phần 6 — Network of Networks (ISP Hierarchy)

---

**Câu 42.** *(Dễ)* ISP là viết tắt của gì?

A. Internet Security Protocol  
B. Internet Service Provider  
C. Integrated Switching Platform  
D. International Standards for Protocols  

> **Đáp án: B**  
> **ISP** (Internet Service Provider) là tổ chức cung cấp dịch vụ truy cập Internet — từ công ty cable/telco đến ISP trường đại học, ISP doanh nghiệp.

---

**Câu 43.** *(Dễ)* Tại sao Internet được gọi là "a network of networks"?

A. Vì Internet dùng nhiều giao thức khác nhau  
B. Vì các access ISPs phải được kết nối với nhau thông qua hệ thống phân cấp các ISP cấp cao hơn  
C. Vì mỗi router tạo ra một mạng con riêng  
D. Vì Internet có nhiều topology khác nhau  

> **Đáp án: B**  
> Để các end systems trên toàn cầu giao tiếp được, các access ISPs phải được kết nối lại — tạo thành **hệ thống phân cấp ISP** (access → regional → tier-1), đây chính là "network of networks."

---

**Câu 44.** *(Trung bình)* Tier-1 ISP có đặc điểm nào sau đây?

A. Phải trả phí cho các ISP cấp trên  
B. Chỉ phục vụ một quốc gia duy nhất  
C. Không phải trả phí cho bất kỳ ISP nào khác vì ở đỉnh của hierarchy  
D. Là các ISP cung cấp dịch vụ trực tiếp cho người dùng cuối  

> **Đáp án: C**  
> **Tier-1 ISPs** (AT&T, Level 3, NTT...) ở đỉnh hierarchy — họ kết nối với nhau theo kiểu **settlement-free peering** và không trả phí cho ai. Đây là "customer-provider relationship" ngược lại.

---

**Câu 45.** *(Trung bình)* **Peering** giữa hai ISP có nghĩa là gì và lợi ích của nó?

A. Một ISP mua dịch vụ của ISP kia  
B. Hai ISP kết nối trực tiếp mạng của nhau, traffic đi thẳng không qua intermediary, thường không thanh toán cho nhau  
C. Hai ISP chia sẻ chung một data center  
D. Một ISP thuê kết nối từ ISP kia với giá ưu đãi  

> **Đáp án: B**  
> **Peering**: hai ISP cùng cấp kết nối trực tiếp → traffic không phải đi qua upstream ISP → **giảm chi phí** và **giảm latency**. Thường là settlement-free.

---

**Câu 46.** *(Trung bình)* IXP (Internet Exchange Point) là gì?

A. Điểm đặt các tier-1 ISP router chính  
B. Địa điểm vật lý nơi nhiều ISP có thể kết nối và peer với nhau  
C. Giao thức trao đổi thông tin định tuyến  
D. Thiết bị chuyển đổi giữa IPv4 và IPv6  

> **Đáp án: B**  
> **IXP** là facility (thường là tòa nhà riêng với switch của nó) nơi nhiều ISP peer với nhau — giúp giảm chi phí và tăng hiệu quả kết nối. Có khoảng 300 IXP trên toàn cầu.

---

**Câu 47.** *(Trung bình)* **Multi-homing** của một ISP nghĩa là gì?

A. Đặt server tại nhiều địa điểm địa lý khác nhau  
B. Kết nối đến hai hoặc nhiều provider ISP khác nhau để đảm bảo redundancy  
C. Phục vụ khách hàng tại nhiều quốc gia  
D. Sử dụng nhiều giao thức định tuyến cùng lúc  

> **Đáp án: B**  
> **Multi-homing**: ISP kết nối với nhiều provider → nếu một provider gặp sự cố, traffic vẫn có thể đi qua provider còn lại — tăng **reliability** và **redundancy**.

---

**Câu 48.** *(Khó)* Google xây dựng mạng riêng (private network) và kết nối trực tiếp với lower-tier ISPs. Mục đích chiến lược chính là gì?

A. Để tăng tốc độ download cho người dùng Google  
B. Để bypass upper-tier ISPs, giảm chi phí trả cho tier-1 ISPs và kiểm soát tốt hơn cách dịch vụ được phân phối đến end users  
C. Để cung cấp dịch vụ ISP cạnh tranh với tier-1  
D. Để tăng bảo mật dữ liệu người dùng  

> **Đáp án: B**  
> Google private network **bypass** tầng tier-1 bằng cách peer trực tiếp với lower-tier ISPs — vừa **giảm tiền** trả cho tier-1, vừa **tăng kiểm soát** QoS từ data center đến end user.

---

## Phần 7 — Delay, Loss, and Throughput

---

**Câu 49.** *(Dễ)* Bốn thành phần của **nodal delay** tại một router là gì?

A. Transmission, propagation, queuing, processing  
B. Encoding, decoding, routing, forwarding  
C. Compression, decompression, encryption, decryption  
D. Packetization, fragmentation, reassembly, delivery  

> **Đáp án: A**  
> **d_nodal = d_proc + d_queue + d_trans + d_prop**. Bốn thành phần: processing delay, queuing delay, transmission delay, propagation delay — cần nắm rõ bản chất từng loại.

---

**Câu 50.** *(Dễ)* **Propagation delay** phụ thuộc vào yếu tố nào?

A. Kích thước packet và tốc độ link  
B. Khoảng cách giữa hai node và tốc độ lan truyền của tín hiệu trên medium  
C. Số lượng packet đang chờ trong queue  
D. Tốc độ xử lý của CPU router  

> **Đáp án: B**  
> **Propagation delay = d/s** (khoảng cách ÷ tốc độ lan truyền). Không liên quan đến kích thước packet hay tốc độ link — đây là điểm dễ nhầm với transmission delay.

---

**Câu 51.** *(Dễ)* **Processing delay** tại router bao gồm những gì?

A. Thời gian packet chờ trong queue  
B. Thời gian kiểm tra header packet, xác định outbound link, kiểm tra lỗi bit  
C. Thời gian truyền bits ra link vật lý  
D. Thời gian tín hiệu lan truyền qua cáp  

> **Đáp án: B**  
> **Processing delay** = thời gian router phân tích header, tra forwarding table, kiểm tra bit errors. Thường cỡ **microseconds hoặc nhỏ hơn** trong high-speed routers.

---

**Câu 52.** *(Trung bình)* Điểm khác biệt căn bản giữa **transmission delay** và **propagation delay** là gì?

A. Transmission delay phụ thuộc khoảng cách, propagation delay phụ thuộc kích thước packet  
B. Transmission delay là thời gian đẩy bits vào link (phụ thuộc L và R), propagation delay là thời gian bit đi từ A đến B (phụ thuộc khoảng cách và tốc độ vật lý)  
C. Chúng đồng nghĩa với nhau trong hầu hết trường hợp  
D. Transmission delay chỉ xuất hiện ở wireless, propagation delay chỉ ở wired  

> **Đáp án: B**  
> **Transmission**: T = L/R, không quan tâm khoảng cách. **Propagation**: T = d/s, không quan tâm kích thước packet hay tốc độ link. Đây là sự phân biệt quan trọng nhất trong phân tích delay.

---

**Câu 53.** *(Trung bình)* **Traffic intensity** (La/R) là gì và ý nghĩa khi nó tiến đến 1?

A. Tỷ lệ bandwidth được sử dụng; khi = 1 có nghĩa mạng hoàn toàn nhàn rỗi  
B. Tỷ lệ giữa tốc độ đến trung bình và tốc độ truyền; khi tiến đến 1, queuing delay tăng nhanh tiến về vô cực  
C. Tỷ lệ packet loss; khi = 1 có nghĩa 100% packet bị mất  
D. Số lượng user đang hoạt động cùng lúc  

> **Đáp án: B**  
> **La/R** = (arrival rate × packet size) / link rate. Khi **La/R → 1**, queue tích lũy không giới hạn → queuing delay → ∞. **Nguyên tắc vàng**: thiết kế sao cho La/R < 1.

---

**Câu 54.** *(Trung bình)* **Bottleneck link** trong một đường truyền là gì?

A. Link bị hỏng hóc  
B. Link có transmission rate thấp nhất trên đường từ source đến destination, quyết định throughput end-to-end  
C. Link có propagation delay cao nhất  
D. Link đầu tiên trong đường truyền  

> **Đáp án: B**  
> **Bottleneck link** = link có tốc độ thấp nhất → **throughput = min{R1, R2,..., RN}**. Giống như một làn đường hẹp quyết định tốc độ cả đoàn xe.

---

**Câu 55.** *(Trung bình)* **Instantaneous throughput** và **average throughput** khác nhau thế nào?

A. Instantaneous throughput tính theo giờ, average tính theo giây  
B. Instantaneous là tốc độ nhận dữ liệu tại một thời điểm cụ thể; average là F/T (tổng bits ÷ tổng thời gian truyền)  
C. Chúng luôn bằng nhau trong điều kiện bình thường  
D. Chỉ có average throughput có ý nghĩa thực tiễn  

> **Đáp án: B**  
> **Instantaneous throughput**: tốc độ nhận tại thời điểm t (hiển thị trên thanh download). **Average throughput**: F/T — đây là thước đo thực tế cho file transfer.

---

**Câu 56.** *(Trung bình)* Bài tập: Server có Rs = 2 Mbps, client có Rc = 1 Mbps, core network rất nhanh. Throughput end-to-end là bao nhiêu?

A. 2 Mbps  
B. 1.5 Mbps  
C. 1 Mbps  
D. 3 Mbps  

> **Đáp án: C**  
> Throughput = min{Rs, Rc} = min{2 Mbps, 1 Mbps} = **1 Mbps**. Bottleneck là access link phía client. Thời gian download file 32 Mb = 32/1 = 32 giây.

---

**Câu 57.** *(Khó)* Queuing delay **khác** với ba loại delay còn lại ở đặc điểm nào?

A. Queuing delay không tồn tại trong thực tế  
B. Queuing delay là loại delay duy nhất biến thiên từ packet đến packet và phụ thuộc vào mức độ congestion — không thể xác định chính xác như các delay khác  
C. Queuing delay chỉ xuất hiện ở wireless networks  
D. Queuing delay luôn nhỏ hơn transmission delay  

> **Đáp án: B**  
> Processing, transmission, propagation delay tương đối ổn định và dự đoán được. **Queuing delay** phụ thuộc vào trạng thái queue tại thời điểm packet đến — biến thiên ngẫu nhiên, cần dùng **phân tích thống kê** (trung bình, phương sai, xác suất vượt ngưỡng).

---

**Câu 58.** *(Khó)* Traceroute hoạt động theo nguyên lý nào?

A. Gửi một packet duy nhất đến destination và đo tổng round-trip time  
B. Gửi N bộ 3 special packets đến destination, mỗi router n trên đường sẽ gửi lại message cho source khi nhận packet thứ n; source đo round-trip time đến từng router  
C. Ping từng router trên đường đi theo danh sách có sẵn  
D. Phân tích header của packets để tái tạo route  

> **Đáp án: B**  
> Traceroute dùng TTL (Time-To-Live) để "kích hoạt" từng router trả về message — source nhận được tên, địa chỉ, và RTT đến mỗi router. Mỗi thí nghiệm lặp 3 lần nên mỗi router có 3 RTT values.

---

## Phần 8 — Protocol Layers & Service Models

---

**Câu 59.** *(Dễ)* Internet protocol stack gồm bao nhiêu tầng và đó là những tầng nào (từ trên xuống)?

A. 7 tầng: Application, Presentation, Session, Transport, Network, Data Link, Physical  
B. 5 tầng: Application, Transport, Network, Link, Physical  
C. 4 tầng: Application, Transport, Network, Physical  
D. 3 tầng: Application, Network, Physical  

> **Đáp án: B**  
> **Internet protocol stack** gồm 5 tầng: **Application → Transport → Network → Link → Physical**. Khác với OSI model 7 tầng (thêm Presentation và Session).

---

**Câu 60.** *(Dễ)* Tầng **Application** chứa những giao thức nào? (Chọn đáp án đầy đủ nhất)

A. TCP và UDP  
B. IP và ICMP  
C. HTTP, SMTP, FTP, DNS  
D. Ethernet và WiFi  

> **Đáp án: C**  
> **Application layer**: HTTP (web), SMTP (email), FTP (file transfer), DNS (name resolution). Đây là tầng nơi các ứng dụng mạng và giao thức của chúng hoạt động.

---

**Câu 61.** *(Dễ)* Tầng **Transport** của Internet có hai giao thức chính. Đó là:

A. HTTP và SMTP  
B. IP và ICMP  
C. TCP và UDP  
D. Ethernet và WiFi  

> **Đáp án: C**  
> **Transport layer**: **TCP** (connection-oriented, reliable, flow control, congestion control) và **UDP** (connectionless, no-frills, không đảm bảo). Hai lựa chọn cơ bản cho ứng dụng.

---

**Câu 62.** *(Dễ)* Đơn vị dữ liệu (PDU) của mỗi tầng trong Internet stack là gì?

A. Application: message; Transport: segment; Network: datagram; Link: frame  
B. Application: packet; Transport: frame; Network: segment; Link: bit  
C. Application: frame; Transport: datagram; Network: packet; Link: message  
D. Tất cả các tầng đều gọi là packet  

> **Đáp án: A**  
> Mỗi tầng có tên PDU riêng: **message** (application), **segment** (transport), **datagram** (network), **frame** (link), **bit** (physical). Đây là quy ước chuẩn cần nhớ.

---

**Câu 63.** *(Trung bình)* Tại sao layered architecture lại có lợi trong thiết kế hệ thống mạng?

A. Vì nó giảm tổng độ trễ của mạng  
B. Vì nó cho phép thay đổi implementation của một tầng mà không ảnh hưởng các tầng khác, miễn là service interface giữ nguyên — tạo modularity  
C. Vì nó tăng tốc độ truyền dữ liệu  
D. Vì nó loại bỏ nhu cầu cần protocols  

> **Đáp án: B**  
> **Modularity** là lợi ích then chốt — có thể thay WiFi bằng 5G ở tầng Link mà Application layer không cần biết. Mỗi tầng chỉ cần cung cấp đúng service interface cho tầng trên.

---

**Câu 64.** *(Trung bình)* **Encapsulation** trong quá trình truyền dữ liệu là gì?

A. Mã hóa dữ liệu để bảo mật  
B. Mỗi tầng thêm header information của mình vào payload từ tầng trên, tạo thành đơn vị dữ liệu của tầng đó  
C. Nén dữ liệu để giảm kích thước  
D. Phân mảnh dữ liệu thành các packet nhỏ hơn  

> **Đáp án: B**  
> **Encapsulation**: Application message → Transport thêm Ht → Network thêm Hn → Link thêm Hl. Mỗi tầng "bọc" thêm header, tạo ra datagram, frame. Phía nhận thực hiện **de-encapsulation**.

---

**Câu 65.** *(Trung bình)* Router trong Internet thực hiện những tầng nào của protocol stack?

A. Chỉ tầng Physical  
B. Physical, Link, và Network (tầng 1-3)  
C. Tất cả 5 tầng  
D. Physical và Link (tầng 1-2)  

> **Đáp án: B**  
> **Routers** implement tầng 1-3 (Physical, Link, Network) — cần đến Network layer để đọc IP address và ra quyết định forwarding. **Link-layer switches** chỉ implement tầng 1-2. **Hosts** implement cả 5 tầng.

---

**Câu 66.** *(Trung bình)* OSI model có thêm 2 tầng so với Internet stack. Đó là tầng nào và chúng có vai trò gì?

A. Security layer và Management layer  
B. Presentation layer (xử lý dữ liệu: nén, mã hóa, định dạng) và Session layer (đồng bộ, quản lý phiên truyền)  
C. Routing layer và Switching layer  
D. Authentication layer và Authorization layer  

> **Đáp án: B**  
> OSI thêm **Presentation** (data compression, encryption, format) và **Session** (synchronization, checkpointing). Trong Internet, chức năng này để **application developer tự quyết định** có cần không.

---

**Câu 67.** *(Khó)* Một nhược điểm tiềm ẩn của protocol layering là gì?

A. Layering luôn làm giảm tốc độ mạng  
B. Một tầng có thể duplicate chức năng của tầng dưới (e.g., error recovery ở cả link layer và end-to-end), và thông tin cần thiết có thể bị ẩn ở tầng khác  
C. Layering không tương thích với wireless networks  
D. Layering làm phức tạp quá trình debugging  

> **Đáp án: B**  
> Hai nhược điểm của layering: (1) **duplication** — error recovery ở nhiều tầng; (2) **information hiding** — tầng n cần thông tin từ tầng khác nhưng không truy cập được. Đây là lý do một số kỹ sư phản đối strict layering.

---

**Câu 68.** *(Khó)* Trong quá trình **de-encapsulation**, điều gì xảy ra tại mỗi tầng ở phía nhận?

A. Header được thêm vào để truyền lên tầng trên  
B. Header của tầng đó được gỡ ra (stripped), payload được chuyển lên tầng cao hơn để xử lý  
C. Dữ liệu được mã hóa thêm một lần  
D. Packet bị chia nhỏ thêm  

> **Đáp án: B**  
> De-encapsulation là quá trình ngược: tầng Link gỡ Hl → tầng Network gỡ Hn → tầng Transport gỡ Ht → Application nhận được message gốc. Mỗi tầng chỉ đọc header của mình.

---

## Phần 9 — Network Security

---

**Câu 69.** *(Dễ)* **Malware** là gì?

A. Phần mềm diệt virus  
B. Phần mềm độc hại có thể xâm nhập thiết bị và gây hại (xóa file, thu thập thông tin, tấn công hệ thống khác)  
C. Giao thức bảo mật mạng  
D. Hệ thống phát hiện xâm nhập  

> **Đáp án: B**  
> **Malware** (malicious software) bao gồm viruses, worms, spyware, ransomware — xâm nhập thiết bị và thực hiện hành vi độc hại, thường lây lan qua Internet.

---

**Câu 70.** *(Dễ)* Sự khác biệt giữa **virus** và **worm** là gì?

A. Virus nhanh hơn worm trong việc lây lan  
B. Virus cần tương tác người dùng (ví dụ: mở file đính kèm), worm tự động lan truyền không cần can thiệp của người dùng  
C. Worm chỉ tấn công hệ điều hành, virus chỉ tấn công ứng dụng  
D. Virus và worm hoàn toàn giống nhau  

> **Đáp án: B**  
> **Virus**: cần user action (click, mở file). **Worm**: tự động exploit lỗ hổng và lây lan — nguy hiểm hơn vì không cần sự trợ giúp của người dùng.

---

**Câu 71.** *(Dễ)* **DoS attack** (Denial-of-Service) có mục tiêu là gì?

A. Đánh cắp dữ liệu từ server  
B. Làm cho server hoặc hạ tầng mạng không thể phục vụ người dùng hợp lệ  
C. Giải mã dữ liệu được mã hóa  
D. Giả mạo danh tính người dùng  

> **Đáp án: B**  
> **DoS attack**: render network, host, hay infrastructure **unusable** bởi legitimate users — không nhất thiết phải đánh cắp dữ liệu mà chỉ cần làm tê liệt dịch vụ.

---

**Câu 72.** *(Trung bình)* Ba loại DoS attack chính là gì?

A. Phishing, spoofing, sniffing  
B. Vulnerability attack, bandwidth flooding, connection flooding  
C. Malware, botnet, ransomware  
D. Man-in-the-middle, replay attack, SQL injection  

> **Đáp án: B**  
> Ba loại DoS: (1) **Vulnerability attack** — khai thác lỗ hổng phần mềm; (2) **Bandwidth flooding** — làm nghẽn access link bằng lượng traffic khổng lồ; (3) **Connection flooding** — tạo lượng lớn TCP half-open connections.

---

**Câu 73.** *(Trung bình)* **Distributed DoS (DDoS)** khác với DoS thông thường ở điểm nào?

A. DDoS tấn công nhiều target cùng lúc, DoS chỉ tấn công một target  
B. Attacker điều khiển nhiều compromised hosts (botnet) để đồng loạt tấn công một target, làm khó phát hiện và ngăn chặn hơn  
C. DDoS chỉ nhắm vào DNS servers  
D. DDoS dùng mã hóa, DoS không dùng  

> **Đáp án: B**  
> **DDoS**: nhiều slave hosts (botnet) đồng loạt gửi traffic đến victim → aggregate traffic rate đủ lớn để làm tê liệt server, đồng thời khó block vì đến từ nhiều nguồn khác nhau.

---

**Câu 74.** *(Trung bình)* **Packet sniffing** là gì và tại sao nó nguy hiểm?

A. Kỹ thuật tăng tốc truyền packet  
B. Passive receiver ghi lại bản sao của mọi packet đi qua kênh truyền, có thể thu thập thông tin nhạy cảm như password, dữ liệu cá nhân  
C. Kỹ thuật kiểm tra chất lượng đường truyền  
D. Cách phát hiện và xóa malware  

> **Đáp án: B**  
> **Packet sniffer** thu thập passively mọi packet (không inject packet mới) → khó phát hiện → nguy hiểm đặc biệt trên wireless và broadcast networks. Biện pháp phòng thủ chính: **mã hóa** (cryptography).

---

**Câu 75.** *(Trung bình)* **IP spoofing** là gì?

A. Làm giả tốc độ kết nối IP  
B. Tạo packet với source IP address giả mạo để giả dạng một địa chỉ đáng tin cậy  
C. Tấn công vào giao thức IP để làm tê liệt routing  
D. Chặn và chỉnh sửa IP packets trên đường truyền  

> **Đáp án: B**  
> **IP spoofing**: inject packet vào Internet với **source address giả** — receiver tin là packet từ nguồn đáng tin và thực hiện lệnh trong packet. Giải pháp: **end-point authentication**.

---

**Câu 76.** *(Khó)* Tại sao Internet ban đầu lại thiếu các cơ chế bảo mật?

A. Vì kỹ thuật mã hóa chưa được phát minh  
B. Vì Internet được thiết kế dựa trên mô hình "mutually trusting users attached to a transparent network" — không có nhu cầu bảo mật theo thiết kế gốc  
C. Vì bảo mật làm giảm hiệu suất quá nhiều  
D. Vì các quốc gia không thể thống nhất về tiêu chuẩn bảo mật  

> **Đáp án: B**  
> Internet ban đầu (ARPAnet) được xây dựng cho môi trường tin tưởng lẫn nhau — mặc định chia sẻ, không xác thực. Các vấn đề bảo mật là **hệ quả của thiết kế gốc**, không phải lỗi kỹ thuật đơn thuần.

---

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

