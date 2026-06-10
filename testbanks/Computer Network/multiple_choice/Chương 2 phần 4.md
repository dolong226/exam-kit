# Bộ câu hỏi trắc nghiệm - Chapter 2: Application Layer


## PHẦN 6 – PEER-TO-PEER APPLICATIONS (Section 2.6)

### Lý thuyết

**Câu 107.** Trong client-server file distribution, nếu có N peers, server phải transmit tổng cộng bao nhiêu bits?

A. F bits  
B. N × F bits  
C. F/N bits  
D. √N × F bits  

**Đáp án: B**  
*Giải thích: Server phải gửi 1 copy của F-bit file đến mỗi trong N peers → tổng N×F bits server phải transmit.*

---

**Câu 108.** Distribution time của client-server architecture (D_cs) được tính theo công thức nào?

A. D_cs = F/us  
B. D_cs = NF/us  
C. D_cs = max(NF/us, F/dmin)  
D. D_cs = NF/(us + Σui)  

**Đáp án: C**  
*Giải thích: D_cs = max(NF/us, F/dmin). Hai bottlenecks: (1) Server phải transmit NF bits với rate us, (2) Slowest peer cần F/dmin giây để download.*

---

**Câu 109.** Distribution time của P2P architecture (D_P2P) được tính theo công thức nào?

A. D_P2P = max(F/us, F/dmin)  
B. D_P2P = max(F/us, F/dmin, NF/(us + Σui))  
C. D_P2P = NF/us  
D. D_P2P = F/(us × N)  

**Đáp án: B**  
*Giải thích: D_P2P = max(F/us, F/dmin, NF/(us + Σui)). Ba bottlenecks: (1) Server upload rate, (2) Slowest peer download, (3) Total system upload capacity phải ≥ NF bits.*

---

**Câu 110.** Trong BitTorrent, "torrent" là gì?

A. Tracker server  
B. Collection of all peers tham gia distribute một file cụ thể  
C. Một chunk của file  
D. Phần mềm BitTorrent client  

**Đáp án: B**  
*Giải thích: Torrent là tập hợp tất cả các peers đang tham gia distribute một file cụ thể. Một torrent có thể có ít hơn 10 hoặc hơn 1000 peers.*

---

**Câu 111.** Tracker trong BitTorrent có chức năng gì?

A. Lưu trữ toàn bộ file cần phân phối  
B. Infrastructure node theo dõi peers đang tham gia torrent  
C. Mã hóa các chunks  
D. Quản lý bandwidth của mỗi peer  

**Đáp án: B**  
*Giải thích: Tracker là infrastructure node track các peers đang participate trong torrent. Khi peer join, nó register với tracker và periodic inform tracker nó vẫn đang online.*

---

**Câu 112.** BitTorrent dùng kỹ thuật gì để quyết định chunk nào request trước?

A. Random selection  
B. Rarest first – request những chunks hiếm nhất trong số các neighbors trước  
C. Largest first  
D. Sequential order  

**Đáp án: B**  
*Giải thích: "Rarest first": Alice xác định chunks mà ít neighbors có nhất và request những chunks đó trước. Mục đích: redistribute rare chunks nhanh hơn, equalize số copies của mỗi chunk.*

---

**Câu 113.** BitTorrent dùng thuật toán "tit-for-tat" cho mục đích gì?

A. Quyết định chunk nào request  
B. Quyết định gửi chunks đến neighbors nào – ưu tiên những neighbors đang feed data với rate cao nhất  
C. Tìm tracker  
D. Mã hóa data truyền đi  

**Đáp án: B**  
*Giải thích: Tit-for-tat: Alice ưu tiên gửi chunks đến 4 neighbors đang feed data cho cô ấy với rate cao nhất (unchoked). Mỗi 30 giây, chọn thêm 1 random peer (optimistically unchoked) để khuyến khích giao tiếp mới.*

---

**Câu 114.** DHT (Distributed Hash Table) là gì?

A. Loại encryption algorithm  
B. Distributed P2P database lưu trữ (key, value) pairs phân tán trên millions of peers  
C. Centralized server quản lý file sharing  
D. Protocol để mã hóa torrent  

**Đáp án: B**  
*Giải thích: DHT là distributed database implement trong P2P network, lưu (key, value) pairs phân tán. Bất kỳ peer nào cũng có thể query với một key và nhận corresponding values.*

---

**Câu 115.** Trong circular DHT, mỗi peer cần biết thông tin về bao nhiêu peers khác (tối thiểu)?

A. Chỉ 1 peer  
B. 2 peers – immediate successor và immediate predecessor  
C. N/2 peers  
D. Tất cả N peers  

**Đáp án: B**  
*Giải thích: Trong circular DHT cơ bản, mỗi peer chỉ cần biết immediate successor và immediate predecessor (modulo 2n).*

---

**Câu 116.** Trade-off trong design của DHT là gì?

A. Security vs Performance  
B. Số neighbors mỗi peer phải track vs số messages cần gửi để resolve một query  
C. Bandwidth vs Storage  
D. Latency vs Reliability  

**Đáp án: B**  
*Giải thích: Nếu mỗi peer track nhiều neighbors → ít messages per query nhưng nhiều overhead. Nếu ít neighbors (circular) → ít overhead nhưng nhiều messages (N/2 trung bình). DHT tối ưu đạt O(log N) cho cả hai.*

---

### Vận dụng

**Câu 117.** Với N = 1.000.000 peers, us = 10u (server upload = 10× peer upload), F/u = 1 giờ. Distribution time của client-server là bao nhiêu so với P2P?

A. Client-server nhanh hơn vì có dedicated server  
B. Client-server mất hàng trăm giờ (NF/us tăng linear với N), P2P dưới 1 giờ bất kể N  
C. Cả hai đều mất khoảng 1 giờ  
D. P2P chậm hơn vì cần coordinate nhiều peers  

**Đáp án: B**  
*Giải thích: Client-server: D = NF/us = 1.000.000 × (1h/10) = 100.000 giờ (tăng linear với N). P2P: ổn định dưới 1 giờ vì total upload capacity tăng cùng với N peers.*

---

**Câu 118.** Trong BitTorrent, khi Alice join torrent mới, cô ấy liên hệ với ai đầu tiên?

A. Ngay lập tức liên hệ với tất cả peers  
B. Contact tracker, nhận danh sách peers, sau đó attempt TCP connections với subset of peers đó  
C. Contact root server để tìm file  
D. Gửi broadcast để tìm peers  

**Đáp án: B**  
*Giải thích: Alice register với tracker → tracker trả về list ~50 peers → Alice attempt concurrent TCP connections với peers đó → neighboring peers là những peers TCP connection thành công.*

---

**Câu 119.** Tại sao trong BitTorrent, "optimistically unchoked" peer được chọn ngẫu nhiên mỗi 30 giây?

A. Để test network performance  
B. Để cho new peers có cơ hội nhận chunks (dù chưa upload nhiều) và tìm trading partners mới tốt hơn  
C. Để random distribute bandwidth  
D. Để reduce congestion  

**Đáp án: B**  
*Giải thích: Random "optimistically unchoked" peer cho phép: (1) New peers có thể nhận data dù chưa có gì để upload, (2) Cả hai peers có thể tìm thấy trading partners tốt hơn hiện tại.*

---

**Câu 120.** Trong DHT với n=4, peers có IDs {1, 3, 4, 5, 8, 10, 12, 15}. Key 11 được store tại peer nào?

A. Peer 10  
B. Peer 12  
C. Peer 15  
D. Peer 8  

**Đáp án: B**  
*Giải thích: Key stored tại peer có ID là closest successor của key. Key 11 → closest successor là peer 12 (12 > 11 và không có peer nào giữa 11 và 12).*

---

**Câu 121.** Trong circular DHT, nếu peer 5 đột ngột leave, peer 4 cần cập nhật state như thế nào?

A. Không cần cập nhật  
B. Peer 4 replace first successor (peer 5) bằng second successor (peer 8), rồi hỏi peer 8 về successor tiếp theo của nó  
C. Peer 4 broadcast đến tất cả peers  
D. Peer 4 contact tracker  

**Đáp án: B**  
*Giải thích: Peer 4 phát hiện peer 5 chết (không respond ping). Peer 4: (1) Set first successor = peer 8, (2) Hỏi peer 8 về ID/IP của successor của nó (peer 10) → set peer 10 làm second successor.*

---

### Vận dụng cao

**Câu 122.** Tại sao P2P distribution time không tăng tuyến tính theo N (như client-server)?

A. P2P dùng faster network  
B. Trong P2P, mỗi peer khi receive data cũng trở thành distributor; total upload capacity (us + Σui) tăng theo N, offsetting demand NF/total_capacity  
C. P2P compress dữ liệu tốt hơn  
D. P2P bypass bottleneck links  

**Đáp án: B**  
*Giải thích: Khi N tăng, demand tăng (NF bits cần distribute) nhưng total supply cũng tăng (thêm N peers × ui upload capacity). Ratio NF/(us+Σui) không nhất thiết tăng mạnh theo N.*

---

**Câu 123.** BitTorrent sử dụng Kademlia DHT như thế nào trong hệ thống của mình?

A. Để encrypt file chunks  
B. Như distributed tracker: key là torrent identifier, value là IP addresses của peers trong torrent đó; tìm peer responsible cho key để track torrent  
C. Để routing TCP connections  
D. Để compress chunks trước khi transfer  

**Đáp án: B**  
*Giải thích: BitTorrent dùng Kademlia DHT làm distributed tracker. Key = torrent ID, Value = IP của peers trong torrent. Peer mới query DHT với torrent ID để tìm tracker peer và biết list of current peers.*

---

**Câu 124.** So sánh mesh overlay với circular DHT: trade-off về số neighbors và số messages?

A. Cả hai đều tương đương  
B. Mesh: mỗi peer track N peers → 1 message per query; Circular: mỗi peer track 2 peers → N/2 messages trung bình per query; DHT với shortcuts đạt O(log N) cho cả hai  
C. Circular luôn tốt hơn mesh  
D. Mesh không thể implement trong thực tế  

**Đáp án: B**  
*Giải thích: Trade-off rõ ràng: Mesh (O(N) neighbors, O(1) messages) ↔ Circular (O(1) neighbors, O(N) messages). DHT tối ưu với shortcuts đạt O(log N) cho cả hai metric.*

---

## PHẦN 7 – SOCKET PROGRAMMING (Section 2.7)

### Lý thuyết

**Câu 125.** Sự khác biệt chính giữa UDP socket và TCP socket trong socket programming là gì?

A. UDP socket dùng AF_INET, TCP socket dùng AF_INET6  
B. UDP socket (SOCK_DGRAM) connectionless, gắn destination address mỗi packet; TCP socket (SOCK_STREAM) connection-oriented, thiết lập connection trước khi gửi data  
C. UDP socket hỗ trợ encryption, TCP socket thì không  
D. TCP socket nhanh hơn UDP socket vì connection-oriented  

**Đáp án: B**  
*Giải thích: UDP: SOCK_DGRAM, attach destination để mỗi packet, không handshaking. TCP: SOCK_STREAM, phải connect() để establish connection trước khi gửi data.*

---

**Câu 126.** Trong UDP socket programming, server phải bind() port number. Điều này có tác dụng gì?

A. Tạo TCP connection  
B. Gán port number cho server socket để packets đến port đó được directed đến socket này  
C. Encrypt communications  
D. Start listening cho TCP connections  

**Đáp án: B**  
*Giải thích: bind() gán port number cho socket. Khi packet đến server's IP tại port đó, hệ điều hành direct packet đến socket đã bind port number đó.*

---

**Câu 127.** Trong TCP socket programming, server tạo hai loại sockets. Đó là gì?

A. Send socket và receive socket  
B. Welcoming socket (serverSocket) nhận initial contacts; connection socket (connectionSocket) dedicated cho từng client  
C. Primary socket và backup socket  
D. UDP socket và TCP socket  

**Đáp án: B**  
*Giải thích: serverSocket (welcoming door): accept initial connections. connectionSocket: được tạo khi client connect, dedicated cho client đó, dùng để communicate.*

---

**Câu 128.** Lệnh serverSocket.listen(1) trong TCP server có tác dụng gì?

A. Bắt đầu gửi data  
B. Server bắt đầu listen cho TCP connection requests từ clients; parameter chỉ định max queued connections  
C. Server connect đến client  
D. Server bind port number  

**Đáp án: B**  
*Giải thích: listen() đặt server vào trạng thái chờ TCP connection requests. Parameter (1) là maximum số queued connections.*

---

**Câu 129.** Trong UDP client, khi gọi clientSocket.sendto(message, (serverName, serverPort)), thông tin nào được tự động thêm bởi OS (không cần code explicitly)?

A. Message content  
B. Source address (source IP và source port number)  
C. Destination IP address  
D. Checksum  

**Đáp án: B**  
*Giải thích: Code explicitly gán destination address. Source address (IP và port) được tự động attach bởi underlying OS, không cần lập trình viên làm thủ công.*

---

**Câu 130.** Điểm khác biệt quan trọng giữa TCPClient và UDPClient trong việc gửi data là gì?

A. TCPClient dùng UDP, UDPClient dùng TCP  
B. TCPClient chỉ cần drop bytes vào TCP connection (không cần attach destination address mỗi lần); UDPClient phải attach destination address với mỗi packet  
C. TCPClient không cần tạo socket  
D. UDPClient nhanh hơn vì gửi nhiều data hơn  

**Đáp án: B**  
*Giải thích: Sau khi TCP connection được establish, TCPClient dùng send() mà không cần specify destination. UDPClient dùng sendto() và phải include (serverName, serverPort) với mỗi message vì connectionless.*

---

### Vận dụng

**Câu 131.** Một developer muốn viết ứng dụng truyền file lớn và cần đảm bảo không mất dữ liệu. Nên chọn SOCK_DGRAM hay SOCK_STREAM?

A. SOCK_DGRAM vì nhanh hơn  
B. SOCK_STREAM vì TCP cung cấp reliable, ordered byte stream delivery  
C. SOCK_DGRAM vì ít overhead hơn  
D. Không quan trọng  

**Đáp án: B**  
*Giải thích: SOCK_STREAM = TCP socket. TCP đảm bảo reliable, ordered, error-free delivery – cần thiết cho file transfer. SOCK_DGRAM = UDP, unreliable.*

---

**Câu 132.** Trong TCP server code, tại sao connectionSocket.close() được gọi sau khi gửi response, nhưng serverSocket vẫn mở?

A. Để tiết kiệm bộ nhớ  
B. connectionSocket phục vụ client đó xong nên đóng; serverSocket (welcoming socket) tiếp tục mở để accept connections từ clients mới  
C. Cả hai nên đóng cùng lúc  
D. connectionSocket.close() cũng đóng serverSocket  

**Đáp án: B**  
*Giải thích: connectionSocket là dedicated cho một client cụ thể; sau khi phục vụ xong thì đóng. serverSocket là welcoming socket luôn open để có thể accept clients mới.*

---

**Câu 133.** Tại sao trong UDP programming, server cần extract clientAddress từ recvfrom() và dùng nó khi sendto()?

A. Để log thông tin kết nối  
B. Vì UDP connectionless, server không có dedicated connection tới client; phải dùng source address từ received packet như return address để gửi reply  
C. Để verify authentication  
D. Để check message size  

**Đáp án: B**  
*Giải thích: UDP không có pre-established connection. Server dùng clientAddress (IP + port của client) extracted từ incoming packet như "return address" để gửi reply về đúng client.*

---

**Câu 134.** Khi client TCP gọi clientSocket.connect((serverName, serverPort)), điều gì xảy ra bên dưới?

A. Chỉ gửi một message đến server  
B. Three-way handshake được thực hiện ở transport layer, thiết lập TCP connection; sau đó client có thể gửi/nhận data  
C. UDP connection được thiết lập  
D. Server tạo một process mới  

**Đáp án: B**  
*Giải thích: connect() trigger three-way handshake ở transport layer (transparent với application). Sau khi handshake xong, TCP connection được establish và application có thể gửi data.*

---

### Vận dụng cao

**Câu 135.** Khi viết một proprietary network application, developer phải cẩn thận điều gì về port numbers?

A. Phải dùng port numbers lớn hơn 1024  
B. Phải tránh dùng well-known port numbers đã được assign cho standard protocols (như 80, 25, 53); nên dùng port numbers không reserved  
C. Phải đăng ký port number với IANA  
D. Không có hạn chế nào về port numbers  

**Đáp án: B**  
*Giải thích: Well-known port numbers (như 80/HTTP, 25/SMTP, 53/DNS) đã được reserve cho standard protocols. Proprietary applications phải dùng port numbers khác để tránh conflicts.*

---

**Câu 136.** Phân biệt "open" network applications và "proprietary" network applications:

A. Open applications free, proprietary phải trả phí  
B. Open applications implement protocols defined in RFCs (publicly available), cho phép independent developers interoperate; proprietary dùng private protocols, chỉ developer đó có thể build compatible clients/servers  
C. Open applications chạy trên Linux, proprietary chạy trên Windows  
D. Không có sự khác biệt quan trọng  

**Đáp án: B**  
*Giải thích: Open (như HTTP, FTP) – spec public trong RFC, Firefox có thể talk to Apache vì cả hai follow HTTP RFC. Proprietary (như Skype) – protocol private, chỉ Skype build compatible software.*

---

## PHẦN 8 – CÂU HỎI TỔNG HỢP (Cross-Section)

### Vận dụng

**Câu 137.** Một developer cần chọn giữa client-server và P2P architecture cho một ứng dụng streaming video đến millions of users. Đâu là phân tích đúng nhất?

A. Client-server luôn tốt hơn vì có server mạnh  
B. P2P phù hợp hơn vì self-scalability: mỗi viewer cũng distribute video, không tạo linear scaling problem cho server; chi phí infrastructure thấp hơn nhiều  
C. P2P không phù hợp vì video cần reliable transfer  
D. Client-server phù hợp hơn vì P2P không hỗ trợ video  

**Đáp án: B**  
*Giải thích: Với millions of users, client-server cần server phải transmit N×F bits (bottleneck cực lớn). P2P: distribution time gần như flat với N, chi phí không tăng tuyến tính.*

---

**Câu 138.** HTTP, FTP, SMTP và DNS đều là application-layer protocols chạy trên TCP/UDP. Nhưng DNS khác ba protocols kia ở điểm quan trọng nào?

A. DNS dùng UDP, các protocols kia dùng TCP  
B. DNS không phải application users interact trực tiếp; DNS là core network function (hostname-to-IP translation) được invoke bởi các applications khác  
C. DNS không cần authentication  
D. DNS chỉ chạy trên root servers  

**Đáp án: B**  
*Giải thích: HTTP, FTP, SMTP là applications users trực tiếp dùng. DNS là "behind the scenes" service cho các applications khác dùng; users không interact trực tiếp với DNS.*

---

**Câu 139.** Web cache hoạt động giống với concept nào trong DNS?

A. DNS recursion  
B. DNS caching – cả hai cache responses để giảm latency và reduce traffic về origin (root servers cho DNS, origin web servers cho Web cache)  
C. DNS authoritative servers  
D. DNS TLD servers  

**Đáp án: B**  
*Giải thích: Cả Web cache và DNS cache đều cache responses từ "source of truth" để serve repeated requests locally, giảm latency và reduce traffic về gốc.*

---

**Câu 140.** Tại sao email cần 3 protocols (SMTP, POP3/IMAP, HTTP) trong khi Web chỉ cần HTTP?

A. Email phức tạp hơn về mặt kỹ thuật  
B. Email có sender (push: SMTP) và receiver (pull: POP3/IMAP/HTTP) phases với khác nhau về direction; SMTP là push protocol không phù hợp để retrieve mail  
C. Email cần encryption nhiều hơn  
D. Email support nhiều file formats hơn  

**Đáp án: B**  
*Giải thích: SMTP (push) để transfer mail giữa servers. Nhưng users retrieve mail là pull operation – cần POP3/IMAP (hoặc HTTP cho web email). SMTP không thể dùng để pull vì nó là push protocol.*

---

**Câu 141.** Khi Alice gửi email cho Bob, con đường của email là gì?

A. Alice's agent → Bob's agent trực tiếp  
B. Alice's agent → (SMTP) → Alice's mail server → (SMTP) → Bob's mail server → (POP3/IMAP/HTTP) → Bob's agent  
C. Alice's agent → DNS server → Bob's mail server → Bob's agent  
D. Alice's agent → (HTTP) → Alice's mail server → (SMTP) → Bob's mail server  

**Đáp án: B**  
*Giải thích: Đường đi chuẩn: Alice's UA dùng SMTP gửi đến Alice's server → Alice's server dùng SMTP relay đến Bob's server → Bob's UA dùng POP3/IMAP/HTTP pull từ Bob's server.*

---

**Câu 142.** Cả HTTP và SMTP đều dùng persistent connections. Điểm khác nhau quan trọng là gì?

A. HTTP nhanh hơn SMTP  
B. HTTP là pull protocol (client pull data từ server); SMTP là push protocol (sender push đến receiver); TCP connection initiated bởi machine muốn receive (HTTP) vs muốn send (SMTP)  
C. SMTP dùng encryption, HTTP không  
D. HTTP hỗ trợ binary data, SMTP không  

**Đáp án: B**  
*Giải thích: HTTP: Pull – TCP initiated bởi machine muốn receive file. SMTP: Push – TCP initiated bởi machine muốn send file. Đây là fundamental architectural difference.*

---

**Câu 143.** Tổng số DNS messages khi cis.poly.edu hỏi gaia.cs.umass.edu với 4 levels (host → local → root → TLD → authoritative) dùng iterative queries là bao nhiêu?

A. 4 messages  
B. 6 messages  
C. 8 messages  
D. 10 messages  

**Đáp án: C**  
*Giải thích: 8 messages: 4 query messages (host→local, local→root, local→TLD, local→authoritative) + 4 reply messages (mỗi pair) = 8 tổng cộng.*

---

**Câu 144.** Một application gửi data ở rate 32 kbps. Tại sao nên dùng UDP thay vì TCP cho ứng dụng này?

A. Vì UDP có throughput guarantee 32 kbps  
B. Vì TCP's congestion control có thể throttle application xuống dưới 32 kbps khi mạng tắc; UDP bypass congestion control, cho phép application pump at desired rate  
C. Vì UDP nhanh hơn TCP trong mọi tình huống  
D. Vì TCP không hỗ trợ real-time applications  

**Đáp án: B**  
*Giải thích: TCP congestion control có thể reduce sending rate khi network congested, xuống dưới required 32 kbps. UDP không có congestion control nên sender có thể transmit at desired rate (dù actual throughput phụ thuộc network).*

---

**Câu 145.** Tại sao data centers (với hundreds of thousands of servers) thay thế single server trong client-server architecture cho các large-scale services?

A. Vì single server đắt hơn data center  
B. Vì single server không thể handle requests từ hàng triệu concurrent clients; data center tạo powerful virtual server bằng cách distribute load  
C. Vì data center dễ bảo mật hơn  
D. Vì data center sử dụng P2P protocols  

**Đáp án: B**  
*Giải thích: Popular services (Google, Amazon, Facebook) nhận hàng tỷ requests; single server sẽ overwhelmed. Data center với hàng trăm nghìn servers distribute load để create a virtually powerful server.*

---

### Vận dụng cao

**Câu 146.** Một social networking app muốn track user's IP address qua servers (server-tracked) nhưng gửi messages trực tiếp user-to-user (P2P messages). Đây là kiến trúc gì?

A. Pure client-server  
B. Pure P2P  
C. Hybrid architecture – kết hợp client-server (track IPs via servers) và P2P (direct user-to-user messages)  
D. Overlay network  

**Đáp án: C**  
*Giải thích: Đây là hybrid architecture (như nhiều instant messaging apps): servers track IP addresses (client-server element), nhưng actual messages đi trực tiếp P2P mà không qua servers.*

---

**Câu 147.** Phân tích tại sao Internet telephony có thể hoạt động ổn dù không có timing guarantees từ transport layer?

A. Vì Internet có timing guarantees ẩn  
B. Applications được thiết kế để "cope" – dùng buffering, adaptive coding, jitter compensation; trong thực tế delay thường đủ nhỏ để acceptable  
C. VoIP apps dùng secret protocols với timing guarantees  
D. Không thể, Internet telephony không hoạt động tốt  

**Đáp án: B**  
*Giải thích: Dù không có guarantees, Internet thường provide satisfactory service. VoIP apps dùng clever design tricks: playback buffers, adaptive coding rates, packet loss concealment để cope với variable delay và loss.*

---

**Câu 148.** Trong thiết kế Web cache, nếu một object có thể stale (cached nhưng đã bị modify ở origin), cơ chế nào giải quyết vấn đề này mà không cần luôn fetch từ origin?

A. Cache tự động refresh mỗi phút  
B. Conditional GET với If-Modified-Since: nếu object chưa thay đổi, server trả 304 Not Modified (không có body), cache dùng bản đang có; chỉ fetch khi thực sự changed  
C. Cache không giải quyết được vấn đề này  
D. Cache dùng hash để verify freshness  

**Đáp án: B**  
*Giải thích: Conditional GET là elegant solution: kiểm tra staleness với minimal overhead. Nếu object unchanged → 304 (không tốn bandwidth truyền object). Nếu changed → 200 OK với fresh object.*

---

**Câu 149.** Tại sao DHT được gọi là "Distributed Hash Table" – vai trò của "hash" là gì?

A. DHT mã hóa data bằng hash function  
B. Hash function map non-integer keys (như content names, social security numbers) sang integer IDs trong range [0, 2n-1] – cùng space với peer IDs – cho phép assign keys to peers một cách deterministic  
C. Hash function để compress data  
D. Hash function verify tính toàn vẹn của data  

**Đáp án: B**  
*Giải thích: Hash function là cầu nối: chuyển arbitrary keys (strings) thành integers trong cùng không gian với peer IDs. Nhờ đó có thể define rule "assign key to closest peer" một cách nhất quán.*

---

**Câu 150.** Một company triển khai Web cache với hit rate 0.6. Access link của company là 10 Mbps. Average object 1 Mbit, request rate 8 req/sec. Không có cache, traffic intensity trên access link là:

A. 0.3  
B. 0.6  
C. 0.8  
D. 1.0  

**Đáp án: C**  
*Giải thích: Traffic intensity = (8 req/s × 1 Mbit) / 10 Mbps = 8/10 = 0.8. Với cache (hit rate 0.6), chỉ 40% requests qua access link: intensity = 0.8 × 0.4 = 0.32, giảm đáng kể.*

---

**Câu 151.** Phân tích: tại sao "rarest first" trong BitTorrent giúp hệ thống hoạt động hiệu quả hơn "random first"?

A. Rarest first download nhanh hơn về tốc độ bits  
B. Rarest first equalize số copies của mỗi chunk trong torrent; nếu dùng random, một số chunks có thể trở nên cực kỳ hiếm khi ít peers có nó, gây bottleneck vào cuối download  
C. Rarest first ít tiêu tốn bandwidth hơn  
D. Rarest first secure hơn  

**Đáp án: B**  
*Giải thích: Rarest first ensures chunks được redistribute trước khi trở nên "critically rare". Nếu một chunk chỉ còn 1 peer có, nó có thể trở thành bottleneck. Rarest first prevent scenario này bằng cách prioritize redistribution của rare chunks.*

---

**Câu 152.** Tại sao P2P architecture gặp thách thức về "Security" nhiều hơn client-server?

A. P2P không dùng encryption  
B. P2P nature high-distributed và open: không có single point of control/trust, bất kỳ peer nào cũng tham gia, khó verify identity, khó enforce security policies  
C. P2P dùng protocol yếu hơn  
D. P2P không có authentication  

**Đáp án: B**  
*Giải thích: P2P không có central authority để verify participants, enforce policies, hay audit behavior. Attackers có thể join P2P network và behave maliciously. Đây là fundamental challenge của distributed open systems.*

---

**Câu 153.** Khi access link của một institution bị congested (traffic intensity ≈ 1), có hai giải pháp: upgrade link hoặc install cache. So sánh hai giải pháp:

A. Upgrade link luôn tốt hơn  
B. Cả hai giảm access link intensity; nhưng cache rẻ hơn (public-domain software trên inexpensive PCs) và có thể hiệu quả hơn upgrade link nếu hit rate đủ cao  
C. Cache không giúp ích gì  
D. Upgrade link là option duy nhất  

**Đáp án: B**  
*Giải thích: Upgrade link 15→100 Mbps giảm intensity xuống 0.15 (delay ~2s). Cache với hit rate 0.4 giảm intensity xuống 0.6 (delay ~1.2s), thậm chí tốt hơn về response time với chi phí thấp hơn nhiều.*

---

**Câu 154.** Liên hệ giữa DNS và layered architecture: DNS là application-layer protocol nhưng phục vụ cho các application-layer protocols khác. Điều này minh họa nguyên tắc gì?

A. DNS là transport-layer protocol  
B. Nguyên tắc "edge complexity": much of Internet's complexity được đặt ở edge (end systems). DNS implement critical name-to-address translation ở application layer (edge), không cần modify network core  
C. DNS vi phạm layer principle  
D. DNS là exception, không có ý nghĩa thiết kế  

**Đáp án: B**  
*Giải thích: DNS minh họa edge-based design: core function (hostname resolution) được implement ở application layer tại edge, không cần routers/core biết về DNS. Reflects Internet design philosophy: put complexity at edges.*

---

**Câu 155.** Trong socket programming với TCP, nếu server cần phục vụ nhiều clients đồng thời, giải pháp đơn giản nhất là gì?

A. Dùng nhiều server ports  
B. Sau khi serverSocket.accept() tạo connectionSocket cho client mới, server spawn a new thread/process để handle connectionSocket đó, trong khi main process tiếp tục listen cho connections mới  
C. Dùng UDP thay vì TCP  
D. Chỉ có thể phục vụ một client tại một thời điểm  

**Đáp án: B**  
*Giải thích: Classic pattern cho concurrent TCP servers: main loop accept() → spawn thread/process với connectionSocket → main loop quay lại accept() để serve clients khác. Mỗi connectionSocket được handled independently.*

---
