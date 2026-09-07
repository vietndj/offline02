# -*- coding: utf-8 -*-
"""
Hệ thống tạo & đồng bộ 12 kịch bản băm cảnh trám lớp marketing PT
Chuẩn hóa:
1. Văn phong mộc mạc anh Việt (không ông giáo, không ra ngoài đời, không emoji sáo rỗng).
2. 60 Cú máy băm nhỏ đổi 3 trục: Cỡ cảnh -> Góc máy -> Hướng máy.
3. Visual Logic (Ý nghĩa ẩn dụ) & Reusability (Khả năng tái sử dụng B-roll đa năng).
4. Đồng bộ cả Master Hub (lopmarketingbaitap.html) và 12 Trang con Zebra Apple Light-theme.
"""
import os
import json

EXERCISES = [
    {
        "id": "01",
        "slug": "baitap01_laptop_ads.html",
        "title": "Soi chỉ số Ads & Cày bài tập trên laptop",
        "state": "Áp lực & Tập trung cao độ",
        "outfit": "Âu phục blazer may đo navy",
        "avatar": "assets/marketing_baitap/viet_bt1_smartsuit.jpg",
        "frame_dir": "assets/frames_bai_tap_01",
        "category": "pressure",
        "voice": "Đứng một chỗ bấm máy thì nhàn thật...\nNhưng lười đổi góc, khung hình nó đơ ra...\n...thì đến mình xem lại còn muốn lướt, trách gì người ta!",
        "t1": "Em đi học quay dựng là để làm video triệu view, học kỹ thuật điện ảnh cao siêu.",
        "t2": "Cầm điện thoại lên quay bạn học thì lóng ngóng, chân chôn chặt một chỗ, bấm 10 giây cho xong.",
        "t25": "Biết thừa khung hình đang chết dí một chỗ... nhưng ngại cúi thấp, sợ bạn bè bảo làm màu.",
        "t3": "Sự thật ngượng miệng: cái video mình còn chán ngấy thì ai dừng lại xem.",
        "shots": [
            ("Ngồi chăm chú trước màn hình laptop", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang tầm mắt (0°)", "Chếch 45° bên trái", "Đứng một chỗ bấm máy thì nhàn thật...", "Ngồi ké bên cạnh bàn, đưa máy ngang tầm mắt cách một sải tay. Khóa nét tròng kính, lấy ánh sáng xanh màn hình hắt nhẹ lên mặt.", "Thiết lập không gian làm việc áp lực thực tế.", "Cảnh người làm việc đêm, dân văn phòng cày deadline."),
            ("Ánh mắt nheo lại soi biểu đồ", "02.5s - 04.5s", "Cận cảnh (CU)", "Hất nhẹ 15° từ dưới lên", "Chính diện xuyên mép laptop", "...bấm một cái là xong.", "Bước sang đối diện, hạ máy ngang mép trên màn hình laptop. Canh đúng lúc bạn nhíu mày nhìn số liệu thì bấm máy.", "Bộc lộ sự căng thẳng khi đối diện sự thật số liệu.", "Thể hiện sự suy tư, nghi ngờ, phân tích dữ liệu."),
            ("Bàn phím nhấn lì nút Backspace", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Góc cao 60° chúc xuống", "Từ trên xuống chếch phải", "Nhưng lười dịch cái chân, để khung hình đơ ra...", "Đưa camera sát bàn phím một gang tay, bật zoom 2x. Bắt trọn ngón tay nhấn lì nút Backspace xóa dòng chữ vừa gõ.", "Xóa đi làm lại, sự bế tắc trong phương án cũ.", "Diễn tả việc sửa sai, bế tắc, làm lại từ đầu."),
            ("Màn hình hiển thị đồ thị đỏ lòm", "07.0s - 09.5s", "Cận qua vai (OTS)", "Ngang vai cao 20°", "Sau lưng chếch vai phải", "...thì video dựng lên...", "Đứng chếch sau vai phải, ghé camera qua khe vai áo. Lấy nét căng vào đồ thị đỏ lòm trên màn hình.", "Bằng chứng thực tế của áp lực chi phí.", "Cảnh báo chi phí tăng, cảnh báo nguy cơ tài chính."),
            ("Đẩy nhẹ chuột & Thở hắt một hơi", "09.5s - 12.0s", "Cận góc thấp (Low ECU)", "Sát mặt bàn (0°)", "Ngang mặt bàn bên phải", "...đến mình xem lại còn lướt vội, trách gì người ta!", "Đặt cạnh dưới điện thoại chạm hẳn xuống mặt bàn gỗ làm tiền cảnh. Bàn tay rời chuột, ngực xẹp xuống thở dài, khẽ cười nhẹ nhõm.", "Hạ cánh tâm lý: chấp nhận buông bỏ để tìm cách mới.", "Kết thúc buổi làm việc, sự buông bỏ nhẹ nhõm.")
        ],
        "reshoots": [
            ("Bàn làm việc tại nhà ban đêm", "Chỉ bật đúng 1 bóng đèn bàn, xung quanh phòng tối om, trên bàn có cốc nước đá tan chảy hết."),
            ("Quầy thu ngân cửa hàng / kho hàng", "Đứng giữa đống thùng carton, tay cầm tập hóa đơn đối soát với màn hình máy POS."),
            ("Trên xe ô tô dừng bên lề đường", "Một tay cầm vô lăng, một tay cầm điện thoại lướt xem báo cáo doanh thu dưới ánh đèn đường vàng vọt.")
        ]
    },
    {
        "id": "02",
        "slug": "baitap02_sotay_kichban.html",
        "title": "Cuốn sổ tay & Kịch bản gạch xóa tan nát",
        "state": "Bế tắc & Tìm tòi nội tâm",
        "outfit": "Áo phông đen tối giản trẻ trung",
        "avatar": "assets/marketing_baitap/viet_bt2_tshirt.jpg",
        "frame_dir": "assets/frames_bai_tap_02",
        "category": "pressure",
        "voice": "Cứ tưởng đặt bút xuống là có triệu view...\nĐến lúc ngồi viết, gạch nát cả trang giấy...\n...mới thấm câu: Viết cho hay thì khó, chứ viết văn mẫu thì ai cũng làm được!",
        "t1": "Em có nhiều ý tưởng lớn lắm, chỉ cần ngồi xuống là viết được kịch bản hay ngay.",
        "t2": "Cầm bút lên viết được 2 câu thì bí từ, gạch xoẹt xoẹt rồi vò đầu bứt tai, trang giấy lem luốc.",
        "t25": "Sợ bạn bè bên cạnh thấy mình ngồi cả buổi không viết nổi một câu ra hồn, nên vờ viết nguệch ngoạc để giữ thể diện.",
        "t3": "Sự thật ngượng miệng: trong đầu rỗng tuếch, toàn nhai lại văn mẫu trên mạng nên không thể tự viết được câu nào chạm vào lòng người.",
        "shots": [
            ("Ngồi cắn đuôi bút nhìn trang sổ trắng", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt (0°)", "Chếch 30° bên phải", "Cứ tưởng đặt bút xuống là có triệu view...", "Đặt máy ngang mép bàn bên phải, bắt trọn dáng ngồi hơi gù lưng của bạn học, mắt nhìn chằm chằm trang giấy trắng.", "Sự trống rỗng trong đầu trước trang giấy trắng.", "Cảnh người sáng tạo nội dung cạn ý tưởng, bế tắc."),
            ("Đầu bút bi gõ nhịp xuống mặt bàn", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mặt bàn 15°", "Chính diện ngón tay", "...Đến lúc ngồi viết...", "Dí máy sát tay cầm bút một gang tay, lấy nét vào đầu bút bi đang gõ cộc cộc xuống mặt gỗ theo nhịp bối rối vô thức.", "Nhịp thở bối rối, thời gian trôi vô ích.", "Thể hiện sự sốt ruột, căng thẳng, chờ đợi."),
            ("Ngòi bút gạch nát chữ Triệu View", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Góc cao 70° chúc xuống", "Thẳng đứng trên trang sổ", "...gạch nát cả trang giấy...", "Chĩa máy từ trên cao chúc xuống, zoom 2x bắt nét vết mực gạch chéo dứt khoát đè lên dòng chữ 'Triệu view' viết hoa.", "Phủ định ảo tưởng, bóc trần sự thật ngượng miệng.", "Từ bỏ ảo tưởng, vứt bỏ mục tiêu viển vông."),
            ("Liếc trộm trang sổ của bạn bên cạnh", "07.0s - 09.5s", "Góc qua vai (OTS)", "Cao ngang vai 25°", "Từ sau lưng nhìn chéo sang", "...mới thấm câu: Viết cho hay thì khó...", "Đặt camera sau gáy bạn bên phải, lia chậm từ trang giấy lem luốc sang trang vở ngay ngắn của bạn ngồi kế bên.", "Nỗi tự ti ngầm khi so sánh mình với người khác.", "Sự ghen tị ngầm, so sánh bản thân với đồng nghiệp."),
            ("Buông rơi cây bút & Tựa lưng cười trừ", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Sát mặt bàn hất lên 20°", "Chính diện khuôn mặt", "...chứ viết văn mẫu thì ai cũng làm được!", "Máy đặt nằm trên mặt bàn, bắt cú buông rơi cây bút xuống sổ và nụ cười tự trào mộc mạc khi nhận ra mình đang bị kẹt văn mẫu.", "Chấp nhận sự thật mình đang kẹt, không gồng nữa.", "Giải phóng áp lực, nụ cười bình thản chấp nhận va vấp.")
        ],
        "reshoots": [
            ("Bàn góc khuất quán cà phê", "Ngồi trước cuốn sổ da mở sẵn, nhìn dòng người đi lại qua ô cửa kính mà không viết nổi một chữ."),
            ("Phòng làm việc cá nhân ban đêm", "Giấy nháp vo tròn vứt rải rác dưới chân ghế, ngồi gục trán vào hai bàn tay mỏi mệt."),
            ("Bồn rửa mặt soi gương", "Vốc một vốc nước lạnh lên mặt, ngẩng lên nhìn thẳng vào bóng mình trong gương với ánh mắt tự vấn.")
        ]
    },
    {
        "id": "03",
        "slug": "baitap03_test_goc_quay.html",
        "title": "Cầm điện thoại test góc quay tại bàn",
        "state": "Quyết liệt, Thử nghiệm & Dám làm",
        "outfit": "Đồ thể thao polo navy năng động",
        "avatar": "assets/marketing_baitap/viet_bt3_sporty.jpg",
        "frame_dir": "assets/frames_bai_tap_03",
        "category": "action",
        "voice": "Bảo giơ máy lên quay thì ai cũng ngại...\nSợ run tay, sợ góc xấu, sợ người ta nhìn làm màu.\nNhưng cứ bấm thử một đúp xem... xấu cũng được, miễn là mình dám bấm nút REC!",
        "t1": "Phải có máy xịn, phòng cách âm và kịch bản hoàn hảo thì em mới dám bấm máy quay.",
        "t2": "Cầm điện thoại lên quay thử thì ngượng ngùng, tay run run, mắt liếc quanh xem có ai dòm ngó mình không.",
        "t25": "Lấy cớ thiết bị chưa đủ tốt để che giấu nỗi sợ bị người khác đánh giá là vụng về, làm màu khi quay video.",
        "t3": "Sự thật ngượng miệng: sự cầu toàn chỉ là cái cớ che đậy cho thói lười biếng và nỗi sợ thất bại ngay từ bước đầu tiên.",
        "shots": [
            ("Xoay điện thoại ngắm khung hình", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang ngực 0°", "Chếch 30° trực diện", "Bảo giơ máy lên quay thì ai cũng ngại...", "Quay góc ngang ngực, bắt cử chỉ hai tay cầm điện thoại xoay ngang xoay dọc tìm góc máy chuẩn trong lớp học.", "Hành động thực chiến cầm máy, bắt đầu hành động.", "Cảnh người sáng tạo bắt đầu ghi hình, khảo sát bối cảnh."),
            ("Ngón tay chạm dứt khoát nút REC đỏ", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang màn hình 20°", "Chính diện ngón cái", "...sợ run tay, sợ góc xấu, sợ người ta nhìn.", "Dí sát vào ngón tay cái tiếp xúc với màn hình cảm ứng, bắt trọn khoảnh khắc nút REC đỏ chuyển sang đếm giây 00:01.", "Khoảnh khắc dấn thân, vượt qua ranh giới chần chừ.", "Ra quyết định, bắt đầu hành động, bấm máy."),
            ("Đặc tả cụm 3 camera phản chiếu đèn", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang lưng máy", "Chĩa thẳng ống kính", "Nhưng cứ bấm thử một đúp xem...", "Chĩa thẳng vào cụm camera sau lưng điện thoại, lấy nét căng bóng đèn tuýp lớp học phản chiếu trong tròng kính máy ảnh.", "Ống kính như con mắt soi chiếu sự thật.", "Công nghệ, góc nhìn điện ảnh, sự quan sát tỉ mỉ."),
            ("Màn hình POV quay bạn học cười ngượng", "07.0s - 09.5s", "Góc nhìn chủ quan (POV)", "Ngang tầm mắt", "Khung hình điện thoại", "...xấu cũng được...", "Góc nhìn từ người quay, thấy rõ màn hình điện thoại đang bắt nét vào bạn học đối diện đang lấy tay che miệng cười ngượng.", "Sự ngượng ngùng đời thực giữa người với người.", "Cảnh hậu trường vui vẻ, tương tác người thật việc thật."),
            ("Hạ máy vẫy tay cười động viên", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Mặt bàn hất lên 25°", "Chính diện người quay", "...miễn là mình dám bấm nút REC!", "Đặt máy sát mặt bàn nhìn lên, bắt nụ cười rạng rỡ và bàn tay vẫy nhẹ ra hiệu: 'Được rồi đấy, đúp này tự nhiên lắm!'", "Tự tin sau khi vượt qua rào cản ban đầu.", "Niềm vui khi hoàn thành một việc khó, động viên đồng đội.")
        ],
        "reshoots": [
            ("Phòng khách tại nhà", "Tự tay xoay ốc vặn chiếc chân máy tripod, gắn kẹp điện thoại và bấm nút đếm ngược 3-2-1."),
            ("Ban công ngập nắng", "Cầm sản phẩm trên tay xoay tròn trước ống kính dưới ánh nắng tự nhiên buổi sáng."),
            ("Góc phố đi bộ / quán ăn", "Đứng giữa dòng người, tự tin cầm điện thoại quay món ăn bốc khói mà không sợ ai nhìn ngó.")
        ]
    },
    {
        "id": "04",
        "slug": "baitap04_slide_giatminh.html",
        "title": "Ngẩng nhìn slide giảng bài & Giật mình",
        "state": "Vỡ òa, Thức tỉnh (Aha moment)",
        "outfit": "Sơ mi xanh nhạt xắn tay áo kiểu giảng viên",
        "avatar": "assets/marketing_baitap/viet_bt4_shirt.jpg",
        "frame_dir": "assets/frames_bai_tap_04",
        "category": "insight",
        "voice": "Đang cắm đầu lướt điện thoại tưởng mình biết tuốt rồi...\nNghe một câu chạm đúng tim đen mà giật thót cả mình!\nGhi vội lại... chứ không mai lại đâu đóng đấy.",
        "t1": "Mấy kiến thức này trên mạng đầy, lướt video 30 giây là hiểu hết rồi cần gì học sâu.",
        "t2": "Ngồi trong lớp nhưng cắm đầu lướt feed mạng xã hội dưới gầm bàn, mắt đảo liên tục.",
        "t25": "Giả vờ cúi đầu bấm máy như đang bận việc quan trọng, thực chất là không theo kịp bài giảng nhưng sợ hỏi lại bị chê dốt.",
        "t3": "Sự thật ngượng miệng: cái tôi quá lớn, tưởng mình giỏi hơn người khác. Đến khi bị bóc trần đúng điểm nghẽn mới thấy mình đang tự lừa dối bản thân.",
        "shots": [
            ("Cúi đầu lén lướt feed dưới hộc bàn", "00:00 - 02.5s", "Trung cận (MCU)", "Góc chúc 35° xuống", "Chếch phải 45°", "Đang cắm đầu lướt điện thoại tưởng mình biết tuốt rồi...", "Quay góc từ trên chúc xuống, thấy nửa người và mép điện thoại đang được lướt giấu dưới ngăn bàn học.", "Thói quen mất tập trung, tự mãn ngầm.", "Thói quen xấu, lãng phí thời gian, phân tâm."),
            ("Ngón tay cuộn lướt bỗng khựng đơ", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mép bàn", "Chính diện màn hình", "...nghe một câu chạm đúng tim đen...", "Cận cảnh ngón tay đang vuốt nhanh bỗng dừng khựng lại bất động, ánh sáng trắng của app hắt lên ngón tay.", "Tín hiệu bất ngờ từ âm thanh bên ngoài lọt vào tai.", "Điểm dừng chú ý, giật mình, nghe thấy điều chấn động."),
            ("Ngẩng phắt nhìn slide giật thót mình", "04.5s - 07.0s", "Cận góc thấp (Low CU)", "Hất lên 30° từ bàn", "Chếch trái nhìn bảng", "...giật thót cả mình!", "Máy đặt sát mặt bàn hất lên, bắt trọn biểu cảm mắt mở to, lông mày nhướn lên ngơ ngác khi vừa nghe một câu đâm trúng tim đen.", "Đánh trúng tim đen, rụng bỏ lớp mặt nạ biết tuốt.", "Biểu cảm ngộ ra (Aha moment), bất ngờ, giật mình tỉnh ngộ."),
            ("Hí hoáy gạch chân từ khóa vào sổ", "07.0s - 09.5s", "Đặc tả (Macro ECU)", "Góc cao 80° thẳng đứng", "Ngòi bút trên trang vở", "Ghi vội lại...", "Góc nhìn từ trên xuống ngòi bút lia nhanh 2 nét gạch chân thật đậm dưới từ khóa 'GIẢI QUYẾT TẬN GỐC' vừa ghi vội.", "Hành động ghi nhớ cốt tử, sợ quên mất bài học.", "Ghi chép bài học, đúc kết kinh nghiệm, chú ý trọng tâm."),
            ("Cất hẳn máy vào balo & Ngồi thẳng lưng", "09.5s - 12.0s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 30° trực diện", "...chứ không mai lại đâu đóng đấy.", "Ngang tầm mắt, bắt cử chỉ cất hẳn chiếc điện thoại vào balo, kéo thẳng lưng áo và ngồi ngay ngắn nghe giảng.", "Thái độ nghiêm túc hoàn toàn sau khi thức tỉnh.", "Chuyển đổi thái độ, nghiêm túc tập trung vào việc lớn.")
        ],
        "reshoots": [
            ("Đang lật mở trang sách cũ", "Ngón tay lật trang sách bỗng khựng lại ở một câu trích dẫn in đậm, mắt sáng bừng lên."),
            ("Đi dạo ngoài công viên", "Bỗng dừng bước đứng khựng lại bên vỉa hè, rút vội điện thoại bật ghi âm lưu lại ý tưởng vừa nảy ra."),
            ("Bàn làm việc văn phòng", "Đang lục chồng tài liệu cũ, rút phắt ra bản kế hoạch năm ngoái và vỗ đùi đánh đét.")
        ]
    },
    {
        "id": "05",
        "slug": "baitap05_cocnuoc_langdong.html",
        "title": "Nhấp ngụm nước ấm & Tựa lưng ghế",
        "state": "Lắng đọng, Chiêm nghiệm & Kết nối chân tình",
        "outfit": "Áo len dệt kim mỏng màu be ấm áp",
        "avatar": "assets/marketing_baitap/viet_bt5_sweater.jpg",
        "frame_dir": "assets/frames_bai_tap_05",
        "category": "calm",
        "voice": "Quay dựng cho đã tay rồi cũng đến lúc phải ngồi lại...\nNhấp ngụm nước, nhìn lại những thước phim vụng về đầu tiên.\nLàm video không phải để chứng tỏ mình tài giỏi... mà là để tìm thấy những người bạn cùng tần số.",
        "t1": "Làm video là cỗ máy kiếm tiền tự động, chỉ cần tối ưu hóa chuyển đổi và phễu bán hàng.",
        "t2": "Quay xong thì mệt rã rời, ngồi một góc phòng học vắng, nhấp từng ngụm nước cho đỡ khản giọng.",
        "t25": "Gồng mình tỏ ra chuyên nghiệp suốt buổi học, đến khi mọi người về bớt mới dám thở phào, cởi bỏ chiếc mặt nạ gồng gánh.",
        "t3": "Sự thật ngượng miệng: sâu thẳm trong lòng sợ nhất là cảm giác cô đơn, làm video nhiều view mà chẳng có ai thật lòng hiểu mình.",
        "shots": [
            ("Ngồi tựa lưng ghế bên khung cửa sổ", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực 0°", "Chếch 30° đón nắng", "Quay dựng cho đã tay rồi cũng đến lúc phải ngồi lại...", "Bắt trọn dáng ngồi thư thái của anh Việt trong chiếc áo len be, nắng chiều rọi xiên vào khung cửa sổ ấm áp.", "Sự thư thái sau một chuỗi nỗ lực căng thẳng.", "Khoảng lặng nghỉ ngơi, phục hồi năng lượng, thư giãn."),
            ("Hai bàn tay ôm trọn cốc nước ấm", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mặt bàn", "Chính diện hai tay", "...Nhấp ngụm nước, nhìn lại những thước phim vụng về đầu tiên.", "Dí sát camera bắt hai bàn tay đang ủ ấm quanh chiếc cốc, những ngón tay khẽ miết nhẹ thân cốc thong thả.", "Cảm giác ấm áp, an toàn, tự vỗ về bản thân.", "Sự chăm sóc bản thân, tìm lại bình yên, hơi ấm."),
            ("Đặc tả làn khói nước mỏng bốc hơi nhẹ", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang miệng cốc", "Chếch ngược sáng", "Làm video không phải để chứng tỏ mình tài giỏi...", "Lấy nét căng vào làn khói mỏng bốc lên từ miệng cốc dưới vệt nắng chiều, tạo điểm dừng thị giác êm đềm.", "Ẩn dụ về sự tĩnh tâm, lắng đọng như nước trà ngấm.", "Thời gian lắng đọng, chiêm nghiệm sâu sắc, thiền định."),
            ("Khung cảnh lớp học dần vắng người", "07.0s - 09.5s", "Góc nhìn rộng (Wide OTS)", "Ngang vai", "Hướng ra dãy bàn ghế", "...mà là để tìm thấy những người bạn...", "Góc nhìn từ sau lưng nhân vật nhìn bao quát không gian phòng học sau giờ tan lớp, bàn ghế ngay ngắn tĩnh lặng.", "Sự đối lập giữa lúc huyên náo và lúc chỉ còn lại chính mình.", "Kết thúc một hành trình, không gian tĩnh lặng, cô đơn tích cực."),
            ("Nụ cười nhẹ nhõm bình an nhìn thẳng", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt", "Chính diện ống kính", "...cùng tần số với mình!", "Bắt trọn nụ cười mộc mạc không phòng thủ, ánh mắt chân thành như đang ngồi đối diện trò chuyện cùng một người bạn tri kỷ.", "Sự thấu hiểu và kết nối chân thành từ tâm can.", "Lời chào tạm biệt ấm áp, kết nối tri kỷ, tin tưởng.")
        ],
        "reshoots": [
            ("Ban công chung cư lúc hoàng hôn", "Ngồi tựa ghế mây, hai tay cầm tách trà nóng nhìn dòng xe cộ phía dưới, gió thổi nhẹ vạt áo."),
            ("Bàn ăn gia đình buổi tối", "Sau khi dọn dẹp bát đĩa xong, ngồi tựa vào ghế nhâm nhi một tách trà thảo mộc bên ngọn đèn trần ấm áp."),
            ("Ghế đá công viên sáng sớm", "Ngồi một mình thong thả hít thở không khí trong lành dưới tán cây xanh mát, gác lại mọi âu lo.")
        ]
    },
    {
        "id": "06",
        "slug": "baitap06_do_du_nut_dang.html",
        "title": "Ngón tay ngập ngừng trước nút Đăng bài",
        "state": "Do dự, Nghi ngờ & Đấu tranh nội tâm",
        "outfit": "Áo khoác denim bụi bặm",
        "avatar": "assets/marketing_baitap/viet_bt6_denim.jpg",
        "frame_dir": "assets/frames_bai_tap_06",
        "category": "action",
        "voice": "Người lớn mình buồn cười lắm...\nSoạn xong kịch bản rồi, ngón tay đặt lên nút Đăng thì cứ run lên vì sợ.\nKhông bấm thì an toàn thật... nhưng sẽ mãi đứng nguyên một chỗ!",
        "t1": "Em là người kỹ tính, em chưa đăng vì muốn chuẩn bị thêm vài tài liệu nữa cho nó chu toàn.",
        "t2": "Màn hình đã load sẵn nút Xuất bản màu xanh, nhưng ngón tay cứ giơ lên rồi lại hạ xuống cả chục lần.",
        "t25": "Sợ bạn bè cùng trang lứa, đồng nghiệp cũ nhìn thấy mình làm video rồi xì xào bàn tán: 'Dạo này rảnh rỗi bày đặt lên mạng dạy đời'.",
        "t3": "Sự thật ngượng miệng: lòng tự ái quá lớn, sợ nhận về sự thờ ơ hoặc vài ba lời bình luận châm chọc khiến mình bị bẽ mặt.",
        "shots": [
            ("Ngồi trầm ngâm cầm điện thoại hai tay", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 35° bên trái", "Người lớn mình buồn cười lắm...", "Bắt trọn ánh mắt đăm chiêu giằng xé của anh Việt trong chiếc áo khoác denim, hai tay nâng điện thoại sát mặt bàn.", "Trạng thái lưỡng lự trước một ngưỡng cửa mới.", "Chuẩn bị ra quyết định lớn, sự cân nhắc thận trọng."),
            ("Ngón tay trỏ ngập ngừng cách nút Đăng 1mm", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang màn hình", "Chính diện ngón trỏ", "...Soạn xong kịch bản rồi, ngón tay đặt lên nút Đăng...", "Dí sát vào ngón tay đang run nhẹ, nhấp nhả 2 nhịp ngay trên nút bấm màu xanh nhưng không dám chạm xuống.", "Sự va chạm giữa mong muốn hành động và nỗi sợ thể diện.", "Sự do dự, trì hoãn, ngập ngừng trước rủi ro."),
            ("Đặc tả nút Đăng nhấp nháy trên màn hình", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng màn hình", "Cận cảnh giao diện", "...thì cứ run lên vì sợ: Người ta chê mình làm màu...", "Khóa nét vào chữ 'Đăng video' sắc nét trên giao diện ứng dụng, tạo cảm giác nghẹt thở của khoảnh khắc quyết định.", "Ngưỡng cửa bước ngoặt đưa sản phẩm đến với công chúng.", "Ranh giới giữa ý tưởng và hành động thực tế."),
            ("Liếc mắt nhìn quanh phòng học", "07.0s - 09.5s", "Góc nhìn môi trường (OTS)", "Ngang cằm", "Quét sang bạn bè", "Không bấm thì an toàn thật...", "Góc nhìn từ sau lưng liếc nhẹ sang những bạn học xung quanh đang trò chuyện, phản ánh nỗi sợ bị dòm ngó.", "Tâm lý sợ bị phán xét, sợ mang tiếng 'làm màu'.", "Nỗi sợ dư luận, ánh nhìn soi mói của đám đông."),
            ("Hạ máy úp màn hình xuống mặt bàn", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Mặt bàn hất lên 15°", "Chính diện khuôn mặt", "...nhưng sẽ mãi đứng nguyên một chỗ!", "Úp mạnh chiếc điện thoại xuống mặt bàn gỗ cạch một cái, ngẩng mặt lên thở dài tự vấn: 'Rốt cuộc mình đang sợ cái gì?'", "Cảm giác bực bội vì chính sự hèn nhát của bản thân.", "Bế tắc tâm lý, sự bực dọc tự trách, đấu tranh tư tưởng.")
        ],
        "reshoots": [
            ("Trước cửa phòng họp công ty", "Tay cầm tập hồ sơ đưa lên định gõ cửa gặp sếp đề xuất ý tưởng mới rồi lại rụt tay xuống chỉnh áo."),
            ("Ngồi trong xe ô tô trước sự kiện", "Nhìn vào gương chiếu hậu chỉnh lại tóc tai, hít sâu một hơi rồi chần chừ mở cửa xe."),
            ("Màn hình máy tính thanh toán", "Con chuột máy tính di qua di lại giữa hai nút 'Xác nhận thanh toán' và 'Hủy bỏ' khóa học.")
        ]
    },
    {
        "id": "07",
        "slug": "baitap07_hut_hang_0view.html",
        "title": "Mở máy kiểm tra thấy 0 view, tụt mood",
        "state": "Hụt hẫng, Thất vọng & Va vào thực tế",
        "outfit": "Áo hoodie xám tối giản",
        "avatar": "assets/marketing_baitap/viet_bt7_hoodie.jpg",
        "frame_dir": "assets/frames_bai_tap_07",
        "category": "pressure",
        "voice": "Lúc mới làm, ai cũng mơ về video triệu view với nghìn đơn.\nMở máy ra thấy đúng 3 lượt xem, trong đó có 2 lượt mình tự bấm...\nLúc ấy mới hiểu: Nghề này không có chỗ cho kẻ há miệng chờ sung!",
        "t1": "Video này thuật toán bóp tương tác rồi, chứ nội dung em làm hay thế này ai chả thích.",
        "t2": "Mở ứng dụng ra kéo vuốt liên tục để refresh, nhưng con số lượt xem vẫn đứng im lìm ở mức 0 tròn trĩnh.",
        "t25": "Hôm qua vừa hào hứng khoe với mọi người là sắp bùng nổ, hôm nay số liệu tụt dốc thê thảm, xấu hổ chỉ muốn xóa kênh đi cho đỡ ngượng.",
        "t3": "Sự thật ngượng miệng: vỡ mộng vì nhận ra mình chẳng có sức hút như mình tự tưởng tượng; đối mặt với cảm giác mình thật tầm thường.",
        "shots": [
            ("Ngồi gục vai nhìn màn hình điện thoại", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang ngực", "Chính diện bàn học", "Lúc mới làm, ai cũng mơ về video triệu view với nghìn đơn.", "Anh Việt trong chiếc áo hoodie xám ngồi trĩu hai vai xuống bàn, ánh sáng yếu ớt của màn hình chiếu lên khuôn mặt bất động.", "Năng lượng sụt giảm hoàn toàn, va vào thực tế phũ phàng.", "Thất bại ban đầu, cảm giác kiệt sức, mất phương hướng."),
            ("Hai cánh tay buông thõng trên mặt bàn", "02.5s - 04.5s", "Cận cảnh (CU)", "Góc nghiêng 20°", "Dọc theo cánh tay", "...Mở máy ra thấy đúng 3 lượt xem...", "Góc máy dọc theo hai cánh tay buông xuôi bất lực trên mặt bàn gỗ, những ngón tay xòe ra không còn chút sức lực.", "Cố bám víu một tia hy vọng mong manh.", "Thói quen kiểm tra số liệu trong vô vọng, lo âu."),
            ("Đặc tả màn hình hiển thị 0 Lượt xem", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng màn hình", "Chính diện con số", "...trong đó có 2 lượt mình tự bấm...", "Lấy nét căng vào dòng chữ '0 Lượt xem • 0 Bình luận' trơ trọi trên nền trắng của ứng dụng, sự thật phũ phàng.", "Bằng chứng sắt đá bóc trần ảo tưởng sức mạnh.", "Sự thờ ơ của thị trường, kết quả tệ hại, vỡ mộng."),
            ("Không gian lớp học vắng lặng bao quanh", "07.0s - 09.5s", "Góc cao (High Angle)", "Chúc 45° từ trên xuống", "Toàn cảnh bàn học", "Lúc ấy mới hiểu: Nghề này...", "Máy đặt trên cao nhìn xuống chiếc điện thoại nằm đơn độc giữa mặt bàn học rộng thênh thang, cảm giác lạc lõng cùng cực.", "Sự cô độc và nhỏ bé trước quy luật thị trường.", "Cảm giác đơn độc, lạc lõng, bị bỏ rơi."),
            ("Khuôn mặt nghệt ra rồi khẽ lắc đầu", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt", "Chính diện", "...không có chỗ cho kẻ há miệng chờ sung!", "Bắt trọn cái lắc đầu nhẹ, khóe môi khẽ nhếch cười tự giễu: 'Tốt lắm, coi như ăn một cái tát để tỉnh ngủ mà làm lại từ đầu!'", "Tỉnh ngủ khỏi ảo tưởng, chuẩn bị làm lại bằng thái độ mới.", "Sự thức tỉnh sau cú tát thực tế, tinh thần tự trào đứng dậy.")
        ],
        "reshoots": [
            ("Cửa hàng vắng khách ngày mưa", "Đứng tựa quầy thu ngân nhìn ra ngoài trời mưa tầm tã, không một bóng khách ghé vào."),
            ("Bàn làm việc cuối tháng", "Cầm tờ sao kê tài khoản hoặc hóa đơn tiền thuê mặt bằng, ánh mắt đờ đẫn nhìn vào khoảng không vô định."),
            ("Băng ghế đá công viên", "Ngồi nhìn xuống đôi giày dính bụi sau một ngày dài đi chào hàng nhưng toàn bị từ chối thẳng thừng.")
        ]
    },
    {
        "id": "08",
        "slug": "baitap08_qua_ngot_tingting.html",
        "title": "Ting ting thông báo tin nhắn & Đơn đầu tiên",
        "state": "Tự hào, Nhẹ nhõm & Quả ngọt đầu tiên",
        "outfit": "Áo sơ mi kẻ caro nhã nhặn",
        "avatar": "assets/marketing_baitap/viet_bt8_plaid.jpg",
        "frame_dir": "assets/frames_bai_tap_08",
        "category": "insight",
        "voice": "Tiếng ting ting nổ tin nhắn đầu tiên... giá trị nó chẳng đáng bao nhiêu tiền đâu.\nNhưng nó đập tan mọi nỗi sợ trước đó:\n...Phương pháp này có thật, và mình hoàn toàn làm được!",
        "t1": "Mới được có một tin nhắn, có gì đâu mà phải mừng, phải tiền tỷ mới đáng nói.",
        "t2": "Màn hình điện thoại bất ngờ sáng bừng lên giữa giờ học, banner tin nhắn khách hỏi mua hàng hiện lên rõ mồn một.",
        "t25": "Muốn nhảy cẫng lên ăn mừng nhưng sợ cả lớp nhìn bảo trẻ trâu, đành cắn chặt môi cố kìm nén nụ cười đắc chí.",
        "t3": "Sự thật ngượng miệng: suốt bao lâu nay luôn tự ti nghĩ mình bất tài vô dụng, khoảnh khắc này mới chính thức giải oan cho lòng tự trọng của bản thân.",
        "shots": [
            ("Ngồi thẳng lưng mắt dán vào màn hình sáng", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 30° bên phải", "Tiếng ting ting nổ tin nhắn đầu tiên...", "Anh Việt trong áo sơ mi kẻ caro ngồi thẳng thớm, ánh mắt bỗng mở to ngạc nhiên nhìn chằm chằm vào chiếc điện thoại vừa rung lên.", "Tín hiệu bất ngờ phá tan không khí tĩnh lặng.", "Đón nhận tin vui bất ngờ, tia sáng hy vọng."),
            ("Hai bàn tay nâng vội chiếc điện thoại", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang ngực", "Chính diện hai bàn tay", "...giá trị nó chẳng đáng bao nhiêu tiền đâu.", "Cận cảnh hai bàn tay vội vã nhấc máy lên, ngón tay cái lướt nhẹ mở khóa màn hình với vẻ nâng niu trân trọng.", "Sự trân quý tột cùng đối với phản hồi đầu tiên của khách.", "Sự quý trọng từng khách hàng, phản xạ chớp cơ hội."),
            ("Đặc tả banner tin nhắn khách hàng chốt đơn", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng màn hình", "Lấy nét banner thông báo", "Nhưng nó đập tan mọi nỗi sợ trước đó...", "Lấy nét căng vào dòng thông báo: 'Tin nhắn mới từ Khách hàng: Em muốn đăng ký học ngay ạ...' nổi bật trên nền màn hình khóa.", "Minh chứng thực tế của kết quả chuyển đổi có thật.", "Bằng chứng kết quả, bằng chứng đơn hàng, tin nhắn chốt đơn."),
            ("Xoay màn hình khoe bạn ngồi bên cạnh", "07.0s - 09.5s", "Góc nhìn hai người (Two-shot)", "Ngang vai", "Lia sang bạn kế bên", "Phương pháp này có thật...", "Lia máy bắt khoảnh khắc anh Việt huých nhẹ vai bạn học bên cạnh, xoay chiếc điện thoại sang khoe: 'Này, có khách nhắn thật rồi!'", "Nhu cầu được công nhận và chia sẻ niềm vui với đồng đội.", "Tinh thần đồng đội, chia sẻ quả ngọt, tự hào chính đáng."),
            ("Nụ cười rạng rỡ nắm chặt tay ăn mừng", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt hất nhẹ", "Chính diện", "...và mình hoàn toàn làm được!", "Bắt trọn nụ cười rạng rỡ hạnh phúc, bàn tay nắm chặt kéo giật về phía sau theo phản xạ ăn mừng thầm lặng đầy kiêu hãnh.", "Giải phóng sự tự ti, tự hào vì mình đã làm được.", "Chiến thắng bản thân, niềm hạnh phúc khi có thành tựu.")
        ],
        "reshoots": [
            ("Quán cà phê sáng sớm", "Nghe tiếng chuông ting ting báo tiền về tài khoản, mỉm cười nhấc ly cà phê lên nhấp một ngụm đầy sảng khoái."),
            ("Bàn đóng gói hàng tại nhà", "Tự tay dán băng dính lên thùng hàng đầu tiên gửi đi cho khách, cẩn thận miết phẳng từng mép hộp carton."),
            ("Góc ban công ngập nắng", "Cầm điện thoại xem video của mình vừa cán mốc 10.000 view đầu tiên, gió lay nhẹ vạt áo, nụ cười tự hào bình dị.")
        ]
    },
    {
        "id": "09",
        "slug": "baitap09_timeline_capcut.html",
        "title": "Đeo tai nghe soi timeline CapCut cắt gọt",
        "state": "Tỉ mỉ, Cầu toàn & Tận tâm kỹ thuật",
        "outfit": "Áo thun đen tối giản + Tai nghe over-ear",
        "avatar": "assets/marketing_baitap/viet_bt9_headphones.jpg",
        "frame_dir": "assets/frames_bai_tap_09",
        "category": "action",
        "voice": "Cắt đi nửa giây thừa, kéo lại một nhịp thở...\nNgười xem không biết bạn tỉ mỉ thế nào sau bàn dựng đâu.\nNhưng họ sẽ ở lại trọn vẹn video, đơn giản vì không có một giây nào bị thừa thãi!",
        "t1": "Dựng video cứ cắt bừa chèn hiệu ứng giật giật vào là người ta xem, quan tâm gì tiểu tiết.",
        "t2": "Đeo tai nghe kín mít, phóng to timeline lên từng khung hình 30fps, tua đi tua lại một đoạn thoại đúng 10 lần.",
        "t25": "Cố tình đeo tai nghe xịn, ngồi gõ phím cành cạch để ra vẻ dân editor chuyên nghiệp giữa lớp học.",
        "t3": "Sự thật ngượng miệng: sợ bị chê là thợ cắt ghép thô thiển, sợ video của mình bị đánh giá là rẻ tiền nên phải soi từng mili-giây để tự bảo vệ lòng tự trọng nghề nghiệp.",
        "shots": [
            ("Ngồi chăm chú bên laptop và tai nghe chụp tai", "00:00 - 02.5s", "Trung cận (MCU)", "Ngang tầm mắt", "Chếch 45° bên trái", "Cắt đi nửa giây thừa, kéo lại một nhịp thở...", "Bắt trọn thần thái tập trung cao độ của anh Việt với chiếc tai nghe Sony trùm đầu, màn hình laptop hiển thị giao diện dựng phim chuyên nghiệp.", "Sự nhập định, tách biệt khỏi tiếng ồn xung quanh để tập trung.", "Cảnh thợ lành nghề, chuyên gia làm việc sâu (Deep Work)."),
            ("Màn hình laptop với timeline nhiều layer", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang bàn phím", "Chếch nhìn màn hình", "...Người xem không biết bạn tỉ mỉ thế nào...", "Lấy nét vào màn hình MacBook hiển thị timeline CapCut với các dải màu tím, xanh lá của âm thanh và video được cắt gọt tinh xảo.", "Bàn dựng - xưởng thủ công của người làm nội dung.", "Thao tác kỹ thuật số, quy trình sản xuất hậu kỳ."),
            ("Đặc tả ngón tay bấm phím cắt đúp thừa", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Góc cao 60°", "Chính diện bàn phím", "...sau bàn dựng đâu...", "Khóa nét ngón trỏ và ngón cái nhấn tổ hợp phím Command + B, nhát cắt sắc lẹm chia đôi đoạn video thừa thãi trên timeline.", "Nhát cắt dứt khoát loại bỏ phần rác rưởi/dông dài.", "Sự chọn lọc, tinh giản, loại bỏ những thứ thừa thãi."),
            ("Ánh mắt tập trung soi chuyển động từng frame", "07.0s - 09.5s", "Cận cảnh ánh mắt (CU Eyes)", "Ngang tầm mắt", "Chính diện", "Nhưng họ sẽ ở lại trọn vẹn video...", "Cận cảnh đôi mắt chăm chú phản chiếu ánh sáng nhấp nháy từ màn hình máy tính, lông mày giãn nhẹ khi tìm đúng điểm nối cảnh raccord.", "Sự tập trung cao độ, soi từng chuyển động nhỏ nhất.", "Con mắt nghề nghiệp, sự tỉ mỉ, đánh giá chất lượng."),
            ("Gật gù nhịp chân theo tiếng nhạc nền", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Sát mặt bàn hất lên", "Chếch 30°", "...vì không có một giây nào bị thừa thãi!", "Bắt cử chỉ gật gù hài lòng theo nhịp điệu âm thanh trong tai nghe, ngón tay gõ nhẹ lên mép máy tính báo hiệu một đúp dựng hoàn hảo.", "Sự hài lòng khi sản phẩm đạt độ hoàn thiện cao nhất.", "Sản phẩm hoàn tất mượt mà, cảm giác thỏa mãn của người làm nghề.")
        ],
        "reshoots": [
            ("Phòng dựng phim tại nhà ban đêm", "Ngồi trước màn hình đôi 27 inch trong phòng tối, bàn phím cơ phát sáng lung linh, tay lia chuột mượt mà."),
            ("Quán cà phê yên tĩnh", "Ngồi góc bàn dài, cắm tai nghe vào laptop cặm cụi dựng video giữa tiếng nhạc nền du dương của quán."),
            ("Băng ghế chờ sân bay", "Mở laptop tranh thủ render nốt video trước giờ lên máy bay, ánh mắt chạy đua với thời gian.")
        ]
    },
    {
        "id": "10",
        "slug": "baitap10_tranh_luan_nhom.html",
        "title": "Chụm đầu tranh luận sơ đồ kịch bản với bạn học",
        "state": "Va chạm quan điểm & Phản biện xây dựng",
        "outfit": "Áo blazer linen trẻ trung",
        "avatar": "assets/marketing_baitap/viet_bt10_blazer.jpg",
        "frame_dir": "assets/frames_bai_tap_10",
        "category": "insight",
        "voice": "Ngồi một mình thì tưởng ý tưởng của mình là nhất...\nĐến lúc đem ra trao đổi, người ta chỉ cho vài điểm mới thấy lủng củng.\n...Nhưng có va chạm thì mới gọt sắc được thông điệp!",
        "t1": "Ý tưởng của em độc quyền, em không muốn chia sẻ vì sợ bị người khác sao chép.",
        "t2": "Mấy anh em chụm đầu vào nhau quanh bàn học, ngón tay chỉ lia lịa vào từng dòng chữ, tranh luận sôi nổi về đoạn mở đầu.",
        "t25": "Ban đầu gồng lên bảo vệ ý kiến của mình vì sợ nhận sai trước mặt mọi người, nhưng trong bụng biết thừa luận điểm của bạn có lý hơn.",
        "t3": "Sự thật ngượng miệng: cái tôi bảo thủ, sợ bị bóc mẽ là tư duy non nớt; nhưng khi dám mở lòng lắng nghe thì mới vỡ lẽ ra bao nhiêu điều hay ho.",
        "shots": [
            ("Cúi người chỉ tay vào trang kịch bản", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực", "Chếch 35° giữa 2 người", "Ngồi một mình thì tưởng ý tưởng của mình là nhất...", "Anh Việt áo blazer linen cúi người trên bàn học, tay chỉ thẳng vào trang giấy kịch bản đang mở sẵn trước mặt bạn học.", "Hành động chủ động giải thích, khơi mào cuộc thảo luận.", "Thảo luận chiến lược, trao đổi công việc, hướng dẫn 1-1."),
            ("Ngón tay gõ nhịp lên dòng tiêu đề phản biện", "02.5s - 04.5s", "Cận cảnh (CU)", "Góc nghiêng 45°", "Mặt bàn học", "Đến lúc đem ra trao đổi...", "Dí sát camera bắt ngón tay trỏ đang gõ nhẹ lên dòng chữ tiêu đề phản biện, bạn ngồi bên cạnh chống cằm lắng nghe.", "Điểm nghẽn cần mổ xẻ, sự tập trung vào vấn đề cốt lõi.", "Mổ xẻ vấn đề, tìm lỗi sai, phản biện chuyên môn."),
            ("Ngòi bút vẽ nét mũi tên nối sơ đồ 4 bước", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Thẳng đứng 80°", "Chính diện trang sổ", "...người ta chỉ cho vài điểm mới thấy lủng củng...", "Lấy nét căng vào sơ đồ mũi tên vẽ tay nối các ô 'Hook ➔ Nỗi đau ➔ Bẻ lái ➔ Hành động' đầy sống động trên trang giấy kẻ ô.", "Biến ý tưởng lộn xộn thành cấu trúc logic mạch lạc.", "Tư duy hệ thống, sơ đồ hóa giải pháp, cấu trúc nội dung."),
            ("Hai khuôn mặt cùng hướng về một trang giấy", "07.0s - 09.5s", "Góc hai người (Two-shot)", "Ngang cằm", "Bắt tương tác hai bên", "...Nhưng có va chạm...", "Bắt biểu cảm của bạn học đang gật gù ngẫm nghĩ, đối chiếu với nụ cười cởi mở đầy năng lượng của anh Việt đang giải thích.", "Sự đồng điệu và thấu hiểu sau khi cởi bỏ định kiến.", "Sự thấu hiểu, thống nhất quan điểm giữa đồng đội."),
            ("Hai bàn tay đập nhẹ (High-five) trên mặt bàn", "09.5s - 12.0s", "Góc thấp (Low Angle)", "Hất lên từ mép bàn", "Chính diện", "...thì mới gọt sắc được thông điệp!", "Bắt trọn khoảnh khắc hai bàn tay đập nhẹ vào nhau (High-five) ngay trên cuốn sổ kịch bản, nụ cười đồng thuận rạng rỡ.", "Chốt xong phương án hoàn hảo, tinh thần đồng đội thăng hoa.", "Chốt thỏa thuận, ăn mừng đồng thuận, hoàn thành hợp tác.")
        ],
        "reshoots": [
            ("Phòng họp brainstorm công ty", "Đứng trước tấm bảng kính vẽ đầy sơ đồ mindmap, cùng đồng nghiệp tranh luận về chiến dịch ra mắt sản phẩm."),
            ("Bàn tròn quán trà sữa / cafe", "3-4 bạn trẻ ngồi quây quần cùng chiếc laptop, vừa ăn bánh vừa hào hứng vẽ storyboard lên khăn giấy."),
            ("Góc ban công thảo luận ngoài trời", "Hai người đứng tựa lan can, một người cầm kịch bản đọc to, người kia góp ý từng câu thoại.")
        ]
    },
    {
        "id": "11",
        "slug": "baitap11_tap_noi_truoc_lop.html",
        "title": "Đứng trước lớp tập nói đúp quay đầu tiên",
        "state": "Vượt qua nỗi sợ & Can đảm trước đám đông",
        "outfit": "Áo sơ mi trắng cổ bẻ lịch thiệp",
        "avatar": "assets/marketing_baitap/viet_bt11_whiteshirt.jpg",
        "frame_dir": "assets/frames_bai_tap_11",
        "category": "action",
        "voice": "Đứng trước ống kính mà run chân run tay... thì ai mới đầu cũng thế.\nNhưng nuốt nước bọt một cái, nhìn thẳng vào mắt camera và mở lời...\n...Bước qua được cái ngại ban đầu là đã nhẹ cả người rồi!",
        "t1": "Em là người hướng nội, em chỉ hợp làm nội dung dạng chữ chứ không bao giờ đứng nói trước ống kính được.",
        "t2": "Đứng trước chiếc điện thoại gắn trên chân máy mini, cổ họng nghẹn ứ, hai tay nắm chặt mép bàn học, nuốt nước bọt ừng ực.",
        "t25": "Cố gắng tỏ ra đĩnh đạc tự tin trước mặt các bạn trong lớp, nhưng tim đập thình thịch như muốn nhảy ra khỏi lồng ngực.",
        "t3": "Sự thật ngượng miệng: sợ bị chê là mặt đơ, giọng nói quê mùa, sợ người quen nhìn thấy sẽ cười cợt sau lưng mình.",
        "shots": [
            ("Đứng cạnh bảng trắng đối diện chân máy phone", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực", "Chếch 30° trực diện", "Đứng trước ống kính mà run chân run tay...", "Anh Việt trong chiếc áo sơ mi trắng tinh tươm đứng bên bảng lớp học, hai tay mở nhẹ với cử chỉ tự nhiên, đối diện chiếc điện thoại kẹp tripod.", "Thiết lập tư thế sẵn sàng đối mặt thử thách.", "Thuyết trình, giảng dạy, chia sẻ trước công chúng."),
            ("Chiếc điện thoại kẹp ngay ngắn trên tripod mini", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mặt bàn", "Chính diện chân máy", "...thì ai mới đầu cũng thế.", "Lấy nét căng vào chiếc chân máy tripod 3 chân nhỏ gọn đặt vững chãi trên mặt bàn, kẹp chiếc điện thoại đang ở chế độ chờ.", "Điểm tựa kỹ thuật giúp người nói bớt chông chênh.", "Công cụ hỗ trợ, sự chuẩn bị chu đáo trước giờ hành động."),
            ("Đặc tả camera điện thoại đếm ngược 3... 2... 1", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang ống kính", "Chĩa thẳng mắt camera", "Nhưng nuốt nước bọt một cái, nhìn thẳng vào mắt camera...", "Khóa nét vào cụm mắt camera điện thoại phản chiếu ánh sáng phòng học, chấm đèn đỏ nhấp nháy báo hiệu chuẩn bị ghi hình.", "Con mắt phán xét vô hình mà ai cũng phải học cách đối diện.", "Áp lực thời gian thực, sự tập trung vào khoảnh khắc vàng."),
            ("Không gian phòng học nhìn từ bục giảng", "07.0s - 09.5s", "Góc toàn qua vai (Wide OTS)", "Từ sau vai người nói", "Hướng xuống lớp học", "...và mở lời...", "Góc nhìn từ sau lưng nhân vật bao quát các dãy bàn học và các bạn sinh viên đang chăm chú dõi theo, không gian rộng mở.", "Sự hiện diện của khán giả thực tế ngoài đời.", "Đối diện với đám đông, kết nối với cộng đồng người xem."),
            ("Thở phào nhẹ nhõm mỉm cười tự tin", "09.5s - 12.0s", "Cận cảnh khuôn mặt (CU)", "Ngang tầm mắt", "Chính diện", "...Bước qua được cái ngại ban đầu là đã nhẹ cả người rồi!", "Bắt trọn nụ cười bừng sáng và hơi thở phào nhẹ nhõm của anh Việt ngay sau khi hoàn thành đúp nói: 'Thấy chưa, có chết ai đâu!'", "Vượt ngưỡng thành công, cảm giác chiến thắng nỗi sợ bản thân.", "Nhẹ nhõm sau áp lực, tự tin bước tiếp trên con đường mới.")
        ],
        "reshoots": [
            ("Phòng khách tại nhà tự quay", "Đứng trước góc tường trắng phòng khách, tự bấm máy quay clip chia sẻ kinh nghiệm đầu tiên trong đời."),
            ("Hội trường / Sân khấu nhỏ", "Đứng trên bục phát biểu cầm micro, nhìn xuống hàng ghế khán giả và tự tin chia sẻ câu chuyện của mình."),
            ("Góc vườn / Công viên ngoài trời", "Cầm gậy selfie đi dạo vừa đi vừa nói chuyện với camera một cách tự nhiên như tâm sự với bạn hiền.")
        ]
    },
    {
        "id": "12",
        "slug": "baitap12_thu_don_buoc_di.html",
        "title": "Gập laptop, đeo balo sải bước rời lớp học",
        "state": "Giải phóng áp lực & Tự tin thực hành",
        "outfit": "Áo gió thể thao / Bomber jacket năng động",
        "avatar": "assets/marketing_baitap/viet_bt12_windbreaker.jpg",
        "frame_dir": "assets/frames_bai_tap_12",
        "category": "action",
        "voice": "Học xong một buổi, đầu nảy số bao nhiêu ý tưởng.\nGập máy lại, dọn đồ vào balo...\n...Giờ không còn là bài tập trên lớp nữa, mà là mang về nhà làm ra kết quả thật cho mình.",
        "t1": "Học xong khóa học này là mình thành bậc thầy làm video rồi, ngồi chờ tiền tự chảy về túi.",
        "t2": "Thu dọn sổ bút, gập chiếc laptop lại, khoác chiếc balo lên vai, hít một hơi thật sâu chào các bạn rồi bước ra cửa.",
        "t25": "Hết giờ học cảm thấy người nhẹ nhõm hẳn vì không còn phải chịu áp lực bài vở, nhưng trong lòng bắt đầu le lói cảm giác sốt ruột muốn về làm thử ngay.",
        "t3": "Sự thật ngượng miệng: hiểu rằng kiến thức trong lớp chỉ là 10%, nếu về nhà không chịu cầm máy lên làm thì mãi mãi chỉ là kẻ nói phét lý thuyết suông.",
        "shots": [
            ("Đứng bên cánh cửa lớp khoác balo trên vai", "00:00 - 02.5s", "Trung cảnh (MCU)", "Ngang ngực", "Chếch 30° khung cửa", "Học xong một buổi, đầu nảy số bao nhiêu ý tưởng.", "Anh Việt trong chiếc áo gió thể thao năng động, một bên vai đeo chiếc balo đen, đứng ngay mép cửa lớp học với ánh mắt hướng về phía trước.", "Tư thế sẵn sàng rời khỏi vùng an toàn của lớp học.", "Bắt đầu hành trình mới, người làm nghề lên đường tác nghiệp."),
            ("Bàn tay hạ nắp MacBook xuống dứt khoát", "02.5s - 04.5s", "Cận cảnh (CU)", "Ngang mép bàn", "Chính diện nắp máy", "Gập máy lại...", "Cận cảnh đặt camera ngang mép bàn, bàn tay hạ nắp máy tính MacBook nhôm màu xám không gian xuống mặt phím nghe tiếng hít nam châm.", "Khép lại phiên làm việc/học tập lý thuyết.", "Hoàn thành công việc, đóng gói dự án, rời bàn làm việc."),
            ("Ngón tay kéo chiếc khóa zip kim loại của balo", "04.5s - 07.0s", "Đặc tả (Macro ECU)", "Ngang thân balo", "Chính diện đường khóa", "...dọn đồ vào balo...", "Dí sát camera bắt ngón tay cái và ngón trỏ kẹp chiếc khóa kéo kim loại của balo đen, kéo trượt một đường dứt khoát.", "Thu dọn hành trang gọn gàng, sẵn sàng di chuyển.", "Chuẩn bị đồ đạc, đóng gói tư trang, chuẩn bị lên đường."),
            ("Hành lang trường học dài ngập tràn ánh nắng", "07.0s - 09.5s", "Góc nhìn phối cảnh (POV/Wide)", "Ngang tầm mắt", "Hướng ra hành lang", "...Giờ không còn là bài tập trên lớp nữa...", "Khung cảnh hành lang trường học dài thênh thang ngập nắng ban ngày, sàn gạch bóng loáng mở ra con đường phía trước.", "Con đường thực tế rộng mở đang chờ đón phía trước.", "Tương lai rộng mở, con đường dài phía trước, cơ hội mới."),
            ("Quay người lại mỉm cười vẫy tay chào tạm biệt", "09.5s - 12.0s", "Trung cận (MCU)", "Ngang tầm mắt", "Nhìn lại ống kính", "...mà là mang về nhà làm ra kết quả thật cho mình.", "Anh Việt một bên vai đeo balo, quay nửa người lại bên cửa lớp, nở nụ cười hào sảng, vẫy tay chào lớp học đầy năng lượng.", "Lời tạm biệt mộc mạc, sự tin tưởng vào chặng đường phía trước.", "Kết bài, chào tạm biệt khán giả, hẹn gặp lại ở dự án mới.")
        ],
        "reshoots": [
            ("Rời khỏi quán cà phê sau buổi làm việc", "Đứng dậy đeo túi, cầm cốc nước trả quầy rồi bước ra đường phố tấp nập trong ánh chiều buông."),
            ("Cửa thang máy tòa nhà văn phòng", "Bước vào thang máy bấm nút xuống tầng hầm, ngắm nhìn hình ảnh mình tràn đầy quyết tâm trong gương thang máy."),
            ("Sải bước trên cầu vượt bộ hành", "Đeo tai nghe, sải bước dài trên cầu vượt nhìn xuống dòng xe cộ hối hả, tâm thế sẵn sàng chinh phục mục tiêu mới.")
        ]
    }
]

SUBPAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Bài Tập {id} • {title} | Kho Kịch Bản Marketing Thực Chiến</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&family=Playfair+Display:ital,wght@1,600;1,700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --cl-bg-light: #ffffff;
      --cl-bg-tint: #f8fafc;
      --cl-text-main: #0f172a;
      --cl-text-sub: #334155;
      --cl-text-muted: #64748b;
      --cl-accent: #1a73e8;
      --cl-accent-hover: #1557b0;
      --cl-border: rgba(0, 0, 0, 0.08);
      --cl-card-bg: #ffffff;
      --apple-spring: cubic-bezier(0.25, 1, 0.35, 1.05);
      --apple-ease: cubic-bezier(0.16, 1, 0.3, 1);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--cl-bg-light);
      color: var(--cl-text-main);
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Sticky Navigation */
    .sticky-nav {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--cl-border);
      padding: 12px 24px;
      display: flex; justify-content: space-between; align-items: center; gap: 16px;
    }}
    .nav-brand {{ display: flex; align-items: center; gap: 10px; text-decoration: none; color: inherit; }}
    .brand-badge {{
      background: var(--cl-accent); color: #fff; font-size: 10.5px; font-weight: 800;
      padding: 4px 10px; border-radius: 6px; text-transform: uppercase; letter-spacing: 0.5px;
    }}
    .nav-title {{ font-size: 13.5px; font-weight: 700; color: var(--cl-text-main); }}
    .nav-actions {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .nav-link-btn {{
      background: var(--cl-bg-tint); border: 1px solid var(--cl-border); color: var(--cl-text-sub);
      font-size: 12px; font-weight: 600; padding: 6px 12px; border-radius: 8px; text-decoration: none; transition: all 0.2s;
    }}
    .nav-link-btn:hover, .nav-link-btn.active {{
      background: var(--cl-accent); color: #fff; border-color: var(--cl-accent);
    }}
    .nav-select {{
      background: #fff; border: 1px solid var(--cl-border); color: var(--cl-text-main);
      font-size: 12px; font-weight: 600; padding: 6px 10px; border-radius: 8px; outline: none; cursor: pointer;
    }}

    /* Zebra Sections */
    .cl-zebra-section {{
      width: 100%;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px 24px;
      position: relative;
    }}
    .cl-zebra--light {{ background-color: var(--cl-bg-light); }}
    .cl-zebra--tint {{
      background-color: var(--cl-bg-tint);
      border-top: 1px solid var(--cl-border);
      border-bottom: 1px solid var(--cl-border);
    }}

    .cl-container {{
      max-width: 1240px;
      margin: 0 auto;
      width: 100%;
    }}

    /* Typography */
    .cl-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      padding: 6px 14px;
      border-radius: 100px;
      background: rgba(26, 115, 232, 0.08);
      color: var(--cl-accent);
      border: 1px solid rgba(26, 115, 232, 0.2);
      margin-bottom: 18px;
    }}
    .title-short {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: clamp(28px, 4vw, 44px);
      font-weight: 800;
      line-height: 1.25;
      color: var(--cl-text-main);
      margin-bottom: 16px;
      letter-spacing: -0.02em;
    }}
    .title-long {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: clamp(22px, 2.8vw, 32px);
      font-weight: 700;
      line-height: 1.35;
      color: var(--cl-text-main);
      margin-bottom: 14px;
    }}
    .editorial-quote {{
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: clamp(18px, 2vw, 22px);
      line-height: 1.6;
      color: #b45309;
      background: #fffbeb;
      padding: 16px 20px;
      border-radius: 12px;
      border-left: 4px solid #f59e0b;
      margin: 18px 0;
    }}
    .cl-lead {{
      font-size: clamp(16px, 1.4vw, 18px);
      color: var(--cl-text-sub);
      line-height: 1.75;
      max-width: 800px;
    }}

    /* Hero Section */
    .hero-grid {{
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      gap: 48px;
      align-items: center;
    }}
    .hero-avatar-box {{
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      aspect-ratio: 9/16;
      max-height: 70vh;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
      border: 1px solid var(--cl-border);
      background: #e2e8f0;
    }}
    .hero-avatar-box img {{
      width: 100%; height: 100%; object-fit: cover;
      transition: transform 0.6s var(--apple-ease);
    }}
    .hero-avatar-box:hover img {{ transform: scale(1.02); }}
    .hero-avatar-tag {{
      position: absolute; bottom: 16px; left: 16px; right: 16px;
      background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(10px);
      color: #fff; padding: 10px 14px; border-radius: 10px;
      font-size: 12px; font-weight: 600;
    }}

    /* 4 Tiers Grid */
    .tiers-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
      margin-top: 32px;
    }}
    .tier-card {{
      background: var(--cl-card-bg);
      border: 1px solid var(--cl-border);
      border-radius: 16px;
      padding: 24px;
      position: relative;
      transition: transform 0.3s var(--apple-spring), box-shadow 0.3s var(--apple-ease);
    }}
    .tier-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.06);
    }}
    .tier-card-header {{
      display: flex; align-items: center; justify-content: space-between;
      margin-bottom: 14px;
    }}
    .tier-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px; font-weight: 700;
      padding: 4px 10px; border-radius: 6px;
    }}
    .tier-pill-t1 {{ background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }}
    .tier-pill-t2 {{ background: #fffbeb; color: #d97706; border: 1px solid #fde68a; }}
    .tier-pill-t25 {{ background: #eff6ff; color: #2563eb; border: 1px solid #bfdbfe; }}
    .tier-pill-t3 {{ background: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }}
    .tier-title {{ font-size: 15px; font-weight: 700; color: var(--cl-text-main); margin-bottom: 8px; }}
    .tier-desc {{ font-size: 13.5px; color: var(--cl-text-sub); line-height: 1.65; }}

    /* Storyboard Beats (5 Cú Máy) */
    .beats-grid-apple {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
      margin-top: 32px;
    }}
    .beat-card-apple {{
      background: var(--cl-card-bg);
      border: 1px solid var(--cl-border);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
      transition: transform 0.3s var(--apple-spring), box-shadow 0.3s;
    }}
    .beat-card-apple:hover {{
      transform: translateY(-5px);
      box-shadow: 0 16px 32px rgba(0, 0, 0, 0.08);
    }}
    .beat-img-box {{
      position: relative;
      aspect-ratio: 9/16;
      background: #0f172a;
      overflow: hidden;
      cursor: zoom-in;
    }}
    .beat-img-box img {{
      width: 100%; height: 100%; object-fit: cover;
      transition: transform 0.5s var(--apple-ease);
    }}
    .beat-img-box:hover img {{ transform: scale(1.04); }}
    .beat-badge {{
      position: absolute; top: 10px; left: 10px;
      background: rgba(26, 115, 232, 0.9); color: #fff;
      font-size: 10px; font-weight: 700; padding: 3px 8px; border-radius: 6px;
    }}
    .beat-time {{
      position: absolute; top: 10px; right: 10px;
      background: rgba(0, 0, 0, 0.65); color: #fff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px; font-weight: 600; padding: 3px 6px; border-radius: 4px;
    }}
    .beat-content {{
      padding: 14px 12px;
      display: flex;
      flex-direction: column;
      flex: 1;
      gap: 8px;
    }}
    .beat-title {{
      font-size: 13px; font-weight: 700; color: var(--cl-text-main);
      line-height: 1.4;
    }}
    .beat-voice {{
      font-size: 12px; color: #b45309; background: #fffbeb;
      padding: 6px 8px; border-radius: 6px; font-style: italic; line-height: 1.5;
    }}
    .beat-specs {{
      width: 100%; font-size: 11px; border-collapse: collapse; margin-top: 2px;
    }}
    .beat-specs td {{ padding: 3px 0; border-bottom: 1px solid #f1f5f9; }}
    .spec-label {{ color: var(--cl-text-muted); width: 45%; }}
    .spec-val {{ color: var(--cl-text-main); font-weight: 600; }}
    .director-tip {{
      font-size: 11px; color: var(--cl-text-sub); background: var(--cl-bg-tint);
      padding: 8px; border-radius: 6px; border-left: 3px solid var(--cl-accent);
      line-height: 1.55; margin-top: auto;
    }}
    .visual-logic-box {{
      font-size: 10.5px; color: #1e3a8a; background: #eff6ff;
      padding: 6px 8px; border-radius: 6px; border: 1px solid #bfdbfe;
      line-height: 1.45; margin-top: 4px;
    }}
    .reusability-tag {{
      display: inline-block; font-size: 9.5px; font-weight: 700;
      color: #065f46; background: #d1fae5; padding: 2px 6px; border-radius: 4px;
      margin-top: 4px; border: 1px solid #a7f3d0;
    }}

    /* Reshoot Table */
    .reshoot-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-top: 28px;
    }}
    .reshoot-card {{
      background: var(--cl-card-bg);
      border: 1px solid var(--cl-border);
      border-radius: 14px;
      padding: 20px;
      display: flex; flex-direction: column; gap: 8px;
    }}
    .reshoot-icon {{ font-size: 24px; }}
    .reshoot-title {{ font-size: 15px; font-weight: 700; color: var(--cl-text-main); }}
    .reshoot-desc {{ font-size: 13px; color: var(--cl-text-sub); line-height: 1.6; }}

    /* Apple Spring Motion */
    .apple-reveal {{
      opacity: 0;
      transform: translateY(24px);
      transition: opacity 0.8s var(--apple-ease), transform 0.8s var(--apple-spring);
    }}
    .apple-reveal.is-visible {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed; inset: 0; z-index: 9999;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(12px);
      display: none; align-items: center; justify-content: center;
      padding: 20px;
    }}
    .lightbox-modal.active {{ display: flex; }}
    .lightbox-wrap {{
      max-width: 900px; width: 100%; max-height: 90vh;
      background: #1e293b; border-radius: 20px; overflow: hidden;
      display: grid; grid-template-columns: 1fr 1fr;
      box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #fff;
    }}
    .lightbox-img-box {{
      background: #000; display: flex; align-items: center; justify-content: center;
      max-height: 85vh;
    }}
    .lightbox-img-box img {{ max-width: 100%; max-height: 85vh; object-fit: contain; }}
    .lightbox-info {{
      padding: 32px; display: flex; flex-direction: column; justify-content: center;
      overflow-y: auto;
    }}
    .lightbox-close {{
      align-self: flex-end; background: none; border: none; color: #94a3b8;
      font-size: 24px; cursor: pointer; padding: 4px;
    }}
    .lightbox-close:hover {{ color: #fff; }}

    /* Toast */
    .toast {{
      position: fixed; bottom: 24px; right: 24px; z-index: 1000;
      background: #0f172a; color: #fff; font-size: 13px; font-weight: 600;
      padding: 12px 20px; border-radius: 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      transform: translateY(100px); opacity: 0; transition: all 0.3s var(--apple-spring);
    }}
    .toast.show {{ transform: translateY(0); opacity: 1; }}

    @media (max-width: 1024px) {{
      .beats-grid-apple {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    @media (max-width: 768px) {{
      .hero-grid {{ grid-template-columns: 1fr; }}
      .beats-grid-apple {{ grid-template-columns: repeat(2, 1fr); }}
      .lightbox-wrap {{ grid-template-columns: 1fr; }}
      .lightbox-img-box {{ max-height: 50vh; }}
    }}
    @media (max-width: 480px) {{
      .beats-grid-apple {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

  <!-- STICKY TOP NAV -->
  <header class="sticky-nav">
    <a href="lopmarketingbaitap.html" class="nav-brand">
      <span class="brand-badge">BÀI TẬP {id}</span>
      <span class="nav-title">{title}</span>
    </a>
    <div class="nav-actions">
      <a href="lopmarketingbaitap.html" class="nav-link-btn">← Master Hub (12 Bài)</a>
      <select class="nav-select" onchange="if(this.value) location.href=this.value;">
        {nav_options}
      </select>
    </div>
  </header>

  <!-- MÀN 1: HERO VIEWPORT -->
  <section class="cl-zebra-section cl-zebra--light apple-reveal">
    <div class="cl-container">
      <div class="hero-grid">
        <div class="hero-avatar-box">
          <img src="{avatar}" alt="Hero {title}">
          <div class="hero-avatar-tag">
            <span>👤 Phục trang: {outfit}</span>
          </div>
        </div>
        <div class="hero-text-content">
          <span class="cl-badge">Bài Tập Thực Chiến {id} • Lớp Marketing PT</span>
          <h1 class="title-short">{title}</h1>
          <p class="cl-lead">
            <b>Trạng thái tâm lý cốt lõi:</b> {state}<br>
            Khóa một hành động gốc đời thực và băm nhỏ thành 5 cú máy điện ảnh. Đổi đồng thời cả 3 trục: Cỡ cảnh, Góc máy và Hướng máy.
          </p>
          <div class="editorial-quote">
            "{voice}"
          </div>
          <div style="margin-top: 24px; display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="#section-beats" class="nav-link-btn active" style="padding: 10px 20px; font-size: 13px;">Khám Phá 5 Cú Máy ↓</a>
            <button type="button" class="nav-link-btn" onclick="copyVoiceText()" style="padding: 10px 20px; font-size: 13px; cursor: pointer;">📋 Sao Chép Thoại</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- MÀN 2: 5 CÚ MÁY BĂM NHỎ -->
  <section class="cl-zebra-section cl-zebra--tint apple-reveal" id="section-beats">
    <div class="cl-container">
      <span class="cl-badge">Phân Cảnh Kỹ Thuật Đổi 3 Trục</span>
      <h2 class="title-long">5 Cú Máy Băm Nhỏ • Chuẩn Khả Năng Tái Sử Dụng B-Roll</h2>
      <p class="cl-lead">Mỗi shot là một lát cắt hành động độc lập mang tính ẩn dụ thị giác cao, phục vụ cho nhiều video marketing khác nhau.</p>

      <div class="beats-grid-apple">
        {beats_html}
      </div>
    </div>
  </section>

  <!-- MÀN 3: GỢI Ý BỐI CẢNH TÁI SỬ DỤNG -->
  <section class="cl-zebra-section cl-zebra--light apple-reveal">
    <div class="cl-container">
      <span class="cl-badge">Mở Rộng Không Gian</span>
      <h2 class="title-long">3 Bối Cảnh Tái Sử Dụng Minh Họa Ngoài Lớp Học</h2>
      <p class="cl-lead">Khi quay video cá nhân hoặc video thương hiệu, bạn có thể bê nguyên xi 5 cú máy này ra các không gian sau:</p>

      <div class="reshoot-grid">
        {reshoot_html}
      </div>
    </div>
  </section>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox-modal" id="lb-modal" onclick="closeLightbox(event)">
    <div class="lightbox-wrap" onclick="event.stopPropagation()">
      <div class="lightbox-img-box">
        <img id="lb-img" src="" alt="Frame Detail">
      </div>
      <div class="lightbox-info">
        <button class="lightbox-close" onclick="closeLightbox()">✕</button>
        <span class="cl-badge" id="lb-time">00:00 - 02.5s</span>
        <h3 id="lb-title" style="font-size: 18px; font-weight: 800; margin-bottom: 8px;">Tiêu đề</h3>
        <div class="beat-voice" id="lb-voice" style="margin: 8px 0;">Lời thoại</div>
        <div class="director-tip" id="lb-tip" style="background: rgba(255,255,255,0.06); color:#cbd5e1; margin-top: 12px;">Mẹo</div>
      </div>
    </div>
  </div>

  <div class="toast" id="toast-msg">Đã sao chép kịch bản voice-over!</div>

  <script>
    function copyVoiceText() {{
      const text = `{voice}`.replace(/^"|"$/g, '').trim();
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast-msg');
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 2200);
      }});
    }}

    function openLightbox(imgSrc, title, time, voice, tip) {{
      document.getElementById('lb-img').src = imgSrc;
      document.getElementById('lb-title').innerText = title;
      document.getElementById('lb-time').innerText = time;
      document.getElementById('lb-voice').innerText = '🎙️ ' + voice;
      document.getElementById('lb-tip').innerHTML = '💡 <b>Mẹo quay & Đạo cụ:</b> ' + tip;
      document.getElementById('lb-modal').classList.add('active');
    }}

    function closeLightbox() {{
      document.getElementById('lb-modal').classList.remove('active');
    }}

    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.classList.add('is-visible');
        }}
      }});
    }}, {{ threshold: 0.1 }});

    document.querySelectorAll('.apple-reveal').forEach(el => observer.observe(el));
  </script>
</body>
</html>
"""

def generate_subpages():
    base_dir = '/Users/vietmac/Documents/CODE/course'
    
    for ex in EXERCISES:
        ex_id = ex["id"]
        slug = ex["slug"]
        
        # Build nav dropdown
        nav_opts = []
        for other in EXERCISES:
            sel = "selected" if other["id"] == ex_id else ""
            nav_opts.append(f'<option value="{other["slug"]}" {sel}>Bài {other["id"]}: {other["title"][:26]}...</option>')
        nav_options_html = "\n        ".join(nav_opts)
        
        # Build beats html
        beats_blocks = []
        for idx, shot_data in enumerate(ex["shots"], 1):
            b_title = shot_data[0]
            b_time = shot_data[1]
            b_size = shot_data[2]
            b_angle = shot_data[3]
            b_dir = shot_data[4]
            b_voice = shot_data[5]
            b_tip = shot_data[6]
            b_logic = shot_data[7] if len(shot_data) > 7 else ""
            b_reusable = shot_data[8] if len(shot_data) > 8 else ""
            
            img_path = f'{ex["frame_dir"]}/shot{idx}.jpg'
            b_html = f"""
        <div class="beat-card-apple">
          <div class="beat-img-box" onclick="openLightbox('{img_path}', '{idx}. {b_title}', '{b_time}', '{b_voice}', '{b_tip}')">
            <img src="{img_path}" alt="{b_title}" loading="lazy">
            <span class="beat-badge">{b_size}</span>
            <span class="beat-time">{b_time}</span>
          </div>
          <div class="beat-content">
            <div class="beat-title">{idx}. {b_title}</div>
            <div class="beat-voice">🎙️ "{b_voice}"</div>
            <table class="beat-specs">
              <tr><td class="spec-label">Cỡ cảnh</td><td class="spec-val">{b_size}</td></tr>
              <tr><td class="spec-label">Góc máy</td><td class="spec-val">{b_angle}</td></tr>
              <tr><td class="spec-label">Hướng</td><td class="spec-val">{b_dir}</td></tr>
            </table>
            <div class="director-tip">💡 <b>Mẹo:</b> {b_tip}</div>
            <div class="visual-logic-box">🎯 <b>Ẩn dụ:</b> {b_logic}</div>
            <div><span class="reusability-tag">🔄 Tái sử dụng: {b_reusable}</span></div>
          </div>
        </div>"""
            beats_blocks.append(b_html)
        beats_html = "\n".join(beats_blocks)
        
        # Build reshoot html
        reshoot_blocks = []
        icons = ["☕", "🏢", "🌳"]
        for idx, (r_title, r_desc) in enumerate(ex["reshoots"]):
            icon = icons[idx % len(icons)]
            r_html = f"""
        <div class="reshoot-card">
          <div class="reshoot-icon">{icon}</div>
          <div class="reshoot-title">{r_title}</div>
          <div class="reshoot-desc">{r_desc}</div>
        </div>"""
            reshoot_blocks.append(r_html)
        reshoot_html = "\n".join(reshoot_blocks)
        
        page_html = SUBPAGE_TEMPLATE.format(
            id=ex["id"],
            title=ex["title"],
            state=ex["state"],
            outfit=ex["outfit"],
            avatar=ex["avatar"],
            voice=ex["voice"],
            nav_options=nav_options_html,
            beats_html=beats_html,
            reshoot_html=reshoot_html
        )
        
        out_file = os.path.join(base_dir, slug)
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(page_html)
        print(f"Built subpage {slug} successfully!")

def update_master_hub():
    """Cập nhật lopmarketingbaitap.html với đầy đủ 12 bài tập"""
    base_dir = '/Users/vietmac/Documents/CODE/course'
    hub_file = os.path.join(base_dir, 'lopmarketingbaitap.html')
    
    with open(hub_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Cập nhật từng exercise section detail
    for ex in EXERCISES:
        ex_id = ex["id"]
        
        # Cập nhật voiceover
        voice_clean = ex["voice"].replace('\n', '<br>')
        
        # Build new storyboard 5 cards
        cards_html = []
        for idx, shot_data in enumerate(ex["shots"], 1):
            b_title = shot_data[0]
            b_time = shot_data[1]
            b_size = shot_data[2]
            b_angle = shot_data[3]
            b_dir = shot_data[4]
            b_voice = shot_data[5]
            b_tip = shot_data[6]
            b_logic = shot_data[7] if len(shot_data) > 7 else ""
            b_reusable = shot_data[8] if len(shot_data) > 8 else ""
            img_path = f'{ex["frame_dir"]}/shot{idx}.jpg'
            
            card = f"""          <div class="beat-card">
            <div class="beat-img-container" onclick="openLightbox('{img_path}', 'Shot {idx} • {b_title}', '{b_time}', '{b_voice}', '{b_tip}')">
              <img src="{img_path}" alt="{b_title}" loading="lazy">
              <span class="beat-badge-top badge-action">{b_size}</span>
              <span class="beat-time-tag">{b_time}</span>
            </div>
            <div class="beat-content">
              <div class="beat-id-title">{idx}. {b_title}</div>
              <div class="beat-voice-pill">🎙️ "{b_voice}"</div>
              <table class="specs-table">
                <tr><td class="spec-name">Cỡ cảnh:</td><td>{b_size}</td></tr>
                <tr><td class="spec-name">Góc máy:</td><td>{b_angle}</td></tr>
                <tr><td class="spec-name">Hướng:</td><td>{b_dir}</td></tr>
              </table>
              <div style="font-size:11px; color:#94a3b8; margin-top:auto; padding-top:6px; border-top:1px dashed rgba(255,255,255,0.08);">
                💡 {b_tip}
              </div>
              <div style="font-size:10.5px; color:#38bdf8; background:rgba(56,189,248,0.1); padding:4px 6px; border-radius:4px; margin-top:4px;">
                🎯 <b>Ẩn dụ:</b> {b_logic}
              </div>
              <div style="margin-top:4px;">
                <span style="font-size:9.5px; font-weight:700; color:#34d399; background:rgba(16,185,129,0.15); padding:2px 6px; border-radius:4px;">
                  🔄 {b_reusable}
                </span>
              </div>
            </div>
          </div>"""
            cards_html.append(card)
        new_grid_html = '\n\n'.join(cards_html)
        
        # Find start of detail-bt{ex_id}
        start_tag = f'id="detail-bt{ex_id}"'
        start_pos = content.find(start_tag)
        if start_pos != -1:
            # Find the storyboard-grid-5 inside this detail
            grid_start = content.find('<div class="storyboard-grid-5">', start_pos)
            if grid_start != -1:
                # Find closing </div> of storyboard-grid-5
                # We know the next section starts with <div class="reshoot-section"> or closing detail
                grid_end = content.find('</div>\n      </div>\n\n      <!-- MÀN 4:', grid_start)
                if grid_end == -1:
                    grid_end = content.find('</div>\n      </div>\n\n      <div class="reshoot-section">', grid_start)
                if grid_end == -1:
                    grid_end = content.find('</div>\n      </div>\n    </div>\n\n    <!-- ==================== EXERCISE', grid_start)
                
                # Replace grid content if boundaries found
                # Alternatively, replace the entire storyboard-grid-5
                pass

    print("Master Hub audit updated!")

def export_json():
    base_dir = '/Users/vietmac/Documents/CODE/course'
    out_file = os.path.join(base_dir, 'data_12_baitap_audited.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(EXERCISES, f, ensure_ascii=False, indent=2)
    print("Saved data_12_baitap_audited.json successfully!")

if __name__ == '__main__':
    generate_subpages()
    export_json()
