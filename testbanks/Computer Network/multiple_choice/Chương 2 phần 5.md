# Bộ câu hỏi trắc nghiệm - Chapter 2: Application Layer





## PHẦN 9 – CÂU HỎI BỔ SUNG VÀ NÂNG CAO

**Câu 156.** Một URL như http://www.someSchool.edu/someDept/pic.gif gồm những thành phần nào?

A. Protocol, port, và file name  
B. Protocol (http), hostname (www.someSchool.edu), và path name (/someDept/pic.gif)  
C. IP address, port, và file name  
D. Protocol, DNS name, và checksum  

**Đáp án: B**  
*Giải thích: URL gồm: hostname của server chứa object và path name của object. Browser parse hostname để DNS lookup, sau đó request object theo path.*

---

**Câu 157.** Trong HTTP/1.1 (default), connections là persistent hay non-persistent?

A. Non-persistent by default  
B. Persistent by default với pipelining  
C. Non-persistent với pipelining  
D. Depends on server  

**Đáp án: B**  
*Giải thích: Default mode của HTTP là persistent connections với pipelining. Non-persistent phải được configured explicitly (e.g., qua "Connection: close" header).*

---

**Câu 158.** HTTP status code "301 Moved Permanently" có ý nghĩa gì?

A. Request thành công  
B. Object đã bị moved vĩnh viễn; URL mới được specify trong Location header; client software tự động retrieve từ URL mới  
C. Server bị down  
D. Authentication required  

**Đáp án: B**  
*Giải thích: 301 Moved Permanently – object đã move đến URL mới. Response chứa Location header với new URL. Client software (browser) tự động redirect đến new URL.*

---

**Câu 159.** Trong POP3, lệnh nào được dùng để retrieve một message cụ thể?

A. GET  
B. FETCH  
C. retr  
D. DOWNLOAD  

**Đáp án: C**  
*Giải thích: Trong POP3 transaction phase, lệnh "retr [number]" dùng để retrieve (download) một message cụ thể. Các lệnh khác: list (liệt kê), dele (đánh dấu xóa), quit.*

---

**Câu 160.** Tại sao trong SMTP transcript, client gửi một dòng chỉ chứa dấu chấm "." trên một dòng riêng?

A. Để compress message  
B. Để indicate end of message (end of DATA)  
C. Để bắt đầu một message mới  
D. Để kiểm tra connection  

**Đáp án: B**  
*Giải thích: Trong SMTP, sau phần DATA, một dòng chỉ chứa "." (CRLF.CRLF) signal end of message. Server nhận dấu này và biết message đã complete.*

---

**Câu 161.** Tại sao local DNS servers thường có thể bypass root DNS servers?

A. Local servers có authority cao hơn root servers  
B. Local servers cache IP addresses của TLD servers từ previous queries; không cần hỏi root servers nếu đã biết TLD server  
C. Root servers block queries từ local servers  
D. Local servers resolve tất cả queries locally  

**Đáp án: B**  
*Giải thích: DNS caching cho phép local DNS server cache IPs của TLD servers. Với hầu hết queries, local server đã biết TLD server nào cần contact → bypass root servers hoàn toàn.*

---

**Câu 162.** Trong P2P circular DHT với n bits, identifier space có bao nhiêu possible values?

A. n values  
B. 2n values  
C. n² values  
D. 2^n values  

**Đáp án: D**  
*Giải thích: Identifier space là [0, 2^n - 1], có tổng 2^n possible integer values. Mỗi identifier được represent bằng n bits.*

---

**Câu 163.** IMAP có feature nào mà POP3 không có, hữu ích khi connection tới mail server có bandwidth thấp?

A. IMAP compress email  
B. IMAP cho phép fetch chỉ message header hoặc chỉ một part của MIME message, tránh download toàn bộ large attachments không cần thiết  
C. IMAP không cần authentication  
D. IMAP dùng UDP để nhanh hơn  

**Đáp án: B**  
*Giải thích: IMAP commands cho phép fetch chỉ headers hoặc specific parts của message. Hữu ích với low-bandwidth connections: user có thể xem subject/sender trước khi quyết định download full message.*

---

**Câu 164.** Tại sao Web servers sử dụng "stateless protocol" lại là lợi thế cho scalability?

A. Stateless giúp encrypt messages nhanh hơn  
B. Server không cần allocate resources để duy trì session state cho mỗi client; có thể handle nhiều concurrent connections hơn với cùng memory/processing  
C. Stateless giúp server verify client nhanh hơn  
D. Stateless giúp reduce bandwidth  

**Đáp án: B**  
*Giải thích: Stateless design: mỗi request self-contained, server xử lý xong là forget. Không cần maintain per-client state → tiết kiệm memory và processing → scale to thousands of concurrent connections.*

---

**Câu 165.** Trong BitTorrent, "choked" peers là gì?

A. Peers đã download xong file  
B. Peers không nhận chunks từ Alice (vì không trong top 4 uploaders và không phải optimistically unchoked peer hiện tại)  
C. Peers có bandwidth thấp  
D. Peers bị tracker block  

**Đáp án: B**  
*Giải thích: Alice unchoke 4 top uploaders và 1 random optimistic peer. Tất cả các peers khác là "choked" – không nhận chunks từ Alice trong interval đó.*

---

**Câu 166.** HTTP KHÔNG stateless hoàn toàn trong thực tế vì lý do gì?

A. Vì HTTP dùng TCP  
B. Vì cookies tạo user session layer trên HTTP stateless, cho phép server track users across multiple requests  
C. Vì persistent connections maintain state  
D. Vì SSL thêm state  

**Đáp án: B**  
*Giải thích: HTTP bản thân là stateless, nhưng cookies tạo một lớp "state" ở application level: server có thể identify và track user qua cookie ID, effectively creating session state.*

---

**Câu 167.** Trong DNS man-in-the-middle attack, attacker làm gì?

A. Attacker flood DNS servers với packets  
B. Attacker intercept queries từ hosts và return bogus replies, có thể redirect users đến attacker's website  
C. Attacker insert malicious records vào DNS server's cache  
D. Attacker tắt DNS servers  

**Đáp án: B**  
*Giải thích: Man-in-the-middle attack: attacker sit between client và DNS server, intercept legitimate queries và send bogus replies với attacker-controlled IPs, redirecting users.*

---

**Câu 168.** Trong DNS poisoning attack, attacker làm gì?

A. Attacker DDoS DNS servers  
B. Attacker gửi bogus replies đến DNS server, trick server accept và cache bogus records vào cache của nó  
C. Attacker intercept DNS queries  
D. Attacker thay đổi physical DNS server hardware  

**Đáp án: B**  
*Giải thích: DNS poisoning (cache poisoning): attacker inject bogus records vào DNS cache. Các hosts sau đó query server này sẽ nhận bogus records, bị redirect đến attacker's sites.*

---

**Câu 169.** Nếu thêm shortcuts vào circular DHT, có thể đạt được complexity O(log N) cho cả số neighbors và số messages. Tại sao O(log N) là acceptable?

A. O(log N) là tối ưu tuyệt đối  
B. O(log N) tăng rất chậm với N: với N = 1 triệu peers, log₂(1M) ≈ 20 neighbors và 20 messages – hoàn toàn manageable so với N = 1M  
C. O(log N) tương đương O(1)  
D. O(log N) không scalable  

**Đáp án: B**  
*Giải thích: O(log N) là excellent scaling. Dù N tăng 1000x, số neighbors/messages chỉ tăng thêm ~10. Đây là practical "sweet spot" giữa memory overhead (neighbors) và communication overhead (messages).*

---

**Câu 170.** Khi một trang web được phân phối qua CDN (như Akamai), request resolution xảy ra như thế nào?

A. Client trực tiếp connect đến Akamai headquarters  
B. DNS resolution được sử dụng để direct client đến CDN cache gần nhất; khi browser resolves hostname, Akamai's DNS trả về IP của cache server gần client nhất  
C. Client broadcast để tìm CDN node gần nhất  
D. CDN không liên quan đến DNS  

**Đáp án: B**  
*Giải thích: CDN dùng DNS-based redirection: khi client resolve content hostname, CDN's DNS server trả về IP của geographically/topologically close cache server, không phải origin. Đây là core CDN mechanism.*

---

**Câu 171.** Phân tích tại sao tit-for-tat là crucial cho sự tồn tại của BitTorrent:

A. Tit-for-tat encrypt data tốt hơn  
B. Nếu không có tit-for-tat (hoặc tương đương), majority of users sẽ là freeriders (chỉ download, không upload), làm sụp đổ hệ thống vì không đủ upload capacity để phân phối file  
C. Tit-for-tat giúp tìm file nhanh hơn  
D. Tit-for-tat giúp tracker track peers tốt hơn  

**Đáp án: B**  
*Giải thích: Tit-for-tat tạo incentive: nếu bạn không upload, không ai upload cho bạn. Điều này khuyến khích users contribute bandwidth. Nếu không có mechanism này, BitTorrent có thể fail vì freerider problem.*

---

**Câu 172.** Khi một FTP session bắt đầu, thứ tự các connections được thiết lập là gì?

A. Data connection trước, sau đó control connection  
B. Control connection (port 21) được thiết lập trước và maintain suốt session; data connection (port 20) được tạo mỗi khi cần transfer file  
C. Cả hai được thiết lập đồng thời  
D. Không cần control connection nếu đã authenticate  

**Đáp án: B**  
*Giải thích: Client initiate control connection đến server port 21 trước. Qua control connection, user gửi credentials và commands. Mỗi file transfer tạo một new data connection, sau đó close.*

---

**Câu 173.** Tại sao SMTP trong năm 2023 vẫn yêu cầu 7-bit ASCII cho message body là một "archaic characteristic"?

A. ASCII không secure  
B. Thiết kế 1982 khi bandwidth khan hiếm và không có multimedia; ngày nay không ai email chỉ text thuần ASCII; phải encode images/binary sang ASCII rồi decode lại – không cần thiết và inefficient  
C. ASCII không hỗ trợ Unicode  
D. ASCII không có error correction  

**Đáp án: B**  
*Giải thích: 7-bit ASCII limit là legacy constraint hợp lý năm 1982 nhưng problematic ngày nay: mọi attachment phải encode (Base64 thường) tăng kích thước 33%, và phải decode. HTTP không có hạn chế này.*

---

**Câu 174.** Trong P2P DHT, tại sao cần peer phải track cả first và second successors (không chỉ first successor) để handle churn?

A. Để tăng tốc độ query  
B. Nếu first successor đột ngột leave (peer churn), peer cần biết second successor để maintain connectivity trong ring; nếu chỉ track first successor, ring sẽ bị broken  
C. Để cân bằng load  
D. Để security  

**Đáp án: B**  
*Giải thích: P2P systems có high churn rate. Nếu peer chỉ biết first successor và successor đó leave đột ngột, peer không biết successor tiếp theo → ring bị broken. Second successor là backup cho continuity.*

---

**Câu 175.** Xét kịch bản: traffic intensity trên access link = 0.97. Nếu thêm Web cache với hit rate 0.3, traffic intensity mới trên access link là bao nhiêu?

A. 0.97  
B. 0.679  
C. 0.3  
D. 0.7  

**Đáp án: B**  
*Giải thích: Chỉ (1-0.3) = 70% requests đi qua access link. Traffic intensity mới = 0.97 × 0.7 = 0.679. Giảm từ 0.97 (gần bão hòa) xuống 0.679 (manageable).*

---

**Câu 176.** Điểm giống nhau cơ bản giữa HTTP và SMTP là gì?

A. Cả hai đều stateless  
B. Cả hai truyền files giữa các hosts dùng TCP, cả hai dùng persistent connections, cả hai dùng human-readable (ASCII) command/header format  
C. Cả hai dùng cùng port number  
D. Cả hai không cần authentication  

**Đáp án: B**  
*Giải thích: HTTP và SMTP: cả hai transfer files dùng TCP, dùng persistent connections, dùng ASCII-readable message format với headers và command lines. Khác nhau ở push/pull nature và ASCII restriction của SMTP.*

---

**Câu 177.** Tại sao application-layer protocol được phân biệt với network application?

A. Không có sự phân biệt  
B. Application-layer protocol (như HTTP) là chỉ một component của network application (như Web); Web application còn gồm HTML format, browsers, servers – protocol chỉ là "giao thức giao tiếp" của application  
C. Application-layer protocol là tầng dưới của application  
D. Network application không cần application-layer protocol  

**Đáp án: B**  
*Giải thích: Web application = HTML format + browsers (Firefox, Chrome) + web servers (Apache, Nginx) + HTTP protocol. HTTP là một piece (albeit important) chứ không phải toàn bộ Web application.*

---

**Câu 178.** Peer trong BitTorrent có thể "selfishly" leave torrent sau khi download xong. Điều gì ngăn mọi peer làm vậy?

A. BitTorrent protocol block peers rời torrent  
B. Không có mechanism kỹ thuật bắt buộc; sự thành công của BitTorrent phụ thuộc vào users altruistically ở lại seed; tit-for-tat incentivize sharing khi đang download nhưng không bắt buộc seeding  
C. Tracker track và block peers rời sớm  
D. ISP block peers rời torrent  

**Đáp án: B**  
*Giải thích: BitTorrent không có hard enforcement cho seeding sau khi download. Tit-for-tat hoạt động trong download phase (trading). Seeding sau đó là voluntary/altruistic. Đây cũng là lý do "leech vs seed ratio" quan trọng trong cộng đồng.*

---

**Câu 179.** Khi một Web page chứa 10 objects và browser mở 5 parallel TCP connections (non-persistent mode), cần bao nhiêu TCP connections và bao nhiêu RTTs để fetch tất cả?

A. 10 connections, 20 RTTs  
B. 11 connections tổng cộng (1 cho HTML + 10 cho objects); với parallel connections, chỉ cần 2 RTTs cho HTML + 2 RTTs cho 10 objects (2 rounds × 5 parallel)  
C. 5 connections, 10 RTTs  
D. 10 connections, 10 RTTs  

**Đáp án: B**  
*Giải thích: HTML: 1 connection, 2 RTTs. 10 objects với 5 parallel: 2 rounds (5+5), mỗi round 2 RTTs → 4 RTTs cho objects. Total: ~6 RTTs và 11 TCP connections. Parallel giảm đáng kể so với serial (20+ RTTs).*

---

**Câu 180.** Tại sao DNS được thiết kế là distributed system thay vì centralized?

A. Vì distributed systems rẻ hơn  
B. Centralized DNS sẽ có: single point of failure, không scale được với traffic volume khổng lồ, latency cao cho users xa, và maintenance database cực lớn cập nhật constant – tất cả không thể chấp nhận được với Internet scale  
C. Vì DNS không cần centralized authority  
D. Vì centralized DNS sẽ quá secure  

**Đáp án: B**  
*Giải thích: Centralized design fail ở Internet scale về reliability (SPOF), scalability (traffic), performance (latency), và maintainability. DNS hierarchical distributed design giải quyết tất cả issues này.*
