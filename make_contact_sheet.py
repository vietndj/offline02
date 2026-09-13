import os
from PIL import Image, ImageDraw, ImageFont

frames_dir = "/Users/vietmac/Documents/CODE/offline02/assets/frames_kb02"
output_path = "/Users/vietmac/Documents/CODE/offline02/assets/kb02_15_beats_contact_sheet.jpg"

beats = [
    # Scene 1
    ("scene1_beat1.jpg", "1.1 ĐẦU CẢNH: TRUNG TOÀN", "Ngang mắt 0° • Phòng Greenhub"),
    ("scene1_beat2.jpg", "1.2 CAO TRÀO: CẬN CẢNH", "Lệch trục 45° • Góc cao 45° lau kệ"),
    ("scene1_beat3.jpg", "1.3 MỒI CHUYỂN: TRUNG CẬN", "Lệch trục 30° • Góc nghiêng 3/4 nhìn xa"),
    # Scene 2
    ("scene2_beat1.jpg", "2.1 ĐẦU CẢNH: QUA VAI (OTS)", "Lệch trục 45° • Góc cao 25° sau vai"),
    ("scene2_beat2.jpg", "2.2 CAO TRÀO: CỰC CẬN (MACRO)", "Lệch trục 45° • Top-down 70° nợ 20tr"),
    ("scene2_beat3.jpg", "2.3 MỒI CHUYỂN: TRUNG CẢNH", "Lệch trục 55° • Góc thấp 15° chống cằm"),
    # Scene 3
    ("scene3_beat1.jpg", "3.1 ĐẦU CẢNH: TOÀN CẢNH", "Lệch trục 45° • Bước ra sảnh vách kính"),
    ("scene3_beat2.jpg", "3.2 CAO TRÀO: CẬN CẢNH", "Lệch trục 45° • Góc nghiêng 45° chiêm nghiệm"),
    ("scene3_beat3.jpg", "3.3 MỒI CHUYỂN: TRUNG CẬN", "Lệch trục 45° • Xoay người 180° kiên định"),
    # Scene 4
    ("scene4_beat1.jpg", "4.1 ĐẦU CẢNH: TRUNG TOÀN", "Lệch trục 45° • Góc thấp 15° với lấy máy"),
    ("scene4_beat2.jpg", "4.2 CAO TRÀO: CẬN A-ROLL", "Lệch trục 45° • Ngang mắt trực diện"),
    ("scene4_beat3.jpg", "4.3 MỒI CHUYỂN: QUA VAI (OTS)", "Lệch trục 30° • Màn hình 9:16 sắp bấm REC"),
    # Scene 5
    ("scene5_beat1.jpg", "5.1 ĐẦU CẢNH: CẬN SELFIE POV", "Lệch trục 45° • Góc cao 15° mỉm cười"),
    ("scene5_beat2.jpg", "5.2 CAO TRÀO: TRUNG TOÀN ĐỘNG", "Lệch trục 45° • Nghiêng 30° bước đi xưởng gỗ"),
    ("scene5_beat3.jpg", "5.3 MỒI CHUYỂN: CẬN 3/4", "Lệch trục 45° • Góc nghiêng 45° nụ cười đĩnh đạc")
]

# Grid parameters
cols = 3
rows = 5
thumb_w = 400
thumb_h = int(thumb_w * 16 / 9) # 711 px
header_h = 100
label_h = 55
margin = 16
title_bar_h = 80

total_w = cols * thumb_w + (cols + 1) * margin
total_h = title_bar_h + rows * (thumb_h + label_h) + (rows + 1) * margin

canvas = Image.new("RGB", (total_w, total_h), "#0f172a") # Slate 900 background
draw = ImageDraw.Draw(canvas)

# Header
draw.rectangle([(0, 0), (total_w, title_bar_h)], fill="#1e293b")
draw.text((margin + 10, 18), "BÀI TẬP 02: TIỀN MẶT BẰNG & CỬA HÀNG VẮNG KHÁCH", fill="#f8fafc")
draw.text((margin + 10, 48), "NGHIỆM THU 15 PHÂN CẢNH CINEMATIC • FACE DNA ANH VIỆT • BỐI CẢNH GREENHUB • QUY TẮC 30 ĐỘ & MATCH-CUT", fill="#38bdf8")

for idx, (fname, title, desc) in enumerate(beats):
    c = idx % cols
    r = idx // cols
    
    x = margin + c * (thumb_w + margin)
    y = title_bar_h + margin + r * (thumb_h + label_h + margin)
    
    img_path = os.path.join(frames_dir, fname)
    if os.path.exists(img_path):
        img = Image.open(img_path).convert("RGB")
        img = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        canvas.paste(img, (x, y))
        
        # Border
        draw.rectangle([(x, y), (x + thumb_w, y + thumb_h)], outline="#334155", width=2)
        
        # Label card below
        lbl_y = y + thumb_h
        draw.rectangle([(x, lbl_y), (x + thumb_w, lbl_y + label_h)], fill="#1e293b")
        draw.text((x + 8, lbl_y + 8), title, fill="#f1f5f9")
        draw.text((x + 8, lbl_y + 30), desc, fill="#94a3b8")

canvas.save(output_path, "JPEG", quality=92)
print(f"✅ Created contact sheet: {output_path} ({total_w}x{total_h})")
