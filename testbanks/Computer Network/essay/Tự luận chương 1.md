## Câu 1. Sự khác biệt giữa host và end system là gì? Liệt kê một số loại end system. Web server có phải end system không?

Không có sự khác biệt. Các end system bao gồm: PC, Web server, mail server, PDA kết nối Internet,…

## Câu 2. Protocol thường được dùng để mô tả quan hệ ngoại giao. Wikipedia mô tả giao thức ngoại giao như thế nào?

Giả sử Alice, đại sứ nước A, muốn mời Bob, đại sứ nước B, đến dự bữa tối. Alice không đơn giản gọi điện và nói “come to our dinner table now”. Thay vào đó, cô gọi điện đề xuất ngày giờ. Bob có thể trả lời rằng hôm đó anh bận nhưng rảnh hôm khác. Hai người tiếp tục trao đổi cho đến khi thống nhất. Bob xuất hiện đúng giờ đã hẹn. Giao thức ngoại giao cũng cho phép một trong hai bên hủy lịch một cách lịch sự nếu có lý do chính đáng.

## Câu 3. Tại sao chuẩn (standards) lại quan trọng đối với giao thức?

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

## Câu 13. Giả sử các người dùng chia sẻ một đường truyền 2 Mpbs. Mỗi người dùng truyền liên tục ở 1 Mbps khi đang truyền, nhưng chỉ truyền 20% thời gian. Nếu dùng circuit switching, bao nhiêu người dùng được hỗ trợ?

Mỗi người dùng cần 1 Mbps, đường truyền có 2 Mbps → Tối đa 2 người dùng.

## Câu 13. Giả sử các người dùng chia sẻ một đường truyền 2 Mpbs. Mỗi người dùng truyền liên tục ở 1 Mbps khi đang truyền, nhưng chỉ truyền 20% thời gian. Nếu dùng packet switching, tại sao hầu như không có trễ hàng đợi khi có ≤ 2 người truyền đồng thời? Tại sao có trễ nếu 3 người cùng truyền?

Nếu ≤ 12 người truyền đồng thời, tổng băng thông yêu cầu ≤ 2 x 1 Mbps = 2 Mbps = dung lượng đường truyền → Không tắc nghẽn, không có hàng đợi. Nếu 3 người cùng truyền, tổng yêu cầu = 3 Mbps > 2 Mbps → hàng đợi bắt đầu tích lũy.

## Câu 13. Giả sử các người dùng chia sẻ một đường truyền 2 Mpbs. Mỗi người dùng truyền liên tục ở 1 Mbps khi đang truyền, nhưng chỉ truyền 20% thời gian.Tìm xác suất một người dùng đang truyền? 

Mỗi người dùng truyền 20% thời gian → p = 0.2.

## Câu 13. Giả sử các người dùng chia sẻ một đường truyền 2 Mpbs. Mỗi người dùng truyền liên tục ở 1 Mbps khi đang truyền, nhưng chỉ truyền 20% thời gian. Giả sử có 3 người dùng. Tìm xác suất cả 3 cùng truyền đồng thời. Tìm tỉ lệ thời gian hàng đợi tăng.

Xác suất cả 3 cùng truyền: P = 0.2^3 = 0.008.


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

## Câu 19. Host A muốn gửi file lớn đến host B qua 3 liên kết R1 = 500 kbps, R2 = 2 Mbps, R3 = 1 Mbps.Thông lượng (throughput) là bao nhiêu?

Throughput = min(500 kbps, 2 Mbps, 1 Mbps) = 500 kbps

## Câu 19. Host A muốn gửi file lớn đến host B qua 3 liên kết R1 = 500 kbps, R2 = 2 Mbps, R3 = 1 Mbps. File 4 triệu byte. Mất bao lâu để truyền xong?

T = 4 x 10^6 x 8 / (500 x 10^3) = 64 giây.

## Câu 20. End system A muốn gửi file lớn đến B. Mô tả cách A tạo ra các gói tin. Khi một gói tin đến switch, switch dùng thông tin gì để xác định liên kết cần chuyển tiếp?

End system A chia file thành các đoạn nhỏ (chunks). Mỗi đoạn được thêm header chứa thông tin điều khiển (địa chỉ nguồn, địa chỉ đích, số thứ tự, v.v..), tạo thành các gói tin (packets).
Switch chuyển tiếp: Switch đọc địa chỉ đích trong header của gói tin, tra forwarding table) để tìm liên kết đầu ra phù hợp.

## Phần 1.5

## Câu 22. Liệt kê năm nhiệm vụ mà một tầng (layer) có thể thực hiện. Có thể một hoặc nhiều nhiệm vụ được thực hiện bởi hai hoặc nhiều tầng không?

Năm nhiệm vụ: kiểm soát lỗi (error control), kiểm soát luồng (flow control), phân đoạn và tái hợp (segmentation & reassembly), ghép kênh (multiplexing), và thiết lập kết nối (connection setup). Có, các nhiệm vụ này có thế được thực hiện ở nhiều tầng. Ví dụ: kiểm soát lỗi được thực hiện ở cả tầng liên kết dữ liệu lẫn tầng vận chuyển.

## Câu 23. Năm tầng trong ngăn xếp giao thức Internet là gì? Trách nhiệm chính của mỗi tầng là gì?

Từ trên xuống:
1. Tầng ứng dụng (Application layer): hỗ trợ các ứng dụng mạng (HTTP, SMTP, FTP, DNS,…).
2. Tầng vận chuyển (Transport layer): truyền dữ liệu đầu cuối giữa các process (TCP, UDP).
3. Tầng mạng (Network layer): định tuyến datagram từ nguồn đến đích qua nhiều mạng (IP, OSPF,…).
4. Tầng liên kết dữ liệu (Link layer): truyền dữ liệu giữa các nút kề nhau trên cùng liên kết (Ethernet, Wifi).
5. Tầng vật lý (Physical Layer): truyền các bit thô qua môi trường vật lý (dây đồng, cáp quang, sóng vô tuyến,…)

## Câu 24. Application-layer message là gì? Transport-layer segment? Network-layer datagram? Link-layer frame?

- Application-layer message: dữ liệu mà ứng dụng muốn gửi, được chuyển xuống tầng vận chuyển (ví dụ: một trang HTML, một email).
- Transport-layer segment: đơn vị dữ liệu do tầng vận chuyển tạo ra, bao gồm message của tầng ứng dụng được đóng gói cùng header của tầng vận chuyển (chứa số port, số thứ tự,…)
- Network-layer datagram: đơn vị dữ liệu của tầng mạng, bao gồm segment tầng vận chuyển được đóng gói cùng header tầng mạng (chứa địa chỉ IP nguồn, đích…)
- Link-layer frame: đơn vị dữ liệu của tầng liên kết, bao gồm datagram tầng mạng được đóng gói cùng header tầng liên kết (chứa địa chỉ MAC…).

## Câu 25. Router xử lý những tầng nào? Link-layer switch xử lý những tầng nào? Host xử lý những tầng nào?

- Router xử lý tầng 1 đến tầng 3 (vật lý, liên kết, mạng). (Lưu ý: router hiện tại đôi khi xử lý cả tầng 4 khi hoạt động như firewall).
- Link-layer switch: xử lý tầng 1 và 2.
- Host: xử lý cả 5 tầng.

## Phần 1.6

## Câu 26. Sự khác biệt giữa virus và worm là gì?

Virus là phần mềm độc hại cần sự tương tác của người dùng để lây lan - ví dụ: người dùng mở file đính kèm email độc hại. Virus thường gắn vào chương trình khác.
Worm tự lan truyền không cần tương tác của người dùng - nó chủ động khai thác lỗ hổng bảo mật để tự sao chếp sang các máy tính khác trong mạng.

## Câu 28. Alice và Bob đang gửi gói tin cho nhau. Trudy đặt mình ở vị trí có thể chặn và gửi tùy ý mọi gói tin. Liệt kê những việc xấu Truly có thể làm.

Truly có thể: nghe lén, giả mạo danh tính, chèn dữ liệu giả, phát lại tấn công, xóa hoặc hoãn trì gói tin.
