# -*- coding: utf-8 -*-
"""
Generate index.html - Master Portal for FEDU Offline Course
"""
import os

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hệ Thống Thực Chiến Offline • 2 Bài Học Cốt Lõi | FEDU AI Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-main: #060911;
      --bg-surface: #0c121e;
      --bg-card: #111a2b;
      --bg-card-hover: #162238;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.35);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --cyan: #38bdf8;
      --amber: #f59e0b;
      --emerald: #10b981;
      --purple: #a855f7;
      --rose: #f43f5e;
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --shadow-card: 0 16px 40px rgba(0, 0, 0, 0.6);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-main);
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.12) 0%, transparent 60%),
        radial-gradient(circle at 15% 45%, rgba(168, 85, 247, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 85% 60%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
      background-attachment: fixed;
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 120px;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* TOP STICKY BAR */
    .top-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(6, 9, 17, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 14px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }

    .brand-badge {
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    }

    .header-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .nav-pill {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 700;
      padding: 7px 16px;
      border-radius: 9999px;
      text-decoration: none;
      transition: all 0.2s;
    }

    .nav-pill:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }

    .nav-pill.active {
      background: var(--cyan);
      color: #000;
      font-weight: 800;
      border-color: var(--cyan);
    }

    /* HERO PORTAL */
    .portal-hero {
      padding: 70px 0 50px;
      text-align: center;
    }

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.35);
      padding: 7px 20px;
      border-radius: 9999px;
      font-size: 12.5px;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 1.2px;
      margin-bottom: 20px;
    }

    .portal-title {
      font-size: 42px;
      font-weight: 900;
      line-height: 1.2;
      margin-bottom: 20px;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 45%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    @media (max-width: 768px) {
      .portal-title { font-size: 30px; }
    }

    .portal-subtitle {
      font-size: 17px;
      color: var(--text-muted);
      max-width: 860px;
      margin: 0 auto 36px;
      line-height: 1.65;
    }

    /* 2 BIG CARDS GRID */
    .master-pillars {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      margin-bottom: 60px;
    }

    @media (max-width: 960px) {
      .master-pillars {
        grid-template-columns: 1fr;
      }
    }

    .pillar-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-card);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.3s ease, border-color 0.3s ease;
      position: relative;
    }

    .pillar-card:hover {
      transform: translateY(-5px);
    }

    .pillar-card.p1:hover { border-color: rgba(56, 189, 248, 0.5); }
    .pillar-card.p2:hover { border-color: rgba(16, 185, 129, 0.5); }

    .pillar-header {
      padding: 28px 30px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .pillar-badge {
      display: inline-block;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }

    .p1 .pillar-badge {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid var(--cyan);
      color: var(--cyan);
    }

    .p2 .pillar-badge {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--emerald);
      color: #34d399;
    }

    .pillar-title {
      font-size: 24px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 10px;
      line-height: 1.3;
    }

    .pillar-desc {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.55;
    }

    /* AVATAR STRIP PREVIEW */
    .pillar-avatars-strip {
      padding: 20px 30px;
      background: rgba(0, 0, 0, 0.25);
      display: flex;
      gap: 10px;
      overflow-x: auto;
      scrollbar-width: thin;
    }

    .avatar-preview-item {
      flex: 0 0 76px;
      aspect-ratio: 9/16;
      border-radius: var(--radius-sm);
      overflow: hidden;
      background: #020408;
      border: 1px solid rgba(255, 255, 255, 0.12);
      position: relative;
    }

    .avatar-preview-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .avatar-mini-tag {
      position: absolute;
      bottom: 2px;
      left: 2px;
      right: 2px;
      background: rgba(0, 0, 0, 0.75);
      font-size: 8.5px;
      font-weight: 700;
      color: #fff;
      text-align: center;
      padding: 2px 0;
      border-radius: 2px;
    }

    .pillar-body {
      padding: 24px 30px;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .feature-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 13.5px;
      color: #cbd5e1;
    }

    .feature-list li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      line-height: 1.45;
    }

    .feature-list li span.bullet {
      color: var(--cyan);
      font-weight: 800;
      flex-shrink: 0;
    }

    .p2 .feature-list li span.bullet {
      color: #34d399;
    }

    .pillar-footer {
      padding: 20px 30px 28px;
      margin-top: auto;
    }

    .btn-pillar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 22px;
      border-radius: var(--radius-md);
      font-size: 14.5px;
      font-weight: 800;
      text-decoration: none;
      transition: all 0.25s ease;
    }

    .p1 .btn-pillar {
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff;
      box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35);
    }

    .p1 .btn-pillar:hover {
      box-shadow: 0 12px 28px rgba(37, 99, 235, 0.55);
      transform: translateY(-2px);
    }

    .p2 .btn-pillar {
      background: linear-gradient(135deg, #059669, #10b981);
      color: #fff;
      box-shadow: 0 8px 20px rgba(16, 185, 129, 0.35);
    }

    .p2 .btn-pillar:hover {
      box-shadow: 0 12px 28px rgba(16, 185, 129, 0.55);
      transform: translateY(-2px);
    }

    /* METHODOLOGY SECTION */
    .method-section {
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 40px;
      margin-bottom: 60px;
    }

    .method-title {
      font-size: 22px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 8px;
      text-align: center;
    }

    .method-sub {
      text-align: center;
      color: var(--text-muted);
      font-size: 14.5px;
      max-width: 750px;
      margin: 0 auto 32px;
    }

    .method-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }

    @media (max-width: 860px) {
      .method-grid {
        grid-template-columns: 1fr;
      }
    }

    .method-card {
      background: var(--bg-card);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: var(--radius-md);
      padding: 24px;
    }

    .method-card h3 {
      font-size: 16px;
      font-weight: 800;
      color: var(--cyan);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .method-card p {
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.6;
    }

    /* DIRECTORY SECTION */
    .directory-section {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 36px;
    }

    .dir-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 36px;
    }

    @media (max-width: 860px) {
      .dir-grid { grid-template-columns: 1fr; }
    }

    .dir-col h3 {
      font-size: 16px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .dir-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .dir-item a {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.04);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      color: #cbd5e1;
      text-decoration: none;
      font-size: 13px;
      transition: all 0.2s;
    }

    .dir-item a:hover {
      background: rgba(56, 189, 248, 0.1);
      border-color: rgba(56, 189, 248, 0.3);
      color: #fff;
      transform: translateX(4px);
    }

    .dir-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 800;
      color: var(--cyan);
    }
  </style>
</head>
<body>

  <!-- TOP STICKY BAR -->
  <header class="top-header">
    <div class="brand-group">
      <span class="brand-badge">FEDU AI STUDIO</span>
      <span class="header-title">Hệ Thống Thực Chiến Offline • 2 Bài Học Cốt Lõi</span>
    </div>
    <div class="header-controls">
      <a href="index.html" class="nav-pill active">🏛️ Hub Tổng</a>
      <a href="9voiceover.html" class="nav-pill">🎙️ Bài 1: 9 Voiceover</a>
      <a href="12canhtram.html" class="nav-pill">📹 Bài 2: 12 Cảnh Trám</a>
    </div>
  </header>

  <div class="container">

    <!-- HERO PORTAL -->
    <div class="portal-hero">
      <div class="hero-eyebrow">
        <span>⚡ KHÓA HỌC OFFLINE 2 NGÀY • THỰC CHIẾN TỪNG KHUNG HÌNH</span>
      </div>
      <h1 class="portal-title">Kịch Bản Phân Cảnh & Thần Thái Diễn Thực Chiến</h1>
      <p class="portal-subtitle">
        Hai trụ cột then chốt giúp người làm nghề vượt qua rào cản sợ máy quay: <b>Bài 1</b> rèn luyện 9 phong cách biểu đạt thoại không văn mẫu, <b>Bài 2</b> băm nhỏ 1 hành động thành 5 cú máy điện ảnh đổi 3 trục.
      </p>
    </div>

    <!-- 2 MASTER PILLARS -->
    <div class="master-pillars">

      <!-- BÀI 1 -->
      <div class="pillar-card p1">
        <div class="pillar-header">
          <span class="pillar-badge">BÀI HỌC 01 • PHÂN CẢNH & VOICEOVER</span>
          <h2 class="pillar-title">1 Kịch Bản • 9 Phong Cách Biểu Đạt</h2>
          <p class="pillar-desc">
            Biến cùng một câu chuyện bế tắc trong kinh doanh thành 9 định vị hoàn toàn khác nhau bằng cách đổi góc nhìn tâm lý, 9 bộ phục trang và thần thái thoại mộc mạc.
          </p>
        </div>

        <!-- STRIP AVATAR 9 PHONG CÁCH -->
        <div class="pillar-avatars-strip">
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk01_cafe_dem_charcoalknit.jpg" alt="PK01" loading="lazy">
            <span class="avatar-mini-tag">PK 01</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk02_chu_shop_oxfordstripes.jpg" alt="PK02" loading="lazy">
            <span class="avatar-mini-tag">PK 02</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk03_tuoi_30_blackpolo.jpg" alt="PK03" loading="lazy">
            <span class="avatar-mini-tag">PK 03</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk04_tien_ads_navyblazer.jpg" alt="PK04" loading="lazy">
            <span class="avatar-mini-tag">PK 04</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk05_khach_quen_beigelinen.jpg" alt="PK05" loading="lazy">
            <span class="avatar-mini-tag">PK 05</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk06_gioi_nghe_workwear.jpg" alt="PK06" loading="lazy">
            <span class="avatar-mini-tag">PK 06</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk07_tong_kho_blacktee.jpg" alt="PK07" loading="lazy">
            <span class="avatar-mini-tag">PK 07</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk08_so_khong_olivehoodie.jpg" alt="PK08" loading="lazy">
            <span class="avatar-mini-tag">PK 08</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/voiceover_9phongcach/pk09_hang_ky_mandarin.jpg" alt="PK09" loading="lazy">
            <span class="avatar-mini-tag">PK 09</span>
          </div>
        </div>

        <div class="pillar-body">
          <ul class="feature-list">
            <li><span class="bullet">✓</span> <b>9 Phục trang độc bản:</b> Áo len than, Oxford sọc, Polo đen, Navy blazer, Linen be, Workwear thợ, Black tee kho, Hoodie olive, Sơ mi cổ tàu.</li>
            <li><span class="bullet">✓</span> <b>Bóc tách 3 điểm nâng cấp:</b> Chỉ ra lỗi góc máy chết, đạo cụ giả tạo, thần thái gượng gạo và nâng cấp để "nhìn là quay được theo luôn".</li>
            <li><span class="bullet">✓</span> <b>Chuẩn hóa Face DNA 99%:</b> Tỉ lệ giống khuôn mặt thật anh Việt tối đa qua kỹ thuật dual-anchor và form tóc ngắn 2cm tự nhiên.</li>
            <li><span class="bullet">✓</span> <b>45 Cú máy phân cảnh băm nhịp:</b> Đồng bộ chi tiết A-roll và B-roll theo từng giây.</li>
          </ul>
        </div>

        <div class="pillar-footer">
          <a href="9voiceover.html" class="btn-pillar">
            <span>Khám Phá Bài 1 • 9 Voiceover</span>
            <span>→</span>
          </a>
        </div>
      </div>

      <!-- BÀI 2 -->
      <div class="pillar-card p2">
        <div class="pillar-header">
          <span class="pillar-badge">BÀI HỌC 02 • B-ROLL & KỸ THUẬT QUAY</span>
          <h2 class="pillar-title">B-Roll 12 Bài Tập Băm Cảnh Trám</h2>
          <p class="pillar-desc">
            Kho bài tập thực chiến tại bàn học: Băm một hành động gốc đời thường thành 5 cú máy điện ảnh độc lập đổi đồng thời cả 3 trục (Cỡ cảnh - Góc máy - Hướng máy).
          </p>
        </div>

        <!-- STRIP AVATAR 12 BÀI TẬP -->
        <div class="pillar-avatars-strip">
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt1_smartsuit.jpg" alt="BT01" loading="lazy">
            <span class="avatar-mini-tag">BT 01</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt2_tshirt.jpg" alt="BT02" loading="lazy">
            <span class="avatar-mini-tag">BT 02</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt3_sporty.jpg" alt="BT03" loading="lazy">
            <span class="avatar-mini-tag">BT 03</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt4_smartcasual.jpg" alt="BT04" loading="lazy">
            <span class="avatar-mini-tag">BT 04</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt5_lightknit.jpg" alt="BT05" loading="lazy">
            <span class="avatar-mini-tag">BT 05</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt6_blackpolo.jpg" alt="BT06" loading="lazy">
            <span class="avatar-mini-tag">BT 06</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt7_hoodie.jpg" alt="BT07" loading="lazy">
            <span class="avatar-mini-tag">BT 07</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt8_bomber.jpg" alt="BT08" loading="lazy">
            <span class="avatar-mini-tag">BT 08</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt9_denim.jpg" alt="BT09" loading="lazy">
            <span class="avatar-mini-tag">BT 09</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt10_flannel.jpg" alt="BT10" loading="lazy">
            <span class="avatar-mini-tag">BT 10</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt11_vest.jpg" alt="BT11" loading="lazy">
            <span class="avatar-mini-tag">BT 11</span>
          </div>
          <div class="avatar-preview-item">
            <img src="assets/marketing_baitap/viet_bt12_windbreaker.jpg" alt="BT12" loading="lazy">
            <span class="avatar-mini-tag">BT 12</span>
          </div>
        </div>

        <div class="pillar-body">
          <ul class="feature-list">
            <li><span class="bullet">✓</span> <b>60 Cú máy b-roll điện ảnh:</b> Đổi linh hoạt giữa Macro ECU (bàn phím, bút viết, màn hình) sang CU, MCU, Low Angle sát mặt bàn.</li>
            <li><span class="bullet">✓</span> <b>Khả năng tái sử dụng cao:</b> Mỗi shot được thiết kế mang tính ẩn dụ thị giác phổ quát (cạn ý tưởng, chờ đợi, dấn thân, vỡ òa).</li>
            <li><span class="bullet">✓</span> <b>12 Trang con Zebra Apple:</b> Trình bày mượt mà 60-120fps theo hệ thống thiết kế cao cấp 30ngayviral.fedu.vn.</li>
            <li><span class="bullet">✓</span> <b>Lọc 100% văn mẫu:</b> Giọng điệu chân thật, dí dỏm, quan sát đời thường, kết bài có nụ cười tự trào mộc mạc.</li>
          </ul>
        </div>

        <div class="pillar-footer">
          <a href="12canhtram.html" class="btn-pillar">
            <span>Khám Phá Bài 2 • 12 Cảnh Trám</span>
            <span>→</span>
          </a>
        </div>
      </div>

    </div>

    <!-- METHODOLOGY EXPLANATION -->
    <div class="method-section">
      <h2 class="method-title">Phương Pháp Đào Tạo • Đi Từ Tâm Lý Đến Ống Kính</h2>
      <p class="method-sub">Video ngắn giữ chân người xem không phải nhờ kỹ xảo hào nhoáng, mà nhờ sự chân thật và nhịp cắt thị giác chuẩn xác.</p>

      <div class="method-grid">
        <div class="method-card">
          <h3>📐 Đổi Đồng Thời 3 Trục</h3>
          <p>Tuyệt đối không giữ nguyên cỡ cảnh hay góc máy quá 2.5 giây. Mỗi lần chuyển shot phải thay đổi cả 3 yếu tố: Cỡ cảnh (Macro sang CU), Góc máy (Ngang sang Thấp), Hướng máy (Trực diện sang Nghiêng 45°).</p>
        </div>
        <div class="method-card">
          <h3>🎙️ Văn Phong Mộc Mạc</h3>
          <p>Lọc sạch các mỹ từ AI sáo rỗng. Thoại phải nói như đang ngồi tâm sự với người bạn tại quán nước: Xưng anh em / mình, dám nhận cái sai, dám cười trừ trước những vấp váp thực tế.</p>
        </div>
        <div class="method-card">
          <h3>✨ Tối Ưu Huấn Luyện AI DNA</h3>
          <p>Tận dụng quy trình Dual-Anchor Conditioning: Kết hợp ảnh thật nguyên bản và ảnh mẫu đã khóa form tóc ngắn 2cm tự nhiên để đảm bảo tính nhất quán 99% trên mọi bối cảnh và trang phục.</p>
        </div>
      </div>
    </div>

    <!-- QUICK JUMP DIRECTORY -->
    <div class="directory-section">
      <div class="dir-grid">
        
        <div class="dir-col">
          <h3>
            <span>🎙️ 9 Kịch Bản Voiceover (Bài 1)</span>
            <a href="9voiceover.html" style="color:var(--cyan); font-size:12px; text-decoration:none;">Xem Tất Cả →</a>
          </h3>
          <ul class="dir-list">
            <li class="dir-item"><a href="kich_ban_01_ngoi_ca_phe_10h_toi.html"><span class="dir-code">PK 01</span> Ngồi Cà Phê 10h Tối Không Dám Về Nhà <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html"><span class="dir-code">PK 02</span> Tiền Mặt Bằng & Cửa Hàng Vắng Khách <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_03_chung_lai_sau_tuoi_30.html"><span class="dir-code">PK 03</span> Chững Lại Sau Tuổi 30 & Nhìn Đối Thủ <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_04_tien_quang_cao_an_het_tien_lai.html"><span class="dir-code">PK 04</span> Tiền Quảng Cáo Ăn Hết Tiền Lãi <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_05_het_khach_tu_moi_quan_he_quen.html"><span class="dir-code">PK 05</span> Hết Khách Từ Mối Quan Hệ Quen <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html"><span class="dir-code">PK 06</span> Tay Nghề Tốt Nhưng Vẫn Vắng Khách <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html"><span class="dir-code">PK 07</span> Bị Cạnh Tranh Bởi Tổng Kho & Giá Gốc <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_08_bat_dau_lai_tu_con_so_0.html"><span class="dir-code">PK 08</span> Bắt Đầu Lại Từ Con Số 0 <span>→</span></a></li>
            <li class="dir-item"><a href="kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html"><span class="dir-code">PK 09</span> Hàng Làm Kỹ Nhưng Bị So Sánh Giá <span>→</span></a></li>
          </ul>
        </div>

        <div class="dir-col">
          <h3>
            <span>📹 12 Bài Tập B-Roll Cảnh Trám (Bài 2)</span>
            <a href="12canhtram.html" style="color:#34d399; font-size:12px; text-decoration:none;">Xem Tất Cả →</a>
          </h3>
          <ul class="dir-list">
            <li class="dir-item"><a href="baitap01_laptop_ads.html"><span class="dir-code" style="color:#34d399;">BT 01</span> Soi chỉ số Ads & Cày trên laptop <span>→</span></a></li>
            <li class="dir-item"><a href="baitap02_sotay_kichban.html"><span class="dir-code" style="color:#34d399;">BT 02</span> Cuốn sổ tay & Kịch bản gạch xóa <span>→</span></a></li>
            <li class="dir-item"><a href="baitap03_test_goc_quay.html"><span class="dir-code" style="color:#34d399;">BT 03</span> Cầm điện thoại test góc quay <span>→</span></a></li>
            <li class="dir-item"><a href="baitap04_slide_giatminh.html"><span class="dir-code" style="color:#34d399;">BT 04</span> Ngẩng nhìn slide & Giật mình <span>→</span></a></li>
            <li class="dir-item"><a href="baitap05_cocnuoc_langdong.html"><span class="dir-code" style="color:#34d399;">BT 05</span> Nhấp ngụm nước ấm & Lắng đọng <span>→</span></a></li>
            <li class="dir-item"><a href="baitap06_do_du_nut_dang.html"><span class="dir-code" style="color:#34d399;">BT 06</span> Ngón tay ngập ngừng nút Đăng <span>→</span></a></li>
            <li class="dir-item"><a href="baitap07_hut_hang_0view.html"><span class="dir-code" style="color:#34d399;">BT 07</span> Mở máy kiểm tra thấy 0 view <span>→</span></a></li>
            <li class="dir-item"><a href="baitap08_qua_ngot_tingting.html"><span class="dir-code" style="color:#34d399;">BT 08</span> Ting ting thông báo tin nhắn <span>→</span></a></li>
            <li class="dir-item"><a href="baitap09_timeline_capcut.html"><span class="dir-code" style="color:#34d399;">BT 09</span> Đeo tai nghe soi timeline CapCut <span>→</span></a></li>
            <li class="dir-item"><a href="baitap10_tranh_luan_nhom.html"><span class="dir-code" style="color:#34d399;">BT 10</span> Chụm đầu tranh luận sơ đồ nhóm <span>→</span></a></li>
            <li class="dir-item"><a href="baitap11_tap_noi_truoc_lop.html"><span class="dir-code" style="color:#34d399;">BT 11</span> Đứng trước lớp tập nói đúp 1 <span>→</span></a></li>
            <li class="dir-item"><a href="baitap12_thu_don_buoc_di.html"><span class="dir-code" style="color:#34d399;">BT 12</span> Gập laptop, đeo balo sải bước <span>→</span></a></li>
          </ul>
        </div>

      </div>
    </div>

  </div>

</body>
</html>"""

with open("/Users/vietmac/Documents/CODE/offline02/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated /Users/vietmac/Documents/CODE/offline02/index.html successfully!")
