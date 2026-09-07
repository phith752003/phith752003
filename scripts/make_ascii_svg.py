"""
=============================================================================
Module: make_ascii_svg.py
Mục đích: Chuyển đổi ảnh chân dung thành Cyberpunk Matrix ASCII Art SVG
- Tông màu: Đỏ Crimson Neon (#FF1E40, #FF0033) trên nền Dark Matte OLED (#08080C)
- Hiệu ứng: Scanline động (CSS keyframes), CRT scanline bar, Neon glow filter
- Khung giao diện: Terminal Cyberpunk HUD chuẩn Founder Hoàng Phi
=============================================================================
"""

import os
import sys
import html
from PIL import Image

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from prep_photo import prepare_image_for_ascii, generate_demo_hero_avatar


# Bảng ký tự ASCII phân cấp theo mật độ pixel và phong cách Matrix Cyberpunk
ASCII_RAMP = " .:-=+*#%@"
# Thêm bảng ký tự Matrix Hex độc đáo
MATRIX_GLYPHS = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def pixel_to_matrix_char(pixel_val: int) -> str:
    """Ánh xạ giá trị độ sáng 0-255 sang ký tự Matrix Cyberpunk"""
    ramp = "@%#*+=-:. " # Đảo ngược nếu nền đen: ký tự dày hơn ở vùng sáng
    ramp = " .:-=+*#%@"
    idx = int((pixel_val / 255.0) * (len(ramp) - 1))
    return ramp[idx]


def get_color_for_brightness(brightness: int) -> str:
    """Trả về mã màu Crimson Neon tương ứng với độ sáng của pixel"""
    if brightness > 210:
        return "#FFFFFF"  # Điểm phản quang cực sáng
    elif brightness > 165:
        return "#FF4D6D"  # Hồng ngọc Crimson Neon rực rỡ
    elif brightness > 115:
        return "#FF1E40"  # Đỏ Crimson Neon chủ đạo
    elif brightness > 65:
        return "#B30024"  # Đỏ nhung Crimson sâu
    elif brightness > 25:
        return "#590014"  # Đỏ bóng đêm
    else:
        return "#260009"  # Nền tối vi mạch


def make_ascii_svg(
    input_image_path: str,
    output_svg_path: str,
    target_width: int = 58,
    font_size: int = 9.8,
    line_height: int = 11.2,
    canvas_width: int = 430,
    canvas_height: int = 510,
) -> str:
    """
    Sinh file founder-ascii.svg với đồ họa Cyberpunk Crimson cao cấp,
    chuẩn hóa kích thước 430x510 để đồng bộ hoàn hảo với info-card.svg
    """
    if not os.path.exists(input_image_path):
        os.makedirs(os.path.dirname(input_image_path), exist_ok=True)
        generate_demo_hero_avatar(input_image_path)

    # 1. Tiền xử lý ảnh thành grayscale matrix với chiều cao vừa khít
    img = prepare_image_for_ascii(
        input_image_path,
        target_width=target_width,
        aspect_ratio_correction=0.52,
        contrast=2.0,
        sharpness=2.2,
    )
    w, h = img.size

    # Cố định số dòng tối đa 37 dòng để không vượt quá canvas_height
    max_lines = 37
    if h > max_lines:
        img = img.crop((0, 0, w, max_lines))
        h = max_lines

    # 2. Xây dựng các dòng text ASCII với span màu neon
    lines_svg = []
    char_width = 6.1
    content_width = w * char_width
    start_x = max(16, int((canvas_width - content_width) / 2))
    start_y = 66

    for y in range(h):
        line_elements = []
        cur_color = None
        cur_chunk = []
        pos_y = int(start_y + (y * line_height))

        for x in range(w):
            brightness = img.getpixel((x, y))
            char = pixel_to_matrix_char(brightness)
            if char == " ":
                char = " "

            color = get_color_for_brightness(brightness)

            if color != cur_color:
                if cur_chunk:
                    text_content = html.escape("".join(cur_chunk))
                    line_elements.append(
                        f'<tspan fill="{cur_color}">{text_content}</tspan>'
                    )
                    cur_chunk = []
                cur_color = color

            cur_chunk.append(char)

        if cur_chunk:
            text_content = html.escape("".join(cur_chunk))
            line_elements.append(f'<tspan fill="{cur_color}">{text_content}</tspan>')

        line_str = f'<text x="{start_x}" y="{pos_y}" class="ascii-line">{"".join(line_elements)}</text>'
        lines_svg.append(line_str)

    ascii_body = "\n    ".join(lines_svg)
    svg_width = canvas_width
    svg_height = canvas_height

    # 3. Tạo template SVG hoàn chỉnh với CSS @keyframes và hiệu ứng scanline
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
  <defs>
    <!-- Bộ lọc Neon Glow -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="red-tint" x="0%" y="0%" width="100%" height="100%">
      <feColorMatrix type="matrix" values="
        1 0 0 0 0.4
        0 0 0 0 0.05
        0 0 0 0 0.1
        0 0 0 1 0" />
    </filter>

    <!-- Gradient viền và thanh tiêu đề -->
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1A0A10" />
      <stop offset="50%" stop-color="#2D0B16" />
      <stop offset="100%" stop-color="#1A0A10" />
    </linearGradient>

    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF1E40" />
      <stop offset="40%" stop-color="#4D0012" />
      <stop offset="70%" stop-color="#FF1E40" />
      <stop offset="100%" stop-color="#80001B" />
    </linearGradient>

    <linearGradient id="scanlineGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="rgba(255, 30, 64, 0)" />
      <stop offset="50%" stop-color="rgba(255, 30, 64, 0.25)" />
      <stop offset="100%" stop-color="rgba(255, 30, 64, 0)" />
    </linearGradient>
  </defs>

  <style>
    .terminal-bg {{
      fill: #08080C;
    }}
    .terminal-border {{
      stroke: url(#borderGrad);
      stroke-width: 1.5;
      fill: none;
    }}
    .ascii-text {{
      font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
      font-size: {font_size}px;
      letter-spacing: 0px;
      font-weight: 600;
    }}
    .title-text {{
      font-family: 'JetBrains Mono', 'Consolas', monospace;
      font-size: 11px;
      font-weight: 700;
      fill: #FF1E40;
      letter-spacing: 1.5px;
    }}
    .hud-sub {{
      font-family: 'JetBrains Mono', 'Consolas', monospace;
      font-size: 9px;
      fill: #808090;
    }}

    /* CSS Keyframes cho tia quét scanline */
    @keyframes scanlineAnim {{
      0% {{ transform: translateY(40px); opacity: 0.1; }}
      50% {{ opacity: 0.7; }}
      100% {{ transform: translateY({svg_height - 40}px); opacity: 0.1; }}
    }}

    @keyframes pulseLive {{
      0% {{ opacity: 0.3; }}
      50% {{ opacity: 1.0; }}
      100% {{ opacity: 0.3; }}
    }}

    @keyframes glitchBorder {{
      0%, 100% {{ stroke-opacity: 0.9; }}
      92% {{ stroke-opacity: 0.9; }}
      93% {{ stroke-opacity: 0.3; stroke: #FF4D6D; }}
      94% {{ stroke-opacity: 1.0; stroke: #FFFFFF; }}
      95% {{ stroke-opacity: 0.9; stroke: #FF1E40; }}
    }}

    .scanline-bar {{
      animation: scanlineAnim 4.5s linear infinite;
    }}
    .live-dot {{
      animation: pulseLive 1.8s ease-in-out infinite;
    }}
    .terminal-box {{
      animation: glitchBorder 8s ease-in-out infinite;
    }}
  </style>

  <!-- Khung Nền Terminal Cyberpunk -->
  <rect x="2" y="2" width="{svg_width - 4}" height="{svg_height - 4}" rx="8" class="terminal-bg" />
  <rect x="2" y="2" width="{svg_width - 4}" height="{svg_height - 4}" rx="8" class="terminal-border terminal-box" />

  <!-- Góc Cyberpunk Vát Cắt Cách Điệu (Corner Accents) -->
  <path d="M 2 18 L 18 2" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {svg_width - 18} 2 L {svg_width - 2} 18" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M 2 {svg_height - 18} L 18 {svg_height - 2}" stroke="#FF1E40" stroke-width="2" fill="none" />
  <path d="M {svg_width - 18} {svg_height - 2} L {svg_width - 2} {svg_height - 18}" stroke="#FF1E40" stroke-width="2" fill="none" />

  <!-- Thanh Tiêu Đề Header Terminal -->
  <rect x="3" y="3" width="{svg_width - 6}" height="32" rx="6" fill="url(#headerGrad)" />
  <line x1="3" y1="36" x2="{svg_width - 3}" y2="36" stroke="#4D0014" stroke-width="1" />

  <!-- 3 Nút Điều Khiển Terminal (Cyberpunk Crimson Theme) -->
  <circle cx="18" cy="19" r="4.5" fill="#FF1E40" />
  <circle cx="32" cy="19" r="4.5" fill="#B30024" />
  <circle cx="46" cy="19" r="4.5" fill="#4D0012" />

  <!-- Tiêu đề Terminal -->
  <text x="70" y="23" class="title-text">[FOUNDER_CORE_MATRIX :: HOANG_PHI_V3.8]</text>

  <!-- Live Status Pulse Badge -->
  <circle cx="{svg_width - 80}" cy="19" r="3.5" fill="#00FF88" class="live-dot" />
  <text x="{svg_width - 70}" y="22" class="hud-sub" fill="#00FF88" font-weight="bold">ONLINE</text>

  <!-- Nội Dung Ký Tự ASCII -->
  <g class="ascii-text" xml:space="preserve">
    {ascii_body}
  </g>

  <!-- Tia Quét Scanline CRT chạy dọc -->
  <g>
    <rect x="4" y="0" width="{svg_width - 8}" height="14" fill="url(#scanlineGrad)" class="scanline-bar" pointer-events="none" />
  </g>

  <!-- Footer HUD Bar -->
  <line x1="12" y1="{svg_height - 24}" x2="{svg_width - 12}" y2="{svg_height - 24}" stroke="#2D0B16" stroke-width="1" />
  <text x="18" y="{svg_height - 10}" class="hud-sub">SYS_STATE: AUTONOMOUS CONDUCTOR</text>
  <text x="{svg_width - 130}" y="{svg_height - 10}" class="hud-sub">0xPHI_CORE // ACTIVE</text>
</svg>
"""

    os.makedirs(os.path.dirname(output_svg_path), exist_ok=True)
    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    return output_svg_path


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    hero_img = os.path.join(base_dir, "..", "data", "hero.png")
    output_svg = os.path.join(base_dir, "..", "founder-ascii.svg")
    make_ascii_svg(hero_img, output_svg)
    print(f"[OK] Đã tạo thành công file: {output_svg}")
