"""
=============================================================================
Module: generate_all.py
Mục đích: Orchestrator tự động tạo trọn bộ Cyberpunk Crimson Assets:
1. data/hero.png: Avatar demo Cyberpunk Matrix (hoặc tối ưu ảnh thật có sẵn)
2. founder-ascii.svg: ASCII Art Matrix Terminal Cyberpunk Crimson
3. info-card.svg: Neofetch Terminal System Spec Card
4. contrib-heatmap.svg: 53-tuần Cyberpunk Crimson GitHub Heatmap
=============================================================================
"""

import os
import sys
import argparse

# Thiết lập bảng mã UTF-8 cho Windows Console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Đảm bảo đường dẫn import tương đối từ thư mục scripts
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.insert(0, CURRENT_DIR)

from prep_photo import generate_demo_hero_avatar
from make_ascii_svg import make_ascii_svg
from make_info_card import make_info_card
from render_heatmap_svg import render_heatmap_svg
from make_stats_card import make_stats_card, make_languages_card


def ensure_banner_capsule(output_path: str):
    """Tạo file banner-capsule.svg nếu chưa có"""
    content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 220" width="900" height="220">
  <defs>
    <filter id="crimsonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="bannerBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#08080C" />
      <stop offset="35%" stop-color="#14060B" />
      <stop offset="70%" stop-color="#1F040C" />
      <stop offset="100%" stop-color="#08080C" />
    </linearGradient>
    <linearGradient id="venomWave" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#330009" stop-opacity="0" />
      <stop offset="25%" stop-color="#800018" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#FF1E40" stop-opacity="0.85" />
      <stop offset="75%" stop-color="#B30024" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#330009" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="60%" stop-color="#FFE5EA" />
      <stop offset="100%" stop-color="#FF4D6D" />
    </linearGradient>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#330009" />
      <stop offset="20%" stop-color="#FF1E40" />
      <stop offset="50%" stop-color="#FF8095" />
      <stop offset="80%" stop-color="#FF1E40" />
      <stop offset="100%" stop-color="#330009" />
    </linearGradient>
  </defs>
  <style>
    .glow-title { font-family: 'JetBrains Mono', sans-serif; font-weight: 900; font-size: 38px; letter-spacing: 5px; fill: url(#textGrad); }
    .glow-sub { font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 13.5px; letter-spacing: 4px; fill: #FF1E40; }
    .telemetry { font-family: 'JetBrains Mono', monospace; font-size: 10px; fill: #858599; letter-spacing: 1px; }
  </style>
  <rect x="2" y="2" width="896" height="216" rx="14" fill="url(#bannerBg)" stroke="url(#borderGrad)" stroke-width="1.8" />
  <g opacity="0.18">
    <line x1="0" y1="40" x2="900" y2="40" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="0" y1="80" x2="900" y2="80" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="0" y1="120" x2="900" y2="120" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="0" y1="160" x2="900" y2="160" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="0" y1="200" x2="900" y2="200" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="100" y1="0" x2="100" y2="220" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="250" y1="0" x2="250" y2="220" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="450" y1="0" x2="450" y2="220" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="650" y1="0" x2="650" y2="220" stroke="#FF1E40" stroke-width="0.8" />
    <line x1="800" y1="0" x2="800" y2="220" stroke="#FF1E40" stroke-width="0.8" />
  </g>
  <path d="M -50 180 Q 200 40 450 140 T 950 80" fill="none" stroke="url(#venomWave)" stroke-width="3" filter="url(#crimsonGlow)" />
  <path d="M -50 120 Q 220 200 480 90 T 950 160" fill="none" stroke="url(#venomWave)" stroke-width="1.8" filter="url(#crimsonGlow)" opacity="0.7" />
  <g transform="translate(68, 62)">
    <polygon points="48,4 92,28 92,76 48,100 4,76 4,28" stroke="#FF1E40" stroke-width="2" fill="#17040A" filter="url(#crimsonGlow)" />
    <polygon points="48,16 80,34 80,70 48,88 16,70 16,34" stroke="#800018" stroke-width="1" fill="#0D0206" />
    <circle cx="48" cy="52" r="16" fill="#FF1E40" filter="url(#crimsonGlow)" />
    <circle cx="48" cy="52" r="8" fill="#FFFFFF" />
  </g>
  <g transform="translate(195, 82)">
    <text x="0" y="0" class="telemetry">AI_COMPANY_OS // NEURAL_ORCHESTRATION_CORE</text>
    <text x="0" y="42" class="glow-title">HOÀNG PHI</text>
    <text x="0" y="70" class="glow-sub">CHIEF CONDUCTOR • ARCHITECT OF AUTONOMOUS EMPIRES</text>
  </g>
  <path d="M 2 24 L 24 2" stroke="#FF1E40" stroke-width="2.5" fill="none" />
  <path d="M 876 2 L 898 24" stroke="#FF1E40" stroke-width="2.5" fill="none" />
  <path d="M 2 196 L 24 218" stroke="#FF1E40" stroke-width="2.5" fill="none" />
  <path d="M 876 218 L 898 196" stroke="#FF1E40" stroke-width="2.5" fill="none" />
  <line x1="30" y1="184" x2="870" y2="184" stroke="#330814" stroke-width="1" />
  <text x="35" y="202" class="telemetry">CORE_FREQUENCY: 5.8 GHz // NEURAL_SYNC: 99.98%</text>
  <text x="450" y="202" class="telemetry" text-anchor="middle">KERNEL: ANTIGRAVITY v2.0 // GEMINI 3.8 SWARMS</text>
  <text x="865" y="202" class="telemetry" text-anchor="end" fill="#00FF88">TELEMETRY: STABLE [ONLINE]</text>
</svg>"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description="Sinh trọn bộ Cyberpunk Crimson Assets cho Founder GitHub Profile")
    parser.add_argument("--image", default=None, help="Đường dẫn tới ảnh chân dung thật (mặc định data/hero.png)")
    parser.add_argument("--username", default="phith752003", help="GitHub username")
    parser.add_argument("--token", default=None, help="GitHub Token (tùy chọn)")
    parser.add_argument("--outdir", default=PROJECT_ROOT, help="Thư mục xuất file SVG")
    args = parser.parse_args()

    out_dir = os.path.abspath(args.outdir)
    os.makedirs(out_dir, exist_ok=True)
    data_dir = os.path.join(out_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    print("==================================================================")
    print("   AI COMPANY OS :: FOUNDER CYBERPUNK CRIMSON GENERATOR")
    print("   Founder: HOÀNG PHI (Chief Conductor)")
    print("==================================================================")

    # 1. Khởi tạo / Chuẩn bị Hero Image
    hero_path = args.image
    if not hero_path:
        hero_path = os.path.join(data_dir, "hero.png")

    if not os.path.exists(hero_path):
        print(f"[*] Chưa tìm thấy ảnh chân dung tại '{hero_path}'.")
        print("[*] Tự động sinh ảnh mẫu Cyberpunk Avatar Matrix Demo...")
        generate_demo_hero_avatar(hero_path)
        print(f"[+] Đã tạo ảnh demo thành công: {hero_path}")
    else:
        print(f"[+] Sử dụng ảnh chân dung: {hero_path}")

    # 2. Sinh founder-ascii.svg
    # Đồng bộ kích thước chuẩn: width=430, height=510 để vừa khớp với info-card.svg
    ascii_svg_path = os.path.join(out_dir, "founder-ascii.svg")
    print("[*] Đang chuyển đổi ảnh sang Cyberpunk ASCII Matrix SVG...")
    make_ascii_svg(
        input_image_path=hero_path,
        output_svg_path=ascii_svg_path,
        target_width=58,
        font_size=9.8,
        line_height=11.2,
        canvas_width=430,
        canvas_height=510,
    )
    print(f"[+] Đã xuất file: {ascii_svg_path}")

    # 3. Sinh info-card.svg
    info_card_path = os.path.join(out_dir, "info-card.svg")
    print("[*] Đang render Neofetch Terminal Cyberpunk Info Card...")
    make_info_card(
        output_svg_path=info_card_path,
        width=430,
        height=510,
    )
    print(f"[+] Đã xuất file: {info_card_path}")

    # 4. Sinh contrib-heatmap.svg
    token = args.token or os.environ.get("GITHUB_TOKEN")
    heatmap_path = os.path.join(out_dir, "contrib-heatmap.svg")
    print("[*] Đang render Biểu đồ đóng góp Cyberpunk Crimson Heatmap...")
    render_heatmap_svg(
        output_path=heatmap_path,
        username=args.username,
        token=token,
        width=890,
        height=240,
    )
    print(f"[+] Đã xuất file: {heatmap_path}")

    # 5. Kiểm tra banner-capsule.svg
    banner_path = os.path.join(out_dir, "banner-capsule.svg")
    if not os.path.exists(banner_path):
        print("[*] Đang khởi tạo Cinematic Banner Capsule...")
        ensure_banner_capsule(banner_path)
        print(f"[+] Đã xuất file: {banner_path}")

    # 6. Sinh stats-card.svg
    stats_path = os.path.join(out_dir, "stats-card.svg")
    print("[*] Đang render Cyberpunk Autonomous Stats Card...")
    make_stats_card(stats_path, width=430, height=195)
    print(f"[+] Đã xuất file: {stats_path}")

    # 7. Sinh languages-card.svg
    lang_path = os.path.join(out_dir, "languages-card.svg")
    print("[*] Đang render Cyberpunk Tech Matrix & Languages Card...")
    make_languages_card(lang_path, width=430, height=195)
    print(f"[+] Đã xuất file: {lang_path}")

    print("==================================================================")
    print("[THÀNH CÔNG] Toàn bộ assets đã sẵn sàng cho README.md!")
    print("==================================================================")


if __name__ == "__main__":
    main()
