"""
=============================================================================
Module: make_info_card.py
Mục đích: Tạo file info-card.svg chuẩn Neofetch Terminal Cyberpunk Red & Black
- Thể hiện vai trò Founder Hoàng Phi: Chief Conductor của AI Company OS
- Thông số kỹ thuật: Kernel, Shell, Tech Stack, Agent Swarms, Mission
- Thanh tiến trình năng lượng Neural Bandwidth & Swarm Capacity
- Bảng màu Cyberpunk Terminal Color Blocks
=============================================================================
"""

import os
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def make_info_card(output_svg_path: str, width: int = 430, height: int = 510) -> str:
    """
    Sinh card SVG Neofetch phong cách Cyberpunk Crimson chuẩn 430x510
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

    <linearGradient id="infoBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF1E40" />
      <stop offset="35%" stop-color="#4D0012" />
      <stop offset="70%" stop-color="#FF1E40" />
      <stop offset="100%" stop-color="#80001B" />
    </linearGradient>

    <linearGradient id="infoHeaderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A0A10" />
      <stop offset="50%" stop-color="#2E0A16" />
      <stop offset="100%" stop-color="#1A0A10" />
    </linearGradient>

    <linearGradient id="barGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#B30024" />
      <stop offset="80%" stop-color="#FF1E40" />
      <stop offset="100%" stop-color="#FF4D6D" />
    </linearGradient>

    <linearGradient id="barGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#80001B" />
      <stop offset="80%" stop-color="#FF0033" />
      <stop offset="100%" stop-color="#FF8095" />
    </linearGradient>
  </defs>

  <style>
    .card-bg {{
      fill: #08080C;
    }}
    .card-border {{
      stroke: url(#infoBorderGrad);
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
      letter-spacing: 1.5px;
    }}
    .key-label {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 700;
      fill: #FF1E40;
    }}
    .value-text {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 400;
      fill: #E2E2E8;
    }}
    .value-bold {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      fill: #FFFFFF;
    }}
    .separator {{
      stroke: #330A14;
      stroke-width: 1;
    }}
    .hud-dim {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px;
      fill: #808095;
    }}
    .prompt-symbol {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 800;
      fill: #00FF88;
    }}

    @keyframes pulseNeon {{
      0%, 100% {{ opacity: 0.9; }}
      50% {{ opacity: 0.5; }}
    }}
    .live-indicator {{
      animation: pulseNeon 2s infinite ease-in-out;
    }}
  </style>

  <!-- Khung nền Card -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="8" class="card-bg" />
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="8" class="card-border" />

  <!-- Góc Cyberpunk Vát Cắt (Corner Bevels) -->
  <path d="M 2 18 L 18 2" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {width - 18} 2 L {width - 2} 18" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M 2 {height - 18} L 18 {height - 2}" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {width - 18} {height - 2} L {width - 2} {height - 18}" stroke="#FF1E40" stroke-width="2" fill="none" />

  <!-- Thanh Header Cửa Sổ -->
  <rect x="3" y="3" width="{width - 6}" height="32" rx="6" fill="url(#infoHeaderGrad)" />
  <line x1="3" y1="36" x2="{width - 3}" y2="36" stroke="#4D0014" stroke-width="1" />

  <!-- 3 Nút Điều Khiển Window -->
  <circle cx="18" cy="19" r="4.5" fill="#FF1E40" />
  <circle cx="32" cy="19" r="4.5" fill="#B30024" />
  <circle cx="46" cy="19" r="4.5" fill="#4D0012" />

  <text x="70" y="23" class="title-header">SYSTEM_PROBE // NEOFETCH_V3.8</text>
  <circle cx="{width - 80}" cy="19" r="3.5" fill="#00FF88" class="live-indicator" />
  <text x="{width - 70}" y="22" class="hud-dim" fill="#00FF88" font-weight="bold">ACTIVE</text>

  <!-- Terminal Command Execution Header -->
  <g transform="translate(20, 56)">
    <text x="0" y="0" class="prompt-symbol">❯</text>
    <text x="14" y="0" class="font-mono" font-size="11.5" fill="#FF4D6D" font-weight="bold">neofetch</text>
    <text x="82" y="0" class="font-mono" font-size="11.5" fill="#888899">--target founder.phith752003</text>
  </g>

  <!-- Dòng phân cách Header -->
  <line x1="20" y1="68" x2="{width - 20}" y2="68" class="separator" />

  <!-- Mini ASCII Emblem / Logo AI Company OS -->
  <g transform="translate(20, 84)">
    <!-- Logo Hexagon Cyberpunk với lõi hạt nhân -->
    <polygon points="28,2 54,16 54,46 28,60 2,46 2,16" stroke="#FF1E40" stroke-width="1.5" fill="#14040A" />
    <polygon points="28,12 44,22 44,40 28,50 12,40 12,22" stroke="#B30024" stroke-width="1" fill="#200008" />
    <circle cx="28" cy="31" r="5" fill="#FF1E40" filter="url(#crimson-glow)" />
    <!-- Chữ viết tắt HP Core -->
    <text x="21" y="34" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="900" fill="#FFFFFF">HP</text>

    <text x="70" y="18" class="font-mono" font-size="14" font-weight="800" fill="#FFFFFF">phith752003<tspan fill="#FF1E40">@</tspan><tspan fill="#FF4D6D">conductor-core</tspan></text>
    <line x1="70" y1="26" x2="{width - 40}" y2="26" stroke="#590014" stroke-width="1.2" stroke-dasharray="3,3" />
    <text x="70" y="42" class="hud-dim">UPTIME: 365 DAYS 24/7 (AUTONOMOUS)</text>
    <text x="70" y="55" class="hud-dim">ORGANIZATION: AI COMPANY OS EMPIRE</text>
  </g>

  <!-- Chi tiết Thông Số Neofetch -->
  <g transform="translate(20, 168)">
    <!-- 1. Founder -->
    <text x="0" y="0" class="key-label">Founder</text>
    <text x="85" y="0" class="value-text">: <tspan class="value-bold">Hoàng Phi (phith752003)</tspan> <tspan fill="#FF1E40">(Chief Conductor)</tspan></text>

    <!-- 2. Role -->
    <text x="0" y="24" class="key-label">Role</text>
    <text x="85" y="24" class="value-text">: <tspan fill="#FF4D6D">AI Orchestrator &amp; Architect</tspan></text>

    <!-- 3. OS -->
    <text x="0" y="48" class="key-label">OS</text>
    <text x="85" y="48" class="value-text">: AI Company OS <tspan fill="#808095">(Autonomous Edition)</tspan></text>

    <!-- 4. Kernel -->
    <text x="0" y="72" class="key-label">Kernel</text>
    <text x="85" y="72" class="value-text">: <tspan fill="#00FF88">Antigravity</tspan> / Gemini 3.8 Multi-Agent</text>

    <!-- 5. Shell -->
    <text x="0" y="96" class="key-label">Shell</text>
    <text x="85" y="96" class="value-text">: Jarvis Flow / Paperclip C-Suite</text>

    <!-- 6. Stack -->
    <text x="0" y="120" class="key-label">Stack</text>
    <text x="85" y="120" class="value-text">: Python, TypeScript, React, Three.js</text>

    <!-- 7. Swarms -->
    <text x="0" y="144" class="key-label">Swarms</text>
    <text x="85" y="144" class="value-text">: 12 Autonomous Agents Active</text>

    <!-- 8. Mission -->
    <text x="0" y="168" class="key-label">Mission</text>
    <text x="85" y="168" class="value-text">: <tspan fill="#FF4D6D" font-weight="600">Orchestrating Autonomous AI Empires</tspan></text>
  </g>

  <!-- Phần Tiến Trình Hệ Thống (Resource Gauges) -->
  <g transform="translate(20, 360)">
    <line x1="0" y1="0" x2="{width - 40}" y2="0" class="separator" />

    <!-- Neural Bandwidth Bar -->
    <text x="0" y="18" class="hud-dim" fill="#E2E2E8">Neural Bandwidth:</text>
    <text x="{width - 80}" y="18" class="hud-dim" fill="#FF4D6D" font-weight="bold">88.5%</text>
    <rect x="0" y="24" width="{width - 40}" height="7" rx="3.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.8" />
    <rect x="1" y="25" width="{int((width - 42) * 0.885)}" height="5" rx="2.5" fill="url(#barGrad)" />

    <!-- Swarm Sync Ratio Bar -->
    <text x="0" y="48" class="hud-dim" fill="#E2E2E8">Agent Swarm Sync:</text>
    <text x="{width - 80}" y="48" class="hud-dim" fill="#00FF88" font-weight="bold">97.2%</text>
    <rect x="0" y="54" width="{width - 40}" height="7" rx="3.5" fill="#1A0A10" stroke="#330A14" stroke-width="0.8" />
    <rect x="1" y="55" width="{int((width - 42) * 0.972)}" height="5" rx="2.5" fill="url(#barGrad2)" />
  </g>

  <!-- Bảng Màu Cyberpunk Palette (Color Blocks chuẩn Neofetch) -->
  <g transform="translate(20, 442)">
    <!-- Hàng 1: Màu Tối & Crimson -->
    <rect x="0"   y="0" width="22" height="12" rx="2" fill="#08080C" stroke="#2D0B16" />
    <rect x="28"  y="0" width="22" height="12" rx="2" fill="#38000D" />
    <rect x="56"  y="0" width="22" height="12" rx="2" fill="#660017" />
    <rect x="84"  y="0" width="22" height="12" rx="2" fill="#990022" />
    <rect x="112" y="0" width="22" height="12" rx="2" fill="#CC002E" />
    <rect x="140" y="0" width="22" height="12" rx="2" fill="#FF1E40" />
    <rect x="168" y="0" width="22" height="12" rx="2" fill="#FF4D6D" />
    <rect x="196" y="0" width="22" height="12" rx="2" fill="#FFA6B7" />

    <!-- Nhãn Footer Góc Phải -->
    <text x="{width - 40}" y="10" class="hud-dim" text-anchor="end">AI_COMPANY_OS // KERNEL v3.8</text>
  </g>

  <!-- Viền góc trang trí dưới -->
  <line x1="10" y1="{height - 12}" x2="30" y2="{height - 12}" stroke="#FF1E40" stroke-width="2" />
  <line x1="{width - 30}" y1="{height - 12}" x2="{width - 10}" y2="{height - 12}" stroke="#FF1E40" stroke-width="2" />
</svg>
"""

    os.makedirs(os.path.dirname(output_svg_path), exist_ok=True)
    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    return output_svg_path


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    output_svg = os.path.join(base_dir, "..", "info-card.svg")
    make_info_card(output_svg)
    print(f"[OK] Đã tạo thành công file: {output_svg}")
