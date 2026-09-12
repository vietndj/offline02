# -*- coding: utf-8 -*-
"""
BUILD ALL 8 LESSONS + MASTER HUB FOR FEDU OFFLINE
Author: Antigravity (Google DeepMind)
"""

import os
import json
import re

OFFLINE_DIR = "/Users/vietmac/Documents/CODE/offline02"
GITHUB_DIR = "/Users/vietmac/Documents/CODE/vietndj.github.io"
COURSE_DIR = "/Users/vietmac/Documents/CODE/course"
GITHUB_COURSE_DIR = "/Users/vietmac/Documents/CODE/vietndj.github.io/course"

SHORT_NAMES = {
    "kich_ban_01_ngoi_ca_phe_10h_toi.html": "bai-01-ca-phe-dem.html",
    "kich_ban_02_tien_mat_bang_va_cua_hang_vang_khach.html": "bai-02-tien-mat-bang.html",
    "kich_ban_03_chung_lai_sau_tuoi_30.html": "bai-03-chung-tuoi-30.html",
    "kich_ban_04_tien_quang_cao_an_het_tien_lai.html": "bai-04-dot-tien-ads.html",
    "kich_ban_05_het_khach_tu_moi_quan_he_quen.html": "bai-05-het-khach-quen.html",
    "kich_ban_06_tay_nghe_tot_nhung_van_vang_khach.html": "bai-06-tay-nghe-gioi.html",
    "kich_ban_07_bi_canh_tranh_boi_tong_kho_va_gia_goc.html": "bai-07-tong-kho-pha-gia.html",
    "kich_ban_08_bat_dau_lai_tu_con_so_0.html": "bai-08-lam-lai-tu-dau.html",
    "kich_ban_09_hang_lam_ky_nhung_bi_so_sanh_gia.html": "bai-09-lam-ky-che-dat.html",
}

# Load templates
with open(os.path.join(OFFLINE_DIR, "template_head.html"), "r", encoding="utf-8") as f:
    TEMPLATE_HEAD = f.read()

with open(os.path.join(OFFLINE_DIR, "template_tail.html"), "r", encoding="utf-8") as f:
    TEMPLATE_TAIL = f.read()

# Load lessons from python module and json
from build_lessons_data import LESSONS
with open(os.path.join(OFFLINE_DIR, "lessons_extra.json"), "r", encoding="utf-8") as f:
    extra_lessons = json.load(f)

ALL_LESSONS = LESSONS + extra_lessons
print(f"Total lessons loaded: {len(ALL_LESSONS)}")

LESSON_META = {
    "1": {
        "context": "Quán cà phê sau 21h - 22h / Phòng học Greenhub",
        "duration": "20 - 22 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: NGỒI CAFE",
    },
    "2": {
        "context": "Cửa hàng vắng khách / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: QUAY CỬA HÀNG",
    },
    "3": {
        "context": "Lướt điện thoại / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: LƯỚT VIDEO ĐỐI THỦ",
    },
    "4": {
        "context": "Màn hình bật app Ads / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: XEM BÁO CÁO ADS",
    },
    "5": {
        "context": "Lướt danh bạ điện thoại / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: LƯỚT DANH BẠ",
    },
    "6": {
        "context": "Bàn đồ nghề nắn nót / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: LAU DỌN ĐỒ NGHỀ",
    },
    "7": {
        "context": "Kệ hàng hóa / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: XẾP HÀNG LÊN KỆ",
    },
    "8": {
        "context": "Góc yên tĩnh bấm máy / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: VIẾT SỔ TAY",
    },
    "9": {
        "context": "Bàn đóng gói tỉ mỉ / Phòng học Greenhub",
        "duration": "20 - 25 Giây",
        "goal": "Có người xem & Có kết nối",
        "title_formatted": "BÀI TẬP VIẾT KỊCH BẢN VÀ QUAY<br>VỚI HOẠT ĐỘNG ĐỜI THƯỜNG: ĐÓNG GÓI HÀNG",
    },
}

def generate_lesson_html(data):
    lesson_id_int = int(data.get("id", "1"))
    meta = LESSON_META.get(str(lesson_id_int), {})
    meta_context = meta.get("context", "Phòng học Greenhub")
    meta_duration = meta.get("duration", "20 - 25 Giây")
    meta_goal = meta.get("goal", "Có người xem & Có kết nối")
    title_formatted = meta.get("title_formatted", data["title_short"])
    badge_label = f"VIDEO OFFLINE • BÀI TẬP TẠI LỚP #{lesson_id_int:02d}"
    clean_page_title = data['page_title'].replace('FEDU', 'VIDEO').replace('fedu', 'video')

    # Construct scenes HTML
    scenes_html = ""
    for sc in data["scenes"]:
        beats_html = ""
        for b_name, b_angle, b_act, b_img, b_note in sc["beats"]:
            badge_class = "badge-in" if "Đầu" in b_name else ("badge-main" if "Cao" in b_name else "badge-out")
            beats_html += f"""
        <!-- Beat -->
        <div class="beat-card-apple">
          <div class="beat-media-container" onclick="openLightbox('{b_img}', '{sc['title']} • {b_name}', '{b_act}', '{b_angle}')">
            <span class="beat-badge-phase {badge_class}">{b_name.split()[1] if len(b_name.split()) > 1 else b_name}</span>
            <span class="beat-badge-angle">📐 {b_angle}</span>
            <img src="{b_img}" alt="{b_name}" loading="lazy">
          </div>
          <div class="beat-body-details">
            <div class="beat-title-row">
              <span class="beat-name">{b_name}</span>
              <span class="beat-angle-desc">{b_angle}</span>
            </div>
            <table class="beat-specs-table">
              <tr><td class="col-label">Góc máy:</td><td class="col-val">{b_angle}</td></tr>
              <tr><td class="col-label">Hành động:</td><td class="col-val">{b_act}</td></tr>
            </table>
            <div class="beat-director-note">💡 <b>Ghi chú đạo diễn:</b> {b_note}</div>
          </div>
        </div>"""
        
        sec_bg = "cl-zebra--tint" if int(sc["id"]) % 2 == 1 else "cl-zebra--light"
        next_target = f"sec-scene-{int(sc['id'])+1}" if int(sc['id']) < 5 else "sec-wisdom"
        next_label = f"TIẾP TỤC SANG CẢNH 0{int(sc['id'])+1} →" if int(sc['id']) < 5 else "XEM ĐÚC KẾT BÀI HỌC CUỐI CÙNG →"
        hint_label = f"Cảnh 0{int(sc['id'])+1}" if int(sc['id']) < 5 else "Đúc kết bài học"

        scenes_html += f"""
  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI: PHÂN CẢNH CẢNH {sc['id']} (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section {sec_bg}" id="sec-scene-{sc['id']}">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge">CẢNH 0{sc['id']} / 05 • THỜI LƯỢNG {sc['dur']}</div>
      <h2 class="title-short">{sc['title'].upper()}</h2>

      <div class="scene-voice-banner">
        <div class="scene-voice-icon">🎙️</div>
        <div class="scene-voice-text">"{sc['voice']}"</div>
      </div>

      <div class="beats-3-grid">
        {beats_html}
      </div>
    </div>
    <a href="#{next_target}" class="cl-scroll-hint">
      <span>Cuộn sang {hint_label}</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>
"""

    # Construct script scenes HTML (Matching bai-01-ca-phe-dem.html .final-script-card)
    script_rows_html = ""
    for idx, (s_title, s_voice) in enumerate(data["script_scenes"], 1):
        dur_match = re.search(r'(\d+)\s*s', s_title)
        dur = dur_match.group(1) if dur_match else "4"
        intent = data["scenes"][idx-1]["title"].split(":", 1)[-1].strip() if idx <= len(data["scenes"]) else ""
        script_rows_html += f"""
        <div class="script-item-row">
          <span class="script-badge-tag script-badge-tag--c{idx}">CẢNH {idx} • A-ROLL ({dur}s)</span>
          <div class="script-line-voice">"{s_voice}"</div>
          <div class="script-line-intent-pill">📍 {intent}</div>
        </div>"""

    # Build the full page HTML
    body_content = f"""
  <!-- ═══ TOP STICKY NAVIGATION BAR ═══ -->
  <header class="top-nav">
    <div class="top-nav__brand">
      <span class="top-nav__badge">VIDEO OFFLINE</span>
      <span class="top-nav__title">{data['nav_title']}</span>
    </div>
    <nav class="top-nav__links">
      <a href="9-bai-tap-thuc-hanh.html" class="top-nav__link top-nav__link--hub">🏛️ Master Hub</a>
      <a href="#sec-de-bai" class="top-nav__link">🎯 Đề Bài</a>
      <a href="#sec-cau-hoi" class="top-nav__link">❓ Tầng 1 (Safe)</a>
      <a href="#sec-step-2" class="top-nav__link">Tầng 2 (Real)</a>
      <a href="#sec-step-3" class="top-nav__link">Tầng 3 (Raw)</a>
      <a href="#sec-step-4" class="top-nav__link">Tầng 2.5</a>
      <a href="#sec-script" class="top-nav__link">📝 Kịch Bản Chốt</a>
      <a href="#sec-toi-uu-hook" class="top-nav__link" style="color: var(--cl-amber); border-color: rgba(217, 119, 6, 0.4); background: var(--cl-amber-bg);">⚡ Tối Ưu Hook</a>
      <a href="#sec-scene-1" class="top-nav__link">🎬 5 Phân Cảnh</a>
      <button class="top-nav__link" onclick="window.print()" style="cursor: pointer; background: var(--cl-tint);">🖨️ In Bài Tập</button>
    </nav>
  </header>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 1: ĐỀ BÀI RIÊNG BIỆT (100dvh) - ĐỂ HỞ 2 PHÚT SUY NGHĨ
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-de-bai">
    <div class="cl-sec-container apple-reveal">
      <div class="cl-badge">{badge_label}</div>
      <h1 class="title-short">{title_formatted}</h1>

      <!-- Thẻ Đề Bài Trọng Tâm -->
      <div class="exercise-hero-card">
        <div class="exercise-meta-pills">
          <span class="exercise-meta-pill">📍 Bối cảnh: <b>{meta_context}</b></span>
          <span class="exercise-meta-pill">⏱️ Thời lượng mục tiêu: <b>{meta_duration}</b></span>
          <span class="exercise-meta-pill">🎯 Mục tiêu: <b>{meta_goal}</b></span>
        </div>
        <div class="exercise-prompt-quote">
          "{data['problem_text']}"
        </div>
      </div>

      <!-- Không Gian Để Hở Cho Học Viên Động Não Suy Nghĩ -->
      <div class="thinking-open-card">
        <div class="thinking-open-header">
          <div class="thinking-open-title">
            <span>🧠</span>
            <span>DÀNH 2 PHÚT SUY NGHĨ: NẾU LÀ BẠN, BẠN SẼ LÀM GÌ?</span>
          </div>
          <span class="thinking-sub-badge">(Tự vấn trước khi kéo xuống xem hướng dẫn)</span>
        </div>
        <div class="thinking-prompts-list">
          <div class="thinking-prompt-item">
            <span class="thinking-prompt-bullet">1</span>
            <span class="thinking-prompt-text">{data['q1']}</span>
          </div>
          <div class="thinking-prompt-item">
            <span class="thinking-prompt-bullet">2</span>
            <span class="thinking-prompt-text">{data['q2']}</span>
          </div>
          <div class="thinking-prompt-item">
            <span class="thinking-prompt-bullet">3</span>
            <span class="thinking-prompt-text">{data['q3']}</span>
          </div>
          <div class="thinking-prompt-item">
            <span class="thinking-prompt-bullet">4</span>
            <span class="thinking-prompt-text">{data['q4']}</span>
          </div>
        </div>
      </div>

      <div style="margin-top: 24px; text-align: center; width: 100%;">
        <a href="#sec-cau-hoi" class="cl-btn">XEM CÁCH GIẢI BÀI TOÁN BẰNG 4 BƯỚC THỰC CHIẾN →</a>
      </div>

    </div>
    <a href="#sec-cau-hoi" class="cl-scroll-hint">
      <span>Cuộn xuống xem phân tích 4 bước</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 2: TIÊU ĐỀ CÂU HỎI & BƯỚC 1 (TẦNG 1 • SAFE) (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-cau-hoi">
    <div class="cl-sec-container apple-reveal">
      <div class="cl-badge cl-badge--red">01 / TẦNG 1 • SAFE (ĐÃI BÔI BỀ NỔI)</div>
      <h2 class="title-short">BƯỚC 1: CÁI MÀ AI CŨNG NGHĨ RA ĐẦU TIÊN</h2>
      <p class="title-long" style="font-size: clamp(17px, 2.2vw, 22px); margin-top: 4px; margin-bottom: 16px; color: var(--cl-text-muted); font-weight: 600;">
        ❓ Cách để làm video với đề bài này hấp dẫn là gì?
      </p>
      <p class="cl-body">
        Phản xạ đầu tiên của 90% người cầm máy là chọn phương án an toàn nhất: nói những điều nghe có vẻ đúng đắn, tích cực nhưng hoàn toàn rỗng ruột.
      </p>

      <div class="step-comparison-grid">
        <div class="step-card" style="border-left: 4px solid var(--cl-danger);">
          <div class="step-card__label" style="color: var(--cl-danger);">
            <span>Thoại Mẫu Ai Cũng Nghĩ Tới</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-danger-bg); color: var(--cl-danger);">VĂN MẪU AN TOÀN</span>
          </div>
          <div class="step-card__quote">
            "{data['step1_quote']}"
          </div>
          <div style="font-size: 12px; font-weight: 700; color: var(--cl-danger); display: flex; align-items: center; gap: 6px;">
            <span>❌ Phản ứng người xem:</span>
            <span>Lướt qua ngay trong 2 giây đầu</span>
          </div>
        </div>

        <div class="step-card">
          <div class="step-card__label" style="color: var(--cl-text-muted);">
            <span>Lý Giải Vì Sao Thất Bại</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-tint); color: var(--cl-text-muted);">PHÂN TÍCH BẢN CHẤT</span>
          </div>
          <div class="step-card__desc">
            {data['step1_critique']}
          </div>
        </div>
      </div>
    </div>
    <a href="#sec-step-2" class="cl-scroll-hint">
      <span>Bước tiếp theo: Cố gắng nói thật hơn</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 3: BƯỚC 2 (TẦNG 2 • REAL) (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-step-2">
    <div class="cl-sec-container apple-reveal">
      <div class="cl-badge cl-badge--amber">02 / TẦNG 2 • REAL (CẢM GIÁC THẬT)</div>
      <h2 class="title-short">BƯỚC 2: CỐ GẮNG NÓI THẬT HƠN</h2>
      <p class="editorial-hook">
        "Nhận ra đạo lý bị người ta ghét, người làm bắt đầu chuyển sang kể cảm giác thật..."
      </p>

      <div class="step-comparison-grid">
        <div class="step-card" style="border-left: 4px solid var(--cl-amber);">
          <div class="step-card__label" style="color: var(--cl-amber);">
            <span>Thoại Mẫu Thường Thấy</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-amber-bg); color: var(--cl-amber);">KỂ CẢM GIÁC ĐỜI THƯỜNG</span>
          </div>
          <div class="step-card__quote">
            "{data['step2_quote']}"
          </div>
          <div style="font-size: 12px; font-weight: 700; color: var(--cl-amber); display: flex; align-items: center; gap: 6px;">
            <span>⚠️ Phản ứng người xem:</span>
            <span>Gật gù nhẹ rồi trôi qua</span>
          </div>
        </div>

        <div class="step-card">
          <div class="step-card__label" style="color: var(--cl-text-muted);">
            <span>Lý Giải Vì Sao Chưa Hiệu Quả</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-tint); color: var(--cl-text-muted);">PHÂN TÍCH BẢN CHẤT</span>
          </div>
          <div class="step-card__desc">
            {data['step2_critique']}
          </div>
        </div>
      </div>
    </div>
    <a href="#sec-step-3" class="cl-scroll-hint">
      <span>Bước tiếp theo: Nói thật đến mức trần trụi</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 4: BƯỚC 3 (TẦNG 3 • RAW) (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-step-3">
    <div class="cl-sec-container apple-reveal">
      <div class="cl-badge cl-badge--red">03 / TẦNG 3 • RAW (TRẦN TRỤI THÔ BẠO)</div>
      <h2 class="title-short">BƯỚC 3: NÓI THẬT ĐẾN TRẦN TRỤI</h2>
      <p class="editorial-hook">
        "Càng muốn thật, người ta càng dễ rơi vào cái bẫy than nghèo kể khổ..."
      </p>

      <div class="step-comparison-grid">
        <div class="step-card" style="border-left: 4px solid var(--cl-danger);">
          <div class="step-card__label" style="color: var(--cl-danger);">
            <span>Thoại Mẫu Bộc Phát Thô Bạo</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-danger-bg); color: var(--cl-danger);">VẠCH ÁO CHO NGƯỜI XEM LƯNG</span>
          </div>
          <div class="step-card__quote">
            "{data['step3_quote']}"
          </div>
          <div style="font-size: 12px; font-weight: 700; color: var(--cl-danger); display: flex; align-items: center; gap: 6px;">
            <span>❌ Phản ứng người xem:</span>
            <span>Ái ngại, ngượng ngùng và tắt video</span>
          </div>
        </div>

        <div class="step-card">
          <div class="step-card__label" style="color: var(--cl-text-muted);">
            <span>Lý Giải Vì Sao Bị Hỏng</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-tint); color: var(--cl-text-muted);">PHÂN TÍCH BẢN CHẤT</span>
          </div>
          <div class="step-card__desc">
            {data['step3_critique']}
          </div>
        </div>
      </div>
    </div>
    <a href="#sec-step-4" class="cl-scroll-hint">
      <span>Bước quyết định: Điểm chạm đắt giá nhất</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 5: BƯỚC 4 (TẦNG 2.5 • ADULT FRICTION) (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-step-4">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge cl-badge--purple">04 / TẦNG 2.5 • ADULT FRICTION (ĐIỂM CHẠM VÀNG)</div>
      <h2 class="title-short">
        BƯỚC 4: ĐIỂM CHẠM VÀNG — NỖI GIẰNG XÉ THỂ DIỆN NGƯỜI LỚN
      </h2>
      <p class="cl-body">
        {data['step4_lead']}
      </p>

      <!-- Grid 4 Góc Nhìn Tầng 2.5 -->
      <div class="friction-triad-grid">
        <div class="friction-card">
          <span class="friction-card__badge">MẮT XÍCH 01</span>
          <h3 class="friction-card__title">Cái Cớ Ngụy Trang</h3>
          <div class="friction-card__quote">
            "{data['step4_disguise']}"
          </div>
          <div class="friction-card__why">
            Bóc trần hành vi ngụy trang bên ngoài để che giấu sự bối rối bên trong.
          </div>
        </div>

        <div class="friction-card">
          <span class="friction-card__badge">MẮT XÍCH 02</span>
          <h3 class="friction-card__title">Áp Lực Thực Tế</h3>
          <div class="friction-card__quote">
            "{data['step4_pressure']}"
          </div>
          <div class="friction-card__why">
            Nỗi sốt ruột có thật của người kinh doanh nhưng nói bằng ngôn ngữ đĩnh đạc.
          </div>
        </div>

        <div class="friction-card">
          <span class="friction-card__badge">MẮT XÍCH 03</span>
          <h3 class="friction-card__title">Điểm Nghẽn Thể Diện</h3>
          <div class="friction-card__quote">
            "{data['step4_ego']}"
          </div>
          <div class="friction-card__why">
            Chạm đúng tử huyệt tâm lý: Rào cản không phải là kỹ thuật mà là thể diện!
          </div>
        </div>

        <div class="friction-card">
          <span class="friction-card__badge">MẮT XÍCH 04</span>
          <h3 class="friction-card__title">Giải Phóng Tâm Lý</h3>
          <div class="friction-card__quote">
            "{data['step4_release']}"
          </div>
          <div class="friction-card__why">
            Tự tin cầm máy lên làm thật việc thật: Việc thật thì ngại gì!
          </div>
        </div>
      </div>

      <!-- Kết Luận Về Phương Án 2.5 -->
      <div class="conclusion-hero-card" style="margin-top: 24px;">
        <div class="conclusion-hero-badge">💡 KẾT LUẬN VỀ PHƯƠNG ÁN 2.5 • LỜI GIẢI GIẢI PHÓNG TÂM LÝ</div>
        <div class="conclusion-hero-text">
          {data['step4_core']}
        </div>
      </div>
    </div>
    <a href="#sec-script" class="cl-scroll-hint">
      <span>Xem kịch bản nói thực chiến đã chốt</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 6: KỊCH BẢN NÓI TRÀ ĐÁ ĐÃ CHỐT (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--tint" id="sec-script">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge cl-badge--green">KỊCH BẢN THỰC CHIẾN • 20 - 22 GIÂY</div>
      <h2 class="title-short">KỊCH BẢN NÓI TRÀ ĐÁ ĐÃ CHỐT</h2>
      <p class="cl-body">
        Ngắt nhịp thở tự nhiên • 100% chuẩn văn nói trà đá đĩnh đạc, không từ ngữ hoa mỹ, không đạo lý sáo rỗng.
      </p>

      <div class="final-script-card">
        {script_rows_html}
      </div>

      <div style="margin-top: 28px;">
        <a href="#sec-toi-uu-hook" class="cl-btn" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #ffffff; font-weight: 700; box-shadow: 0 6px 20px rgba(217, 119, 6, 0.28);">⚡ BƯỚC TIẾP THEO: TỐI ƯU HOOK ĐỂ GIẢM THIỆT THÒI TRÊN VIDEO NGẮN ↓</a>
      </div>
    </div>
    <a href="#sec-toi-uu-hook" class="cl-scroll-hint">
      <span>Cuộn xuống xem phần Tối ưu Hook</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 7: TỐI ƯU HOOK (SO SÁNH 2 CỘT) (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-toi-uu-hook">
    <div class="cl-sec-container cl-sec-container--wide apple-reveal">
      <div class="cl-badge cl-badge--amber">⚡ NÂNG CẤP THỰC CHIẾN • TỐI ƯU HOOK 2 GIÂY ĐẦU</div>
      <h2 class="title-short">
        ĐỂ GIẢM THIỆT THÒI TRÊN VIDEO NGẮN: CẦN TỐI ƯU HOOK
      </h2>
      <p class="editorial-hook" style="margin-bottom: 24px;">
        "Nội dung kịch bản ở trên đã có độ sâu rất tốt, nhưng nếu Cảnh 1 không giữ được ngón tay người xem trong 2 giây đầu thì thông điệp hay đến mấy cũng không ai xem."
      </p>

      <!-- BẢNG 2 CỘT SO SÁNH TRỰC DIỆN -->
      <div class="step-comparison-grid" style="margin-top: 0; gap: 24px;">
        
        <!-- CỘT 1: LÚC CHƯA CÓ HOOK -->
        <div class="step-card" style="border-left: 4px solid var(--cl-danger); background: #ffffff;">
          <div class="step-card__label" style="color: var(--cl-danger);">
            <span>CẢNH 1 • LÚC CHƯA CÓ HOOK (4S)</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-danger-bg); color: var(--cl-danger);">BẢN GỐC TRẦN THUẬT</span>
          </div>
          
          <div class="step-card__quote" style="border-left-color: var(--cl-danger); background: var(--cl-danger-bg); font-size: 16px; margin-bottom: 12px;">
            🎙️ "{data['hook_old']}"
          </div>

          <div style="font-family: var(--font-mono); font-size: 11px; font-weight: 700; color: var(--cl-danger); margin-bottom: 14px; background: rgba(220, 38, 38, 0.08); padding: 4px 10px; border-radius: 6px; display: inline-block;">
            📍 Trạng thái: {data['hook_old_note']}
          </div>

          <div class="step-card__desc" style="font-size: 14.5px; line-height: 1.7;">
            <b style="color: var(--cl-danger);">❌ TÌNH TRẠNG & TÂM LÝ NGƯỜI XEM (LÚC CHƯA CÓ HOOK):</b><br>
            {data['hook_old_critique']}
          </div>
        </div>

        <!-- CỘT 2: LÚC CÓ HOOK -->
        <div class="step-card" style="border-left: 4px solid var(--cl-success); background: #ffffff;">
          <div class="step-card__label" style="color: var(--cl-success);">
            <span>CẢNH 1 • HOOK (4S)</span>
            <span style="font-size: 10px; padding: 2px 8px; border-radius: 4px; background: var(--cl-success-bg); color: var(--cl-success);">PHƯƠNG ÁN ĐÃ CHỌN TỐI ƯU</span>
          </div>
          
          <div class="step-card__quote" style="border-left-color: var(--cl-success); background: var(--cl-success-bg); font-size: 16px; margin-bottom: 12px;">
            🎙️ "{data['hook_new']}"
          </div>

          <div style="font-family: var(--font-mono); font-size: 11px; font-weight: 700; color: var(--cl-purple); margin-bottom: 14px; background: var(--cl-purple-bg); padding: 4px 10px; border-radius: 6px; display: inline-block;">
            📍 {data['hook_new_note']}
          </div>

          <div class="step-card__desc" style="font-size: 14.5px; line-height: 1.7;">
            <b style="color: var(--cl-success);">🎯 HIỆU QUẢ GIỮ CHÂN & TÂM LÝ NGƯỜI XEM (LÚC CÓ HOOK):</b><br>
            {data['hook_new_critique']}
          </div>
        </div>

      </div>

      <!-- Khối đúc kết logic -->
      <div class="conclusion-hero-card" style="margin-top: 24px; background: linear-gradient(135deg, #fffbeb 0%, #ffffff 100%); border-color: rgba(217, 119, 6, 0.3);">
        <div class="conclusion-hero-badge" style="color: var(--cl-amber);">💡 ĐÚC KẾT SƯ PHẠM: BẢN CHẤT CỦA HOOK TRONG VIDEO NGẮN</div>
        <div class="conclusion-hero-text" style="font-size: 15px;">
          <strong>Hook trong video ngắn không phải là giật tít sốc, làm trò hề hay hét to vào micro.</strong><br>
          Hook thực chiến là <strong>lực kéo tâm lý trong 2 giây đầu tiên</strong> khiến ngón tay người xem phải khựng lại vì nhận ra: <em>"Câu chuyện này đang nói đúng về mình, nói hộ sự thật ngượng ngùng mà mình không dám thừa nhận."</em> Khi Cảnh 1 có Hook đảo ngược hành vi, toàn bộ các cảnh tiếp theo sẽ được người xem đón nhận trọn vẹn.
        </div>
      </div>

      <div style="margin-top: 28px;">
        <a href="#sec-scene-1" class="cl-btn">XEM BẢNG PHÂN CẢNH QUAY CHI TIẾT (ÁP DỤNG BỐI CẢNH GREENHUB) →</a>
      </div>
    </div>
    <a href="#sec-scene-1" class="cl-scroll-hint">
      <span>Cuộn xuống xem phân cảnh quay</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>
    </a>
  </section>

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 8 ➔ 12: 5 CẢNH PHÂN CẢNH CHI TIẾT
       ═══════════════════════════════════════════════════════════════════ -->
  {scenes_html}

  <!-- ═══════════════════════════════════════════════════════════════════
       KHỐI 13: ĐÚC KẾT BÀI HỌC (100dvh)
       ═══════════════════════════════════════════════════════════════════ -->
  <section class="cl-zebra-section cl-zebra--light" id="sec-wisdom">
    <div class="cl-sec-container cl-sec-container--narrow apple-reveal">
      <div class="cl-badge">LỜI DẶN DÒ THỰC CHIẾN CỦA ANH VIỆT</div>
      <h2 class="title-short">ĐÚC KẾT BÀI HỌC</h2>

      <blockquote class="editorial-hook" style="margin-bottom: 24px;">
        "{data['wisdom_quote']}"
      </blockquote>

      <div class="takeaways-list">
        <div class="takeaway-card">
          <div class="takeaway-num">01</div>
          <div class="takeaway-content">
            <h4>{data['lesson1_title']}</h4>
            <p>{data['lesson1_desc']}</p>
          </div>
        </div>

        <div class="takeaway-card">
          <div class="takeaway-num">02</div>
          <div class="takeaway-content">
            <h4>{data['lesson2_title']}</h4>
            <p>{data['lesson2_desc']}</p>
          </div>
        </div>

        <div class="takeaway-card">
          <div class="takeaway-num">03</div>
          <div class="takeaway-content">
            <h4>{data['lesson3_title']}</h4>
            <p>{data['lesson3_desc']}</p>
          </div>
        </div>
      </div>

      <div style="margin-top: 32px; display: flex; gap: 16px; flex-wrap: wrap;">
        <a href="9-bai-tap-thuc-hanh.html" class="cl-btn">🏛️ QUAY VỀ MASTER HUB 9 KỊCH BẢN</a>
        <a href="#sec-de-bai" class="cl-btn" style="background: var(--cl-tint); color: var(--cl-text-base); border: 1px solid var(--cl-line); box-shadow: none;">↑ VỀ ĐẦU TRANG</a>
      </div>
    </div>
  </section>
"""

    # Assemble HTML
    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>{clean_page_title}</title>
  {TEMPLATE_HEAD[TEMPLATE_HEAD.find('<link'):]}
<body>
{body_content}
{TEMPLATE_TAIL}
"""
    return full_html

def main():
    print("Building all lessons (KB02 - KB09)...")
    for ldata in ALL_LESSONS:
        html = generate_lesson_html(ldata)
        old_name = ldata["file_name"]
        short_name = SHORT_NAMES.get(old_name, old_name)

        # 1. Write short name to COURSE_DIR
        out_course = os.path.join(COURSE_DIR, short_name)
        with open(out_course, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Saved to course/: {short_name}")

        # 2. Write short name to GITHUB_COURSE_DIR
        os.makedirs(GITHUB_COURSE_DIR, exist_ok=True)
        out_gh_course = os.path.join(GITHUB_COURSE_DIR, short_name)
        with open(out_gh_course, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Saved to vietndj.github.io/course/: {short_name}")

        # 3. Write short name and old name to OFFLINE_DIR
        out_offline_short = os.path.join(OFFLINE_DIR, short_name)
        with open(out_offline_short, "w", encoding="utf-8") as f:
            f.write(html)
        out_offline_old = os.path.join(OFFLINE_DIR, old_name)
        with open(out_offline_old, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Saved to Offline: {short_name} & {old_name}")

    # Also copy bai-01-ca-phe-dem.html
    bai01_src = os.path.join(OFFLINE_DIR, "bai-01-ca-phe-dem.html")
    with open(bai01_src, "r", encoding="utf-8") as f:
        bai01_content = f.read()
    with open(os.path.join(COURSE_DIR, "bai-01-ca-phe-dem.html"), "w", encoding="utf-8") as f:
        f.write(bai01_content)
    with open(os.path.join(GITHUB_COURSE_DIR, "bai-01-ca-phe-dem.html"), "w", encoding="utf-8") as f:
        f.write(bai01_content)
    with open(os.path.join(OFFLINE_DIR, "kich_ban_01_ngoi_ca_phe_10h_toi.html"), "w", encoding="utf-8") as f:
        f.write(bai01_content)
    print("Synchronized bai-01-ca-phe-dem.html to course/ and vietndj.github.io/course/")

    print("\nAll 9 lessons synchronized successfully in all target directories!")

if __name__ == "__main__":
    main()
