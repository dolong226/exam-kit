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
