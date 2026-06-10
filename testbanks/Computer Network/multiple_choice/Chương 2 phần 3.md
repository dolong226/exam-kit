# Bộ câu hỏi trắc nghiệm - Chapter 2: Application Layer



## PHẦN 4 – ELECTRONIC MAIL IN THE INTERNET (Section 2.4)

### Lý thuyết

**Câu 68.** Ba major components của Internet e-mail system là gì?

A. User agents, email clients, và SMTP  
B. User agents, mail servers, và SMTP  
C. Mail servers, DNS servers, và POP3  
D. SMTP, IMAP, và POP3  

**Đáp án: B**  
*Giải thích: Ba components chính: user agents (đọc/viết email), mail servers (mailboxes, message queues), và SMTP (protocol truyền mail).*

---

**Câu 69.** SMTP là gì và dùng protocol tầng dưới nào?

A. Simple Mail Transfer Protocol; dùng UDP  
B. Simple Mail Transfer Protocol; dùng TCP  
C. Secure Mail Transfer Protocol; dùng SSL  
D. Standard Mail Transfer Protocol; dùng IP  

**Đáp án: B**  
*Giải thích: SMTP (Simple Mail Transfer Protocol) là application-layer protocol chính cho Internet email, sử dụng TCP's reliable data transfer service để truyền mail.*

---

**Câu 70.** SMTP có giới hạn quan trọng gì về format của message?

A. Chỉ hỗ trợ file nhỏ hơn 10MB  
B. Yêu cầu toàn bộ message body phải ở dạng 7-bit ASCII  
C. Không hỗ trợ attachments  
D. Chỉ truyền text, không có hình ảnh  

**Đáp án: B**  
*Giải thích: SMTP là legacy technology, yêu cầu body của mọi messages phải ở dạng 7-bit ASCII. Binary data (images, audio) phải được encode sang ASCII trước khi gửi.*

---

**Câu 71.** SMTP là push hay pull protocol?

A. Pull protocol  
B. Push protocol  
C. Cả hai tùy cấu hình  
D. Không phải pull cũng không phải push  

**Đáp án: B**  
*Giải thích: SMTP là push protocol – sending mail server pushes email đến receiving mail server. TCP connection được initiate bởi machine muốn gửi file.*

---

**Câu 72.** Tại sao SMTP thường không dùng intermediate mail servers?

A. Vì SMTP không hỗ trợ routing  
B. SMTP direct connection từ sender's server đến recipient's server; nếu recipient's server down, message ở lại sender's server và retry sau  
C. Vì intermediate servers sẽ đọc nội dung email  
D. Vì intermediate servers quá đắt  

**Đáp án: B**  
*Giải thích: SMTP tạo direct TCP connection giữa sending và receiving mail servers. Nếu Bob's server down, Alice's server giữ message và retry (thường mỗi 30 phút) cho đến khi thành công hoặc hết thời gian.*

---

**Câu 73.** So sánh SMTP và HTTP: điểm khác biệt về cách handle document gồm text và images?

A. SMTP không hỗ trợ images  
B. HTTP encapsulates mỗi object trong HTTP response riêng; SMTP đặt tất cả objects của message vào một message  
C. HTTP không hỗ trợ attachments  
D. Cả hai xử lý giống nhau  

**Đáp án: B**  
*Giải thích: HTTP encapsulates từng object (text, image) trong HTTP response message riêng. SMTP đặt tất cả objects (cả text lẫn attachments sau khi encode) vào một message duy nhất.*

---

**Câu 74.** POP3 protocol hoạt động qua ba phases nào theo thứ tự?

A. Authentication → Update → Transaction  
B. Connection → Authorization → Transfer  
C. Authorization → Transaction → Update  
D. Login → Download → Logout  

**Đáp án: C**  
*Giải thích: POP3 gồm 3 phases: (1) Authorization – authenticate user, (2) Transaction – retrieve/delete messages, (3) Update – thực hiện các deletion sau khi quit.*

---

**Câu 75.** IMAP khác POP3 ở điểm quan trọng nào?

A. IMAP nhanh hơn POP3  
B. IMAP maintain user state information across sessions và cho phép tạo remote folders, quản lý mail trên server  
C. IMAP không yêu cầu authentication  
D. POP3 hỗ trợ nhiều folders hơn IMAP  

**Đáp án: B**  
*Giải thích: IMAP maintain state across sessions (folder names, message-folder associations) và cho phép manage mail trên server. POP3 không có server-side state across sessions và không có remote folder management.*

---

**Câu 76.** Tại sao user agent thường không dialogue trực tiếp với recipient's mail server bằng SMTP?

A. Vì SMTP quá phức tạp  
B. Vì user agent không thể handle trường hợp recipient's server down; cần relay qua sender's mail server để retry  
C. Vì recipient's server chỉ nhận từ trusted servers  
D. Vì SMTP không hỗ trợ direct connections  

**Đáp án: B**  
*Giải thích: Nếu user agent gửi trực tiếp và recipient's server down, email bị mất. Qua sender's mail server, server có thể hold và retry. Sender's server là "reliable middleman".*

---

**Câu 77.** Web-based email (như Gmail) dùng protocol gì giữa browser và mail server?

A. SMTP để cả gửi lẫn nhận  
B. POP3 để cả gửi lẫn nhận  
C. HTTP giữa browser và mail server; SMTP giữa các mail servers  
D. IMAP cho tất cả  

**Đáp án: C**  
*Giải thích: Web email dùng HTTP giữa browser và mail server (thay vì POP3/IMAP để receive và SMTP để send). Nhưng giữa các mail servers, vẫn dùng SMTP.*

---

**Câu 78.** Email header line nào là bắt buộc (required) theo RFC 5322?

A. Subject: và Date:  
B. From: và To:  
C. Content-Type: và MIME-Version:  
D. Reply-To: và Cc:  

**Đáp án: B**  
*Giải thích: Theo RFC 5322, mọi email header phải có From: và To:. Subject: và các header khác là optional.*

---

### Vận dụng

**Câu 79.** Bob thường check email từ nhiều thiết bị (laptop, phone, máy tính công ty). POP3 "download-and-delete" mode có phù hợp không?

A. Có, vì download-and-delete nhanh hơn  
B. Không, vì sau khi download ở một thiết bị, email bị xóa khỏi server và các thiết bị khác không thể truy cập  
C. Có, vì mode này encrypt email tốt hơn  
D. Không, vì download-and-delete không hoạt động trên mobile  

**Đáp án: B**  
*Giải thích: Với download-and-delete, email bị xóa khỏi server sau khi download từ một thiết bị. Bob sẽ không thể truy cập email đó từ các thiết bị khác. Nên dùng IMAP hoặc download-and-keep.*

---

**Câu 80.** Tại sao SMTP encode binary data (như image) sang 7-bit ASCII trước khi gửi, trong khi HTTP thì không?

A. Vì SMTP cần nén dữ liệu  
B. SMTP là legacy protocol được thiết kế trong thời kỳ bandwidth khan hiếm và chỉ xử lý ASCII; HTTP được thiết kế sau nên linh hoạt hơn với data types  
C. Vì SMTP cần security  
D. HTTP không hỗ trợ binary data  

**Đáp án: B**  
*Giải thích: SMTP RFC gốc từ 1982 giới hạn body 7-bit ASCII do constraints thời đó. HTTP được thiết kế sau (1990s) không có hạn chế này và có thể carry binary data trực tiếp.*

---

**Câu 81.** Một SMTP session transcript có lệnh "RCPT TO: <bob@hamburger.edu>". Lệnh này có tác dụng gì?

A. Xác định người gửi  
B. Xác định người nhận email  
C. Bắt đầu truyền nội dung email  
D. Kết thúc session  

**Đáp án: B**  
*Giải thích: RCPT TO chỉ định email address của recipient. MAIL FROM chỉ định sender. DATA bắt đầu truyền nội dung.*

---

**Câu 82.** Nếu Alice's mail server down khi cô ấy muốn gửi email, điều gì xảy ra?

A. Email bị mất ngay lập tức  
B. User agent của Alice gửi trực tiếp đến Bob's server  
C. Không có gì xảy ra; email không thể gửi cho đến khi Alice's server lên lại  
D. Alice có thể complain với system administrator; server sẽ retry khi online trở lại  

**Đáp án: D**  
*Giải thích: Đây là lợi thế của việc relay qua Alice's mail server. Nếu Alice's server down, Alice có thể complain với sysadmin. Khi server lên lại, nó sẽ retry việc gửi.*

---

### Vận dụng cao

**Câu 83.** Phân tích tại sao email system cần 2-step procedure (user agent → sender's server → recipient's server) thay vì direct (user agent → recipient's server)?

A. Vì SMTP không cho phép direct connections  
B. Vì user agent không có cơ chế retry khi recipient's server down; relay qua sender's server tạo reliable intermediate store-and-forward; nếu recipient's server down, sender's server retry tự động  
C. Vì user agent không biết IP của recipient's server  
D. Vì direct connection sẽ không secure  

**Đáp án: B**  
*Giải thích: 2-step procedure đảm bảo reliability: sender's server có thể retry nhiều lần (mỗi 30 phút) cho đến thành công. User agent thường offline và không thể retry. Đây là store-and-forward design.*

---

**Câu 84.** Tại sao IMAP là lựa chọn tốt hơn POP3 cho người dùng nomadic (dùng nhiều thiết bị)?

A. IMAP nhanh hơn POP3  
B. IMAP maintain server-side folder hierarchy và state across sessions; user có thể truy cập cùng mail structure từ bất kỳ device nào; POP3 chỉ quản lý mail cục bộ trên từng device  
C. IMAP encrypt email tốt hơn  
D. IMAP dùng ít bandwidth hơn POP3  

**Đáp án: B**  
*Giải thích: IMAP giữ folders và mail trên server, maintain state across sessions. Dù dùng device nào, user thấy cùng một mailbox structure. POP3 thường download mail về local, tạo sự không nhất quán giữa các devices.*

---

## PHẦN 5 – DNS (Section 2.5)

### Lý thuyết

**Câu 85.** DNS là gì? Hãy chọn định nghĩa đầy đủ nhất:

A. Một Web server đặc biệt  
B. Hệ thống distributed database implement trong hierarchy của DNS servers, kết hợp với application-layer protocol cho phép hosts query database đó  
C. Một loại encryption protocol  
D. Một cơ chế routing trong Internet  

**Đáp án: B**  
*Giải thích: DNS là (1) distributed database implement trong hierarchy of DNS servers và (2) application-layer protocol cho phép hosts query database đó.*

---

**Câu 86.** DNS protocol chạy trên transport protocol nào và port number nào?

A. TCP, port 80  
B. TCP, port 53  
C. UDP, port 53  
D. UDP, port 25  

**Đáp án: C**  
*Giải thích: DNS protocol chạy trên UDP và sử dụng port 53.*

---

**Câu 87.** Ba loại DNS servers trong hierarchy là gì?

A. Primary, Secondary, và Tertiary  
B. Root, TLD (Top-Level Domain), và Authoritative  
C. Local, Regional, và Global  
D. Client, Proxy, và Origin  

**Đáp án: B**  
*Giải thích: Hierarchy DNS servers gồm: Root DNS servers (13 servers labeled A-M), TLD servers (com, org, edu, country codes), và Authoritative servers (của từng organization).*

---

**Câu 88.** Local DNS server (default name server) có vai trò gì?

A. Lưu trữ toàn bộ DNS database  
B. Nhận DNS queries từ hosts và forward vào DNS server hierarchy như một proxy  
C. Là authoritative server cho tất cả hostnames  
D. Chỉ phục vụ các TLD servers  

**Đáp án: B**  
*Giải thích: Local DNS server nhận queries từ hosts và forward vào hierarchy. Nó không thuộc hierarchy chính thức nhưng là central trong DNS architecture.*

---

**Câu 89.** DNS cung cấp những services nào ngoài hostname-to-IP translation?

A. Email encryption và authentication  
B. Host aliasing, mail server aliasing, và load distribution  
C. Bandwidth allocation và traffic shaping  
D. Certificate management và security  

**Đáp án: B**  
*Giải thích: DNS cung cấp thêm: host aliasing (canonical vs alias hostnames), mail server aliasing (MX records), và load distribution (rotates IP addresses cho replicated servers).*

---

**Câu 90.** Trong DNS load distribution, khi nhiều servers cùng phục vụ một hostname (như cnn.com), DNS làm gì khi nhận query?

A. Trả về IP của server gần nhất  
B. Trả về IP của server ít tải nhất  
C. Trả về toàn bộ set of IP addresses nhưng rotate thứ tự, để phân tán traffic  
D. Chỉ trả về một IP duy nhất  

**Đáp án: C**  
*Giải thích: DNS trả về toàn bộ set of IP addresses nhưng rotate thứ tự trong mỗi reply. Client thường gửi request đến IP đầu tiên, nên rotation phân phối traffic.*

---

**Câu 91.** Recursive query trong DNS là gì?

A. Query được gửi nhiều lần đến cùng một server  
B. Query mà DNS server được hỏi phải tự tìm câu trả lời thay mặt cho querying host, rồi trả kết quả về cho host  
C. Query chỉ đến root servers  
D. Query sử dụng TCP thay vì UDP  

**Đáp án: B**  
*Giải thích: Recursive query: DNS server "chịu trách nhiệm" tìm câu trả lời thay mặt cho client. Trái với iterative query, nơi server trả về referral để client tự query tiếp.*

---

**Câu 92.** Iterative query trong DNS là gì?

A. Query được lặp đi lặp lại đến cùng một server  
B. Server chỉ trả về best answer nó biết (thường là referral đến server khác), client tự query tiếp cho đến khi có câu trả lời cuối  
C. Query sử dụng multiple TCP connections  
D. Query yêu cầu server cache kết quả  

**Đáp án: B**  
*Giải thích: Iterative query: mỗi server trả về referral đến server tiếp theo mà nó biết, client (thường là local DNS server) phải tự gửi query tiếp theo.*

---

**Câu 93.** DNS resource record (RR) có format gì?

A. (Name, IP, TTL)  
B. (Name, Value, Type, TTL)  
C. (Hostname, Address, Protocol)  
D. (Key, Value, Expiry)  

**Đáp án: B**  
*Giải thích: DNS RR là 4-tuple: (Name, Value, Type, TTL). TTL là time-to-live, xác định khi nào record nên bị xóa khỏi cache.*

---

**Câu 94.** DNS record Type=A có ý nghĩa gì?

A. Name là domain, Value là hostname của authoritative DNS server  
B. Name là hostname, Value là IP address  
C. Name là alias hostname, Value là canonical hostname  
D. Name là domain, Value là canonical name của mail server  

**Đáp án: B**  
*Giải thích: Type A record: Name = hostname, Value = IP address. Đây là standard hostname-to-IP mapping.*

---

**Câu 95.** DNS record Type=NS có ý nghĩa gì?

A. Name là hostname, Value là IP address  
B. Name là domain, Value là hostname của authoritative DNS server cho domain đó  
C. Name là alias hostname, Value là canonical hostname  
D. Name là domain, Value là IP của mail server  

**Đáp án: B**  
*Giải thích: Type NS record: Name = domain (như foo.com), Value = hostname của authoritative DNS server. Dùng để route DNS queries trong chain.*

---

**Câu 96.** DNS record Type=CNAME có ý nghĩa gì?

A. Name là hostname, Value là IP address  
B. Name là domain, Value là hostname của NS server  
C. Name là alias hostname, Value là canonical hostname  
D. Name là domain, Value là mail server hostname  

**Đáp án: C**  
*Giải thích: Type CNAME: Name = alias hostname, Value = canonical hostname. Cho phép querying hosts biết canonical name của một hostname.*

---

**Câu 97.** DNS record Type=MX có ý nghĩa gì?

A. Name là hostname, Value là IP address  
B. Name là alias hostname của mail server, Value là canonical name của mail server  
C. Name là domain, Value là hostname của NS server  
D. Name là alias hostname, Value là canonical hostname của web server  

**Đáp án: B**  
*Giải thích: Type MX: Name = alias hostname của mail server, Value = canonical name của mail server. Cho phép mail servers có simple alias hostnames.*

---

**Câu 98.** DNS caching hoạt động như thế nào?

A. DNS servers lưu trữ vĩnh viễn tất cả hostname-to-IP mappings  
B. Khi DNS server nhận reply, nó cache mapping đó trong local memory; cached info bị discard sau một khoảng thời gian (TTL, thường 2 ngày)  
C. Chỉ local DNS servers mới cache  
D. Caching chỉ xảy ra tại root DNS servers  

**Đáp án: B**  
*Giải thích: Bất kỳ DNS server nào khi nhận reply đều có thể cache mapping đó. Cached entries bị discard sau TTL (thường ~2 ngày) vì hostnames/IPs có thể thay đổi.*

---

### Vận dụng

**Câu 99.** Để access trang web www.amazon.com, browser cần thực hiện gì trước khi gửi HTTP request?

A. Gửi SMTP message đến amazon.com  
B. Invoke DNS để translate www.amazon.com thành IP address, sau đó initiate TCP connection đến server tại IP đó port 80  
C. Gửi UDP packet đến amazon.com trực tiếp  
D. Contact FTP server của amazon.com trước  

**Đáp án: B**  
*Giải thích: Browser extract hostname → pass cho DNS client → DNS query → nhận IP → browser initiate TCP connection đến IP đó, port 80 → gửi HTTP request.*

---

**Câu 100.** Trong ví dụ DNS lookup cis.poly.edu muốn biết IP của gaia.cs.umass.edu, có bao nhiêu DNS messages được trao đổi (không tính caching)?

A. 2 messages  
B. 4 messages  
C. 8 messages  
D. 16 messages  

**Đáp án: C**  
*Giải thích: 4 query messages + 4 reply messages = 8 DNS messages tổng cộng (đến root, TLD, authoritative, và final reply về local DNS, rồi từ local DNS về client).*

---

**Câu 101.** Một registrar cần insert gì vào TLD com servers khi register networkutopia.com?

A. Chỉ IP address của Web server  
B. Type NS record (networkutopia.com, dns1.networkutopia.com) và Type A record (dns1.networkutopia.com, IP address)  
C. Chỉ MX records  
D. CNAME records cho tất cả subdomains  

**Đáp án: B**  
*Giải thích: Registrar insert: (1) NS record pointing đến authoritative DNS server và (2) Type A record providing IP của authoritative DNS server đó.*

---

**Câu 102.** DNS caching giúp gì trong ví dụ cis.poly.edu query gaia.cs.umass.edu?

A. Không giúp gì  
B. Nếu local DNS server đã cache IP của TLD edu servers, nó có thể bypass root DNS servers, giảm số messages cần gửi  
C. Caching chỉ giúp sau khi query giống hệt được gửi  
D. Caching giúp mã hóa query  

**Đáp án: B**  
*Giải thích: Nếu local DNS cache IP của TLD servers, nó không cần contact root servers. Có thể bắt đầu query từ TLD level, giảm latency và số messages.*

---

**Câu 103.** DNS attack nào send DNS queries với spoofed source address của target, gây ra DNS servers gửi large replies về target?

A. DDoS flooding attack  
B. Man-in-the-middle attack  
C. DNS poisoning attack  
D. DNS reflection/amplification attack  

**Đáp án: D**  
*Giải thích: Reflection/amplification attack: attacker gửi queries với spoofed source = target's IP. DNS servers gửi large replies về target. "Amplification" vì response lớn hơn query nhiều lần.*

---

**Câu 104.** Tại sao DDoS attack vào root DNS servers năm 2002 gây ít thiệt hại?

A. Root servers quá mạnh để bị tấn công  
B. Root servers được protect bởi packet filters blocking ICMP ping, và local DNS servers đã cache IP của TLD servers nên bypass được root servers  
C. Attacker dùng phương pháp không hiệu quả  
D. Root servers ở địa điểm bí mật  

**Đáp án: B**  
*Giải thích: Hai lý do: (1) Nhiều root servers có packet filters block ICMP ping. (2) Local DNS servers cache IP của TLD servers, cho phép bypass root servers entirely.*

---

### Vận dụng cao

**Câu 105.** Tại sao DNS không dùng single centralized server? Liệt kê các vấn đề:

A. Single server quá đắt để maintain  
B. Single point of failure (toàn Internet down nếu server crash), traffic volume quá lớn, distant centralized database gây latency cao cho users xa, và maintenance database khổng lồ cập nhật liên tục  
C. Single server không hỗ trợ IPv6  
D. Single server sẽ bị DDoS tấn công dễ dàng  

**Đáp án: B**  
*Giải thích: Bốn vấn đề của centralized DNS: (1) Single point of failure, (2) Traffic volume quá lớn, (3) Distant DB gây delay, (4) Maintenance (database lớn, cập nhật thường xuyên). DNS là ví dụ điển hình của distributed design.*

---

**Câu 106.** Một company muốn mail server và web server có cùng alias hostname "enterprise.com". Cần những DNS records nào?

A. Hai Type A records  
B. MX record cho mail server (alias → canonical mail server name) và CNAME record (hoặc A record) cho web server  
C. Hai Type NS records  
D. Hai CNAME records  

**Đáp án: B**  
*Giải thích: MX record cho phép enterprise.com alias đến canonical mail server name. Để phân biệt, client query MX record để tìm mail server, query CNAME/A record để tìm web server. Cả hai có thể share alias nhờ record types khác nhau.*

---
