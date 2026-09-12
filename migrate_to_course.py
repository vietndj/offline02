# -*- coding: utf-8 -*-
"""
MIGRATE ALL 9 LESSONS + MASTER HUB TO REPO COURSE
Shorten filenames to ~4 words
Update links in voice-over-cho-nguoi-moi.html#sec-scripts
"""

import os
import shutil
import re

COURSE_DIR = "/Users/vietmac/Documents/CODE/course"
GITHUB_COURSE_DIR = "/Users/vietmac/Documents/CODE/vietndj.github.io/course"
GITHUB_ROOT_DIR = "/Users/vietmac/Documents/CODE/vietndj.github.io"
OFFLINE_DIR = "/Users/vietmac/Documents/CODE/offline02"

MAPPING = {
    "9_kich_ban_thuc_chien.html": "9-bai-tap-thuc-hanh.html",
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

print("1. Copying and updating Master Hub and 9 lesson files...")

for old_name, new_name in MAPPING.items():
    src_file = os.path.join(GITHUB_ROOT_DIR, old_name)
    if not os.path.exists(src_file):
        src_file = os.path.join(OFFLINE_DIR, old_name)
    
    with open(src_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Update internal references within the HTML
    content = content.replace("9_kich_ban_thuc_chien.html", "9-bai-tap-thuc-hanh.html")
    for o, n in MAPPING.items():
        content = content.replace(o, n)

    # Save to COURSE_DIR
    dst_course = os.path.join(COURSE_DIR, new_name)
    with open(dst_course, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Saved to course/: {new_name}")

    # Save to GITHUB_COURSE_DIR
    os.makedirs(GITHUB_COURSE_DIR, exist_ok=True)
    dst_gh_course = os.path.join(GITHUB_COURSE_DIR, new_name)
    with open(dst_gh_course, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Saved to vietndj.github.io/course/: {new_name}")

    # Save to OFFLINE_DIR
    dst_offline = os.path.join(OFFLINE_DIR, new_name)
    with open(dst_offline, "w", encoding="utf-8") as f:
        f.write(content)

print("\n2. Updating voice-over-cho-nguoi-moi.html in both locations...")

def update_voiceover_page(filepath):
    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Update hub link
    text = text.replace("https://fedu.vn/9_kich_ban_thuc_chien.html", "https://fedu.vn/course/9-bai-tap-thuc-hanh.html")
    text = text.replace("9_kich_ban_thuc_chien.html", "9-bai-tap-thuc-hanh.html")

    # Update each lesson link
    for old_file, new_file in MAPPING.items():
        old_url = f"https://fedu.vn/{old_file}"
        new_url = f"https://fedu.vn/course/{new_file}"
        text = text.replace(old_url, new_url)
        # Also relative or other forms
        text = text.replace(f"href=\"{old_file}\"", f"href=\"{new_file}\"")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  ✓ Updated: {filepath}")

update_voiceover_page(os.path.join(COURSE_DIR, "voice-over-cho-nguoi-moi.html"))
update_voiceover_page(os.path.join(GITHUB_COURSE_DIR, "voice-over-cho-nguoi-moi.html"))

print("\n3. Creating root alias / forwarder for backward compatibility...")
root_hub_alias = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Chuyển Hướng Đến 9 Bài Tập Thực Hành Tại Lớp</title>
  <meta http-equiv="refresh" content="0; URL='course/9-bai-tap-thuc-hanh.html'" />
  <script>window.location.href = "course/9-bai-tap-thuc-hanh.html";</script>
</head>
<body>
  <p>Đang chuyển hướng đến <a href="course/9-bai-tap-thuc-hanh.html">9 Bài Tập Thực Hành Tại Lớp</a>...</p>
</body>
</html>
"""
with open(os.path.join(GITHUB_ROOT_DIR, "9_kich_ban_thuc_chien.html"), "w", encoding="utf-8") as f:
    f.write(root_hub_alias)
print("  ✓ Created alias at vietndj.github.io/9_kich_ban_thuc_chien.html -> course/9-bai-tap-thuc-hanh.html")

print("\nAll tasks completed cleanly!")
