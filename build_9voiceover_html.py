# -*- coding: utf-8 -*-
"""
Generate 9voiceover.html - Master Hub for Bài 1
"""
import os
from generate_9voiceover import STYLES

def render_html():
    styles_html = []
    
    for s in STYLES:
        # Flaws HTML
        flaws_items = []
        for i, f in enumerate(s["flaws"], 1):
            flaw_block = f"""
            <div class="flaw-item">
              <div class="flaw-header">
                <span class="flaw-num">Điểm {i}</span>
                <span class="flaw-title">{"Cỡ cảnh & Góc máy" if i==1 else ("Bối cảnh & Đạo cụ" if i==2 else "Thần thái & Văn phong")}</span>
              </div>
              <div class="flaw-comparison">
                <div class="flaw-old">
                  <span class="badge-old">❌ Chưa Được (Cũ)</span>
                  <p>{f["issue"]}</p>
                </div>
                <div class="flaw-new">
                  <span class="badge-new">✅ Nâng Cấp (Quay Theo Luôn)</span>
                  <p>{f["fix"]}</p>
                </div>
              </div>
            </div>"""
            flaws_items.append(flaw_block)
        
        flaws_html = "\n".join(flaws_items)

        # Shots HTML
        shots_rows = []
        for idx, shot in enumerate(s["shots"], 1):
            s_title, s_time, s_size, s_angle, s_dir, s_voice, s_desc = shot
            row = f"""
            <div class="shot-row">
              <div class="shot-meta">
                <span class="shot-idx">Shot {idx}</span>
                <span class="shot-time">{s_time}</span>
                <span class="shot-size-pill">{s_size}</span>
              </div>
              <div class="shot-details">
                <div class="shot-name"><b>{s_title}</b></div>
                <div class="shot-dir-line">📐 <b>Góc máy:</b> {s_angle} • <b>Hướng:</b> {s_dir}</div>
                <div class="shot-desc-line">🎬 {s_desc}</div>
                <div class="shot-voice-line">🎙️ <i>"{s_voice}"</i></div>
              </div>
            </div>"""
            shots_rows.append(row)
        shots_html = "\n".join(shots_rows)

        card_html = f"""
    <!-- CARD {s["code"]} -->
    <article class="pk-card" data-category="{s["category"]}" data-search="{s["title"].lower()} {s["context"].lower()} {s["target"].lower()} {s["outfit"].lower()} {s["code"].lower()}">
      <div class="pk-card-inner">
        
        <!-- CỘT TRÁI: HERO AVATAR 9:16 -->
        <div class="pk-visual-col">
          <div class="avatar-9-16" onclick="openLightbox('{s["avatar"]}', '{s["code"]} • {s["title"]}', '{s["outfit"]}')">
            <img src="{s["avatar"]}" alt="{s["title"]}" loading="lazy">
            <div class="avatar-tag-top">
              <span class="dna-badge">✨ Face DNA 99%</span>
            </div>
            <div class="avatar-tag-bottom">
              <span class="outfit-badge">👔 {s["outfit"]}</span>
            </div>
            <div class="zoom-hint">🔍 Chạm để phóng to</div>
          </div>
          
          <div class="quick-action-col">
            <a href="{s["slug"]}" class="btn-primary-glow">
              <span>📖 Xem Toàn Bộ Phân Cảnh</span>
              <span>→</span>
            </a>
            <button type="button" class="btn-copy-voice" onclick="copyVoice(`{s["voice"]}`)">
              📋 Sao Chép Thoại
            </button>
          </div>
        </div>

        <!-- CỘT PHẢI: CHI TIẾT & BÓC TÁCH -->
        <div class="pk-content-col">
          
          <!-- HEADER THÔNG TIN -->
          <div class="pk-header">
            <div class="pk-badge-row">
              <span class="code-pill">{s["code"]}</span>
              <span class="category-pill">{s["category_name"]}</span>
            </div>
            <h2 class="pk-title"><a href="{s["slug"]}">{s["title"]}</a></h2>
            <div class="pk-meta-grid">
              <div class="meta-item">📍 <b>Bối cảnh:</b> {s["context"]}</div>
              <div class="meta-item">🎯 <b>Tệp khán giả:</b> {s["target"]}</div>
            </div>
          </div>

          <!-- PHÂN TÍCH 3 ĐIỂM CHƯA ĐƯỢC & NÂNG CẤP THỰC CHIẾN -->
          <div class="section-box flaws-box">
            <div class="box-title">
              <span>🛠️ Phân Tích 3 Điểm Nâng Cấp • "Nhìn Là Quay Được Theo Luôn"</span>
            </div>
            <div class="flaws-list">
              {flaws_html}
            </div>
          </div>

          <!-- VOICEOVER THOẠI -->
          <div class="section-box voice-box">
            <div class="box-title">
              <span>🎙️ Thoại Voiceover Mộc Mạc (Chuẩn Giọng Anh Việt)</span>
            </div>
            <div class="hook-line">
              <b>Hook mở màn:</b> "{s["hook"]}"
            </div>
            <div class="voice-text">
              "{s["voice"]}"
            </div>
          </div>

          <!-- 5 CÚ MÁY PHÂN CẢNH BĂM NHỊP -->
          <div class="section-box shots-box">
            <div class="box-title accordion-toggle" onclick="toggleShots(this)">
              <span>🎞️ 5 Cú Máy Băm Nhịp Phân Cảnh (Storyboard Beats)</span>
              <span class="arrow-indicator">▼</span>
            </div>
            <div class="shots-list">
              {shots_html}
            </div>
          </div>

        </div>

      </div>
    </article>"""
        styles_html.append(card_html)

    all_cards = "\n\n".join(styles_html)

    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bài 1 • Thực Hành 1 Kịch Bản Với 9 Phong Cách Voiceover | FEDU AI Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #060911;
      --bg-surface: #0c121e;
      --bg-card: #111a2b;
      --bg-card-hover: #162238;
      --card-inner: #152035;
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
      --purple: #a855f7;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --shadow-card: 0 10px 30px rgba(0, 0, 0, 0.5);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-main);
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.08) 0%, transparent 65%),
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

    /* STICKY TOP BAR */
    .top-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(6, 9, 17, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
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
    }}

    .header-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
    }}

    .header-controls {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .nav-pill {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 9999px;
      text-decoration: none;
      transition: all 0.2s;
    }}

    .nav-pill:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }}

    .nav-pill.active {{
      background: var(--cyan);
      color: #000;
      font-weight: 800;
      border-color: var(--cyan);
    }}

    /* HERO BANNER */
    .hero-banner {{
      padding: 50px 0 35px;
      text-align: center;
    }}

    .hero-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 16px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 16px;
    }}

    .hero-title {{
      font-size: 34px;
      font-weight: 900;
      line-height: 1.25;
      margin-bottom: 16px;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
      font-size: 16px;
      color: var(--text-muted);
      max-width: 850px;
      margin: 0 auto 28px;
      line-height: 1.6;
    }}

    .stats-row {{
      display: flex;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
      margin-bottom: 35px;
    }}

    .stat-badge {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      padding: 8px 18px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .stat-badge b {{ color: var(--cyan); font-family: 'JetBrains Mono', monospace; }}

    /* FILTER & CONTROLS */
    .filter-bar {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 35px;
    }}

    .filter-tabs {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .tab-btn {{
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 700;
      padding: 7px 14px;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .tab-btn:hover {{
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
    }}

    .tab-btn.active {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--cyan);
      color: var(--cyan);
    }}

    .search-box {{
      position: relative;
      min-width: 280px;
    }}

    .search-box input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 9999px;
      padding: 9px 18px 9px 36px;
      color: #fff;
      font-size: 13px;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
    }}

    .search-box input:focus {{
      border-color: var(--cyan);
    }}

    .search-box::before {{
      content: "🔍";
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      opacity: 0.6;
    }}

    /* STYLES LIST */
    .styles-container {{
      display: flex;
      flex-direction: column;
      gap: 32px;
    }}

    /* CARD STRUCTURE */
    .pk-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-card);
      overflow: hidden;
      transition: transform 0.25s ease, border-color 0.25s ease;
    }}

    .pk-card:hover {{
      border-color: var(--border-accent);
      transform: translateY(-2px);
    }}

    .pk-card-inner {{
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: 28px;
      padding: 28px;
    }}

    @media (max-width: 960px) {{
      .pk-card-inner {{
        grid-template-columns: 1fr;
      }}
    }}

    /* CỘT TRÁI */
    .pk-visual-col {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .avatar-9-16 {{
      position: relative;
      aspect-ratio: 9/16;
      border-radius: var(--radius-md);
      overflow: hidden;
      background: #020408;
      border: 1px solid rgba(255, 255, 255, 0.1);
      cursor: zoom-in;
    }}

    .avatar-9-16 img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}

    .avatar-9-16:hover img {{
      transform: scale(1.03);
    }}

    .avatar-tag-top {{
      position: absolute;
      top: 12px;
      left: 12px;
    }}

    .dna-badge {{
      background: rgba(16, 185, 129, 0.9);
      backdrop-filter: blur(8px);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }}

    .avatar-tag-bottom {{
      position: absolute;
      bottom: 12px;
      left: 12px;
      right: 12px;
    }}

    .outfit-badge {{
      background: rgba(6, 9, 17, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      font-size: 11.5px;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 6px;
      display: block;
      line-height: 1.4;
    }}

    .zoom-hint {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.6);
      color: #cbd5e1;
      font-size: 10px;
      padding: 3px 8px;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.2s;
    }}

    .avatar-9-16:hover .zoom-hint {{
      opacity: 1;
    }}

    .quick-action-col {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .btn-primary-glow {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff;
      text-decoration: none;
      font-size: 13px;
      font-weight: 800;
      padding: 10px 16px;
      border-radius: var(--radius-sm);
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: opacity 0.2s, transform 0.2s;
    }}

    .btn-primary-glow:hover {{
      opacity: 0.95;
      transform: translateY(-1px);
    }}

    .btn-copy-voice {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      font-size: 12.5px;
      font-weight: 700;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-copy-voice:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: #fff;
    }}

    /* CỘT PHẢI */
    .pk-content-col {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .pk-badge-row {{
      display: flex;
      gap: 10px;
      align-items: center;
      margin-bottom: 8px;
    }}

    .code-pill {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid var(--cyan);
      color: var(--cyan);
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 800;
      padding: 2px 10px;
      border-radius: 6px;
    }}

    .category-pill {{
      background: rgba(168, 85, 247, 0.15);
      border: 1px solid rgba(168, 85, 247, 0.3);
      color: #c084fc;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .pk-title {{
      font-size: 22px;
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 8px;
    }}

    .pk-title a {{
      color: #fff;
      text-decoration: none;
      transition: color 0.2s;
    }}

    .pk-title a:hover {{
      color: var(--cyan);
    }}

    .pk-meta-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 6px;
      font-size: 13px;
      color: var(--text-muted);
    }}

    .meta-item b {{
      color: #cbd5e1;
    }}

    /* SECTION BOXES */
    .section-box {{
      background: var(--card-inner);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: var(--radius-md);
      padding: 16px 20px;
    }}

    .box-title {{
      font-size: 13px;
      font-weight: 800;
      color: #cbd5e1;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    /* FLAWS SECTION */
    .flaws-box {{
      border-left: 3px solid var(--amber);
    }}

    .flaws-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .flaw-item {{
      background: rgba(0, 0, 0, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
    }}

    .flaw-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}

    .flaw-num {{
      background: rgba(245, 158, 11, 0.2);
      color: var(--amber);
      font-size: 10px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
    }}

    .flaw-title {{
      font-size: 12px;
      font-weight: 700;
      color: #f1f5f9;
    }}

    .flaw-comparison {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      font-size: 12.5px;
      line-height: 1.5;
    }}

    @media (max-width: 640px) {{
      .flaw-comparison {{
        grid-template-columns: 1fr;
      }}
    }}

    .flaw-old {{
      background: rgba(244, 63, 94, 0.06);
      border: 1px solid rgba(244, 63, 94, 0.18);
      padding: 8px 10px;
      border-radius: 6px;
    }}

    .flaw-new {{
      background: rgba(16, 185, 129, 0.06);
      border: 1px solid rgba(16, 185, 129, 0.2);
      padding: 8px 10px;
      border-radius: 6px;
    }}

    .badge-old {{
      font-size: 10.5px;
      font-weight: 800;
      color: #fb7185;
      display: block;
      margin-bottom: 4px;
    }}

    .badge-new {{
      font-size: 10.5px;
      font-weight: 800;
      color: #34d399;
      display: block;
      margin-bottom: 4px;
    }}

    .flaw-old p, .flaw-new p {{
      margin: 0;
      color: #cbd5e1;
    }}

    /* VOICE BOX */
    .voice-box {{
      border-left: 3px solid var(--cyan);
    }}

    .hook-line {{
      background: rgba(56, 189, 248, 0.08);
      border: 1px dashed rgba(56, 189, 248, 0.3);
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 13px;
      color: #e0f2fe;
      margin-bottom: 10px;
    }}

    .voice-text {{
      font-size: 13.5px;
      line-height: 1.6;
      color: #cbd5e1;
      font-style: italic;
      background: rgba(0, 0, 0, 0.2);
      padding: 12px 14px;
      border-radius: 6px;
    }}

    /* SHOTS BOX */
    .shots-box {{
      border-left: 3px solid var(--purple);
    }}

    .accordion-toggle {{
      cursor: pointer;
      user-select: none;
    }}

    .shots-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .shot-row {{
      background: rgba(0, 0, 0, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.04);
      border-radius: 6px;
      padding: 10px 14px;
      display: grid;
      grid-template-columns: 180px 1fr;
      gap: 14px;
      align-items: center;
    }}

    @media (max-width: 720px) {{
      .shot-row {{
        grid-template-columns: 1fr;
        gap: 6px;
      }}
    }}

    .shot-meta {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .shot-idx {{
      font-size: 12px;
      font-weight: 800;
      color: var(--cyan);
      font-family: 'JetBrains Mono', monospace;
    }}

    .shot-time {{
      font-size: 11px;
      color: var(--text-dim);
      font-family: 'JetBrains Mono', monospace;
    }}

    .shot-size-pill {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.12);
      color: var(--cyan);
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      width: fit-content;
    }}

    .shot-name {{
      font-size: 13px;
      color: #fff;
      margin-bottom: 2px;
    }}

    .shot-dir-line {{
      font-size: 11.5px;
      color: #94a3b8;
      margin-bottom: 4px;
    }}

    .shot-desc-line {{
      font-size: 12px;
      color: #cbd5e1;
      margin-bottom: 2px;
    }}

    .shot-voice-line {{
      font-size: 11.5px;
      color: #38bdf8;
    }}

    /* LIGHTBOX MODAL */
    .lightbox-modal {{
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: 2000;
      background: rgba(2, 4, 8, 0.94);
      backdrop-filter: blur(12px);
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}

    .lightbox-modal.active {{
      display: flex;
    }}

    .lightbox-content {{
      position: relative;
      max-width: 550px;
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8);
    }}

    .lightbox-img-wrap {{
      aspect-ratio: 9/16;
      max-height: 75vh;
      overflow: hidden;
      background: #000;
    }}

    .lightbox-img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .lightbox-footer {{
      padding: 16px 20px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .lightbox-title {{
      font-size: 14px;
      font-weight: 800;
      color: #fff;
    }}

    .lightbox-desc {{
      font-size: 12px;
      color: var(--text-muted);
    }}

    .btn-close-lightbox {{
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #fff;
      font-size: 14px;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 9999px;
      cursor: pointer;
    }}

    /* TOAST NOTIFICATION */
    .toast {{
      position: fixed;
      bottom: 30px;
      right: 30px;
      background: #10b981;
      color: #fff;
      font-size: 13px;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: 8px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      z-index: 3000;
    }}

    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- TOP STICKY BAR -->
  <header class="top-header">
    <div class="brand-group">
      <a href="index.html" style="text-decoration:none; display:flex; align-items:center; gap:10px;">
        <span class="brand-badge">FEDU OFFLINE 2.0</span>
        <span class="header-title">Bài 1 • Thực Hành 1 Kịch Bản Với 9 Phong Cách Voiceover</span>
      </a>
    </div>
    <div class="header-controls">
      <a href="index.html" class="nav-pill">🏛️ Hub Tổng</a>
      <a href="9voiceover.html" class="nav-pill active">🎙️ Bài 1: 9 Voiceover (Active)</a>
      <a href="12canhtram.html" class="nav-pill">📹 Bài 2: 12 Cảnh Trám</a>
    </div>
  </header>

  <div class="container">

    <!-- HERO BANNER -->
    <div class="hero-banner">
      <div class="hero-eyebrow">
        <span>🎙️ Master Hub • Phân Cảnh & Thần Thái Voiceover</span>
      </div>
      <h1 class="hero-title">1 Kịch Bản • 9 Phong Cách Biểu Đạt Thực Chiến</h1>
      <p class="hero-subtitle">
        Cùng một câu chuyện bế tắc trong kinh doanh, khi thay đổi <b>9 góc nhìn tâm lý, 9 phục trang độc bản</b> và <b>cỡ cảnh băm nhịp</b>, bạn sẽ tạo ra 9 định vị hoàn toàn khác nhau để chạm tới từng tệp khán giả riêng biệt.
      </p>

      <div class="stats-row">
        <div class="stat-badge">🎭 <b>9</b> Phong Cách Biểu Đạt</div>
        <div class="stat-badge">👔 <b>9</b> Phục Trang Độc Bản</div>
        <div class="stat-badge">🎞️ <b>45</b> Cú Máy Phân Cảnh</div>
        <div class="stat-badge">✨ <b>99%</b> Độ Giống Face DNA Anh Việt</div>
      </div>
    </div>

    <!-- FILTER & SEARCH BAR -->
    <div class="filter-bar">
      <div class="filter-tabs" id="filterTabs">
        <button type="button" class="tab-btn active" onclick="filterCategory('all', this)">Tất Cả (9)</button>
        <button type="button" class="tab-btn" onclick="filterCategory('pressure', this)">Áp Lực Cày Đêm</button>
        <button type="button" class="tab-btn" onclick="filterCategory('finance', this)">Vốn & Tiền Ads</button>
        <button type="button" class="tab-btn" onclick="filterCategory('career', this)">Tuổi Tác & Bảo Thủ</button>
        <button type="button" class="tab-btn" onclick="filterCategory('craftsman', this)">Nghề & Chuyên Môn</button>
        <button type="button" class="tab-btn" onclick="filterCategory('pricing', this)">Cạnh Tranh Giá</button>
        <button type="button" class="tab-btn" onclick="filterCategory('restart', this)">Làm Lại Từ Số 0</button>
      </div>
      <div class="search-box">
        <input type="text" id="searchInput" placeholder="Tìm theo từ khóa, phục trang, bối cảnh..." onkeyup="handleSearch()">
      </div>
    </div>

    <!-- 9 STYLES CARDS LIST -->
    <div class="styles-container" id="stylesContainer">
      {all_cards}
    </div>

  </div>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox(event)">
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <div class="lightbox-img-wrap">
        <img src="" id="lightboxImg" alt="Phóng to ảnh">
      </div>
      <div class="lightbox-footer">
        <div>
          <div class="lightbox-title" id="lightboxTitle"></div>
          <div class="lightbox-desc" id="lightboxDesc"></div>
        </div>
        <button type="button" class="btn-close-lightbox" onclick="closeLightbox()">Đóng ✕</button>
      </div>
    </div>
  </div>

  <!-- TOAST -->
  <div class="toast" id="toast">Đã sao chép kịch bản thoại vào khay nhớ tạm!</div>

  <script>
    // FILTER CATEGORY
    function filterCategory(cat, btn) {{
      const tabs = document.querySelectorAll('.tab-btn');
      tabs.forEach(t => t.classList.remove('active'));
      btn.classList.add('active');

      const cards = document.querySelectorAll('.pk-card');
      cards.forEach(card => {{
        if (cat === 'all' || card.getAttribute('data-category') === cat) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // REALTIME SEARCH
    function handleSearch() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.pk-card');
      
      cards.forEach(card => {{
        const searchData = card.getAttribute('data-search');
        if (!query || searchData.includes(query)) {{
          card.style.display = 'block';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // TOGGLE SHOTS ACCORDION
    function toggleShots(header) {{
      const list = header.nextElementSibling;
      const arrow = header.querySelector('.arrow-indicator');
      if (list.style.display === 'none') {{
        list.style.display = 'flex';
        arrow.textContent = '▼';
      }} else {{
        list.style.display = 'none';
        arrow.textContent = '▶';
      }}
    }}

    // COPY VOICE TO CLIPBOARD
    function copyVoice(text) {{
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast');
        toast.classList.add('show');
        setTimeout(() => {{
          toast.classList.remove('show');
        }}, 2200);
      }});
    }}

    // LIGHTBOX FUNCTIONS
    function openLightbox(src, title, desc) {{
      document.getElementById('lightboxImg').src = src;
      document.getElementById('lightboxTitle').textContent = title;
      document.getElementById('lightboxDesc').textContent = desc;
      document.getElementById('lightboxModal').classList.add('active');
    }}

    function closeLightbox(e) {{
      document.getElementById('lightboxModal').classList.remove('active');
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeLightbox();
    }});
  </script>
</body>
</html>"""
    
    out_path = "/Users/vietmac/Documents/CODE/offline02/9voiceover.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Rendered {out_path} ({len(full_html)} bytes)")

if __name__ == "__main__":
    render_html()
