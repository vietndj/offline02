# -*- coding: utf-8 -*-
import os
from build_all_course_system import EXERCISES

def generate_overview_cards():
    cards = []
    for ex in EXERCISES:
        ex_id = ex["id"]
        cat = ex.get("category", "insight")
        first_line = ex["voice"].split('\n')[0][:75] + "..."
        c = f"""        <div class="overview-card" data-category="{cat}" onclick="showExercise('{ex_id}')" id="card-tab-{ex_id}">
          <div class="overview-img-box">
            <img src="{ex['avatar']}" alt="{ex['title']}" loading="lazy">
            <span class="card-badge-top" style="background:#1a73e8; color:#fff;">Bài tập {ex_id}</span>
            <span class="card-outfit-tag">{ex['outfit']}</span>
          </div>
          <div class="overview-body">
            <div class="overview-card-title">{ex['title']}</div>
            <div class="overview-quote">"{first_line}"</div>
            <div class="overview-t25"><b>Tâm lý:</b> {ex['state']}</div>
            <div style="display:flex; gap:8px; margin-top:auto;">
              <a href="{ex['slug']}" target="_blank" class="overview-btn" style="flex:1;">Mở Trang Riêng ↗</a>
              <button type="button" class="overview-btn" style="background:#0284c7; color:#fff; border:none;" onclick="event.stopPropagation(); showExercise('{ex_id}')">Xem 5 Shot ↓</button>
            </div>
          </div>
        </div>"""
        cards.append(c)
    return "\n\n".join(cards)

def generate_exercise_detail(ex):
    ex_id = ex["id"]
    voice_display = ex["voice"].replace('\n', '<br>')
    
    # 5 beats
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
        img_path = f"{ex['frame_dir']}/shot{idx}.jpg"
        
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
    beats_html = "\n\n".join(cards_html)
    
    # 3 reshoots
    reshoot_items = []
    for r_title, r_desc in ex["reshoots"]:
        reshoot_items.append(f'<li style="margin-bottom:8px;"><b>{r_title}:</b> {r_desc}</li>')
    reshoots_html = "\n".join(reshoot_items)
    
    active_class = " active" if ex_id == "01" else ""
    
    return f"""      <!-- EXERCISE {ex_id} DETAIL -->
      <div class="exercise-detail-wrap{active_class}" id="detail-bt{ex_id}">
        <div class="master-audio-box">
          <div class="master-audio-content">
            <div class="master-voice-icon">🎙️</div>
            <div>
              <div class="master-voice-title">Bài tập {ex_id} • Lời thoại Voice-Over ngầm</div>
              <div class="master-voice-text" id="voice-text-{ex_id}">"{voice_display}"</div>
            </div>
          </div>
          <div style="display:flex; gap:10px; align-items:center;">
            <button class="copy-btn" onclick="copyVoice('{ex_id}')">Sao chép kịch bản</button>
            <a href="{ex['slug']}" target="_blank" class="copy-btn" style="background:#0284c7; border-color:#0284c7; text-decoration:none;">Mở trang riêng ↗</a>
          </div>
        </div>

        <!-- 5 Beats Grid -->
        <div style="margin-bottom:14px; display:flex; justify-content:space-between; align-items:center;">
          <h3 style="font-size:16px; font-weight:800; color:#fff;">🎬 CHI TIẾT 5 CÚ MÁY BĂM NHỎ (BÀI TẬP {ex_id})</h3>
          <span style="font-size:12px; color:var(--cyan);">Bấm vào ảnh để phóng to chi tiết</span>
        </div>
        <div class="storyboard-grid-5">
{beats_html}
        </div>

        <!-- Reshoot Box -->
        <div style="background:#090e17; border:1px solid rgba(255,255,255,0.08); border-radius:14px; padding:18px 22px; margin-top:20px;">
          <h4 style="font-size:14px; font-weight:800; color:#fde047; margin-bottom:10px;">📍 3 Gợi Ý Bối Cảnh Quay Lại Ngoài Lớp Học:</h4>
          <ul style="padding-left:20px; font-size:13px; color:#cbd5e1; line-height:1.6;">
            {reshoots_html}
          </ul>
        </div>
      </div>"""

def main():
    hub_path = "/Users/vietmac/Documents/CODE/course/lopmarketingbaitap.html"
    with open(hub_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update overview cards
    cards_start_tag = '<div class="overview-grid" id="overview-grid">'
    cards_end_tag = '</div>\n\n    <!-- Detail Sections Container -->'
    
    cs_pos = html.find(cards_start_tag)
    ce_pos = html.find(cards_end_tag, cs_pos)
    
    if cs_pos != -1 and ce_pos != -1:
        new_cards = generate_overview_cards()
        html = html[:cs_pos + len(cards_start_tag)] + "\n\n" + new_cards + "\n    " + html[ce_pos:]
        print("Updated Overview Cards successfully!")
    else:
        print(f"Cards tags not found! cs_pos={cs_pos}, ce_pos={ce_pos}")

    # 2. Update all 12 detail wraps
    details_start_tag = '<div id="details-container">'
    details_end_tag = '</div>\n\n  </div>\n\n  <!-- Lightbox Modal -->'
    
    ds_pos = html.find(details_start_tag)
    de_pos = html.find(details_end_tag, ds_pos)
    
    if ds_pos != -1 and de_pos != -1:
        all_details = []
        for ex in EXERCISES:
            all_details.append(generate_exercise_detail(ex))
        all_details_html = "\n\n".join(all_details)
        
        html = html[:ds_pos + len(details_start_tag)] + "\n\n" + all_details_html + "\n    " + html[de_pos:]
        print("Updated all 12 Detail Wraps successfully!")
    else:
        print(f"Details tags not found! ds_pos={ds_pos}, de_pos={de_pos}")

    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Master Hub lopmarketingbaitap.html written successfully!")

if __name__ == '__main__':
    main()
