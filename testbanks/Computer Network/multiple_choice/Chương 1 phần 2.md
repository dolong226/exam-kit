# Bộ câu hỏi trắc nghiệm — Chương 1: Computer Networks and the Internet


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
