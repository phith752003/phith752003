"""
=============================================================================
Module: make_stats_card.py
Mục đích: Tự động tạo stats-card.svg & languages-card.svg nội bộ
- Phong cách: Cyberpunk Crimson Red & Black (#FF1E40, #08080C)
- Thay thế hoàn toàn các dịch vụ bên thứ 3 (Vercel/Heroku) bị sập hoặc cache sai
- Tích hợp chuẩn thông số Founder Hoàng Phi (@phith752003):
  + Total Contributions: 8,246+
  + Current Streak: 250+ Days
  + Public Repositories: 8
  + Autonomous Swarms: 16 Agents
  + Global Velocity: Top Tier Conductor
  + S+ Omega Grade Conductor Badge
=============================================================================
"""

import os
import sys
import argparse

# Thiết lập UTF-8 cho console Windows
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def make_stats_card(output_svg_path: str, width: int = 430, height: int = 195) -> str:
    """
    Tạo card stats-card.svg chuẩn Cyberpunk Crimson Red & Black
    Hiển thị toàn bộ Autonomous Metrics của Founder Hoàng Phi
    """
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Filter Neon Glow cho đường viền và text highlight -->
    <filter id="crimson-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <linearGradient id="statsBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF1E40" />
      <stop offset="35%" stop-color="#4D0012" />
      <stop offset="70%" stop-color="#FF1E40" />
      <stop offset="100%" stop-color="#80001B" />
    </linearGradient>

    <linearGradient id="statsHeaderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A0A10" />
      <stop offset="50%" stop-color="#2E0A16" />
      <stop offset="100%" stop-color="#1A0A10" />
    </linearGradient>

    <linearGradient id="crimsonRingGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF1E40" />
      <stop offset="50%" stop-color="#FF4D6D" />
      <stop offset="100%" stop-color="#80001B" />
    </linearGradient>
  </defs>

  <style>
    .card-bg {{
      fill: #08080C;
    }}
    .card-border {{
      stroke: url(#statsBorderGrad);
      stroke-width: 1.5;
      fill: none;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    }}
    .title-header {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      fill: #FF1E40;
      letter-spacing: 1.2px;
    }}
    .metric-label {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 500;
      fill: #C8C8D4;
    }}
    .metric-val {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 800;
      fill: #FFFFFF;
    }}
    .hud-dim {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px;
      fill: #808095;
    }}
    @keyframes pulseNeon {{
      0%, 100% {{ opacity: 0.95; }}
      50% {{ opacity: 0.4; }}
    }}
    .live-indicator {{
      animation: pulseNeon 2s infinite ease-in-out;
    }}
  </style>

  <!-- Khung nền Card -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="8" class="card-bg" />
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="8" class="card-border" />

  <!-- Góc Cyberpunk Vát Cắt (Corner Bevels) -->
  <path d="M 2 16 L 16 2" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {width - 16} 2 L {width - 2} 16" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M 2 {height - 16} L 16 {height - 2}" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {width - 16} {height - 2} L {width - 2} {height - 16}" stroke="#FF1E40" stroke-width="2" fill="none" />

  <!-- Thanh Header Window Terminal -->
  <rect x="3" y="3" width="{width - 6}" height="30" rx="6" fill="url(#statsHeaderGrad)" />
  <line x1="3" y1="33" x2="{width - 3}" y2="33" stroke="#4D0014" stroke-width="1" />

  <!-- 3 Nút Điều Khiển Window -->
  <circle cx="18" cy="18" r="4" fill="#FF1E40" />
  <circle cx="31" cy="18" r="4" fill="#B30024" />
  <circle cx="44" cy="18" r="4" fill="#4D0012" />

  <!-- Tiêu đề Header -->
  <text x="64" y="22" class="title-header">PHITH752003 // AUTONOMOUS METRICS</text>
  <circle cx="{width - 65}" cy="18" r="3.5" fill="#00FF88" class="live-indicator" />
  <text x="{width - 55}" y="21" class="hud-dim" fill="#00FF88" font-weight="bold">SYNCED</text>

  <!-- ================= DANH SÁCH METRICS BÊN TRÁI ================= -->
  <g transform="translate(20, 42)">
    <!-- 1. Total Contributions -->
    <g transform="translate(0, 14)">
      <!-- Icon: Contribution Star / Sparkle -->
      <svg x="0" y="-11" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FF1E40" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
      </svg>
      <text x="24" y="1" class="metric-label">Total Contributions</text>
      <text x="180" y="1" class="font-mono" font-size="11" fill="#808095">:</text>
      <text x="195" y="1" class="metric-val" fill="#FF1E40">8,246+</text>
    </g>

    <!-- 2. Current Streak -->
    <g transform="translate(0, 40)">
      <!-- Icon: Lightning / Flame -->
      <svg x="0" y="-11" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FF4D6D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
      </svg>
      <text x="24" y="1" class="metric-label">Current Streak</text>
      <text x="180" y="1" class="font-mono" font-size="11" fill="#808095">:</text>
      <text x="195" y="1" class="metric-val" fill="#FF4D6D">250+ Days</text>
    </g>

    <!-- 3. Public Repositories -->
    <g transform="translate(0, 66)">
      <!-- Icon: Git Repo / Book -->
      <svg x="0" y="-11" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FF1E40" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
      </svg>
      <text x="24" y="1" class="metric-label">Public Repositories</text>
      <text x="180" y="1" class="font-mono" font-size="11" fill="#808095">:</text>
      <text x="195" y="1" class="metric-val">8</text>
    </g>

    <!-- 4. Autonomous Swarms -->
    <g transform="translate(0, 92)">
      <!-- Icon: Robot / Swarm CPU -->
      <svg x="0" y="-11" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#00FF88" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="4" y="4" width="16" height="16" rx="2"/>
        <rect x="9" y="9" width="6" height="6"/>
        <line x1="9" y1="1" x2="9" y2="4"/>
        <line x1="15" y1="1" x2="15" y2="4"/>
        <line x1="9" y1="20" x2="9" y2="23"/>
        <line x1="15" y1="20" x2="15" y2="23"/>
        <line x1="20" y1="9" x2="23" y2="9"/>
        <line x1="20" y1="14" x2="23" y2="14"/>
        <line x1="1" y1="9" x2="4" y2="9"/>
        <line x1="1" y1="14" x2="4" y2="14"/>
      </svg>
      <text x="24" y="1" class="metric-label">Autonomous Swarms</text>
      <text x="180" y="1" class="font-mono" font-size="11" fill="#808095">:</text>
      <text x="195" y="1" class="metric-val" fill="#00FF88">16 Agents</text>
    </g>

    <!-- 5. Global Velocity -->
    <g transform="translate(0, 118)">
      <!-- Icon: Activity Wave -->
      <svg x="0" y="-11" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FF1E40" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
      </svg>
      <text x="24" y="1" class="metric-label">Global Velocity</text>
      <text x="180" y="1" class="font-mono" font-size="11" fill="#808095">:</text>
      <text x="195" y="1" class="metric-val" fill="#FF8095" font-size="10.5">Top Tier Conductor</text>
    </g>
  </g>

  <!-- ================= HUY HIỆU RANK OMEGA BÊN PHẢI ================= -->
  <g transform="translate(362, 112)">
    <!-- Vòng tròn nền -->
    <circle cx="0" cy="0" r="42" fill="#100307" stroke="#2B000C" stroke-width="1.5" />
    
    <!-- Vòng tròn tiến độ Neon Crimson -->
    <circle cx="0" cy="0" r="42" fill="none" stroke="url(#crimsonRingGrad)" stroke-width="3.5"
            stroke-dasharray="230 40" stroke-dashoffset="10" stroke-linecap="round" filter="url(#crimson-glow)" />

    <!-- Vòng chấm tia Cyberpunk ngoài cùng -->
    <circle cx="0" cy="0" r="47" fill="none" stroke="#FF1E40" stroke-width="1" stroke-dasharray="3 4" opacity="0.55" />

    <!-- Nội dung Rank Badge -->
    <text x="0" y="-16" text-anchor="middle" class="hud-dim" font-weight="700" letter-spacing="1">RANK</text>
    <text x="0" y="9" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="900" fill="#FFFFFF" filter="url(#crimson-glow)">S+</text>
    <text x="0" y="24" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="800" fill="#FF1E40" letter-spacing="0.5">OMEGA TIER</text>
  </g>

  <!-- Viền góc trang trí dưới -->
  <line x1="12" y1="{height - 10}" x2="36" y2="{height - 10}" stroke="#FF1E40" stroke-width="1.5" />
  <line x1="{width - 36}" y1="{height - 10}" x2="{width - 12}" y2="{height - 10}" stroke="#FF1E40" stroke-width="1.5" />
</svg>
"""
    os.makedirs(os.path.dirname(os.path.abspath(output_svg_path)), exist_ok=True)
    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    return output_svg_path


def make_languages_card(output_svg_path: str, width: int = 430, height: int = 195) -> str:
    """
    Tạo card languages-card.svg chuẩn Cyberpunk Crimson Red & Black
    Hiển thị Tech Matrix và phân bổ ngôn ngữ lập trình của Founder Hoàng Phi
    """
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <!-- Filter Neon Glow cho đường viền và text highlight -->
    <filter id="crimson-glow-lang" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <linearGradient id="langBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF1E40" />
      <stop offset="35%" stop-color="#4D0012" />
      <stop offset="70%" stop-color="#FF1E40" />
      <stop offset="100%" stop-color="#80001B" />
    </linearGradient>

    <linearGradient id="langHeaderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A0A10" />
      <stop offset="50%" stop-color="#2E0A16" />
      <stop offset="100%" stop-color="#1A0A10" />
    </linearGradient>
  </defs>

  <style>
    .card-bg {{
      fill: #08080C;
    }}
    .card-border {{
      stroke: url(#langBorderGrad);
      stroke-width: 1.5;
      fill: none;
    }}
    .font-mono {{
      font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    }}
    .title-header {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      fill: #FF1E40;
      letter-spacing: 1.2px;
    }}
    .lang-name {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      fill: #FFFFFF;
    }}
    .lang-scope {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5px;
      font-weight: 400;
      fill: #808095;
    }}
    .lang-percent {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 800;
    }}
    .hud-dim {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px;
      fill: #808095;
    }}
    @keyframes pulseNeon {{
      0%, 100% {{ opacity: 0.95; }}
      50% {{ opacity: 0.4; }}
    }}
    .live-indicator {{
      animation: pulseNeon 2s infinite ease-in-out;
    }}
  </style>

  <!-- Khung nền Card -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="8" class="card-bg" />
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="8" class="card-border" />

  <!-- Góc Cyberpunk Vát Cắt (Corner Bevels) -->
  <path d="M 2 16 L 16 2" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {width - 16} 2 L {width - 2} 16" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M 2 {height - 16} L 16 {height - 2}" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {width - 16} {height - 2} L {width - 2} {height - 16}" stroke="#FF1E40" stroke-width="2" fill="none" />

  <!-- Thanh Header Window Terminal -->
  <rect x="3" y="3" width="{width - 6}" height="30" rx="6" fill="url(#langHeaderGrad)" />
  <line x1="3" y1="33" x2="{width - 3}" y2="33" stroke="#4D0014" stroke-width="1" />

  <!-- 3 Nút Điều Khiển Window -->
  <circle cx="18" cy="18" r="4" fill="#FF1E40" />
  <circle cx="31" cy="18" r="4" fill="#B30024" />
  <circle cx="44" cy="18" r="4" fill="#4D0012" />

  <!-- Tiêu đề Header -->
  <text x="64" y="22" class="title-header">PHITH752003 // TECH MATRIX</text>
  <circle cx="{width - 65}" cy="18" r="3.5" fill="#00FF88" class="live-indicator" />
  <text x="{width - 55}" y="21" class="hud-dim" fill="#00FF88" font-weight="bold">ACTIVE</text>

  <!-- ================= THANH TỔNG HỢP MATRIX MULTI-SEGMENT ================= -->
  <g transform="translate(20, 43)">
    <!-- Nền thanh tổng hợp (Tổng width = 390, height = 7) -->
    <rect x="0" y="0" width="390" height="7" rx="3.5" fill="#14040A" stroke="#2B000C" stroke-width="0.8" />
    
    <!-- Segment 1: Python (45.5% -> 177.5px) -->
    <rect x="0" y="0" width="177.5" height="7" rx="3.5" fill="#FF1E40" />
    <!-- Segment 2: TypeScript / JS (26.5% -> 103.4px) -->
    <rect x="178.5" y="0" width="103.4" height="7" fill="#FF4D6D" />
    <!-- Segment 3: Shell / Automation (13.0% -> 50.7px) -->
    <rect x="282.9" y="0" width="50.7" height="7" fill="#FF758F" />
    <!-- Segment 4: WebGL / HTML / CSS (9.0% -> 35.1px) -->
    <rect x="334.6" y="0" width="35.1" height="7" fill="#B30024" />
    <!-- Segment 5: Go / Rust / Kernels (6.0% -> 23.4px) -->
    <rect x="370.7" y="0" width="19.3" height="7" rx="3.5" fill="#660017" />
  </g>

  <!-- ================= DANH SÁCH CHI TIẾT NGÔN NGỮ & STACK ================= -->
  <g transform="translate(20, 60)">
    <!-- 1. Python -->
    <g transform="translate(0, 14)">
      <circle cx="4" cy="-3" r="4" fill="#FF1E40" />
      <text x="16" y="1" class="lang-name">Python</text>
      <text x="68" y="1" class="lang-scope">(Core AI Swarms &amp; Conductor)</text>
      <text x="295" y="1" class="lang-percent" fill="#FF1E40">45.5%</text>
      <!-- Mini bar -->
      <rect x="340" y="-7" width="50" height="5" rx="2.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.6" />
      <rect x="340" y="-7" width="23" height="5" rx="2.5" fill="#FF1E40" />
    </g>

    <!-- 2. TypeScript / JS -->
    <g transform="translate(0, 38)">
      <circle cx="4" cy="-3" r="4" fill="#FF4D6D" />
      <text x="16" y="1" class="lang-name">TypeScript / JS</text>
      <text x="120" y="1" class="lang-scope">(Spatial UI &amp; Next.js)</text>
      <text x="295" y="1" class="lang-percent" fill="#FF4D6D">26.5%</text>
      <!-- Mini bar -->
      <rect x="340" y="-7" width="50" height="5" rx="2.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.6" />
      <rect x="340" y="-7" width="13.5" height="5" rx="2.5" fill="#FF4D6D" />
    </g>

    <!-- 3. Shell / Automation -->
    <g transform="translate(0, 62)">
      <circle cx="4" cy="-3" r="4" fill="#FF758F" />
      <text x="16" y="1" class="lang-name">Shell / Automation</text>
      <text x="136" y="1" class="lang-scope">(CLI &amp; Kernel Hooks)</text>
      <text x="295" y="1" class="lang-percent" fill="#FF758F">13.0%</text>
      <!-- Mini bar -->
      <rect x="340" y="-7" width="50" height="5" rx="2.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.6" />
      <rect x="340" y="-7" width="6.5" height="5" rx="2.5" fill="#FF758F" />
    </g>

    <!-- 4. WebGL / HTML / SVG -->
    <g transform="translate(0, 86)">
      <circle cx="4" cy="-3" r="4" fill="#B30024" />
      <text x="16" y="1" class="lang-name">WebGL / CSS / SVG</text>
      <text x="136" y="1" class="lang-scope">(Cyberpunk Telemetry)</text>
      <text x="295" y="1" class="lang-percent" fill="#B30024">9.0%</text>
      <!-- Mini bar -->
      <rect x="340" y="-7" width="50" height="5" rx="2.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.6" />
      <rect x="340" y="-7" width="4.5" height="5" rx="2.5" fill="#B30024" />
    </g>

    <!-- 5. Go / Rust / Kernels -->
    <g transform="translate(0, 110)">
      <circle cx="4" cy="-3" r="4" fill="#660017" />
      <text x="16" y="1" class="lang-name">Go / Rust / Kernels</text>
      <text x="142" y="1" class="lang-scope">(High-Velocity Concurrency)</text>
      <text x="295" y="1" class="lang-percent" fill="#FFA6B7">6.0%</text>
      <!-- Mini bar -->
      <rect x="340" y="-7" width="50" height="5" rx="2.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.6" />
      <rect x="340" y="-7" width="3" height="5" rx="2.5" fill="#FFA6B7" />
    </g>
  </g>

  <!-- Viền góc trang trí dưới -->
  <line x1="12" y1="{height - 10}" x2="36" y2="{height - 10}" stroke="#FF1E40" stroke-width="1.5" />
  <line x1="{width - 36}" y1="{height - 10}" x2="{width - 12}" y2="{height - 10}" stroke="#FF1E40" stroke-width="1.5" />
</svg>
"""
    os.makedirs(os.path.dirname(os.path.abspath(output_svg_path)), exist_ok=True)
    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    return output_svg_path


def main():
    parser = argparse.ArgumentParser(description="Tạo card SVG stats-card và languages-card phong cách Cyberpunk")
    parser.add_argument("--outdir", default=None, help="Thư mục xuất file SVG (mặc định là thư mục gốc founder-github-profile)")
    parser.add_argument("--width", type=int, default=430, help="Chiều rộng card SVG")
    parser.add_argument("--height", type=int, default=195, help="Chiều cao card SVG")
    args = parser.parse_args()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir) if args.outdir is None else os.path.abspath(args.outdir)

    stats_svg_path = os.path.join(project_root, "stats-card.svg")
    languages_svg_path = os.path.join(project_root, "languages-card.svg")

    print("==================================================================")
    print("   AI COMPANY OS :: AUTONOMOUS STATS & TECH MATRIX CARD GENERATOR")
    print("==================================================================")
    print(f"[*] Đang tạo: {stats_svg_path}")
    make_stats_card(stats_svg_path, width=args.width, height=args.height)
    print(f"[+] Thành công: stats-card.svg ({args.width}x{args.height})")

    print(f"[*] Đang tạo: {languages_svg_path}")
    make_languages_card(languages_svg_path, width=args.width, height=args.height)
    print(f"[+] Thành công: languages-card.svg ({args.width}x{args.height})")

    print("==================================================================")
    print("[THÀNH CÔNG] Đã render đầy đủ bộ đôi SVG Metrics nội bộ!")
    print("==================================================================")


if __name__ == "__main__":
    main()
