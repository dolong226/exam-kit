# Computer network Chương 1

## Câu 1. Sự khác biệt giữa host và end system là gì? Liệt kê một số loại end system. Web server có phải end system không?**

Không có sự khác biệt. Các end system bao gồm: PC, Web server, mail server, PDA kết nối Internet,…

## Câu 2. Protocol thường được dùng để mô tả quan hệ ngoại giao. Wikipedia mô tả giao thức ngoại giao như thế nào?**

Giả sử Alice, đại sứ nước A, muốn mời Bob, đại sứ nước B, đến dự bữa tối. Alice không đơn giản gọi điện và nói “come to our dinner table now”. Thay vào đó, cô gọi điện đề xuất ngày giờ. Bob có thể trả lời rằng hôm đó anh bận nhưng rảnh hôm khác. Hai người tiếp tục trao đổi cho đến khi thống nhất. Bob xuất hiện đúng giờ đã hẹn. Giao thức ngoại giao cũng cho phép một trong hai bên hủy lịch một cách lịch sự nếu có lý do chính đáng.

## Câu 3. Tại sao chuẩn (standards) lại quan trọng đối với giao thức?**

** Vì chúng đảm bảo khả năng tương tác giữa các thiết bị và phần mềm từ nhiều nhà sản xuất khác nhau. Nếu không có chuẩn thống nhất, một máy tính của hãng A sẽ không thể giao tiếp với máy tính của hãng B. Chuẩn cũng tạo nền tảng ổn định để các nhà phát triển xây dựng sản phẩm, tránh lãng phí khi mỗi bên tự phát minh lại “bánh xe”. Ví dụ: chuẩn TCP/IP cho phép mọi thiết bị trên thế giới kết nối vào Internet.

## Phần 1.2

## Câu 4. Liệt kê sau công nghệ truy cập. Phân loại mỗi loại là truy cập tại nhà, truy cập doanh nghiệp, hay truy cập không dây diện rộng.

1. Modem quay số (dial-up modem) qua đường điện thoại → tại nhà.
2. DSL (Digital Subcriber Line) qua đường điện thoại → tại nhà hoặc văn phòng nhỏ.
3. Cáp HFC (Hybrid Fiber Coaxial) → tại nhà.
4. Ethernet 100Mbps có chuyển mạch → doanh nghiệp.
5. Mạng LAN không dây (WiFi) → di động.
6. Truy cập di động (4G/5G) → không dây diện rộng.

## Câu 5. Tốc độ truyền HFC là dùng chung hay riêng biệt giữa các người dùng? Có xảy ra va chạm (collision) trên kênh HFC chiều xuống không? Tại sao?

Băng thông HFC được dùng chung giữa các người dùng. Trên kênh chiều xuống, tất cả các gói tin đều xuất phát từ một người duy nhất là đầu cuối (head end), do đó không xảy ra va chạm trên kênh chiều xuống.

## Câu 6. Liệt kê các công nghệ truy cập Internet tại nhà hiện có ở thành phố của bạn.

Các công nghệ phổ biến gồm:

- FTTH (Fiber to the Home): tốc độ tải xuống 100 Mbps - 1 Gbps, tải lên 50-500 Mbps.
- Cáp đồng trục (DOCSIS/HFC): ít phổ biến hơn, 30-200 Mbps.
- 4G/5G di động: tốc độ tải xuống 30-300 Mbps.

## Câu 7. Tốc độ truyền của Ethernet LAN là bao nhiêu?

Ethernet LAN có tốc độ truyền: 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps. Với Ethernet X Mbps, một người dùng có thể truyền liên tục ở X Mbps nếu họ là người duy nhất gửi dữ liệu. Khi có nhiều người dùng cùng hoạt động, mỗi người không thể duy trì liên tục tốc độ X Mbps.

## Câu 8. Ethernet có thể chạy trên những loại phương tiện vật lý nào?

Ethernet phổ biến nhất chạy trên dây đồng xoắn đôi (twisted-pair copper wire) và cáp đồng trục mỏng. Ngoài ra còn có thể chạy trên cáp quang (fiber optic) và cáp đồng trục dày.

## Câu 9. Modem quay số, HFC, DSL và FTTH đều được dùng cho truy cập tại nhà. Với mỗi loại, cho biết dải tốc độ truyền và nhận xét xem tốc độ đó dùng chung hay riêng biệt.

- Modem quay số: tối đa 56 Kpbs - riêng biệt.
- DSL: tải xuống 0.5-8 Mbps, tải lên tối đa 1 Mpbs - riêng biệt
- HFC: tải xuống 10-30 Mpbs, tải lên vài Mbps - dùng chung
- FTTH: tải xuống 100 Mbps - 1 Gbps, tải lên 50 Mbps - 1Gbps - thường riêng biệt.

## Câu 10. Mô tả các các công nghệ truy cập Internet không dây phổ biến nhất hiện nay. So sánh và đối chiếu chúng.

Hai công nghệ phổ biến nhất:

- WiFi: Phạm vi ngắn, tốc độ cao, người dùng phải ở gần điểm truy cập (access point).
- Mạng di động (4G/ 5G): Phạm vi rộng, do nhà mạng viễn thông cung cấp.

## Phần 1.3

## Câu 11. Giả sử có đúng một bộ chuyển mạch gói (packed switch) giữa host gửi và host nhận. Tốc độ truyền giữa host gửi và switch là R1, giữa switch và host nhận là R2. Giả sử switch dùng store-and-forward, trễ đầu cuối tổng cộng để gửi một gói tin có độ dài L là bao nhiêu?

time delay = L/R1 + L/R2

## Câu 12. Mạng chuyển mạch kênh (circuit-switched) có ưu điểm gì so với mạng chuyển mạch gói (packet-switched)? TDM có ưu điểm gì với FDM trong mạng chuyển mạch kênh.

Nhắc lại:

Hai phương thức truyền dữ liệu nền tảng, đại diện cho cách mạng điện thoại truyền thống (Circuit) và Internet hiện đại (Packet).

- Circuit-switched:
    - Khi hai bên muốn liên lạc, một tuyến đường gọi là kênh (circuit) dedicated (dành riêng/cố định) sẽ được thiết lập từ đầu đến cuối và giữ nguyên trong suốt cuộc gọi.
    - Đặc điểm: Tài nguyên (băng thông) được đảm bảo 100%, không bị tranh chấp. Nếu không nói gì, băng thông vẫn bị lãng phí.
    - Ví dụ: Mạng điện thoại bàn truyền thống.
- Packet-switched:
    - Dự liệu được chia nhỏ thành các packet. Mỗi packet tự tìm đường đi tối ưu nhất qua các router/switch để tới đích.
    - Đặc điểm: Tài nguyên được chia sẻ dùng chung. Nhiều nguồn có thể gửi dữ liệu cùng lúc trên một đường truyền. Sử dụng băng thông hiệu quả hơn nhưng xảy ra hiện tượng tắc nghẽn (trễ, mất gói tin) nếu lưu lượng quá tải.
    - Ví dụ: Internet,…

Các phương thức phân chia tài nguyên trong Chuyển mạch kênh

- FDM (Frequency-Division Multiplexing - Đa truy cập phân chia theo tần số)
    - Khái niệm: Bằng thông của đường truyền chia thành các dải tần số khác nhau. Mỗi người dùng sở hữu riêng một dài tần số cố định.
    - Ví dụ: Các đài phát thanh (FM 91MHz, FM 100MHz,…) hoặc truyền hình cáp.
- TDM (Time-Division Multiplexing - Đa truy cập phân chia theo thời gian)
    - Khái niệm: Tất cả người dùng chia sẻ chung một tần số, nhưng mỗi người chỉ được phép truyền dữ liệu trong một khoảng thời gian cực ngắn (time slot) được luân phiên liên tục.
    - Ví dụ: Hệ thống điện thoại di động thế hệ cũ (GSM).

Mạng chuyển mạch kênh có thể đảm bảo băng thông đầu cuối nhất định trong suốt thời gian cuộc gọi.

Về TDM và FDM: Trong TDM, mỗi người dùng được phân bổ toàn bộ băng thông kênh trong khe thời gian của mình - giúp tốc độ truyền trong khe đó cao hơn. FDM chia bằng tần nên mỗi người dùng chỉ có một phần nhỏ băng thông liên tục. TDM cũng dễ điều chỉnh số khe thời gian hơn khi nhu cầu thay đổi.

## Câu 13. Giả sử các người dùng chia sẻ một đường truyền 2 Mpbs. Mỗi người dùng truyền liên tục ở 1 Mbps khi đang truyền, nhưng chỉ truyền 20% thời gian.

1. Nếu dùng circuit switching, bao nhiêu người dùng được hỗ trợ?
2. Nếu dùng packet switching, tại sao hầu như không có trễ hàng đợi khi có ≤ 2 người truyền đồng thời? Tại sao có trễ nếu 3 người cùng truyền?
3. Tìm xác suất một người dùng đang truyền?
4. Giả sử có 3 người dùng. Tìm xác suất cả 3 cùng truyền đồng thời. Tìm tỉ lệ thời gian hàng đợi tăng.

1. Mỗi người dùng cần 1 Mbps, đường truyền có 2 Mbps → Tối đa 2 người dùng.
2. Nếu ≤ 12 người truyền đồng thời, tổng băng thông yêu cầu ≤ 2 x 1 Mbps = 2 Mbps = dung lượng đường truyền → Không tắc nghẽn, không có hàng đợi. Nếu 3 người cùng truyền, tổng yêu cầu = 3 Mbps > 2 Mbps → hàng đợi bắt đầu tích lũy.
3. Mỗi người dùng truyền 20% thời gian → p = 0.2.
4. Xác suất cả 3 cùng truyền: P = 0.2^3 = 0.008.

## Câu 14. Tại sao ISP cùng cấp bậc thường kết nối ngang hàng với nhau? IXP kiếm tiền như nào?

Nhắc lại:

- ISP: Internet Service Provider.
    - Đơn vị trung gian bán hoặc cấp quyền truy cập Internet.
    - Ví dụ: Viettel, VNPT, FPT,…
- IXP: Internet Exchange Point.
    - Trung tâm/nút hạ tầng vật lý, nơi các ISP lớn và các big tech kết nối trực tiếp với nhau để trao đổi lưu lượng dữ liệu qua lại.
    - Thay vì dữ liệu phải đi đường vòng qua quốc tế, các bên gặp nhau tại IXP để truyền dữ liệu nhanh hơn, giảm độ trễ và tiết kiệm chi phí.

Hai ISP cùng cấp bậc kết nối ngang hàng để trao đổi lưu lượng trực tiếp mà không phải trả phí cho ISP cấp trên, giúp giảm chi phí và cải thiện hiệu năng. IXP kiếm tiền bằng cách thu phí từ các ISP muốn kết nối qua điểm trao đổi của họ.

## Câu 15. Một số nhà cung cấp nội dung (content provider) đã tạo ra mạng riêng. Mô tả mạng của Google. Điều gì thúc đẩy họ làm vậy?

Google xây dựng một mạng riêng toàn cầu bao gồm hàng chục trung tâm dữ liệu trên khắp thế giới, nối với nhau bằng cáp quang riêng. Google cũng triển khai các máy chủ caching (Google Global Cache) đặt ngay trong mạng của các ISP để đưa nội dung đến gần người dùng hơn. Google kết nối trực tiếp với nhiều ISP cấp 1 tại các IXP lớn, thay vì phải trung chuyển qua nhiều tầng ISP.

Động cơ: kiểm soát hoàn toàn chất lượng dịch vụ (giảm trễ), giảm chi phí trung chuyển phải trả cho các ISP, đảm bảo độ tin cậy và bảo mật lưu lượng nội bộ (tìm kiếm, YouTube, Gmail…).

## Phần 1.4

## Câu 16. Xem xét gửi một gói tin từ host nguồn đến host đích qua một tuyến đường cố định. Liệt kê các thành phần trễ trong trễ đầu cuối. Thành phần nào cố định, thành phần nào biến đổi.

Nhắc lại: 

D_nodal = d_proc + d_queue + d_trans + d_prop

- Processing Delay:
    - Thời gian mà router cần để kiểm tra header của gói tin và quyết định sẽ chuyển tiếp gói tin đó đi đâu.
    - Kiểm tra lỗi bit trong gói tin (checksum), kiểm tra routing table.
- Queuing Delay:
    - Thời gian gói tin nằm đợi trong buffer của cổng ra để chờ đến lượt được truyền đi.
- Transmission Delay:
    - Thời gian cần thiết để router đẩy toàn bộ bit của gói tin từ buffer lên đường truyền vật lý.
    - d_trans = L/R.
- Propagation Delay:
    - Thời gian cần thiết để 1 bit tín hiệu di chuyển hành trình trên dây cáp từ đầu bên này sang đầu bên kia của đường truyền.
    - d_prop = d/s

Queue Delay là biến đổi, phụ thuộc mức độ tắc nghẽn tại mỗi nút mạng.

## Câu 18. Mất bao lâu để một gói tin 1000 byte lan truyền qua một liên kết dài 2500km, tốc độ lan truyền 2.5x10^8 m/s, tốc độ truyền 2 Mbps?

Tranmission Delay: d_trans = L/R = 1000 x 8 / (2 x 10^6) = 4 ms.

Propagation Delay: d_prop = 2500 x 10^6 / (2.5 x 10^8) = 10ms.

Tuy nhiên, thời gian lan truyền chỉ là d_prop = 10 ms.

## Câu 1. 9. Host A muốn gửi file lớn đến host B qua 3 liên kết R1 = 500 kbps, R2 = 2 Mbps, R3 = 1 Mbps. 

1. Thông lượng (throughput) là bao nhiêu?
2. File 4 triệu byte. Mất bao lâu để truyền xong?
3. Lặp lại với R2 = 100 kbps.

Nhắc lại: Throughput (thông lượng) là tốc độ truyền dữ liệu thực tế giữa hai điểm trong một khoảng thời gian nhất định.

1. Throughput = min(500 kbps, 2 Mbps, 1 Mbps) = 500 kbps
2. T = 4 x 10^6 x 8 / (500 x 10^3) = 64 giây.

Q20. End system A muốn gửi file lớn đến B. Mô tả cách A tạo ra các gói tin. Khi một gói tin đến switch, switch dùng thông tin gì để xác định liên kết cần chuyển tiếp?

A20. 

End system A chia file thành các đoạn nhỏ (chunks). Mỗi đoạn được thêm header chứa thông tin điều khiển (địa chỉ nguồn, địa chỉ đích, số thứ tự, v.v..), tạo thành các gói tin (packets).

Switch chuyển tiếp: Switch đọc địa chỉ đích trong header của gói tin, tra forwarding table) để tìm liên kết đầu ra phù hợp.

## Phần 1.5

Q22. Liệt kê năm nhiệm vụ mà một tầng (layer) có thể thực hiện. Có thể một hoặc nhiều nhiệm vụ được thực hiện bởi hai hoặc nhiều tầng không?

A22. Năm nhiệm vụ: kiểm soát lỗi (error control), kiểm soát luồng (flow control), phân đoạn và tái hợp (segmentation & reassembly), ghép kênh (multiplexing), và thiết lập kết nối (connection setup). Có, các nhiệm vụ này có thế được thực hiện ở nhiều tầng. Ví dụ: kiểm soát lỗi được thực hiện ở cả tầng liên kết dữ liệu lẫn tầng vận chuyển.

Q23. Năm tầng trong ngăn xếp giao thức Internet là gì? Trách nhiệm chính của mỗi tầng là gì?

A23. Từ trên xuống:

1. Tầng ứng dụng (Application layer): hỗ trợ các ứng dụng mạng (HTTP, SMTP, FTP, DNS,…).
2. Tầng vận chuyển (Transport layer): truyền dữ liệu đầu cuối giữa các process (TCP, UDP).
3. Tầng mạng (Network layer): định tuyến datagram từ nguồn đến đích qua nhiều mạng (IP, OSPF,…).
4. Tầng liên kết dữ liệu (Link layer): truyền dữ liệu giữa các nút kề nhau trên cùng liên kết (Ethernet, Wifi).
5. Tầng vật lý (Physical Layer): truyền các bit thô qua môi trường vật lý (dây đồng, cáp quang, sóng vô tuyến,…)

Q24. Application-layer message là gì? Transport-layer segment? Network-layer datagram? Link-layer frame?

A24.

- Application-layer message: dữ liệu mà ứng dụng muốn gửi, được chuyển xuống tầng vận chuyển (ví dụ: một trang HTML, một email).
- Transport-layer segment: đơn vị dữ liệu do tầng vận chuyển tạo ra, bao gồm message của tầng ứng dụng được đóng gói cùng header của tầng vận chuyển (chứa số port, số thứ tự,…)
- Network-layer datagram: đơn vị dữ liệu của tầng mạng, bao gồm segment tầng vận chuyển được đóng gói cùng header tầng mạng (chứa địa chỉ IP nguồn, đích…)
- Link-layer frame: đơn vị dữ liệu của tầng liên kết, bao gồm datagram tầng mạng được đóng gói cùng header tầng liên kết (chứa địa chỉ MAC…).

Q25. Router xử lý những tầng nào? Link-layer switch xử lý những tầng nào? Host xử lý những tầng nào?

A25. 

- Router xử lý tầng 1 đến tầng 3 (vật lý, liên kết, mạng). (Lưu ý: router hiện tại đôi khi xử lý cả tầng 4 khi hoạt động như firewall).
- Link-layer switch: xử lý tầng 1 và 2.
- Host: xử lý cả 5 tầng.

## Phần 1.6

Q26. Sự khác biệt giữa virus và worm là gì?

A26. 

Virus là phần mềm độc hại cần sự tương tác của người dùng để lây lan - ví dụ: người dùng mở file đính kèm email độc hại. Virus thường gắn vào chương trình khác.

Worm tự lan truyền không cần tương tác của người dùng - nó chủ động khai thác lỗ hổng bảo mật để tự sao chếp sang các máy tính khác trong mạng.

Q28. Alice và Bob đang gửi gói tin cho nhau. Trudy đặt mình ở vị trí có thể chặn và gửi tùy ý mọi gói tin. Liệt kê những việc xấu Truly có thể làm.

A28. Truly có thể: nghe lén, giả mạo danh tính, chèn dữ liệu giả, phát lại tấn công, xóa hoặc hoãn trì gói tin.


## Phần 1.1

**Q1. Sự khác biệt giữa host và end system là gì? Liệt kê một số loại end system. Web server có phải end system không?**

**A1**. Không có sự khác biệt. Các end system bao gồm: PC, Web server, mail server, PDA kết nối Internet,…

**Q2. Protocol thường được dùng để mô tả quan hệ ngoại giao. Wikipedia mô tả giao thức ngoại giao như thế nào?**

**A2**. Giả sử Alice, đại sứ nước A, muốn mời Bob, đại sứ nước B, đến dự bữa tối. Alice không đơn giản gọi điện và nói “come to our dinner table now”. Thay vào đó, cô gọi điện đề xuất ngày giờ. Bob có thể trả lời rằng hôm đó anh bận nhưng rảnh hôm khác. Hai người tiếp tục trao đổi cho đến khi thống nhất. Bob xuất hiện đúng giờ đã hẹn. Giao thức ngoại giao cũng cho phép một trong hai bên hủy lịch một cách lịch sự nếu có lý do chính đáng.

**Q3. Tại sao chuẩn (standards) lại quan trọng đối với giao thức?**

**A3.** Vì chúng đảm bảo khả năng tương tác giữa các thiết bị và phần mềm từ nhiều nhà sản xuất khác nhau. Nếu không có chuẩn thống nhất, một máy tính của hãng A sẽ không thể giao tiếp với máy tính của hãng B. Chuẩn cũng tạo nền tảng ổn định để các nhà phát triển xây dựng sản phẩm, tránh lãng phí khi mỗi bên tự phát minh lại “bánh xe”. Ví dụ: chuẩn TCP/IP cho phép mọi thiết bị trên thế giới kết nối vào Internet.

## Phần 1.2

**Q4**. Liệt kê sau công nghệ truy cập. Phân loại mỗi loại là truy cập tại nhà, truy cập doanh nghiệp, hay truy cập không dây diện rộng.

A4.

1. Modem quay số (dial-up modem) qua đường điện thoại → tại nhà.
2. DSL (Digital Subcriber Line) qua đường điện thoại → tại nhà hoặc văn phòng nhỏ.
3. Cáp HFC (Hybrid Fiber Coaxial) → tại nhà.
4. Ethernet 100Mbps có chuyển mạch → doanh nghiệp.
5. Mạng LAN không dây (WiFi) → di động.
6. Truy cập di động (4G/5G) → không dây diện rộng.

Q5. Tốc độ truyền HFC là dùng chung hay riêng biệt giữa các người dùng? Có xảy ra va chạm (collision) trên kênh HFC chiều xuống không? Tại sao?

A5. Băng thông HFC được dùng chung giữa các người dùng. Trên kênh chiều xuống, tất cả các gói tin đều xuất phát từ một người duy nhất là đầu cuối (head end), do đó không xảy ra va chạm trên kênh chiều xuống.

Q6. Liệt kê các công nghệ truy cập Internet tại nhà hiện có ở thành phố của bạn.

A6. Các công nghệ phổ biến gồm:

- FTTH (Fiber to the Home): tốc độ tải xuống 100 Mbps - 1 Gbps, tải lên 50-500 Mbps.
- Cáp đồng trục (DOCSIS/HFC): ít phổ biến hơn, 30-200 Mbps.
- 4G/5G di động: tốc độ tải xuống 30-300 Mbps.

Q7. Tốc độ truyền của Ethernet LAN là bao nhiêu?

A7. Ethernet LAN có tốc độ truyền: 10 Mbps, 100 Mbps, 1 Gbps, 10 Gbps. Với Ethernet X Mbps, một người dùng có thể truyền liên tục ở X Mbps nếu họ là người duy nhất gửi dữ liệu. Khi có nhiều người dùng cùng hoạt động, mỗi người không thể duy trì liên tục tốc độ X Mbps.

Q8. Ethernet có thể chạy trên những loại phương tiện vật lý nào?

A8. Ethernet phổ biến nhất chạy trên dây đồng xoắn đôi (twisted-pair copper wire) và cáp đồng trục mỏng. Ngoài ra còn có thể chạy trên cáp quang (fiber optic) và cáp đồng trục dày.

Q9. Modem quay số, HFC, DSL và FTTH đều được dùng cho truy cập tại nhà. Với mỗi loại, cho biết dải tốc độ truyền và nhận xét xem tốc độ đó dùng chung hay riêng biệt.

A9. 

- Modem quay số: tối đa 56 Kpbs - riêng biệt.
- DSL: tải xuống 0.5-8 Mbps, tải lên tối đa 1 Mpbs - riêng biệt
- HFC: tải xuống 10-30 Mpbs, tải lên vài Mbps - dùng chung
- FTTH: tải xuống 100 Mbps - 1 Gbps, tải lên 50 Mbps - 1Gbps - thường riêng biệt.

Q10. Mô tả các các công nghệ truy cập Internet không dây phổ biến nhất hiện nay. So sánh và đối chiếu chúng.

A10. Hai công nghệ phổ biến nhất:

- WiFi: Phạm vi ngắn, tốc độ cao, người dùng phải ở gần điểm truy cập (access point).
- Mạng di động (4G/ 5G): Phạm vi rộng, do nhà mạng viễn thông cung cấp.

## Phần 1.3

Q11. Giả sử có đúng một bộ chuyển mạch gói (packed switch) giữa host gửi và host nhận. Tốc độ truyền giữa host gửi và switch là R1, giữa switch và host nhận là R2. Giả sử switch dùng store-and-forward, trễ đầu cuối tổng cộng để gửi một gói tin có độ dài L là bao nhiêu?

A11. time delay = L/R1 + L/R2

Q12. Mạng chuyển mạch kênh (circuit-switched) có ưu điểm gì so với mạng chuyển mạch gói (packet-switched)? TDM có ưu điểm gì với FDM trong mạng chuyển mạch kênh.

Nhắc lại:

Hai phương thức truyền dữ liệu nền tảng, đại diện cho cách mạng điện thoại truyền thống (Circuit) và Internet hiện đại (Packet).

- Circuit-switched:
    - Khi hai bên muốn liên lạc, một tuyến đường gọi là kênh (circuit) dedicated (dành riêng/cố định) sẽ được thiết lập từ đầu đến cuối và giữ nguyên trong suốt cuộc gọi.
    - Đặc điểm: Tài nguyên (băng thông) được đảm bảo 100%, không bị tranh chấp. Nếu không nói gì, băng thông vẫn bị lãng phí.
    - Ví dụ: Mạng điện thoại bàn truyền thống.
- Packet-switched:
    - Dự liệu được chia nhỏ thành các packet. Mỗi packet tự tìm đường đi tối ưu nhất qua các router/switch để tới đích.
    - Đặc điểm: Tài nguyên được chia sẻ dùng chung. Nhiều nguồn có thể gửi dữ liệu cùng lúc trên một đường truyền. Sử dụng băng thông hiệu quả hơn nhưng xảy ra hiện tượng tắc nghẽn (trễ, mất gói tin) nếu lưu lượng quá tải.
    - Ví dụ: Internet,…

Các phương thức phân chia tài nguyên trong Chuyển mạch kênh

- FDM (Frequency-Division Multiplexing - Đa truy cập phân chia theo tần số)
    - Khái niệm: Bằng thông của đường truyền chia thành các dải tần số khác nhau. Mỗi người dùng sở hữu riêng một dài tần số cố định.
    - Ví dụ: Các đài phát thanh (FM 91MHz, FM 100MHz,…) hoặc truyền hình cáp.
- TDM (Time-Division Multiplexing - Đa truy cập phân chia theo thời gian)
    - Khái niệm: Tất cả người dùng chia sẻ chung một tần số, nhưng mỗi người chỉ được phép truyền dữ liệu trong một khoảng thời gian cực ngắn (time slot) được luân phiên liên tục.
    - Ví dụ: Hệ thống điện thoại di động thế hệ cũ (GSM).

A12. Mạng chuyển mạch kênh có thể đảm bảo băng thông đầu cuối nhất định trong suốt thời gian cuộc gọi.

Về TDM và FDM: Trong TDM, mỗi người dùng được phân bổ toàn bộ băng thông kênh trong khe thời gian của mình - giúp tốc độ truyền trong khe đó cao hơn. FDM chia bằng tần nên mỗi người dùng chỉ có một phần nhỏ băng thông liên tục. TDM cũng dễ điều chỉnh số khe thời gian hơn khi nhu cầu thay đổi.

Q13. Giả sử các người dùng chia sẻ một đường truyền 2 Mpbs. Mỗi người dùng truyền liên tục ở 1 Mbps khi đang truyền, nhưng chỉ truyền 20% thời gian.

1. Nếu dùng circuit switching, bao nhiêu người dùng được hỗ trợ?
2. Nếu dùng packet switching, tại sao hầu như không có trễ hàng đợi khi có ≤ 2 người truyền đồng thời? Tại sao có trễ nếu 3 người cùng truyền?
3. Tìm xác suất một người dùng đang truyền?
4. Giả sử có 3 người dùng. Tìm xác suất cả 3 cùng truyền đồng thời. Tìm tỉ lệ thời gian hàng đợi tăng.

A13.

1. Mỗi người dùng cần 1 Mbps, đường truyền có 2 Mbps → Tối đa 2 người dùng.
2. Nếu ≤ 12 người truyền đồng thời, tổng băng thông yêu cầu ≤ 2 x 1 Mbps = 2 Mbps = dung lượng đường truyền → Không tắc nghẽn, không có hàng đợi. Nếu 3 người cùng truyền, tổng yêu cầu = 3 Mbps > 2 Mbps → hàng đợi bắt đầu tích lũy.
3. Mỗi người dùng truyền 20% thời gian → p = 0.2.
4. Xác suất cả 3 cùng truyền: P = 0.2^3 = 0.008.

Q14. Tại sao ISP cùng cấp bậc thường kết nối ngang hàng với nhau? IXP kiếm tiền như nào?

Nhắc lại:

- ISP: Internet Service Provider.
    - Đơn vị trung gian bán hoặc cấp quyền truy cập Internet.
    - Ví dụ: Viettel, VNPT, FPT,…
- IXP: Internet Exchange Point.
    - Trung tâm/nút hạ tầng vật lý, nơi các ISP lớn và các big tech kết nối trực tiếp với nhau để trao đổi lưu lượng dữ liệu qua lại.
    - Thay vì dữ liệu phải đi đường vòng qua quốc tế, các bên gặp nhau tại IXP để truyền dữ liệu nhanh hơn, giảm độ trễ và tiết kiệm chi phí.

A14. Hai ISP cùng cấp bậc kết nối ngang hàng để trao đổi lưu lượng trực tiếp mà không phải trả phí cho ISP cấp trên, giúp giảm chi phí và cải thiện hiệu năng. IXP kiếm tiền bằng cách thu phí từ các ISP muốn kết nối qua điểm trao đổi của họ.

Q15. Một số nhà cung cấp nội dung (content provider) đã tạo ra mạng riêng. Mô tả mạng của Google. Điều gì thúc đẩy họ làm vậy?

A15. Google xây dựng một mạng riêng toàn cầu bao gồm hàng chục trung tâm dữ liệu trên khắp thế giới, nối với nhau bằng cáp quang riêng. Google cũng triển khai các máy chủ caching (Google Global Cache) đặt ngay trong mạng của các ISP để đưa nội dung đến gần người dùng hơn. Google kết nối trực tiếp với nhiều ISP cấp 1 tại các IXP lớn, thay vì phải trung chuyển qua nhiều tầng ISP.

Động cơ: kiểm soát hoàn toàn chất lượng dịch vụ (giảm trễ), giảm chi phí trung chuyển phải trả cho các ISP, đảm bảo độ tin cậy và bảo mật lưu lượng nội bộ (tìm kiếm, YouTube, Gmail…).

## Phần 1.4

Q16. Xem xét gửi một gói tin từ host nguồn đến host đích qua một tuyến đường cố định. Liệt kê các thành phần trễ trong trễ đầu cuối. Thành phần nào cố định, thành phần nào biến đổi.

Nhắc lại: 

D_nodal = d_proc + d_queue + d_trans + d_prop

- Processing Delay:
    - Thời gian mà router cần để kiểm tra header của gói tin và quyết định sẽ chuyển tiếp gói tin đó đi đâu.
    - Kiểm tra lỗi bit trong gói tin (checksum), kiểm tra routing table.
- Queuing Delay:
    - Thời gian gói tin nằm đợi trong buffer của cổng ra để chờ đến lượt được truyền đi.
- Transmission Delay:
    - Thời gian cần thiết để router đẩy toàn bộ bit của gói tin từ buffer lên đường truyền vật lý.
    - d_trans = L/R.
- Propagation Delay:
    - Thời gian cần thiết để 1 bit tín hiệu di chuyển hành trình trên dây cáp từ đầu bên này sang đầu bên kia của đường truyền.
    - d_prop = d/s

A16. Queue Delay là biến đổi, phụ thuộc mức độ tắc nghẽn tại mỗi nút mạng.

Q18. Mất bao lâu để một gói tin 1000 byte lan truyền qua một liên kết dài 2500km, tốc độ lan truyền 2.5x10^8 m/s, tốc độ truyền 2 Mbps?

A18. 

Tranmission Delay: d_trans = L/R = 1000 x 8 / (2 x 10^6) = 4 ms.

Propagation Delay: d_prop = 2500 x 10^6 / (2.5 x 10^8) = 10ms.

Tuy nhiên, thời gian lan truyền chỉ là d_prop = 10 ms.

Q19. Host A muốn gửi file lớn đến host B qua 3 liên kết R1 = 500 kbps, R2 = 2 Mbps, R3 = 1 Mbps. 

1. Thông lượng (throughput) là bao nhiêu?
2. File 4 triệu byte. Mất bao lâu để truyền xong?
3. Lặp lại với R2 = 100 kbps.

Nhắc lại: Throughput (thông lượng) là tốc độ truyền dữ liệu thực tế giữa hai điểm trong một khoảng thời gian nhất định.

1. Throughput = min(500 kbps, 2 Mbps, 1 Mbps) = 500 kbps
2. T = 4 x 10^6 x 8 / (500 x 10^3) = 64 giây.

Q20. End system A muốn gửi file lớn đến B. Mô tả cách A tạo ra các gói tin. Khi một gói tin đến switch, switch dùng thông tin gì để xác định liên kết cần chuyển tiếp?

A20. 

End system A chia file thành các đoạn nhỏ (chunks). Mỗi đoạn được thêm header chứa thông tin điều khiển (địa chỉ nguồn, địa chỉ đích, số thứ tự, v.v..), tạo thành các gói tin (packets).

Switch chuyển tiếp: Switch đọc địa chỉ đích trong header của gói tin, tra forwarding table) để tìm liên kết đầu ra phù hợp.

## Phần 1.5

Q22. Liệt kê năm nhiệm vụ mà một tầng (layer) có thể thực hiện. Có thể một hoặc nhiều nhiệm vụ được thực hiện bởi hai hoặc nhiều tầng không?

A22. Năm nhiệm vụ: kiểm soát lỗi (error control), kiểm soát luồng (flow control), phân đoạn và tái hợp (segmentation & reassembly), ghép kênh (multiplexing), và thiết lập kết nối (connection setup). Có, các nhiệm vụ này có thế được thực hiện ở nhiều tầng. Ví dụ: kiểm soát lỗi được thực hiện ở cả tầng liên kết dữ liệu lẫn tầng vận chuyển.

Q23. Năm tầng trong ngăn xếp giao thức Internet là gì? Trách nhiệm chính của mỗi tầng là gì?

A23. Từ trên xuống:

1. Tầng ứng dụng (Application layer): hỗ trợ các ứng dụng mạng (HTTP, SMTP, FTP, DNS,…).
2. Tầng vận chuyển (Transport layer): truyền dữ liệu đầu cuối giữa các process (TCP, UDP).
3. Tầng mạng (Network layer): định tuyến datagram từ nguồn đến đích qua nhiều mạng (IP, OSPF,…).
4. Tầng liên kết dữ liệu (Link layer): truyền dữ liệu giữa các nút kề nhau trên cùng liên kết (Ethernet, Wifi).
5. Tầng vật lý (Physical Layer): truyền các bit thô qua môi trường vật lý (dây đồng, cáp quang, sóng vô tuyến,…)

Q24. Application-layer message là gì? Transport-layer segment? Network-layer datagram? Link-layer frame?

A24.

- Application-layer message: dữ liệu mà ứng dụng muốn gửi, được chuyển xuống tầng vận chuyển (ví dụ: một trang HTML, một email).
- Transport-layer segment: đơn vị dữ liệu do tầng vận chuyển tạo ra, bao gồm message của tầng ứng dụng được đóng gói cùng header của tầng vận chuyển (chứa số port, số thứ tự,…)
- Network-layer datagram: đơn vị dữ liệu của tầng mạng, bao gồm segment tầng vận chuyển được đóng gói cùng header tầng mạng (chứa địa chỉ IP nguồn, đích…)
- Link-layer frame: đơn vị dữ liệu của tầng liên kết, bao gồm datagram tầng mạng được đóng gói cùng header tầng liên kết (chứa địa chỉ MAC…).

Q25. Router xử lý những tầng nào? Link-layer switch xử lý những tầng nào? Host xử lý những tầng nào?

A25. 

- Router xử lý tầng 1 đến tầng 3 (vật lý, liên kết, mạng). (Lưu ý: router hiện tại đôi khi xử lý cả tầng 4 khi hoạt động như firewall).
- Link-layer switch: xử lý tầng 1 và 2.
- Host: xử lý cả 5 tầng.

## Phần 1.6

Q26. Sự khác biệt giữa virus và worm là gì?

A26. 

Virus là phần mềm độc hại cần sự tương tác của người dùng để lây lan - ví dụ: người dùng mở file đính kèm email độc hại. Virus thường gắn vào chương trình khác.

Worm tự lan truyền không cần tương tác của người dùng - nó chủ động khai thác lỗ hổng bảo mật để tự sao chếp sang các máy tính khác trong mạng.

Q28. Alice và Bob đang gửi gói tin cho nhau. Trudy đặt mình ở vị trí có thể chặn và gửi tùy ý mọi gói tin. Liệt kê những việc xấu Truly có thể làm.

A28. Truly có thể: nghe lén, giả mạo danh tính, chèn dữ liệu giả, phát lại tấn công, xóa hoặc hoãn trì gói tin.


Q1. Liệt kê năm ứng dụng Internet không độc quyền và các giao thức tầng ứng dụng mà chúng sử dụng.

A1. Web: HTTP; truyền file: FTTP; đăng nhập từ xa: Telnet; Network News: NTTP; email: SMTP.

Q2. Sự khác biệt giữa kiến trúc mạng (network architecture) và kiến trúc ứng dụng (application architecture) là gì?

A2. Kiến trúc mạng đề cập đến việc tổ chức quá trình giao tiếp thành các tầng (ví dụ: kiến trúc Internet 5 tầng). Mặt khác, kiến trúc ứng dụng thiết kế bởi nhà phát triển ứng dụng và quy định cấu trúc tổng thể của ứng dụng (ví dụ: client-server hoặc P2P).

Q3. Trong một phiên giao tiếp giữa một cặp tiến trình, tiến trình nào là client và tiến trình nào là server?

A3. Tiến trình khởi tạo giao tiếp là client; tiến trình chờ đợi liên hệ là server.

Q4. Đối với ứng dụng chia sẻ file P2P, bạn có đồng ý với nhận định: Không có khái niệm phía client và phía server trong một phiên giao tiếp không?

A4. Không. Mọi phiên giao tiếp đều có phía client và phía server. Trong ứng dụng chia sẻ file P2P, peer đang nhận file thường là client và peer đang gửi file thường là server.

Q5. Thông tin nào được sử dụng bởi một tiến trình chạy trên một host để xác định một tiến trình chạy trên một host khác?

A5. Địa chỉ IP của host đích và port number của socket đích.

Q6. Giả sử bạn muốn thực hiện một giao dịch từ một client từ xa đến một server càng nhành càng tốt. Bạn sẽ sử dụng UDP hay TCP? Tại sao?

A6. Sẽ sử dụng UDP. Vì UDP là giao thức hướng không kết nối (connectionless), nó tránh được độ trễ phát sinh do quá trình bắt tay ba bước của TCP, giúp dữ liệu được gửi đi nhanh hơn ngay lập tức.

Q8. Liệt kê bốn lớp dịch vụ chính mà một giao thức tầng giao vận có thể cung cấp. Đối với mỗi lớp dịch vụ, chỉ ra TCP hoặc UDP (hoặc cả hai) có cung cấp dịch vụ đó hay không.

A8.

- Truyền dữ liệu đáng tin cậy (TCP có, UDP không).
- Đảm bảo thông lượng (TCP, UDP đều không).
- Đảm bảo thời gian (TCP, UDP đều không).
- Bảo mật (Cả TCP và UDP đều không tích hợp sẵn, nhưng TCP có thể được tăng cường với SSL/TLS_.

Q10. Giao thức bắt tay (handshaking protocol) là gì?

A10. Một giao thức sử dụng bắt tay nếu hai thực thể giao tiếp trao đổi các gói điều khiển trước khi thực sự gửi dữ liệu cho nhau. SMTP sử dụng bắt tay ở tầng ứng dụng, trong khi HTTP thì không.

Q11. Tại sao HTTP, FTP, SMTP và POP3 chạy trên TCP thay vì UDP?

A11. Nhắc lại:

HTTP (HyperText Transfer Protocol)

- Là giao thức dùng để truyền tải các trang web giữa trình duyệt và máy chủ web.
- Cách hoạt động:
    - Khi truy cập: https://www.google.com
    - Trình duyệt gửi yêu cầu:
        - GET / HTTP/1.1
        - Host: google.com
    - Máy chủ trả về:
        - HTTP/1.1 200 OK
        - Content-Type: text/html
- Đặc điểm:
    - Hoạt động theo mô hình Client-Server.
    - Stateless (không nhớ trạng thái giữa các lần gửi yêu cầu).
    - Dùng TCP làm giao thức vận chuyển.
    - Mặc định cổng: HTTP (80), HTTPS (443).
- Các phương thức phổ biến: GET (lấy dữ liệu), POST (gửi dữ liệu), PUT (cập nhật dữ liệu), DELETE (xóa dữ liệu).

FTP (File Transfer Protocol)

- FTP được thiết kế để truyền tệp giữa hai máy tính.
- Cách hoạt động: FTP sử dụng hai kết nối TCP.
    - Control Connection: dùng gửi lệnh.
        - USER alice
        - PASS 123456
    - Data connection: Truyền dữ liệu thực tế.
        - RETR report.pdf
- Cổng FTP: control (21), data (20).
- Một số lệnh: USER (Tên đăng nhập), PASS, LIST (danh sách file), RETR (Retrive: tải xuống file), STOR (tải lên file), QUIT.
- Nhược điểm:
    - FTP truyền Username, Password, Dữ liệu dưới dạng plaintext, kẻ tấn công có thể nghe lén.
    - Ngày nay thường dùng: SFTP, FTPS.

SMTP (Simple Mail Transfer Protocol)

- Dùng để gửi email, không dùng để đọc.
- Luồng hoạt động: Người gửi → SMTP Server Gmail → SMTP Server người nhận → Hộp thư người nhận.
- Port 25.
- Một phiên SMTP đơn giản:
    - Client: HELO mail.com
    - Server: 250 OK
    - Client: MAIL FROM:<abc@gmail.com>
    - Server: 250 OK
    - Client: RCPT TO :<xyz@yahoo.com>
    - Server: 250 OK
    - Client: DATA
    - Client: ………..
- Đặc điểm:
    - Push protocol (đẩy thư đi).
    - Dùng TCP.
    - Không dùng để đọc email.

POP3 (Post Office Protocol Version 3)

- Dùng để nhận email từ mail server về máy người dùng.
- Luồng: Mail Server → POP3 → Outlook/Thunderbird.
- Port 110.
- Quy trình:
    - USER alice
    - PASS 123456
    - STAT
    - RETR 1
    - DELE 1
- Nhược điểm:  Sau khi tải thư có thể bị xóa trên server; khó đồng bộ nhiều thiết bị.

POP3 và SMTP phối hợp như nào?

- Khi gửi email: Người gửi → SMTP → Mail Server → SMTP → Mail Server người nhận.
- Khi nhận email: Mail Server → POP3 → Người nhận

POP3 và IMAP?

- IMAP ra đời để khắc phục hạn chế lớn nhất của POP3: email ngày nay có thể được đọc trên nhiều thiết bị.
- IMAP (Internet Message Access Protocol) là giao thức cho phép truy cập và quản lý email trực tiếp trên mail server.
- Khác với POP3, IMAP không mặc định tải toàn bộ thư về máy rồi xóa trên server.
- Port: IMAP (143), IMAPS (993). Ngày nay hầu hết dùng 993.

Trả lời:

Các ứng dụng gắn với giao thức này yêu cầu tất cả dữ liệu ứng dụng phải được nhận theo đúng thứ tự và không bị mất mát. TCP cung cấp đảm bảo tính nguyên vẹn dữ liệu.

Q12. Xem xét một trang web thương mai điện tử muốn lưu lại hồ sơ mua hàng của từng khách hàng. Mô tả cách thực hiện điều này bằng cookie.

A12. Khi người dùng truy cập trang web lần đầu, trang web trả về một số cookie. Số cookie này được lưu trữ trên host của người dùng và do trình duyệt quản lý. Trong mỗi lần truy cập tiếp theo, trình duyệt gửi lại số cookie đó cho trang web. Do đó trang web biết khi nào người dùng này đang truy cập trang web.

Q13. Mô tả cách Web caching (bộ nhớ cache Web) có thể làm giảm độ trễ trong việc nhận một đối tượng được yêu cầu. Web caching sẽ làm giảm độ trễ cho tất cả các đối tượng được người dùng yêu cầu hay chỉ một số đối tượng? Tại sao?

A13. Nhắc lại:
Web Caching là kỹ thuật lưu tạm dữ liệu web đã truy cập trước đó để lần sau không cần lấy lại từ server gốc, giúp tăng tốc độ truy cập và giảm tải mạng.

Cache Hit và Cache Miss

304 Not Modified: Không cần lấy dữ liệu mới vì không có chỉnh sửa.

Trả lời: Web caching có thể mang nội dung mong muốn đến gần người dùng hơn, có thể là nằm trên cùng mạng LAN mà host của người dùng được kết nối. Web caching có thể làm giảm độ trễ cho tất cả các đối tượng, ngay cả những đối tượng không được lưu trong cache, vì caching làm giảm lưu lượng giao thông trên các đường truyền.

Q15. Tại sao nói rằng FTP gửi thông tin điều khiển “out-of-band” (ngoài băng tần)?

A15. FTP sử dụng hai kết nối TCP song song, một kết nối để gửi thông tin điều khiển (như yêu cầu truyền file) và một kết nối khác để thực sự truyền file. Bởi vì thông tin điều khiển không được gửi qua cùng một kết nối để truyền file, nên FTP gửi thông tin điều khiển “out-of-band”.

Q16. Giả sử Alice, với một tài khoản email trên nền web (như Hotmail hoặc Gmail), gửi một tin nhắn cho Bob, người truy cập thư từ mail server của mình bằng POP3. Thảo luận cách tin nhắn đi từ host của Alice đến host của Bob. Hãy chắc chắn liệt kê chuỗi các giao thức tầng ứng dụng được sử dụng để di chuyển tin nhắn giữa hai host.

A16. Host của Alice → HTTP → Mail server của Alice → SMTP → Mail server của Bob → POP3 → Host của Bob.

**Q18:** Từ góc độ người dùng, sự khác biệt giữa chế độ "tải xuống và xóa" (download-and-delete) và "tải xuống và giữ lại" (download-and-keep) trong POP3 là gì?
**A18:** Với chế độ tải xuống và xóa, sau khi người dùng lấy tin nhắn từ POP server, các tin nhắn đó sẽ bị xóa. Điều này gây vấn đề cho người dùng hay di chuyển, người muốn truy cập tin nhắn từ nhiều máy khác nhau (PC văn phòng, PC ở nhà, v.v.). Trong cấu hình tải xuống và giữ lại, tin nhắn không bị xóa sau khi người dùng lấy tin nhắn. Điều này cũng có thể bất tiện, vì mỗi lần người dùng lấy các tin nhắn đã lưu từ một máy tính mới, tất cả các tin nhắn chưa bị xóa sẽ được chuyển sang máy tính mới đó (bao gồm cả những tin nhắn rất cũ).

**Q26:** Trong Phần 2.7, UDP server được mô tả chỉ cần 1 socket, trong khi TCP server cần 2 socket. Tại sao? Nếu TCP server hỗ trợ n kết nối đồng thời, mỗi kết nối từ một host client khác nhau, thì TCP server sẽ cần bao nhiêu socket?
**A26:** UDP server chỉ cần 1 socket vì UDP là giao thức không trạng thái/không kết nối; tất cả dữ liệu từ vô số các client khác nhau đều gửi chung vào một cổng (socket) duy nhất đó. TCP server cần 2 socket ban đầu vì TCP hướng kết nối: 1 socket dùng để thường trực lắng nghe (welcoming socket) và 1 socket dành riêng được tạo ra để phục vụ cho client vừa kết nối xong. Nếu hỗ trợ n kết nối đồng thời, TCP server sẽ cần tổng cộng n + 1 socket (1 socket lắng nghe chung và n socket phục vụ riêng biệt cho n client).
**Q27:** Đối với ứng dụng client-server qua TCP, tại sao chương trình server phải được thực thi trước chương trình client? Đối với ứng dụng client-server qua UDP, tại sao chương trình client có thể được thực thi trước chương trình server?
**A27:** Với TCP, trước khi gửi được bất kỳ dữ liệu nào, client phải khởi tạo một phiên "bắt tay" (thiết lập kết nối) với server. Để việc bắt tay thành công, chương trình server buộc phải chạy trước để mở một socket đón đợi kết nối. Với UDP, hoàn toàn không có quá trình thiết lập kết nối nào cả. Client cứ việc đóng gói dữ liệu và đẩy vào mạng lưới gửi đến địa chỉ đích, không cần quan tâm server có đang chạy và sẵn sàng nhận hay không. Do đó client hoàn toàn có thể chạy trước (dù gói tin gửi đi có thể sẽ bị rớt/thất lạc nếu server chưa thực thi).

Q28. Đúng hai sai

a). Một người dùng yêu cầu một trang Web bao gồm một đoạn văn bản và ba hình ảnh. Đối với trang này, client sẽ gửi một thông điệp yêu cầu (request) và nhận bốn thông điệp phản hồi (response). 

b)  Hai trang web riêng biệt có thể được gửi qua cùng một kết nối kiên trì (persistent connection).

c) Với kết nối không kiên trì giữa trình duyệt và origin server, một phân đoạn TCP (TCP segment) đơn lẻ có thể mang hai thông điệp yêu cầu HTTP Khác nhau.

d) Dòng header  “Date:” trong response của HTTP cho biết thời điểm đối tượng trong response được sửa đổi lần cuối.

e) HTTP response không bao giờ có phần message body trống.

A28

a). Sai.

Persistent HTTP và non-persistent HTTP không khác nhau ở số lượng request. Chúng khác nhau ở số lượng kết nối TCP.

Ví dụ trang web gồm 4 đối tượng, client vẫn phải gửi 4 request và nhận 4 response trong cả 2 trường hợp.

b) Đúng. Đây là ưu điểm của persistent HTTP: nhiều đối tượng nằm trên cùng một server có thể được truyền tải qua một kết nối TCP duy nhất mà không cần đóng/mở liên tục.

c) Sai. Trong non-per connection, mỗi kết nối TCP chỉ phục vụ duy nhất một thông điệp yêu cầu và một thông điệp phản hồi, sau đó kết nối sẽ bị đóng lại. Do đó, một phân đoạn TCP không thể chứa hai yêu cầu HTTP khác nhau.

d) Sai. Dòng “Date:” biểu thị thời gian server tạo ra và gửi thông điệp phản hồi đó. Thời điểm đối tượng được sửa đổi lần cuối được biểu thị bằng dòng header Last-Modified:.

e) Sai. Có nhiều HTTP response có phần body trống, ví dụ như phản hồi có mã trạng thái 304 Not Modified hoặc 204 No Content.