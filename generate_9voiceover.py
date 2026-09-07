# -*- coding: utf-8 -*-
"""
Script to generate 9voiceover.html - Master Hub for Bài 1 (1 Kịch bản 9 phong cách)
"""
import json
import os

STYLES = [
    {
        "id": "01",
        "code": "PK 01",
        "title": "Ngồi Cà Phê 10h Tối Không Dám Về Nhà",
        "slug": "kich_ban_01_ngoi_ca_phe_10h_toi.html",
        "category": "pressure",
        "category_name": "TÂM LÝ & ÁP LỰC CÀY ĐÊM",
        "avatar": "assets/voiceover_9phongcach/pk01_cafe_dem_charcoalknit.jpg",
        "outfit": "Áo len cổ tròn xám than (Charcoal Knit) mộc mạc",
        "context": "Góc quán cà phê đêm • Ánh đèn vàng ấm • Ly cà phê tan đá • Màn hình laptop",
        "target": "Chủ kinh doanh nhỏ, người làm nghề cày cuốc trong đêm vì bất an tài chính",
        "hook": "10h đêm rồi... ngồi ở góc quán này không phải vì chăm chỉ đâu anh em ạ.",
        "voice": "10h đêm rồi... ngồi ở góc quán này không phải vì chăm chỉ đâu anh em ạ. Ở nhà nằm lướt điện thoại thì thấy tội lỗi, ra đây nhìn vào máy tính cho đỡ bất an. Thấy bạn bè kiếm tiền kinh quá, mình mệt lả rồi mà không dám ngủ. Càng cố cày đêm thì càng thấy mình tụt lại phía sau... Đến khi nào mới thoát được cái vòng lặp này?",
        "flaws": [
            {
                "issue": "Cỡ cảnh trung tính (bán thân lơ lửng), góc máy đặt ngang mặt dead-center thiếu chiều sâu, không gợi được sự cô đơn lẻ loi.",
                "fix": "Chuyển sang MCU (Trung cận) góc chéo 45° kết hợp Low Angle 15° hắt nhẹ, đặt ly cafe tan đá ở tiền cảnh làm mờ (blur foreground) để tạo độ sâu thị giác và cảm giác bơ vơ giữa quán vắng."
            },
            {
                "issue": "Bối cảnh quán cà phê chung chung, đồ đạc xếp ngay ngắn giả tạo, thiếu các chi tiết thể hiện một đêm làm việc kiệt sức.",
                "fix": "Bổ sung đạo cụ chuẩn đời thực: Ly cà phê đá tan nước đọng thành vũng quanh đế ly, quai balo vắt hờ trên lưng ghế, ánh sáng xanh từ màn hình laptop hắt trực diện vào sống mũi và mắt."
            },
            {
                "issue": "Diễn viên nhìn máy quay cười gượng gạo, văn phong cũ dùng từ ngữ AI đao to búa lớn làm mất đi sự đồng cảm.",
                "fix": "Biểu cảm tự nhiên: Mắt hơi nheo mỏi mệt, ngón tay day nhẹ khóe mắt trước khi ngẩng lên nhìn ống kính với nụ cười tự trào mộc mạc; thoại xưng 'anh em' gần gũi, chia sẻ thẳng thắn nỗi bất an."
            }
        ],
        "shots": [
            ("A-Roll 1 (Selfie quán vắng)", "00:00 - 00:03", "Cận cảnh (CU)", "Ngang tầm mắt 0°", "Cầm tay chéo 30°", "10h đêm rồi... ngồi đây không phải vì chăm đâu anh em ạ.", "Cầm máy selfie lia một vòng góc quán cafe đêm vắng người, cười trừ tự sự."),
            ("A-Roll 2 (Tại bàn làm việc)", "00:03 - 00:07", "Trung cận (MCU)", "Hơi chúc 15°", "Chính diện đối diện", "Ở nhà nằm lướt điện thoại thì thấy tội lỗi, ra đây nhìn vào máy tính cho đỡ bất an.", "Đặt máy xuống bàn cà phê, mặt trầm lại chân thành kể chuyện."),
            ("B-Roll 1 (Cận tay day trán)", "00:07 - 00:12", "Cận đặc tả (CU)", "Ngang mắt 10°", "Chếch vai trái", "Thấy bạn bè kiếm tiền kinh quá, mình mệt lả rồi mà không dám ngủ.", "Bàn tay vuốt trán mệt mỏi, màn hình laptop sáng giữa không gian phòng tối."),
            ("B-Roll 2 (Góc nghiêng gọng kính)", "00:12 - 00:16", "Cận cảnh (CU)", "Ngang tai 0°", "Cắt nghiêng 90°", "Càng cố cày đêm thì càng thấy mình tụt lại phía sau...", "Khóa nét tròng kính phản chiếu các tab báo cáo doanh số tụt giảm."),
            ("A-Roll 3 (Khép nắp laptop thở dài)", "00:16 - 00:20", "Trung cảnh (MS)", "Hạ thấp 20°", "Từ dưới hắt lên", "Đến khi nào mới thoát được cái vòng lặp này?", "Hai tay từ từ gập nắp máy tính lại, thở hắt ra một hơi, tự cười nhẹ nhõm chấp nhận.")
        ]
    },
    {
        "id": "02",
        "code": "PK 02",
        "title": "Tiền Mặt Bằng & Cửa Hàng Vắng Khách",
        "slug": "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html",
        "category": "finance",
        "category_name": "VỐN & CHI PHÍ MẶT BẰNG",
        "avatar": "assets/voiceover_9phongcach/pk02_chu_shop_oxfordstripes.jpg",
        "outfit": "Sơ mi Oxford sọc xanh xắn tay áo kiểu chủ tiệm thực chiến",
        "context": "Cửa hàng mặt phố vắng khách • Đồng hồ treo tường chạy • Camera an ninh • Quầy thu ngân",
        "target": "Chủ shop offline, chủ tiệm gánh áp lực tiền nhà 20-30 triệu/tháng",
        "hook": "Sáng mở mắt ra là bay mất một triệu tiền mặt bằng... khách thì lướt mạng, mình thì ngồi ngáp vặt.",
        "voice": "Sáng mở mắt ra là bay mất một triệu tiền mặt bằng... Khách thì đi ngang qua nhìn vào rồi lướt tiếp, mình thì ngồi sau quầy thu ngân bấm máy tính đếm chi phí. Tiền điện, tiền nhân viên, tiền cọc tháng sau... Cứ ngỡ mở quán ra là khách tự vào, ai ngờ ngoài kia họ mua trên sàn với xem video hết rồi.",
        "flaws": [
            {
                "issue": "Ảnh cũ chụp một người đứng ở quầy hàng như người mẫu thời trang, không toát lên gánh nặng của người làm chủ tiệm đang bị tiền nhà đè nặng.",
                "fix": "Chuyển tư thế ngồi tựa quầy thu ngân xắn tay áo mộc mạc, một tay cầm xấp hóa đơn tiền điện/nhà, mắt nhìn chênh chếch ra ngoài cửa kính với vẻ mặt tính toán căng thẳng nhưng điềm tĩnh."
            },
            {
                "issue": "Cửa hàng quá sáng trưng, kệ hàng trống trơn vô lý hoặc tràn ngập hàng hiệu xa lạ, không đúng chất tiệm bán lẻ thực tế.",
                "fix": "Thiết lập bối cảnh quầy thu ngân thực tế với máy POS cà thẻ, cuộn giấy in bill, đồng hồ treo tường đang nhích từng giây; ánh sáng ban ngày hắt qua kính cửa mặt tiền vắng bóng khách."
            },
            {
                "issue": "Góc máy tĩnh không có sự đối lập giữa không gian tiệm rộng mênh mông và bóng dáng đơn độc của người chủ tiệm.",
                "fix": "Thiết kế góc Wide OTS (từ trong quầy nhìn ra cửa kính vắng bóng người) đối lập với Extreme Close-up màn hình máy tính bỏ túi đang cộng dồn chi phí tiền triệu mỗi ngày."
            }
        ],
        "shots": [
            ("A-Roll 1 (Quầy thu ngân)", "00:00 - 00:03", "Trung cảnh (MCU)", "Ngang tầm ngực", "Chính diện quầy", "Sáng mở mắt ra là bay mất một triệu tiền mặt bằng...", "Đứng sau quầy thu ngân xắn tay áo, tay cầm xấp hóa đơn, nhìn vào ống kính chia sẻ."),
            ("B-Roll 1 (Đồng hồ & Cửa vắng)", "00:03 - 00:07", "Toàn cảnh (Wide)", "Góc cao 45°", "Nhìn từ góc trần", "Khách thì đi ngang qua nhìn vào rồi lướt tiếp...", "Góc nhìn camera an ninh từ góc tường: cửa hàng sáng đèn nhưng không một bóng khách ghé."),
            ("B-Roll 2 (Máy tính tính tiền)", "00:07 - 00:11", "Đặc tả (Macro ECU)", "Thẳng đứng 80°", "Từ trên xuống", "Tiền điện, tiền nhân viên, tiền cọc tháng sau...", "Ngón tay bấm liên tục trên bàn phím máy tính cầm tay: cộng dồn từng khoản chi phí đỏ rực."),
            ("B-Roll 3 (Lướt xem video shop khác)", "00:11 - 00:15", "Cận qua vai (OTS)", "Ngang vai 15°", "Sau lưng chếch phải", "Cứ ngỡ mở quán ra là khách tự vào, ai ngờ ngoài kia họ xem video hết rồi.", "Cầm điện thoại soi video livestream của đối thủ nườm nượp đơn hàng trên sàn."),
            ("A-Roll 2 (Gật đầu tự vấn)", "00:15 - 00:20", "Cận cảnh (CU)", "Ngang tầm mắt 0°", "Chính diện", "Không lên mạng làm video thì làm sao người ta biết mình ở đâu?", "Nhìn thẳng vào ống kính, khẽ thở ra mỉm cười quyết tâm thay đổi tư duy bán hàng.")
        ]
    },
    {
        "id": "03",
        "code": "PK 03",
        "title": "Chững Lại Sau Tuổi 30 & Nhìn Đối Thủ Triệu View",
        "slug": "kich_ban_03_chung_lai_sau_tuoi_30.html",
        "category": "career",
        "category_name": "TUỔI TÁC & BẢO THỦ NGHỀ",
        "avatar": "assets/voiceover_9phongcach/pk03_tuoi_30_blackpolo.jpg",
        "outfit": "Áo polo dệt kim đen tuyền tối giản, đứng đắn tuổi 30+",
        "context": "Bàn làm việc đêm • Màn hình soi kênh TikTok đối thủ trẻ • Nếp nhăn khóe mắt • Ánh đèn vàng",
        "target": "Người làm nghề 30+, có chuyên môn nhưng ngại xuất hiện video ngắn vì sợ mất hình ảnh",
        "hook": "Hơn 30 tuổi, làm nghề cả chục năm... nhìn đứa mới vào nghề nó hốt hết khách nhờ video ngắn.",
        "voice": "Hơn 30 tuổi, làm nghề cả chục năm... Nhìn mấy bạn trẻ mới vào nghề họ quay video ngắn hút hết khách, trong lòng vừa tức vừa ngượng. Mình có tay nghề thật thì giấu kín trong phòng, người ta nói hay hơn thì lên xu hướng mỗi ngày. Cái tôi bảo thủ nó giết chết mình từ lúc nào không biết!",
        "flaws": [
            {
                "issue": "Ảnh cũ thể hiện sự già nua mệt mỏi tiêu cực, ánh mắt nhìn vào khoảng không vô định thiếu tính kết nối với người xem.",
                "fix": "Tạo hình người đàn ông ngoài 30 chững chạc, áo polo đen dệt kim lịch thiệp, ánh mắt sâu sắc đối diện camera với nụ cười chua chát nhưng cầu thị, dám nhìn thẳng vào sự thật bảo thủ của mình."
            },
            {
                "issue": "Thiếu sự đối chiếu trực quan giữa chuyên môn lâu năm và thế giới video ngắn của giới trẻ.",
                "fix": "Sử dụng màn hình điện thoại/iPad đặt nghiêng trên bàn gỗ phản chiếu video TikTok đối thủ, bên cạnh là cuốn giáo trình hoặc dụng cụ nghề lâu năm có dấu vết thời gian."
            },
            {
                "issue": "Ánh sáng đơn điệu, không tạo được chiều sâu tâm lý của người đứng ở ngã ba đường sự nghiệp.",
                "fix": "Bố trí ánh sáng Key Light ấm một bên mặt, phần còn lại chìm nhẹ trong bóng đổ (chiaroscuro) nhấn mạnh sự trăn trở nội tâm và khoảnh khắc thức tỉnh."
            }
        ],
        "shots": [
            ("A-Roll 1 (Tâm sự tuổi 30)", "00:00 - 00:03", "Trung cận (MCU)", "Ngang tầm mắt 0°", "Chính diện trực tiếp", "Hơn 30 tuổi, làm nghề cả chục năm...", "Ngồi thẳng lưng trước bàn làm việc, ánh mắt tự sự nhìn thẳng người xem."),
            ("B-Roll 1 (Màn hình soi đối thủ)", "00:03 - 00:07", "Cận qua vai (OTS)", "Ngang vai 20°", "Chếch lưng phải", "...nhìn đứa mới vào nghề nó hốt hết khách nhờ video ngắn.", "Màn hình điện thoại hiển thị kênh TikTok của bạn trẻ với hàng triệu lượt xem."),
            ("B-Roll 2 (Khóe mắt & Nếp nhăn)", "00:07 - 00:11", "Đặc tả (Macro ECU)", "Ngang trán 0°", "Cắt góc nghiêng 45°", "Mình có tay nghề thật thì giấu kín trong phòng...", "Cận cảnh khóe mắt và nếp nhăn trăn trở, biểu cảm vừa tiếc nuối vừa thức tỉnh."),
            ("B-Roll 3 (Gõ nhẹ ngón tay)", "00:11 - 00:15", "Cận cảnh (CU)", "Sát mặt bàn", "Chính diện tay", "...cái tôi bảo thủ nó giết chết mình từ lúc nào không biết!", "Ngón tay đeo nhẫn gõ nhẹ nhịp nhàng xuống mặt bàn gỗ, nhịp điệu của sự dứt khoát."),
            ("A-Roll 2 (Cười buông bỏ cái tôi)", "00:15 - 00:20", "Trung cảnh (MS)", "Hơi ngửa nhẹ 10°", "Chính diện", "Hạ cái tôi xuống, cầm máy lên quay... thì có sao đâu?", "Nở nụ cười thanh thản, tay vươn ra chạm vào chiếc điện thoại trên giá đỡ.")
        ]
    },
    {
        "id": "04",
        "code": "PK 04",
        "title": "Tiền Quảng Cáo Ăn Hết Tiền Lãi",
        "slug": "kich_ban_04_tien_quang_cao_an_het_tien_lai.html",
        "category": "finance",
        "category_name": "VỐN & CHI PHÍ MẶT BẰNG",
        "avatar": "assets/voiceover_9phongcach/pk04_tien_ads_navyblazer.jpg",
        "outfit": "Casual navy blazer mặc ngoài áo thun trắng tối giản",
        "context": "Trình quản lý Ads Manager đỏ lòm chỉ số chi phí • Đèn bàn studio • Biểu đồ cắn tiền",
        "target": "Chủ shop online phụ thuộc vào Facebook/TikTok Ads, chi phí cắn sạch lợi nhuận",
        "hook": "Cứ 5 phút tôi lại mở màn hình kiểm tra một lần... tiền nạp thì trừ đều mà đơn không thấy đâu.",
        "voice": "Cứ 5 phút tôi lại mở màn hình kiểm tra một lần... Tiền quảng cáo trừ đều đặn từng phút mà tin nhắn về toàn hỏi dạo rồi im lặng. Doanh thu nhìn thì hoành tráng mấy trăm triệu, trừ tiền ads, tiền hoàn hàng, tiền kho bãi... mở két ra chả còn được bao nhiêu. Mình làm thuê cho các nền tảng quảng cáo mất rồi!",
        "flaws": [
            {
                "issue": "Ảnh cũ chụp chung chung trước máy tính như lập trình viên, không thấy rõ nỗi đau của người chạy ads bị cắn tiền.",
                "fix": "Nâng cấp góc MCU với navy blazer phối thun trắng chỉn chu, tay chống cằm suy tư, màn hình hiển thị trực tiếp đồ thị chiến dịch quảng cáo đỏ rực chỉ số CPM/CPA tăng vọt."
            },
            {
                "issue": "Ánh sáng màn hình quá chói lòa làm cháy sáng mặt, mất hết chi tiết da và biểu cảm đôi mắt.",
                "fix": "Cân bằng ánh sáng viền xanh (screen glow) nhẹ nhàng ở cạnh mặt, phối hợp đèn key light studio vàng ấm tạo độ nổi khối khuôn mặt chuẩn 8K."
            },
            {
                "issue": "Không có điểm nhấn hành động để người quay hình học viên thực hành theo được ngay.",
                "fix": "Chia rõ động tác cụ thể: Tay cuộn chuột liên tục -> Mắt nheo lại nhìn số tiền trừ -> Thở dài tựa lưng -> Bấm nút tắt chiến dịch đốt tiền."
            }
        ],
        "shots": [
            ("A-Roll 1 (Soi màn hình ads)", "00:00 - 00:03", "Trung cận (MCU)", "Ngang mắt 0°", "Chếch 30° màn hình", "Cứ 5 phút tôi lại mở màn hình kiểm tra một lần...", "Ngồi trước màn hình máy tính hiển thị Ads Manager, tay vuốt cằm trầm tư."),
            ("B-Roll 1 (Số dư trừ liên tục)", "00:03 - 00:07", "Đặc tả (Macro ECU)", "Ngang màn hình", "Chính diện số liệu", "...tiền nạp thì trừ đều mà đơn không thấy đâu.", "Cận cảnh dòng tiền nạp và số tiền đã chi tiêu nhảy số liên tục, đơn hàng = 0."),
            ("B-Roll 2 (Điện thoại tin nhắn rác)", "00:07 - 00:11", "Cận cảnh (CU)", "Sát mặt bàn", "Từ trên chúc xuống", "Tin nhắn về toàn hỏi dạo rồi im lặng...", "Màn hình điện thoại hiện danh sách tin nhắn hỏi giá rồi 'đã xem' không phản hồi."),
            ("B-Roll 3 (Gập sổ tính lãi lỗ)", "00:11 - 00:15", "Trung cảnh (MS)", "Ngang ngực", "Chếch vai trái", "Mở két ra chẳng còn được bao nhiêu, làm thuê cho nền tảng rồi!", "Bàn tay ném bút xuống cuốn sổ chi phí, hai tay xoa mặt ngao ngán."),
            ("A-Roll 2 (Thức tỉnh tự làm kênh)", "00:15 - 00:20", "Cận cảnh (CU)", "Ngang tầm mắt", "Chính diện", "Thay vì nuôi ads, sao mình không tự làm video kéo khách tự nhiên?", "Ngẩng đầu lên, ánh mắt sắc sảo, dứt khoát tìm hướng đi mới.")
        ]
    },
    {
        "id": "05",
        "code": "PK 05",
        "title": "Hết Khách Từ Mối Quan Hệ Quen",
        "slug": "kich_ban_05_het_khach_tu_moi_quan_he_quen.html",
        "category": "relationships",
        "category_name": "TỆP KHÁCH & QUAN HỆ QUEN",
        "avatar": "assets/voiceover_9phongcach/pk05_khach_quen_beigelinen.jpg",
        "outfit": "Sơ mi linen đũi màu be mở cúc cổ tự nhiên mộc mạc",
        "context": "Danh bạ điện thoại • Tin nhắn Zalo đã nhắn hết một lượt • Bàn gỗ ấm áp • Ánh sáng cửa sổ",
        "target": "Người làm dịch vụ, tư vấn, bảo hiểm, bất động sản, bán hàng đa kênh",
        "hook": "Lướt danh bạ từ trên xuống dưới mà không biết nhắn cho ai... bán cho người quen hết cửa rồi.",
        "voice": "Lướt danh bạ từ trên xuống dưới mà không biết nhắn cho ai... Ban đầu mở ra thì bạn bè, người thân ủng hộ nhiệt tình lắm. Nhưng người quen thì mua được mấy lần? Nhắn mãi người ta ngại, người ta lảng đi lúc nào không hay. Không tìm được tệp khách lạ ngoài kia thì sớm muộn cũng đóng cửa!",
        "flaws": [
            {
                "issue": "Hình ảnh cũ quá kịch, tạo dáng cầm điện thoại giả tạo như chụp ảnh stock ngân hàng ảnh miễn phí.",
                "fix": "Nâng cấp áo sơ mi linen đũi be ấm áp, ngồi tại bàn làm việc gỗ tự nhiên, hai tay cầm điện thoại ngón cái cuộn danh bạ Zalo thật, ánh mắt đăm chiêu chân thực."
            },
            {
                "issue": "Thiếu tính đời thường, không gian xa hoa không phản ánh được sự đơn độc của người bán hàng tự thân.",
                "fix": "Bối cảnh ánh sáng cửa sổ tự nhiên dịu nhẹ (soft window light), điểm xuyết cây xanh góc phòng, tạo bầu không khí tĩnh lặng sâu sắc."
            },
            {
                "issue": "Không có góc quay thể hiện chi tiết màn hình tin nhắn khách hàng một cách tinh tế.",
                "fix": "Thiết lập góc máy POV màn hình điện thoại mờ danh sách tên liên hệ, bắt trọn khoảnh khắc ngón tay dừng lại không dám bấm gửi."
            }
        ],
        "shots": [
            ("A-Roll 1 (Cuộn danh bạ ngập ngừng)", "00:00 - 00:03", "Trung cận (MCU)", "Ngang tầm ngực", "Chính diện", "Lướt danh bạ từ trên xuống dưới mà không biết nhắn cho ai...", "Cầm điện thoại, ngón tay cuộn chậm danh bạ, ánh mắt ngập ngừng suy tư."),
            ("B-Roll 1 (Màn hình tin nhắn Zalo)", "00:03 - 00:07", "Đặc tả (Macro ECU)", "Thẳng đứng 60°", "Vào màn hình", "...người quen ủng hộ mãi sao được, nhắn thêm thì người ta ngại.", "Cận cảnh tin nhắn cũ 'Dạo này thế nào bạn?' đã xem nhưng không trả lời."),
            ("B-Roll 2 (Cốc nước trên bàn gỗ)", "00:07 - 00:11", "Cận cảnh (CU)", "Sát mặt bàn", "Góc ngang 0°", "Khách quen mua một lần rồi thôi, còn khách lạ thì không biết mình là ai.", "Bàn tay cầm cốc nước xoay nhẹ, nhìn dòng người vội vã qua khung kính."),
            ("B-Roll 3 (Đặt điện thoại úp xuống)", "00:11 - 00:15", "Cận thấp (Low Angle)", "Mặt bàn hất nhẹ 15°", "Chéo bàn tay", "Không chủ động hút tệp khách mới thì sớm muộn cũng cạn đường.", "Dứt khoát úp màn hình điện thoại xuống mặt bàn gỗ."),
            ("A-Roll 2 (Mỉm cười thấu hiểu)", "00:15 - 00:20", "Cận cảnh (CU)", "Ngang tầm mắt", "Chính diện ấm áp", "Phải xuất hiện ngoài kia để khách lạ tự tìm đến mình thôi!", "Ngẩng lên nở nụ cười điềm tĩnh, ấm áp, sẵn sàng kết nối cộng đồng mới.")
        ]
    },
    {
        "id": "06",
        "code": "PK 06",
        "title": "Tay Nghề Tốt Nhưng Vẫn Vắng Khách",
        "slug": "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html",
        "category": "craftsman",
        "category_name": "NGHỀ & CHUYÊN MÔN SÂU",
        "avatar": "assets/voiceover_9phongcach/pk06_gioi_nghe_workwear.jpg",
        "outfit": "Áo khoác thợ canvas màu caramel/nâu đất, lót thun xám",
        "context": "Xưởng chế tác thủ công • Đồ nghề sáng bóng • Mẫu thiết kế tỉ mỉ • Đèn vàng xưởng thợ",
        "target": "Thợ thủ công, kỹ thuật viên, chuyên gia có chuyên môn sâu nhưng yếu truyền thông",
        "hook": "Làm nghề mười mấy năm, đồ mình làm ra tự tin không thua ai... thế mà quán đối diện làm dở lại đông hơn.",
        "voice": "Làm nghề mười mấy năm, đồ mình làm ra tự tin không thua ai... Thế mà cái tiệm đối diện làm ẩu hơn mình, dùng đồ rẻ tiền hơn mà khách cứ nườm nượp. Hóa ra trong thời buổi này, làm giỏi mà không biết kể chuyện thì coi như giấu nghề dưới đáy giếng. Khách hàng họ đâu có mắt thần để biết mình tâm huyết thế nào!",
        "flaws": [
            {
                "issue": "Ảnh cũ mặc sơ mi trắng đứng trong xưởng thợ trông hoàn toàn lạc quẻ, không ra chất nghệ nhân/thợ làm nghề.",
                "fix": "Nâng cấp áo khoác thợ canvas màu caramel/nâu đất phong trần, ngồi bên bàn gỗ mộc xưởng thủ công với dụng cụ thước kẹp, dao tỉa, bản vẽ phác thảo."
            },
            {
                "issue": "Gương mặt nghiêm nghị kiểu trừng phạt, tạo cảm giác cay cú hằn học thay vì sự chiêm nghiệm sâu sắc của người làm nghề.",
                "fix": "Ánh mắt ấm áp, nụ cười tự trào rạng rỡ của một người thợ lành nghề nhận ra chân lý: Kỹ năng giỏi phải đi đôi với khả năng truyền thông chân thực."
            },
            {
                "issue": "Bối cảnh xưởng thiếu chi tiết bề mặt vật liệu, ánh sáng phẳng dẹt.",
                "fix": "Đèn vàng tungsten chiếu rọi chi tiết thớ gỗ, đường may và các công cụ thủ công sáng bóng, tạo cảm giác xưởng nghề thực thụ."
            }
        ],
        "shots": [
            ("A-Roll 1 (Tâm sự bên bàn thợ)", "00:00 - 00:03", "Trung cận (MCU)", "Ngang tầm ngực", "Chính diện", "Làm nghề mười mấy năm, đồ mình làm ra không thua ai...", "Ngồi cạnh bàn làm việc xưởng thợ, cười tự sự chia sẻ nỗi lòng."),
            ("B-Roll 1 (Bàn tay vuốt đường kim mũi chỉ)", "00:03 - 00:07", "Đặc tả (Macro ECU)", "Góc nghiêng 45°", "Vào phôi sản phẩm", "...từng đường cắt, từng mối nối đều làm kỹ đến từng milimet.", "Đôi bàn tay thô ráp tỉ mỉ nắn nót từng góc cạnh sản phẩm thủ công tinh xảo."),
            ("B-Roll 2 (Nhìn qua cửa tiệm đối diện)", "00:07 - 00:11", "Cận qua vai (OTS)", "Ngang vai 10°", "Hướng ra đường", "Thế mà tiệm đối diện làm dở hơn lại đông khách hơn mình...", "Ánh mắt nhìn qua khung cửa kính sang quán đối diện tấp nập xe cộ qua lại."),
            ("B-Roll 3 (Cầm đồ nghề ngẫm nghĩ)", "00:11 - 00:15", "Cận cảnh (CU)", "Hạ thấp 15°", "Chính diện bàn tay", "Khách đâu có mắt thần để thấy được cái tâm của người làm nghề!", "Bàn tay đặt chiếc búa thợ xuống mặt bàn gỗ, tiếng 'cộc' dứt khoát thức tỉnh."),
            ("A-Roll 2 (Nụ cười người thợ thức thời)", "00:15 - 00:20", "Trung cận (MCU)", "Ngang tầm mắt", "Chính diện rạng rỡ", "Phải tự cầm máy quay lại từng công đoạn cho người ta thấy thôi!", "Nụ cười bừng sáng, cầm chiếc điện thoại lên chuẩn bị quay quá trình chế tác.")
        ]
    },
    {
        "id": "07",
        "code": "PK 07",
        "title": "Bị Cạnh Tranh Bởi Tổng Kho & Giá Gốc",
        "slug": "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html",
        "category": "pricing",
        "category_name": "CẠNH TRANH & GIÁ GỐC",
        "avatar": "assets/voiceover_9phongcach/pk07_tong_kho_blacktee.jpg",
        "outfit": "Áo thun đen streetwear phom suông dày dặn, đứng đắn",
        "context": "Kho hàng hiện đại • Kệ thép cao tầng • Thùng carton • Máy quét mã vạch",
        "target": "Cửa hàng bán lẻ, đại lý phân phối truyền thống bị tổng kho livestream bóp nghẹt",
        "hook": "Khách cầm điện thoại vào hỏi: 'Sao trên mạng bán rẻ hơn anh mấy chục ngàn?'... cứng họng luôn!",
        "voice": "Khách cầm điện thoại vào hỏi: 'Sao trên mạng bán rẻ hơn anh mấy chục ngàn?'... Cứng họng luôn! Người ta xả kho trực tiếp từ xưởng, mình ôm một đống hàng tồn ở đây thì làm sao mà đọ nổi giá? Đâm đầu vào cuộc chiến giá rẻ là con đường chết nhanh nhất. Mình phải bán giá trị, bán sự phục vụ chứ không thể bán rẻ mãi được!",
        "flaws": [
            {
                "issue": "Ảnh cũ chụp trong phòng họp máy chiếu, hoàn toàn sai bối cảnh kho vận và bán buôn.",
                "fix": "Nâng cấp bối cảnh kho hàng thực tế: Kệ thép xanh công nghiệp xếp tầng tầng lớp lớp thùng carton, máy quét mã vạch cầm tay, ánh sáng LED công nghiệp kết hợp rim light vàng ấm."
            },
            {
                "issue": "Trang phục áo sơ mi vest công sở giả tạo, không đúng thực tế người đứng kho kiểm kê đơn hàng.",
                "fix": "Áo thun đen tối giản vải cotton dày dặn, phom suông năng động của người chủ kho thực chiến lăn xả với hàng hóa."
            },
            {
                "issue": "Biểu cảm hoang mang bất lực tiêu cực, không tạo được động lực bứt phá giải pháp cho người học.",
                "fix": "Ánh mắt kiên định, rắn rỏi, đối diện trực diện camera; thể hiện bản lĩnh của người nhìn thấu cuộc chiến giá rẻ và chọn lối đi khác biệt về chất lượng phục vụ."
            }
        ],
        "shots": [
            ("A-Roll 1 (Đứng giữa kho hàng)", "00:00 - 00:03", "Trung cảnh (MS)", "Ngang tầm ngực", "Chính diện lối đi kho", "Khách cầm điện thoại hỏi: Sao trên mạng bán rẻ thế anh?", "Đứng giữa lối đi kho hàng cao tầng, cầm máy quét mã vạch chia sẻ."),
            ("B-Roll 1 (Màn hình livestream xả kho)", "00:03 - 00:07", "Cận cảnh (CU)", "Ngang mắt", "Vào điện thoại", "...người ta livestream xả kho giá sốc, bóp nghẹt các shop nhỏ.", "Màn hình điện thoại hiển thị phiên live hò hét bán phá giá '99k 3 cái'."),
            ("B-Roll 2 (Thùng hàng xếp kín kệ)", "00:07 - 00:11", "Toàn cảnh (Wide)", "Góc cao 30°", "Nhìn xuống dãy kệ", "Hàng hóa nhập về nằm im trên kệ, đọng vốn cả trăm triệu.", "Camera lia chậm dọc theo các tầng kệ thép chứa đầy thùng carton đóng gói cẩn thận."),
            ("B-Roll 3 (Máy quét tít một tiếng)", "00:11 - 00:15", "Đặc tả (Macro ECU)", "Ngang tay", "Vào tia laser đỏ", "Đua giảm giá là tự thắt cổ mình, phải bán giá trị khác biệt!", "Tia laser đỏ từ máy quét quét qua mã barcode trên thùng hàng kêu một tiếng 'tít' dứt khoát."),
            ("A-Roll 2 (Khẳng định bản lĩnh)", "00:15 - 00:20", "Trung cận (MCU)", "Ngang tầm mắt", "Chính diện kiên định", "Họ bán giá rẻ, còn mình bán sự an tâm và bảo hành chu đáo!", "Nhìn thẳng vào ống kính, ánh mắt rắn rỏi, tự tin định vị thương hiệu uy tín.")
        ]
    },
    {
        "id": "08",
        "code": "PK 08",
        "title": "Bắt Đầu Lại Từ Con Số 0",
        "slug": "kich_ban_08_bat_dau_lai_tu_con_so_0.html",
        "category": "restart",
        "category_name": "LÀM LẠI TỪ CON SỐ 0",
        "avatar": "assets/voiceover_9phongcach/pk08_so_khong_olivehoodie.jpg",
        "outfit": "Áo hoodie mỏng màu xanh rêu (Olive Green) trẻ trung, tinh thần khởi đầu mới",
        "context": "Bàn làm việc gỗ sáng màu • Sổ tay mới tinh • Tia nắng ban mai chiếu xiên • Không gian tối giản",
        "target": "Người từng vấp ngã thất bại, phải làm lại từ đầu sau khi mất vốn hoặc dừng dự án cũ",
        "hook": "Đóng cửa tiệm cũ, trong tay gần như về lại số 0... Sợ nhất không phải nghèo, mà là sợ bạn bè cười chê.",
        "voice": "Đóng cửa tiệm cũ, trong tay gần như về lại số 0... Sợ nhất lúc đó không phải là thiếu tiền, mà là sợ người quen hỏi han, sợ bạn bè họ cười vào mặt mình. Nhưng nằm buồn mãi thì ai nuôi mình? Còn đôi bàn tay, còn khối óc, mở cuốn sổ mới ra viết lại từ đầu. Vấp một lần để khôn ra cả đời!",
        "flaws": [
            {
                "issue": "Ảnh cũ u ám quá mức như phim kinh dị, người gục đầu xuống bàn tạo cảm giác tuyệt vọng tiêu cực.",
                "fix": "Thay đổi hoàn toàn sang tông màu tươi sáng buổi sáng (warm morning sunlight), người ngồi thẳng lưng tự tin trong áo hoodie olive mỏng, mở trang sổ trắng tinh chuẩn bị kế hoạch mới."
            },
            {
                "issue": "Cỡ cảnh bị đóng khung quá chật chội, không có khoảng thở (headroom & breathing space).",
                "fix": "Khung hình MCU cân đối, ánh nắng ban mai rọi qua cửa sổ tạo viền sáng (rim light) tượng trưng cho hy vọng và năng lượng tái sinh."
            },
            {
                "issue": "Nụ cười gượng hoặc mặt đăm đăm vô hồn.",
                "fix": "Nụ cười rạng rỡ, tự tin, đôi mắt sáng rực nhìn về phía trước; ngôn ngữ cơ thể tràn đầy nội lực của người đã vượt qua đáy vực và đang đi lên."
            }
        ],
        "shots": [
            ("A-Roll 1 (Mở trang sổ trắng)", "00:00 - 00:03", "Trung cận (MCU)", "Ngang tầm ngực", "Chính diện bàn gỗ", "Đóng cửa tiệm cũ, về lại số 0... sợ nhất người ta cười chê.", "Ngồi bên bàn gỗ ban mai, mở trang sổ tay trắng tinh, mỉm cười tự sự."),
            ("B-Roll 1 (Nắng sớm qua khung cửa)", "00:03 - 00:07", "Toàn cảnh (Wide)", "Ngang tầm mắt", "Hướng cửa sổ", "Nhưng nằm lì một chỗ thì ai nuôi mình? Phải tự đứng dậy thôi!", "Ánh nắng vàng ban mai tràn qua ô cửa kính, chiếu ấm góc phòng làm việc tinh gọn."),
            ("B-Roll 2 (Cây bút đặt lên trang giấy)", "00:07 - 00:11", "Cận cảnh (CU)", "Hạ thấp 20°", "Chính diện ngòi bút", "Còn đôi bàn tay, còn khối óc, viết lại từ bài học đầu tiên.", "Bàn tay cầm bút máy đặt nét mực đầu tiên lên trang giấy trắng muốt."),
            ("B-Roll 3 (Uống ngụm trà sớm)", "00:11 - 00:15", "Cận cảnh (CU)", "Ngang cằm", "Chếch bên phải", "Vấp ngã một lần để khôn ra cả đời, không có gì phải ngượng!", "Nhấp một ngụm trà sớm, nhìn ra xa với ánh mắt trong trẻo, an yên."),
            ("A-Roll 2 (Nụ cười tái sinh)", "00:15 - 00:20", "Cận cảnh (CU)", "Ngang tầm mắt", "Chính diện rạng ngời", "Làm lại từ đầu với một cái đầu tỉnh táo hơn nhiều!", "Nở nụ cười rạng rỡ, tràn ngập năng lượng tích cực truyền cảm hứng mạnh mẽ.")
        ]
    },
    {
        "id": "09",
        "code": "PK 09",
        "title": "Hàng Làm Kỹ Nhưng Bị So Sánh Giá",
        "slug": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html",
        "category": "craftsman",
        "category_name": "NGHỀ & CHUYÊN MÔN SÂU",
        "avatar": "assets/voiceover_9phongcach/pk09_hang_ky_mandarin.jpg",
        "outfit": "Sơ mi cổ lãnh tụ màu trắng ngà cao cấp (Mandarin Collar Shirt)",
        "context": "Showroom thủ công tinh tế • Sản phẩm da thật hoàn thiện • Ánh sáng gallery spot",
        "target": "Chủ xưởng sản xuất, người làm hàng thủ công / kỹ nghệ tâm huyết bị khách chê đắt",
        "hook": "Mất 3 ngày gia công từng đường kim mũi chỉ, khách vào phán một câu: 'Trên mạng bán có nửa giá'...",
        "voice": "Mất 3 ngày gia công từng đường kim mũi chỉ, khách vào phán một câu: 'Trên mạng bán có nửa giá'... Nghe mà đau quặn ruột! Nhưng trách ai được? Mình không cho họ thấy loại da mình dùng là thảo mộc tự nhiên, không cho họ thấy từng đường khâu tay mất bao nhiêu giọt mồ hôi... Thì họ so sánh với hàng dập máy công nghiệp là phải. Người mua hàng kỹ luôn ở đó, chỉ chờ mình kể đúng câu chuyện thôi!",
        "flaws": [
            {
                "issue": "Ảnh cũ cầm sản phẩm giơ lên ống kính như nhân viên bán hàng tiếp thị đa cấp, làm giảm giá trị món đồ thủ công cao cấp.",
                "fix": "Nâng cấp tư thế nâng niu sản phẩm da thuộc trước ngực bằng hai tay trân trọng, mặc sơ mi cổ lãnh tụ trắng ngà nhã nhặn, ánh mắt tự hào và trân quý sản phẩm của mình."
            },
            {
                "issue": "Bối cảnh xưởng bừa bộn rác và phôi vụn làm mất đi tính cao cấp của dòng sản phẩm kỹ nghệ.",
                "fix": "Không gian showroom studio mộc mạc phong cách tối giản Bắc Âu, ánh sáng gallery dịu nhẹ làm nổi bật màu da bò sáp tự nhiên và từng đường may thủ công."
            },
            {
                "issue": "Biểu cảm cay cú vì bị chê giá đắt.",
                "fix": "Biểu cảm điềm đạm, nụ cười nhẹ nhàng thấu hiểu tâm lý khách hàng: Khách chê đắt là vì họ chưa thấy được quá trình, việc của mình là làm video mở tung quy trình cho họ xem."
            }
        ],
        "shots": [
            ("A-Roll 1 (Nâng niu sản phẩm trước ngực)", "00:00 - 00:03", "Trung cận (MCU)", "Ngang tầm ngực", "Chính diện", "Mất 3 ngày gia công, khách bảo trên mạng bán nửa giá...", "Mặc sơ mi cổ lãnh tụ, tay nâng niu chiếc ví da bò thủ công, chia sẻ với nụ cười điềm đạm."),
            ("B-Roll 1 (Soi đường khâu tay tỉ mỉ)", "00:03 - 00:07", "Đặc tả (Macro ECU)", "Ngang mặt da", "Sát đường chỉ", "...từng mũi kim khâu tay thủ công, chỉ sáp nhập khẩu bền cả chục năm.", "Ống kính macro bắt nét từng mũi chỉ dập tay đều tăm tắp trên nền da thảo mộc mộc mạc."),
            ("B-Roll 2 (Khách lướt sàn so giá)", "00:07 - 00:11", "Cận cảnh (CU)", "Ngang vai 15°", "Vào điện thoại", "Họ nhìn bề ngoài thấy giống nhau nên so sánh là điều dễ hiểu...", "Màn hình điện thoại hiển thị sản phẩm da simili công nghiệp giá rẻ ngoài sàn."),
            ("B-Roll 3 (Ấn ngón tay thử độ đàn hồi)", "00:11 - 00:15", "Đặc tả (Macro ECU)", "Thẳng đứng 60°", "Vào vân da", "Mình không mở quy trình cho họ thấy thì trách ai được!", "Ngón tay ấn nhẹ vào miếng da thật, vân da đàn hồi trở lại tự nhiên mềm mịn."),
            ("A-Roll 2 (Tự tin vào khách hàng kỹ tính)", "00:15 - 00:20", "Trung cận (MCU)", "Ngang tầm mắt", "Chính diện uy tín", "Khách quý đồ kỹ luôn ở đó, việc của mình là làm video kể cho đúng!", "Mỉm cười tự tin, ánh mắt sáng rực niềm tự hào về giá trị thực của sản phẩm.")
        ]
    }
]

print(f"Loaded {len(STYLES)} styles data ready.")
