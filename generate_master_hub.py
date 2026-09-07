#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Hub Generator for Offline02 Course Scripts
Redesigned with Premium Dark Cinematic Design, Full 3-Tier Psychological Matrix,
Interactive Filters, Search, Accordions, and Direct Links to all scripts.
"""

import json
import html
import os

with open("/tmp/extracted_kb_data.json", "r", encoding="utf-8") as f:
    kb_data = json.load(f)

core_scripts = [
    {
        "id": "kb01",
        "code": "KB 01",
        "title": "Ngồi Cà Phê 10h Tối Không Dám Về Nhà",
        "short_title": "Ngồi Cà Phê 10h Tối",
        "file": "kich_ban_01_ngoi_ca_phe_10h_toi.html",
        "category": "core",
        "category_badge": "TÂM LÝ & ÁP LỰC CÀY ĐÊM",
        "badge_color": "#818cf8",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • J-Cut Thoại",
        "context": "Góc quán cà phê đêm • Ánh đèn vàng ấm • Ly cà phê tan đá • Màn hình laptop",
        "target": "Chủ kinh doanh nhỏ, người làm nghề cày cuốc trong đêm vì bất an",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_01_ngoi_ca_phe_10h_toi/assets/frames/scene1_beat1.jpg",
        "hook": "10h đêm rồi... ngồi ở góc quán này không phải vì chăm chỉ đâu anh em ạ.",
        "cta": "Cứ cắm đầu làm theo cách cũ thì chỉ có dẹp tiệm. Muốn sống thì phải thay đổi. Cầm máy lên quay thôi!",
        "tier1": "Ra cà phê đêm đổi gió cho dễ tập trung làm việc.",
        "tier2": "Ở nhà nằm một chỗ thấy tội lỗi, ra quán ngồi ngáp vặt cũng đỡ cắn rứt lương tâm.",
        "tier25": "Mở laptop lên gõ cộc cộc cho người ngoài nhìn vào tưởng mình đang bận rộn dự án lớn, nhưng thực tế tab màn hình chỉ lướt tới lướt lui đồ thị doanh số tụt dốc.",
        "tier3": "Mệt lả người rồi nhưng không dám nghỉ, sợ dừng lại một cái là bạn bè nó vượt mặt hết. Doanh số cả tuần đứng im, nhân viên thì chờ lương."
    },
    {
        "id": "kb02",
        "code": "KB 02",
        "title": "Tiền Mặt Bằng & Cửa Hàng Vắng Khách",
        "short_title": "Tiền Mặt Bằng & Cửa Hàng Vắng",
        "file": "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html",
        "category": "core",
        "category_badge": "MẶT BẰNG & RETAIL",
        "badge_color": "#f43f5e",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Cắt Đổi Trục",
        "context": "Cửa hàng mặt phố vắng khách • Đồng hồ treo tường chạy • Camera an ninh quay cảnh ngáp vặt",
        "target": "Chủ shop offline, chủ tiệm gánh áp lực tiền nhà 20-30 triệu/tháng",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tien_mat_bang_va_cua_hang_vang_khach/assets/frames/scene1_beat1.jpg",
        "hook": "Sáng mở mắt ra là bay mất một triệu tiền mặt bằng... Khách thì lướt mạng, mình thì ngồi ngáp vặt.",
        "cta": "Đến lúc này thì cái gì giúp mình kéo được khách về cửa hàng thì phải bắt tay vào học thôi!",
        "tier1": "Đi học thêm kỹ năng mới để nâng cấp trải nghiệm cửa hàng.",
        "tier2": "Ngồi ở quán cả ngày ngáp vặt sốt ruột quá, mở app ngân hàng ra chỉ thấy tin nhắn trừ tiền cố định.",
        "tier25": "Vẫn cố ăn mặc chỉn chu, lau dọn kệ tủ và xếp từng món hàng ngay ngắn để bảo vệ thể diện 'ông chủ', nhưng trong lòng nhói đau mỗi lần chuông tin nhắn báo trừ 20 triệu tiền nhà.",
        "tier3": "Mỗi tháng mất đứt hai chục củ tiền nhà. Khách ở trên mạng hết rồi, mình cứ ngồi ôm cái quán thì có mà ăn cám."
    },
    {
        "id": "kb03",
        "code": "KB 03",
        "title": "Chững Lại Sau Tuổi 30 & Nhìn Đối Thủ Triệu View",
        "short_title": "Chững Lại Sau Tuổi 30",
        "file": "kich_ban_03_chung_lai_sau_tuoi_30.html",
        "category": "core",
        "category_badge": "TUỔI 30 & ĐỐI THỦ TRIỆU VIEW",
        "badge_color": "#f59e0b",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Thấu Cảm Tự Sự",
        "context": "Bàn làm việc đêm • Màn hình soi kênh TikTok đối thủ trẻ • Nếp nhăn khóe mắt",
        "target": "Người làm nghề 30+, người có chuyên môn nhưng ngại xuất hiện video ngắn",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_03_chung_lai_sau_tuoi_30/assets/frames/scene1_beat1.jpg",
        "hook": "Hơn 30 tuổi, làm nghề cả chục năm... nhìn đứa mới vào nghề nó hốt hết khách nhờ video ngắn.",
        "cta": "Bớt ngại đi, chịu khó học lại từ đầu còn hơn cứ ngồi yên nhìn công việc của mình đi xuống.",
        "tier1": "Xem video đối thủ để nghiên cứu xu hướng thị trường và hành vi người tiêu dùng.",
        "tier2": "Cay cú vì bọn nó mới vào nghề mà đơn nổ ầm ầm, mình làm cả chục năm tay nghề cứng lại chật vật.",
        "tier25": "Miệng chê bọn trẻ làm clip nhảm nhí nông cạn để giữ thể diện người có thâm niên, nhưng đêm về lén mở kênh của chúng nó xem từng giây, vừa xem vừa run vì nhận ra thị trường đã bỏ rơi mình.",
        "tier3": "Cái tôi quá lớn, ngại xuất hiện, sợ người quen chê cười. Nếu không dẹp bỏ sĩ diện thì mất hết khách."
    },
    {
        "id": "kb04",
        "code": "KB 04",
        "title": "Tiền Quảng Cáo Ăn Hết Tiền Lãi",
        "short_title": "Tiền Quảng Cáo Ăn Hết Lãi",
        "file": "kich_ban_04_tien_quang_cao_an_het_tien_lai.html",
        "category": "core",
        "category_badge": "TIỀN ADS & BẪY LỖ",
        "badge_color": "#ec4899",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Nhịp Nhanh Dồn Dập",
        "context": "Trình quản lý Ads Manager đỏ lòm chỉ số chi phí • Cafe nguội ngắt • Màn hình điện thoại",
        "target": "Chủ shop online phụ thuộc vào Facebook/TikTok Ads, chi phí cắn sạch lợi nhuận",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_04_tien_quang_cao_an_het_tien_lai/assets/frames/scene1_beat1.jpg",
        "hook": "Cứ 5 phút tôi lại mở màn hình kiểm tra một lần... Tiền nạp thì trừ đều mà đơn không thấy đâu.",
        "cta": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi!",
        "tier1": "Tối ưu lại chiến dịch quảng cáo và tệp đối tượng cho hiệu quả hơn.",
        "tier2": "Tiền nạp ads ngày nào cũng trừ cả triệu bạc mà không ra đơn, càng chạy càng lỗ.",
        "tier25": "Đi cafe với bạn bè vẫn khoe doanh thu trăm triệu để giữ uy tín, nhưng giấu tiệt chuyện tiền lãi thực tế sau khi trừ ads không bằng lương đi làm thuê học việc.",
        "tier3": "Lệ thuộc vào quảng cáo như con nghiện, tắt ads là chết đói. Bắt buộc phải tự làm video kéo traffic tự nhiên."
    },
    {
        "id": "kb05",
        "code": "KB 05",
        "title": "Hết Khách Từ Mối Quan Hệ Quen",
        "short_title": "Hết Khách Người Quen",
        "file": "kich_ban_05_het_khach_tu_moi_quan_he_quen.html",
        "category": "core",
        "category_badge": "KHÁCH QUEN & RÀO CẢN",
        "badge_color": "#a855f7",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Chân Thành Lắng Đọng",
        "context": "Danh bạ điện thoại • Tin nhắn Zalo đã nhắn hết một lượt • Ánh mắt ngập ngừng",
        "target": "Người làm dịch vụ, tư vấn, bảo hiểm, bất động sản, bán hàng đa kênh",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_05_het_khach_tu_moi_quan_he_quen/assets/frames/scene1_beat1.jpg",
        "hook": "Lướt danh bạ từ trên xuống dưới mà không biết nhắn cho ai... Bán cho người quen hết cửa rồi.",
        "cta": "Muốn đi đường dài thì phải tự học cách tiếp cận người lạ bằng nội dung tử tế thôi.",
        "tier1": "Mở rộng tệp khách hàng tiềm năng mới ngoài các kênh truyền thống.",
        "tier2": "Anh em bạn bè mua ủng hộ một hai lần đầu rồi thôi, giờ mở lời chào hàng ai cũng lảng đi chỗ khác.",
        "tier25": "Đăng bài bán hàng lên Facebook cá nhân nhưng phải cài đặt chế độ loại trừ sếp cũ và bạn đại học vì sợ họ xì xào mình đang sa cơ lỡ vận.",
        "tier3": "Cứ dựa vào người quen thì quy mô không bao giờ lớn được. Phải dám xuất hiện trên mạng để bán cho người lạ."
    },
    {
        "id": "kb06",
        "code": "KB 06",
        "title": "Tay Nghề Tốt Nhưng Vẫn Vắng Khách",
        "short_title": "Tay Nghề Tốt Vẫn Vắng Khách",
        "file": "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html",
        "category": "core",
        "category_badge": "TAY NGHỀ & MARKETING",
        "badge_color": "#14b8a6",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Trực Diện Đanh Thép",
        "context": "Xưởng/tiệm làm việc tỉ mỉ • Đồ nghề sáng bóng • Nhìn sang tiệm đối diện nhộn nhịp",
        "target": "Thợ thủ công, kỹ thuật viên, chuyên gia có chuyên môn sâu nhưng yếu truyền thông",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_06_tay_nghe_tot_nhung_van_vang_khach/assets/frames/scene1_beat1.jpg",
        "hook": "Làm nghề mười mấy năm, đồ mình làm ra tự tin không thua ai... Thế mà quán đối diện làm dở lại đông hơn.",
        "cta": "Giỏi nghề mà giữ trong xưởng thì không ai biết, phải tự đưa nghề của mình ra ánh sáng!",
        "tier1": "Tập trung nâng cao chất lượng dịch vụ và tay nghề, hữu xạ tự nhiên hương.",
        "tier2": "Ấm ức vì mình làm kỹ hơn, vật liệu tốt hơn mà quán khác đông hơn nhờ biết làm marketing.",
        "tier25": "Lấy cái cớ 'người làm nghề chân chính không thích làm màu' để ru ngủ bản thân trốn tránh việc học quay video, trong khi lòng đau quặn thắt nhìn thợ tay nghề dở hơn hốt hết khách VIP.",
        "tier3": "Tự phụ vào tay nghề là tự sát. Thời buổi này tay nghề tốt chỉ là điều kiện cần, biết làm video xuất hiện mới là điều kiện đủ."
    },
    {
        "id": "kb07",
        "code": "KB 07",
        "title": "Bị Cạnh Tranh Bởi Tổng Kho & Giá Gốc",
        "short_title": "Cạnh Tranh Tổng Kho Giá Gốc",
        "file": "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html",
        "category": "core",
        "category_badge": "TỔNG KHO & GIÁ RẺ",
        "badge_color": "#06b6d4",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Cảnh Báo Sâu Sắc",
        "context": "Cửa hàng bán lẻ • Khách cầm điện thoại soi giá sàn • Màn hình livestream xả kho giá sốc",
        "target": "Cửa hàng bán lẻ, đại lý phân phối truyền thống bị tổng kho livestream bóp nghẹt",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc/assets/frames/scene1_beat1.jpg",
        "hook": "Khách cầm điện thoại vào hỏi: 'Sao trên mạng bán rẻ hơn anh mấy chục ngàn?'...",
        "cta": "Đua giá rẻ với tổng kho là tự sát! Thứ duy nhất tổng kho không sao chép được là sự tử tế và uy tín của bạn!",
        "tier1": "Tìm nguồn hàng mới có giá cạnh tranh hơn để tiếp tục bán lẻ.",
        "tier2": "Nhìn tổng kho livestream bán lẻ rẻ hơn cả giá mình nhập buôn số lượng lớn mà bất lực cay đắng.",
        "tier25": "Cố gồng mình giảm giá 10-15% để giữ chân vài khách lẻ, vừa bán vừa cắn răng chịu lỗ để không bị mang tiếng là bán đắt cắt cổ.",
        "tier3": "Cạnh tranh về giá là cuộc đua xuống đáy. Chỉ có uy tín cá nhân và làm video trực diện mới giữ chân được khách trung thành."
    },
    {
        "id": "kb08",
        "code": "KB 08",
        "title": "Bắt Đầu Lại Từ Con Số 0",
        "short_title": "Bắt Đầu Lại Từ Con Số 0",
        "file": "kich_ban_08_bat_dau_lai_tu_con_so_0.html",
        "category": "core",
        "category_badge": "LÀM LẠI TỪ ĐẦU",
        "badge_color": "#10b981",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Vươn Lên Quyết Liệt",
        "context": "Góc phòng trọ mới thuê • Điện thoại trên chân tripod rẻ tiền • Không gian tinh gọn",
        "target": "Người từng vấp ngã thất bại, phải làm lại từ đầu sau khi mất vốn/dẹp tiệm",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_08_bat_dau_lai_tu_con_so_0/assets/frames/scene1_beat1.jpg",
        "hook": "Đóng cửa tiệm cũ, trong tay gần như về lại số 0... Sợ nhất không phải nghèo, mà là sợ bạn bè cười chê.",
        "cta": "Sĩ diện có mài ra ăn được đâu! Dẹp bỏ tự ái, cầm điện thoại lên làm lại từ đầu!",
        "tier1": "Khởi động một dự án kinh doanh mới với kế hoạch bài bản hơn.",
        "tier2": "Từng có thành công nhưng giờ thất bại phải làm lại từ đầu, đi đâu cũng sợ người quen nhìn thấy hỏi han.",
        "tier25": "Quay video giấu mặt hoặc lấy nick ảo vì sợ đối tác cũ nhìn thấy mình đang phải bắt đầu lại từ đáy vực, không dám thừa nhận mình đã thất bại.",
        "tier3": "Cái sĩ diện hão không nuôi sống được gia đình. Dẹp bỏ tự ái, cầm máy lên quay từ số 0 để lấy lại những gì đã mất."
    },
    {
        "id": "kb09",
        "code": "KB 09",
        "title": "Hàng Làm Kỹ Nhưng Bị So Sánh Giá",
        "short_title": "Hàng Làm Kỹ Bị So Giá",
        "file": "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html",
        "category": "core",
        "category_badge": "LÀM KỸ & BỊ ÉP GIÁ",
        "badge_color": "#f97316",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • Phơi Bày Công Phu",
        "context": "Xưởng đồ da thủ công / Chế tác tỉ mỉ • Khách so sánh với hàng chợ công nghiệp",
        "target": "Chủ xưởng sản xuất, người làm hàng thủ công / kỹ nghệ tâm huyết bị khách chê đắt",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia/assets/frames/scene1_beat1.jpg",
        "hook": "Mất 3 ngày gia công từng đường kim mũi chỉ, khách vào phán một câu: 'Trên mạng bán có nửa giá'...",
        "cta": "Thay vì ngồi bực mình khi bị so sánh, tôi chọn quay lại từng công đoạn thật để khách tự nhìn thấy giá trị!",
        "tier1": "Giải thích chi tiết về nguyên vật liệu cao cấp và nguồn gốc da nhập khẩu cho khách hiểu.",
        "tier2": "Tức điên khi hàng tâm huyết làm bằng tay bị so sánh với đồ công nghiệp dập khuôn rẻ tiền trên sàn.",
        "tier25": "Im lặng nuốt cục tức vào trong, cười gượng tiếp khách nhưng trong lòng ấm ức chỉ muốn đuổi khách ra khỏi tiệm vì thấy tay nghề của mình bị coi thường.",
        "tier3": "Khách không có lỗi, lỗi do mình không biết cách làm video phơi bày công sức và sự tỉ mỉ. Phải show toàn bộ quy trình lên video."
    }
]

extra_scripts = [
    {
        "id": "bai_tap_01",
        "code": "BÀI TẬP 01",
        "title": "Bài Tập 01 • Băm Nhỏ Cảnh Trám Marketing Tại Lớp",
        "short_title": "Bài Tập 01: Băm Cảnh Trám",
        "file": "bai_tap_01_phan_canh_canh_tram.html",
        "category": "exercise",
        "category_badge": "BÀI TẬP TẠI LỚP (HOT)",
        "badge_color": "#38bdf8",
        "duration": "12 Giây • 5 Cú Máy • 2.5s/Shot",
        "rhythm": "Đổi đồng thời 3 trục: Cỡ • Góc • Hướng",
        "context": "Lớp học Marketing PT • Bàn học thực tế • Sinh viên soi chỉ số Ads và cày laptop",
        "target": "Học viên lớp Offline thực hành quay ngay tại bàn học bằng smartphone cá nhân",
        "thumb": "assets/frames_bai_tap_01/shot1.jpg",
        "hook": "Nhìn đồ thị Ads đăm chiêu, ngón tay cuộn chuột liên tục... 1 hành động băm thành 5 cú máy đắt giá!",
        "cta": "Áp dụng ngay tại bàn: Cắt nhỏ hành động gốc để tiêu diệt tận gốc căn bệnh 'cảnh trám chết dí'!",
        "tier1": "Quay bạn học gõ máy tính để làm cảnh nền chèn vào video marketing.",
        "tier2": "Đặt máy một chỗ quay đơ đơ suốt 8-10 giây, nhìn khung hình lờ đờ, buồn ngủ, khán giả lướt qua sau 1 giây.",
        "tier25": "Nghĩ mình quay cảnh trám chỉ là phụ nên lười đổi góc, giơ máy lên quay đại một đoạn cho có để nộp bài tập.",
        "tier3": "Cảnh trám chết dí thể hiện tư duy lười biếng. Băm nhỏ 5 cú máy đổi 3 trục mới là vũ khí giữ chân người xem từng giây.",
        "shots_preview": [
            {"time": "00:00 - 00:02.5", "badge": "Shot 1 • MCU (Cận ngực)", "visual": "Mắt đăm chiêu nhìn màn hình, ánh sáng xanh hắt nhẹ lên khuôn mặt.", "voice": "\"Mở chiến dịch ra soi từng con số...\""},
            {"time": "00:02.5 - 00:05", "badge": "Shot 2 • CU (Cận cảnh)", "visual": "Bàn tay gõ phím lách cách, ngón tay đổi phím dứt khoát.", "voice": "\"...tiền nạp ads thì cắn đều từng phút...\""},
            {"time": "00:05 - 00:07.5", "badge": "Shot 3 • Macro (Đặc tả)", "visual": "Màn hình CapCut timeline & bảng báo cáo chi phí Facebook Ads.", "voice": "\"...nhưng đơn về thì lẹt đẹt vài ba cái...\""},
            {"time": "00:07.5 - 00:10", "badge": "Shot 4 • OTS (Qua vai)", "visual": "Góc qua vai thấy cả bạn cùng bàn đang cắm cúi viết kịch bản.", "voice": "\"...người ngoài nhìn vào tưởng dân marketing oách lắm...\""},
            {"time": "00:10 - 00:12.5", "badge": "Shot 5 • Low Angle (Hất thấp)", "visual": "Góc máy đặt sát mặt bàn hất lên, mặt căng thẳng thở hắt ra.", "voice": "\"...nhưng thật ra là đang toát mồ hôi hột tìm đường sống!\""}
        ]
    },
    {
        "id": "salon_toc_10nam",
        "code": "CASE STUDY 01",
        "title": "Chiến Lược & Visual Storyboard Salon Tóc 10 Năm Hải Phòng",
        "short_title": "Salon Tóc 10 Năm (Khương Minh)",
        "file": "chien_luoc_xay_kenh_toc_10_nam.html",
        "category": "case",
        "category_badge": "SALON TÓC VIP",
        "badge_color": "#ec4899",
        "duration": "15 Giây / Video • 4 Cảnh • 8 Beats",
        "rhythm": "Zoom-cut theo Beat Nhạc (No-Voice)",
        "context": "Salon tóc Khương Minh Hải Phòng • Góc gội đầu • Ghế cắt tóc • Đèn Nanlite vàng ấm",
        "target": "Chủ salon tóc, thợ tóc lâu năm muốn xây kênh TikTok hút tệp khách VIP",
        "thumb": "assets/frames_toc_10nam/04_hero_model.jpg",
        "hook": "Mặt Tròn Cắt Gì Cho Sang? / Từng Bị Tóc Cháy Khô Xơ? (Cắt theo điệu nhạc lofi cực sang)",
        "cta": "Chiến lược Quiet Luxury khai thác tay nghề 10 năm và đòn bẩy tâm lý Mẫu Xinh (Halo Effect).",
        "tier1": "Quay video salon tóc theo trào lưu biến hình rầm rộ trên mạng.",
        "tier2": "Khách đến salon toàn hỏi giá rẻ, khách VIP không thấy đâu dù tay nghề thợ 10 năm kinh nghiệm.",
        "tier25": "Ngại xuất hiện nói chuyện trước ống kính vì sợ mất hình ảnh chủ tiệm đứng đắn.",
        "tier3": "Không cần nói lời nào! Dùng video 15s Zoom-cut nhịp nhạc + mẫu xinh để kéo tệp khách chịu chi.",
        "shots_preview": [
            {"time": "00:00 - 00:03", "badge": "Cảnh 1 • Hook Tóc Khô", "visual": "Cận cảnh bàn tay thợ vuốt lọn tóc xơ rối của khách.", "voice": "(Nhạc Lofi nhẹ) Nhịp bass 1 drop"},
            {"time": "00:03 - 00:07", "badge": "Cảnh 2 • Pha Thuốc Phục Hồi", "visual": "Bát thuốc collagen thơm, thìa khuấy mịn, tay đeo găng đen.", "voice": "(Tiếng ASMR khuấy thuốc & chải tóc)"},
            {"time": "00:07 - 00:11", "badge": "Cảnh 3 • Kéo Cắt Tỉa Tỉ Mỉ", "visual": "Mũi kéo bén cắt từng ngọn tóc bay trong ánh đèn vàng ấm.", "voice": "(Tiếng kéo rẹt rẹt cực đã tai)"},
            {"time": "00:11 - 00:15", "badge": "Cảnh 4 • Hero Shot Mẫu Xinh", "visual": "Mái tóc bồng bềnh, mẫu quay đầu cười tỏa sáng, quạt thổi nhẹ.", "voice": "Hải Phòng • Inbox nhận tư vấn dáng tóc phù hợp"}
        ]
    },
    {
        "id": "nguyet_store",
        "code": "CASE STUDY 02",
        "title": "Kịch Bản Thực Chiến: Nguyệt Store Hải Phòng (5 Video B-Roll Theo Beat)",
        "short_title": "Nguyệt Store Hải Phòng",
        "file": "kich_ban_nguyet_store_hai_phong.html",
        "category": "case",
        "category_badge": "BÁN LẺ IPHONE LIKE NEW",
        "badge_color": "#06b6d4",
        "duration": "18 - 22 Giây / Video • 5 Cảnh • 16 Beats",
        "rhythm": "1.5s / Beat • ASMR Âm Thanh Vật Lý",
        "context": "Cửa hàng điện thoại Like New Hải Phòng • Bàn test máy • Hộp phụ kiện • Tem ốc zin",
        "target": "Cửa hàng điện thoại, bán iPhone/iPad Like New cần xây dựng niềm tin kiểm định máy zin",
        "thumb": "assets/kb1_c1.jpg",
        "hook": "15 Pro Max Like New Có Zin Như Lời Đồn? (Tiếng click mở hộp & soi ốc sắc bén)",
        "cta": "Bảo hành lỗi 1 đổi 1 tận nơi Hải Phòng • Nhận hàng check zin mới trả tiền.",
        "tier1": "Đăng ảnh chụp máy lên fanpage và chạy quảng cáo khuyến mãi giảm giá.",
        "tier2": "Khách sợ mua phải máy dựng, ép kính, thay vỏ trôi nổi trên mạng nên nghi ngờ đủ thứ.",
        "tier25": "Cứ phải thanh minh 'hàng em chuẩn xịn anh ơi' nhưng càng giải thích khách càng nghi.",
        "tier3": "Show toàn bộ quy trình soi ốc zin, quét 3uTools và vạch khuyết điểm trừ tiền ngay trên video!",
        "shots_preview": [
            {"time": "00:00 - 00:04", "badge": "Beat 1 • Cầm Máy", "visual": "Tay đeo găng nhấc chiếc iPhone Titan tự nhiên ra khỏi hộp.", "voice": "\"15 Pro Max lướt này có thực sự nguyên bản?\""},
            {"time": "00:04 - 00:08", "badge": "Beat 2 • Soi Ốc Đáy", "visual": "Kính lúp phóng to 2 con ốc đít, ren ốc sắc cạnh chưa từng mở.", "voice": "\"Ốc đít chưa một vết tì, gioăng chống nước nguyên vẹn.\""},
            {"time": "00:08 - 00:13", "badge": "Beat 3 • Quét 3uTools", "visual": "Cắm cáp máy tính, màn hình hiện 100% xanh lá điểm linh kiện.", "voice": "\"Pin 100%, số lần sạc chuẩn zin, màn hình True Tone đầy đủ.\""},
            {"time": "00:13 - 00:18", "badge": "Beat 4 • Chốt Đơn & Giao Hàng", "visual": "Dán tem bảo hành, đóng gói hỏa tốc giao tận tay khách Hải Phòng.", "voice": "\"Nhận hàng kiểm tra ưng ý mới thanh toán!\""}
        ]
    },
    {
        "id": "tu_dot_tien",
        "code": "DEMO GỐC",
        "title": "Kịch Bản Gốc: Từ Đốt Tiền Quảng Cáo Đến Tự Tin Xuất Hiện",
        "short_title": "Từ Đốt Tiền Đến Tự Tin",
        "file": "tu_dot_tien_den_tu_tin_xuat_hien.html",
        "category": "core",
        "category_badge": "DEMO BỐI CẢNH LỚP",
        "badge_color": "#38bdf8",
        "duration": "30 Giây • 5 Cảnh • 15 Beats",
        "rhythm": "1.5s / Beat • J-Cut Âm Thanh",
        "context": "Lớp học thực tế • Màn hình điện thoại trừ tiền • Nụ cười vỡ òa khi tự quay video",
        "target": "Chủ doanh nghiệp nhỏ, người bán hàng online bế tắc vì phụ thuộc quảng cáo",
        "thumb": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg",
        "hook": "Cứ 5 phút tôi lại mở màn hình kiểm tra một lần... Tiền nạp ăn hết lãi.",
        "cta": "Không thể dựa mãi vào việc đi mua quảng cáo, phải tự học cách xuất hiện trước khách hàng thôi.",
        "tier1": "Đi tìm công thức vít ads nghìn đơn từ các khóa học online.",
        "tier2": "Chi phí ads tăng gấp đôi, chạy bao nhiêu nuôi nền tảng bấy nhiêu mà không dám tắt.",
        "tier25": "Vẫn khoe đơn hàng ngập tràn với gia đình nhưng đêm về mất ngủ vì tài khoản ads bị khóa.",
        "tier3": "Xuất hiện trước ống kính là con đường độc lập tự chủ duy nhất của người làm kinh doanh.",
        "shots_preview": [
            {"time": "00:00 - 00:05", "badge": "Cảnh 1 • Soi Ads", "visual": "Cầm điện thoại vuốt màn hình ads, mặt đăm chiêu.", "voice": "\"Cứ 5 phút lại mở điện thoại xem tiền trừ...\""},
            {"time": "00:05 - 00:11", "badge": "Cảnh 2 • Nhìn Bảng Lỗ", "visual": "Bàn làm việc giấy tờ sổ sách ghi chi phí quảng cáo tăng vọt.", "voice": "\"Doanh thu thì cao mà tiền lãi chẳng thấy đâu...\""},
            {"time": "00:11 - 00:18", "badge": "Cảnh 3 • Đến Lớp Học", "visual": "Bước vào phòng học, nhìn thấy bạn bè đang thực hành quay video.", "voice": "\"Nhìn mọi người tự tin đứng trước máy quay...\""},
            {"time": "00:18 - 00:24", "badge": "Cảnh 4 • Cầm Tripod", "visual": "Hai tay cầm chân máy, bấm nút REC đỏ, hít một hơi thật sâu.", "voice": "\"...mình nhận ra chỉ có tự xuất hiện mới bền vững.\""},
            {"time": "00:24 - 00:30", "badge": "Cảnh 5 • Nụ Cười Thật", "visual": "Nhìn thẳng ống kính cười tự nhiên, phong thái chủ tiệm đĩnh đạc.", "voice": "\"Tự tin xuất hiện, khách hàng tự tìm tới!\""}
        ]
    },
    {
        "id": "miumiu_dalieu",
        "code": "CASE STUDY 03",
        "title": "Chiến Lược Nội Dung & 5 Kịch Bản 2 Góc Máy: Da Liễu Miu Miu",
        "short_title": "Da Liễu Miu Miu",
        "file": "miumiu_dalieu.html",
        "category": "case",
        "category_badge": "DA LIỄU CHUẨN Y KHOA",
        "badge_color": "#ec4899",
        "duration": "30 - 45 Giây / Video • 2 Góc Máy",
        "rhythm": "A-Roll Chuyên Gia & B-Roll Lâm Sàng",
        "context": "Phòng khám da liễu • Kính soi da • Đèn khám y khoa • Ca trị mụn thực tế",
        "target": "Bác sĩ, chủ spa, chuyên gia thẩm mỹ muốn bán liệu trình cao cấp không chèo kéo",
        "thumb": "assets/frames_toc_10nam/01_studio_chair.jpg",
        "hook": "Trị mụn 3 năm không khỏi không phải do da bạn yếu, mà do bạn chưa biết điều này...",
        "cta": "Chiến lược 2 góc máy xóa bỏ hoàn toàn rào cản phòng khám và tạo niềm tin tuyệt đối.",
        "tier1": "Đăng ảnh trước sau (Before/After) trị mụn và cam kết khỏi 100%.",
        "tier2": "Khách hàng bị bội thực quảng cáo mỹ phẩm kem trộn nên mất niềm tin vào spa.",
        "tier25": "Cố tỏ ra là chuyên gia đẳng cấp bằng cách dùng thuật ngữ y khoa khó hiểu làm khách sợ.",
        "tier3": "Bóc trần sự thật ngượng miệng về thói quen tự nặn mụn tại nhà và giải thích cơ chế sinh học mộc mạc.",
        "shots_preview": [
            {"time": "00:00 - 00:06", "badge": "A-Roll • Bác Sĩ", "visual": "Bác sĩ ngồi bàn tư vấn, áo blouse trắng, ánh mắt thấu hiểu.", "voice": "\"Trị mụn 3 năm không khỏi không phải do da bạn yếu...\""},
            {"time": "00:06 - 00:15", "badge": "B-Roll • Soi Da", "visual": "Kính soi da phóng to cồi mụn viêm và lớp màng ẩm bị bào mòn.", "voice": "\"...mà do hàng rào bảo vệ da đã bị kem trộn tàn phá.\""},
            {"time": "00:15 - 00:25", "badge": "B-Roll • Thao Tác Chuẩn", "visual": "Dụng cụ y tế vô trùng, sát khuẩn kỹ càng, gắp cồi nhẹ nhàng.", "voice": "\"Ở đây chúng tôi không bán kem thần thánh, chúng tôi phục hồi nền da.\""},
            {"time": "00:25 - 00:35", "badge": "A-Roll • Lời Dặn Dò", "visual": "Bác sĩ đưa phác đồ điều trị tận tay bệnh nhân kèm nụ cười an tâm.", "voice": "\"Kiên trì 4 tuần, da bạn sẽ tự chữa lành.\""}
        ]
    },
    {
        "id": "ads_prompt",
        "code": "AI TOOL",
        "title": "Miss Video Ads Mega Prompt (Gemini AI Studio)",
        "short_title": "Mega Prompt Video Ads",
        "file": "ads.html",
        "category": "exercise",
        "category_badge": "MEGA PROMPT GEMINI",
        "badge_color": "#f59e0b",
        "duration": "1-Click Copy • Tự Động Hóa Kịch Bản",
        "rhythm": "Framework Video Chuyển Đổi Cao",
        "context": "Môi trường AI Studio • Tối ưu hóa prompt kịch bản chuyển đổi cao",
        "target": "Editor, Marketer, Học viên muốn gen nhanh kịch bản video quảng cáo chuẩn FEDU",
        "thumb": "assets/frames_bai_tap_01/shot3.jpg",
        "hook": "Chỉ 1 click sao chép toàn bộ Mega Prompt độc quyền chuẩn hóa kịch bản chuyển đổi cao.",
        "cta": "Copy vào Google AI Studio hoặc ChatGPT để băm kịch bản video bán hàng trong 3 giây.",
        "tier1": "Tự viết kịch bản quảng cáo theo cảm tính hoặc copy văn mẫu trên mạng.",
        "tier2": "Viết mãi không ra được kịch bản hay, bí ý tưởng hook giữ chân khách trong 3 giây đầu.",
        "tier25": "Dùng ChatGPT với prompt ngô nghê ra toàn kịch bản sáo rỗng 'Chào các bạn, hôm nay tôi sẽ...'.",
        "tier3": "Mega Prompt nạp sẵn tư duy bóc trần 3 tầng và cấu trúc nhịp A-Roll/B-Roll không tì vết.",
        "shots_preview": [
            {"time": "Bước 1", "badge": "Setup Context", "visual": "Nhập thông tin sản phẩm, chân dung khách hàng và nỗi đau cốt lõi.", "voice": "Mega Prompt kích hoạt vai trò Đạo diễn chuyển đổi"},
            {"time": "Bước 2", "badge": "Bóc Tách 3 Tầng", "visual": "AI tự động bóc tách Tầng 1 (Đãi bôi) sang Tầng 3 (Ngượng miệng).", "voice": "Sinh ra 3 phương án Hook đắt giá"},
            {"time": "Bước 3", "badge": "Băm Phân Cảnh", "visual": "Xuất bảng phân cảnh 5 nhịp A-Roll/B-Roll khớp từng giây thoại.", "voice": "Sẵn sàng đưa vào CapCut dựng phim"}
        ]
    }
]

# Combine all cards
all_items = []
for s in core_scripts:
    kbid = s["id"]
    rows = kb_data.get(kbid, {}).get("rows", [])
    s["shots_preview"] = rows
    all_items.append(s)

for s in extra_scripts:
    all_items.append(s)

print(f"Total master items: {len(all_items)}")

# Generate HTML
html_output = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🏛️ Master Hub • Tổng Hợp Toàn Bộ Kịch Bản Thực Chiến Lớp Offline | FEDU AI Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #060911;
      --bg-surface: #0c121e;
      --bg-card: #111a2b;
      --bg-card-hover: #162238;
      --card-inner: #17243c;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.35);
      --border-glow: rgba(56, 189, 248, 0.6);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --cyan: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.16);
      --amber: #f59e0b;
      --amber-glow: rgba(245, 158, 11, 0.16);
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.16);
      --rose: #f43f5e;
      --rose-glow: rgba(244, 63, 94, 0.16);
      --purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.16);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;
      --shadow-card: 0 10px 30px rgba(0, 0, 0, 0.4);
      --shadow-hover: 0 20px 45px rgba(0, 0, 0, 0.6), 0 0 25px rgba(56, 189, 248, 0.2);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    
    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-main);
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.1) 0%, transparent 65%),
        radial-gradient(circle at 10% 40%, rgba(168, 85, 247, 0.05) 0%, transparent 45%),
        radial-gradient(circle at 90% 70%, rgba(16, 185, 129, 0.05) 0%, transparent 45%);
      background-attachment: fixed;
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 120px;
      -webkit-font-smoothing: antialiased;
    }}

    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* TOP STICKY BAR */
    .top-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(6, 9, 17, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      transition: all 0.2s ease;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }}

    .brand-badge {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }}

    .brand-title {{
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-title span {{
      color: var(--cyan);
    }}

    .header-nav {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .nav-link {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 12.5px;
      font-weight: 600;
      padding: 7px 14px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .nav-link:hover, .nav-link.active {{
      background: var(--cyan);
      color: #060911;
      border-color: var(--cyan);
      font-weight: 700;
    }}

    .nav-link.highlight {{
      border-color: rgba(56, 189, 248, 0.4);
      background: var(--cyan-glow);
      color: var(--cyan);
    }}
    .nav-link.highlight:hover {{
      background: var(--cyan);
      color: #060911;
    }}

    /* HERO BANNER */
    .hero {{
      background: linear-gradient(180deg, rgba(17, 26, 43, 0.9) 0%, rgba(12, 18, 30, 0.95) 100%);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: var(--radius-lg);
      padding: 44px 36px 36px;
      margin: 24px 0 32px;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
    }}

    .hero::before {{
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle at center, rgba(56, 189, 248, 0.08) 0%, transparent 60%);
      pointer-events: none;
    }}

    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--cyan-glow);
      color: var(--cyan);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 6px 18px;
      border-radius: var(--radius-full);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      margin-bottom: 16px;
    }}

    .hero h1 {{
      font-size: clamp(26px, 3.2vw, 38px);
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 14px;
      line-height: 1.25;
      letter-spacing: -0.5px;
    }}

    .hero-desc {{
      color: #cbd5e1;
      font-size: 15.5px;
      max-width: 880px;
      margin: 0 auto 28px;
      line-height: 1.7;
    }}

    .hero-desc b {{
      color: var(--cyan);
    }}

    /* STATS GRID */
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
      gap: 16px;
      background: rgba(6, 9, 17, 0.65);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 18px 24px;
      max-width: 960px;
      margin: 0 auto;
    }}

    .stat-item {{
      text-align: center;
      position: relative;
    }}

    .stat-item:not(:last-child)::after {{
      content: '';
      position: absolute;
      right: -8px;
      top: 15%;
      height: 70%;
      width: 1px;
      background: var(--border-subtle);
    }}

    @media (max-width: 768px) {{
      .stat-item:not(:last-child)::after {{ display: none; }}
    }}

    .stat-number {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 30px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.1;
    }}

    .stat-number span {{
      color: var(--cyan);
    }}

    .stat-label {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-top: 4px;
      letter-spacing: 0.5px;
    }}

    /* METHODOLOGY SECTION (3 TẦNG & BĂM CẢNH TRÁM) */
    .methodology-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 24px 28px;
      margin-bottom: 32px;
    }}

    .methodology-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      cursor: pointer;
      user-select: none;
    }}

    .methodology-title {{
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .toggle-icon {{
      font-size: 14px;
      color: var(--cyan);
      transition: transform 0.2s ease;
    }}

    .methodology-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }}

    .method-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      position: relative;
      border-top: 4px solid;
    }}

    .method-card.m1 {{ border-top-color: var(--rose); }}
    .method-card.m2 {{ border-top-color: var(--amber); }}
    .method-card.m25 {{ border-top-color: var(--purple); }}
    .method-card.m3 {{ border-top-color: var(--emerald); }}
    .method-card.m4 {{ border-top-color: var(--cyan); }}

    .method-label {{
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .method-card.m1 .method-label {{ color: var(--rose); }}
    .method-card.m2 .method-label {{ color: var(--amber); }}
    .method-card.m25 .method-label {{ color: var(--purple); }}
    .method-card.m3 .method-label {{ color: var(--emerald); }}
    .method-card.m4 .method-label {{ color: var(--cyan); }}

    .method-title {{
      font-size: 15px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 6px;
    }}

    .method-desc {{
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.55;
    }}

    /* CONTROLS & FILTER BAR */
    .controls-bar {{
      position: sticky;
      top: 60px;
      z-index: 900;
      background: rgba(6, 9, 17, 0.95);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 12px 18px;
      margin-bottom: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }}

    .filter-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 2px;
    }}

    .filter-tab {{
      white-space: nowrap;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: var(--radius-sm);
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .filter-tab:hover {{
      background: var(--card-inner);
      color: #ffffff;
    }}

    .filter-tab.active {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border-color: var(--cyan);
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }}

    .search-box {{
      position: relative;
      min-width: 280px;
      flex: 1;
      max-width: 420px;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 9px 14px 9px 36px;
      color: #ffffff;
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--cyan);
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
      background: var(--bg-surface);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 14px;
      pointer-events: none;
    }}

    /* SCRIPT CARDS GRID */
    .scripts-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(440px, 1fr));
      gap: 24px;
    }}

    @media (max-width: 960px) {{
      .scripts-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    /* SCRIPT CARD COMPONENT */
    .script-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-card);
    }}

    .script-card:hover {{
      border-color: var(--border-accent);
      transform: translateY(-3px);
      box-shadow: var(--shadow-hover);
    }}

    /* Card Top: Thumb + Headers */
    .card-top {{
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }}

    .card-thumb-wrap {{
      flex: 0 0 115px;
      aspect-ratio: 9 / 16;
      border-radius: var(--radius-sm);
      overflow: hidden;
      background: #000;
      position: relative;
      border: 1px solid rgba(255, 255, 255, 0.1);
      cursor: pointer;
    }}

    .card-thumb-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }}

    .card-thumb-wrap:hover img {{
      transform: scale(1.06);
    }}

    .thumb-badge-duration {{
      position: absolute;
      bottom: 6px;
      right: 6px;
      background: rgba(0, 0, 0, 0.85);
      color: #fff;
      font-size: 9px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }}

    .card-info {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .card-tag-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .code-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      font-weight: 800;
      background: rgba(56, 189, 248, 0.15);
      color: var(--cyan);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      text-transform: uppercase;
    }}

    .category-pill {{
      font-size: 10px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      border: 1px solid;
    }}

    .card-title {{
      font-size: 18px;
      font-weight: 800;
      line-height: 1.35;
      color: #ffffff;
      margin-top: 2px;
    }}

    .card-title a {{
      color: #ffffff;
      text-decoration: none;
      transition: color 0.2s;
    }}

    .card-title a:hover {{
      color: var(--cyan);
    }}

    .meta-line {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .meta-line b {{
      color: var(--text-main);
    }}

    /* 3 Tiers Box inside card */
    .tiers-box {{
      background: rgba(0, 0, 0, 0.28);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .tier-row {{
      font-size: 12px;
      line-height: 1.45;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}

    .tier-tag {{
      font-size: 10px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      white-space: nowrap;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      flex-shrink: 0;
      margin-top: 1px;
    }}

    .tier-tag.t1 {{ background: var(--rose-glow); color: var(--rose); border: 1px solid rgba(244, 63, 94, 0.3); }}
    .tier-tag.t2 {{ background: var(--amber-glow); color: var(--amber); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .tier-tag.t25 {{ background: var(--purple-glow); color: var(--purple); border: 1px solid rgba(168, 85, 247, 0.35); font-weight: 900; }}
    .tier-tag.t3 {{ background: var(--emerald-glow); color: var(--emerald); border: 1px solid rgba(16, 185, 129, 0.3); }}

    .tier-content {{
      color: #cbd5e1;
      font-size: 12.5px;
    }}

    /* Hook Highlight Quote */
    .hook-quote {{
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.08) 0%, rgba(0,0,0,0.3) 100%);
      border-left: 3px solid var(--cyan);
      padding: 10px 14px;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }}

    .hook-label {{
      font-size: 10.5px;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .hook-text {{
      font-size: 13px;
      color: #ffffff;
      font-weight: 600;
      font-style: italic;
    }}

    /* Accordion 5 Scenes */
    .accordion-trigger {{
      background: var(--card-inner);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s;
    }}

    .accordion-trigger:hover {{
      background: rgba(56, 189, 248, 0.1);
      color: #ffffff;
      border-color: rgba(56, 189, 248, 0.3);
    }}

    .accordion-content {{
      display: none;
      margin-top: 8px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 10px;
      flex-direction: column;
      gap: 8px;
    }}

    .accordion-content.open {{
      display: flex;
    }}

    .scene-item {{
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      padding-bottom: 6px;
      font-size: 12px;
    }}
    .scene-item:last-child {{
      border-bottom: none;
      padding-bottom: 0;
    }}

    .scene-badge-line {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2px;
    }}

    .scene-pill {{
      font-size: 10px;
      font-weight: 700;
      color: var(--cyan);
    }}

    .scene-time {{
      font-size: 10px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-dim);
    }}

    .scene-visual {{
      color: var(--text-muted);
      font-size: 11.5px;
      margin-bottom: 2px;
    }}

    .scene-voice {{
      color: #f1f5f9;
      font-weight: 600;
      font-size: 12px;
    }}

    /* Card Footer & Action CTA */
    .card-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-top: auto;
      padding-top: 14px;
      border-top: 1px solid var(--border-subtle);
      flex-wrap: wrap;
    }}

    .btn-view-storyboard {{
      flex: 1;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff !important;
      font-size: 12.5px;
      font-weight: 800;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
      border: 1px solid rgba(56, 189, 248, 0.5);
      transition: all 0.2s ease;
      white-space: nowrap;
    }}

    .btn-view-storyboard:hover {{
      background: var(--cyan);
      color: #060911 !important;
      box-shadow: 0 6px 20px rgba(56, 189, 248, 0.6);
      transform: translateY(-2px);
    }}

    .btn-copy-script {{
      background: var(--card-inner);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 700;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
      white-space: nowrap;
    }}

    .btn-copy-script:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }}

    /* TOAST NOTIFICATION */
    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: rgba(16, 185, 129, 0.95);
      color: #ffffff;
      padding: 12px 20px;
      border-radius: var(--radius-sm);
      font-size: 13.5px;
      font-weight: 700;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
      display: none;
      align-items: center;
      gap: 10px;
      z-index: 9999;
      animation: fadeIn 0.3s ease;
    }}

    .toast.show {{
      display: flex;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(12px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* LIGHTBOX MODAL */
    .lightbox-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(10px);
      z-index: 10000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .lightbox-modal.active {{
      display: flex;
    }}

    .lightbox-inner {{
      max-width: 460px;
      width: 100%;
      aspect-ratio: 9 / 16;
      background: #000;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-accent);
      position: relative;
    }}

    .lightbox-inner img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .lightbox-close {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      font-size: 20px;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: 0.2s;
    }}

    .lightbox-close:hover {{
      background: var(--rose);
    }}

    /* FOOTER */
    footer {{
      margin-top: 80px;
      border-top: 1px solid var(--border-subtle);
      padding-top: 36px;
      text-align: center;
      color: var(--text-dim);
      font-size: 13px;
      line-height: 1.8;
    }}

    footer b {{
      color: var(--text-muted);
    }}

    /* FLOATING ACTIONS */
    .floating-bar {{
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(12, 18, 30, 0.94);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-full);
      padding: 8px 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      z-index: 800;
    }}

    .floating-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      transition: all 0.2s;
    }}

    .floating-btn:hover {{
      background: var(--cyan);
      color: #060911;
    }}
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header class="top-header">
    <a href="index.html" class="brand-group">
      <span class="brand-badge">FEDU OFFLINE 02</span>
      <div class="brand-title">🏛️ MASTER HUB <span>• 9 KỊCH BẢN THỰC CHIẾN</span></div>
    </a>
    <nav class="header-nav">
      <a href="bai_tap_01_phan_canh_canh_tram.html" class="nav-link highlight">🎯 Bài Tập 01 (Băm Cảnh Trám)</a>
      <a href="kich_ban_01_ngoi_ca_phe_10h_toi.html" class="nav-link">☕ Kịch Bản 01</a>
      <a href="chien_luoc_xay_kenh_toc_10_nam.html" class="nav-link">💈 Salon 10 Năm</a>
      <a href="https://fedu.vn/scene.html" target="_blank" class="nav-link">🌐 Scene Hub</a>
      <button class="nav-link" onclick="window.print()">📄 In / PDF</button>
    </nav>
  </header>

  <div class="container">
    
    <!-- HERO -->
    <section class="hero">
      <div class="hero-badge">⚡ Tổng Kho Kịch Bản & Phân Cảnh Thực Chiến • Lớp Offline Hà Nội</div>
      <h1>Kho Quản Trị & Tổng Hợp Kịch Bản Thực Chiến Lớp Offline</h1>
      <p class="hero-desc">
        Hệ thống <b>9 Kịch Bản Cốt Lõi (Style Trà Đá • Bóc Trần 3 Tầng Sự Thật)</b> & Toàn bộ <b>Bài tập phân cảnh băm nhịp tại lớp</b> của Mentor Nguyễn Đức Việt.<br>
        Bấm vào từng kịch bản để xem toàn bộ <b>18 Beats AI</b>, góc máy, cỡ cảnh, raccord chống jump-cut và bảng thông số kỹ thuật điện ảnh 9:16.
      </p>

      <div class="stats-bar">
        <div class="stat-item">
          <div class="stat-number">15</div>
          <div class="stat-label">Tổng Kịch Bản & Bài Tập</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">09</div>
          <div class="stat-label">Kịch Bản Trà Đá Cốt Lõi</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">65<span>+</span></div>
          <div class="stat-label">Phân Cảnh Băm 3 Beats</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">100<span>%</span></div>
          <div class="stat-label">Storyboard AI & Ảnh Độc Lập</div>
        </div>
      </div>
    </section>

    <!-- METHODOLOGY BOX -->
    <section class="methodology-box">
      <div class="methodology-header" onclick="toggleMethodology()">
        <div class="methodology-title">
          <span>💡 BẢN ĐỒ TƯ DUY 3 TẦNG SỰ THẬT & CÔNG THỨC BĂM CẢNH TRÁM ĐỘC QUYỀN ANH VIỆT</span>
        </div>
        <span class="toggle-icon" id="method-icon">▼ Thu Gọn</span>
      </div>

      <div class="methodology-grid" id="method-grid">
        <div class="method-card m1">
          <div class="method-label">❌ TẦNG 1 • NÓI ĐÃI BÔI (SAFE)</div>
          <div class="method-title">Lý Do Xã Giao Bề Nổi</div>
          <div class="method-desc">Lý do an toàn ngoài miệng, đạo lý văn mẫu ai cũng nói được. Người xem lướt qua sau 3 giây vì quá nhạt và sáo rỗng.</div>
        </div>

        <div class="method-card m2">
          <div class="method-label">⚠️ TẦNG 2 • CẢM GIÁC THẬT (REAL)</div>
          <div class="method-title">Bất An Mắt Thấy Tai Nghe</div>
          <div class="method-desc">Cảm xúc sốt ruột, bất an thực tế: mệt mỏi, thử mãi không xong, mở app chỉ thấy trừ tiền. Người xem bắt đầu thấy quen và gật gù.</div>
        </div>

        <div class="method-card m25">
          <div class="method-label">⚡ TẦNG 2.5 • XUNG ĐỘT THỂ DIỆN (FRICTION)</div>
          <div class="method-title">Cái Cớ & Giằng Xé Nội Tâm</div>
          <div class="method-desc">Đặc sản tư duy anh Việt: Người lớn phải diễn vở kịch gì trước mặt người quen để bảo vệ lòng tự trọng và giấu đi sự bế tắc?</div>
        </div>

        <div class="method-card m3">
          <div class="method-label">✅ TẦNG 3 • SỰ THẬT NGƯỢNG MIỆNG (RAW)</div>
          <div class="method-title">Chạm Đáy Nỗi Đau Sinh Tồn</div>
          <div class="method-desc">Áp lực cơm áo gạo tiền, sợ tụt hậu, sợ dẹp tiệm, sợ bạn bè coi thường. Đánh trúng tim đen để kích hoạt hành động ngay lập tức.</div>
        </div>

        <div class="method-card m4">
          <div class="method-label">🎬 CÔNG THỨC BĂM 3 TRỤC CẢNH TRÁM</div>
          <div class="method-title">Khử Căn Bệnh 'Cảnh Trám Chết Dí'</div>
          <div class="method-desc">1 Hành động gốc $\\rightarrow$ Băm 5 cú máy 2s-2.5s. Đổi đồng thời: <b>Cỡ cảnh</b> (MCU $\\rightarrow$ CU $\\rightarrow$ Macro), <b>Góc máy</b> và <b>Hướng máy</b>.</div>
        </div>
      </div>
    </section>

    <!-- CONTROLS & FILTER BAR -->
    <div class="controls-bar">
      <div class="filter-tabs">
        <button class="filter-tab active" onclick="filterCategory('all', this)">✨ Tất Cả (15)</button>
        <button class="filter-tab" onclick="filterCategory('core', this)">☕ 9 Kịch Bản Cốt Lõi (Trà Đá)</button>
        <button class="filter-tab" onclick="filterCategory('exercise', this)">🎯 Bài Tập Thực Hành Tại Lớp</button>
        <button class="filter-tab" onclick="filterCategory('case', this)">💈 Case Study Học Viên</button>
      </div>

      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm theo từ khóa (cà phê, mặt bằng, tuổi 30, ads, cảnh trám...)" onkeyup="filterSearch()">
      </div>
    </div>

    <!-- SCRIPT CARDS GRID -->
    <div class="scripts-grid" id="scriptsGrid">
"""

# Render each script card
for item in all_items:
    card_id = item["id"]
    code = item["code"]
    title = item["title"]
    short_title = item.get("short_title", title)
    file_href = item["file"]
    category = item["category"]
    cat_badge = item.get("category_badge", category.upper())
    badge_color = item.get("badge_color", "#38bdf8")
    duration = item.get("duration", "30 Giây")
    rhythm = item.get("rhythm", "1.5s / Beat")
    context = item.get("context", "")
    target = item.get("target", "")
    thumb = item.get("thumb", "")
    hook = item.get("hook", "")
    cta = item.get("cta", "")
    t1 = item.get("tier1", "")
    t2 = item.get("tier2", "")
    t25 = item.get("tier25", "")
    t3 = item.get("tier3", "")
    shots = item.get("shots_preview", [])

    # Escape texts
    title_esc = html.escape(title)
    context_esc = html.escape(context)
    target_esc = html.escape(target)
    hook_esc = html.escape(hook)
    t1_esc = html.escape(t1)
    t2_esc = html.escape(t2)
    t25_esc = html.escape(t25)
    t3_esc = html.escape(t3)

    # Build full voice for copy
    copy_text_lines = [f"{code} • {title}"]
    if hook: copy_text_lines.append(f"Hook: {hook}")
    for idx, s in enumerate(shots, 1):
        voice_s = s.get("voice", "")
        if voice_s:
            copy_text_lines.append(f"- Cảnh {idx}: {voice_s}")
    if cta: copy_text_lines.append(f"CTA: {cta}")
    full_copy_text = "\\n".join(copy_text_lines).replace('"', '&quot;').replace("'", "&#39;")

    # Build shots accordion HTML
    shots_html = ""
    for idx, s in enumerate(shots, 1):
        s_badge = html.escape(s.get("badge", f"Cảnh {idx}"))
        s_time = html.escape(s.get("time", ""))
        s_visual = html.escape(s.get("visual", ""))
        s_voice = html.escape(s.get("voice", ""))
        shots_html += f"""
          <div class="scene-item">
            <div class="scene-badge-line">
              <span class="scene-pill">{s_badge}</span>
              <span class="scene-time">{s_time}</span>
            </div>
            <div class="scene-visual">🎥 {s_visual}</div>
            <div class="scene-voice">🎙️ {s_voice}</div>
          </div>
        """

    card_html = f"""
      <article class="script-card" data-category="{category}" data-search="{title.lower()} {context.lower()} {target.lower()} {code.lower()} {hook.lower()}">
        <!-- TOP: THUMB & HEADER -->
        <div class="card-top">
          <div class="card-thumb-wrap" onclick="openLightbox('{thumb}')">
            <img src="{thumb}" alt="{title_esc}" loading="lazy" onerror="this.src='https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/storyboards/tu_dot_tien_den_tu_tin_xuat_hien/assets/frames/scene1_beat1.jpg'">
            <span class="thumb-badge-duration">{duration.split('•')[0].strip()}</span>
          </div>

          <div class="card-info">
            <div class="card-tag-row">
              <span class="code-pill">{code}</span>
              <span class="category-pill" style="background: {badge_color}18; color: {badge_color}; border-color: {badge_color}40;">{cat_badge}</span>
            </div>
            <h3 class="card-title"><a href="{file_href}">{title_esc}</a></h3>
            <div class="meta-line">📍 <b>Bối cảnh:</b> {context_esc}</div>
            <div class="meta-line">🎯 <b>Đối tượng:</b> {target_esc}</div>
          </div>
        </div>

        <!-- 3 TIERS PSYCHOLOGY BOX -->
        <div class="tiers-box">
          <div class="tier-row">
            <span class="tier-tag t1">T1 ĐÃI BÔI</span>
            <span class="tier-content">"{t1_esc}"</span>
          </div>
          <div class="tier-row">
            <span class="tier-tag t2">T2 CẢM GIÁC THẬT</span>
            <span class="tier-content">"{t2_esc}"</span>
          </div>
          <div class="tier-row">
            <span class="tier-tag t25">T2.5 THỂ DIỆN</span>
            <span class="tier-content" style="color: #e9d5ff;">{t25_esc}</span>
          </div>
          <div class="tier-row">
            <span class="tier-tag t3">T3 NGƯỢNG MIỆNG</span>
            <span class="tier-content" style="color: #6ee7b7;">"{t3_esc}"</span>
          </div>
        </div>

        <!-- HOOK QUOTE -->
        <div class="hook-quote">
          <div class="hook-label">🎙️ Hook Mở Màn Đắt Giá:</div>
          <div class="hook-text">"{hook_esc}"</div>
        </div>

        <!-- QUICK 5 SCENES ACCORDION -->
        <div class="accordion-box">
          <div class="accordion-trigger" onclick="toggleAccordion(this)">
            <span>🎞️ Xem Nhanh {len(shots)} Phân Cảnh Băm Nhịp</span>
            <span class="acc-arrow">▼</span>
          </div>
          <div class="accordion-content">
            {shots_html}
          </div>
        </div>

        <!-- CARD FOOTER ACTIONS -->
        <div class="card-footer">
          <a href="{file_href}" class="btn-view-storyboard" target="_blank">
            🎬 Xem Bảng Phân Cảnh 18 Beats AI ➔
          </a>
          <button class="btn-copy-script" onclick="copyScriptText('{full_copy_text}', '{code}')">
            📋 Copy Thoại
          </button>
        </div>
      </article>
    """
    html_output += card_html

html_output += """
    </div><!-- end scripts-grid -->

    <!-- FOOTER -->
    <footer>
      <p><b>FEDU AI STUDIO • KHO QUẢN TRỊ BẢNG PHÂN CẢNH & KỊCH BẢN THỰC CHIẾN 2026</b></p>
      <p>Hệ thống bài giảng và bài tập thực hành độc quyền dành cho học viên lớp Video Thực Chiến Lớp Offline.</p>
      <p>Giảng viên: <b>Nguyễn Đức Việt</b> • Hotline / Zalo: <b>0934.688.632</b> • Website: <a href="https://fedu.vn" target="_blank" style="color: var(--cyan); text-decoration: none;">fedu.vn</a></p>
    </footer>

  </div><!-- end container -->

  <!-- FLOATING QUICK BAR -->
  <div class="floating-bar">
    <a href="#top" class="floating-btn">⬆ Đầu Trang</a>
    <a href="bai_tap_01_phan_canh_canh_tram.html" class="floating-btn">🎯 Bài Tập 01</a>
    <button class="floating-btn" onclick="copyCurrentUrl()">🔗 Copy Link Hub</button>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="toast" id="toastBox">
    <span>✅</span>
    <span id="toastMsg">Đã sao chép kịch bản vào bộ nhớ tạm!</span>
  </div>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox(event)">
    <div class="lightbox-inner">
      <button class="lightbox-close" onclick="closeLightbox(event)">✕</button>
      <img id="lightboxImg" src="" alt="Storyboard Frame Preview">
    </div>
  </div>

  <script>
    // Toggle methodology box
    function toggleMethodology() {
      const grid = document.getElementById('method-grid');
      const icon = document.getElementById('method-icon');
      if (grid.style.display === 'none') {
        grid.style.display = 'grid';
        icon.textContent = '▼ Thu Gọn';
      } else {
        grid.style.display = 'none';
        icon.textContent = '▶ Mở Rộng';
      }
    }

    // Toggle card accordion
    function toggleAccordion(btn) {
      const content = btn.nextElementSibling;
      const arrow = btn.querySelector('.acc-arrow');
      content.classList.toggle('open');
      if (content.classList.contains('open')) {
        arrow.textContent = '▲';
      } else {
        arrow.textContent = '▼';
      }
    }

    // Filter by Category
    function filterCategory(cat, tabElem) {
      document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
      tabElem.classList.add('active');

      const cards = document.querySelectorAll('.script-card');
      cards.forEach(card => {
        if (cat === 'all' || card.dataset.category === cat) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
      filterSearch(); // keep search applied
    }

    // Live search filter
    function filterSearch() {
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const activeTab = document.querySelector('.filter-tab.active');
      const activeCat = activeTab ? activeTab.getAttribute('onclick').match(/'([^']+)'/)[1] : 'all';

      const cards = document.querySelectorAll('.script-card');
      cards.forEach(card => {
        const cardCat = card.dataset.category;
        const searchData = card.dataset.search || '';
        const matchCat = (activeCat === 'all' || cardCat === activeCat);
        const matchQuery = !query || searchData.includes(query);

        if (matchCat && matchQuery) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }

    // Copy script
    function copyScriptText(text, code) {
      const decoded = text.replace(/\\n/g, '\\n');
      navigator.clipboard.writeText(decoded).then(() => {
        showToast('Đã sao chép kịch bản ' + code + ' vào bộ nhớ tạm!');
      }).catch(() => {
        // fallback
        const ta = document.createElement('textarea');
        ta.value = decoded;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast('Đã sao chép kịch bản ' + code + ' vào bộ nhớ tạm!');
      });
    }

    // Copy current URL
    function copyCurrentUrl() {
      navigator.clipboard.writeText(window.location.href).then(() => {
        showToast('Đã sao chép đường link Master Hub!');
      });
    }

    // Show Toast
    function showToast(msg) {
      const t = document.getElementById('toastBox');
      const m = document.getElementById('toastMsg');
      m.textContent = msg;
      t.classList.add('show');
      setTimeout(() => {
        t.classList.remove('show');
      }, 2500);
    }

    // Lightbox
    function openLightbox(src) {
      const m = document.getElementById('lightboxModal');
      const img = document.getElementById('lightboxImg');
      img.src = src;
      m.classList.add('active');
    }

    function closeLightbox(e) {
      if (e.target.id === 'lightboxModal' || e.target.classList.contains('lightbox-close')) {
        document.getElementById('lightboxModal').classList.remove('active');
      }
    }
  </script>
</body>
</html>
"""

# Write to 9_kich_ban_thuc_chien.html in offline02
dest_9kb = "/Users/vietmac/Documents/CODE/offline02/9_kich_ban_thuc_chien.html"
with open(dest_9kb, "w", encoding="utf-8") as f:
    f.write(html_output)
print(f"Generated {dest_9kb} successfully ({len(html_output)} bytes)")

# Also write/sync to index.html in offline02
dest_index = "/Users/vietmac/Documents/CODE/offline02/index.html"
with open(dest_index, "w", encoding="utf-8") as f:
    f.write(html_output)
print(f"Generated {dest_index} successfully ({len(html_output)} bytes)")

# Also copy to workspace facebook, skool
dest_workspace_9kb = "/Users/vietmac/Documents/CODE/facebook, skool/9_kich_ban_thuc_chien.html"
with open(dest_workspace_9kb, "w", encoding="utf-8") as f:
    f.write(html_output)
print(f"Synced {dest_workspace_9kb}")

dest_workspace_index = "/Users/vietmac/Documents/CODE/facebook, skool/index.html"
with open(dest_workspace_index, "w", encoding="utf-8") as f:
    f.write(html_output)
print(f"Synced {dest_workspace_index}")
