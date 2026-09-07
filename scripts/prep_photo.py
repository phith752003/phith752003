"""
=============================================================================
Module: prep_photo.py
Mục đích: Xử lý và tiền xử lý ảnh chân dung (Hero Photo) cho Cyberpunk Crimson Profile
- Tăng cường độ tương phản (Contrast Enhancement, Histogram Equalization / S-Curve)
- Tự động sinh ảnh avatar demo Cyberpunk nếu chưa có ảnh hero.png thực tế
- Tối ưu hóa ma trận pixel chuẩn bị chuyển đổi sang ASCII Art sắc nét
=============================================================================
"""

import os
import sys
import math
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageOps

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def generate_demo_hero_avatar(output_path: str, size: tuple = (400, 480)) -> str:
    """
    Tự động sinh ảnh chân dung Cyberpunk Matrix / Crimson Silhouette chất lượng cao
    để làm ảnh mẫu hero.png khi Founder chưa cung cấp ảnh chụp thực tế.
    """
    width, height = size
    # Nền đen OLED bóng đêm
    img = Image.new("RGB", (width, height), color=(8, 8, 12))
    draw = ImageDraw.Draw(img)

    # 1. Vẽ lưới Cyberpunk Grid nền phía sau
    grid_color = (25, 10, 18)
    step = 20
    for x in range(0, width, step):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, step):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)

    # 2. Hiệu ứng Neon Crimson Glow ở trung tâm (Backlight)
    glow_center_x, glow_center_y = width // 2, height // 2 - 20
    for r in range(160, 20, -10):
        alpha = int(45 * (1 - r / 160))
        glow_color = (min(255, 180 + alpha), min(255, int(15 + alpha * 0.4)), min(255, int(40 + alpha * 0.5)))
        draw.ellipse(
            [glow_center_x - r, glow_center_y - r, glow_center_x + r, glow_center_y + r],
            outline=glow_color,
            width=2,
        )

    # 3. Silhouette chân dung Founder Hoàng Phi (Cyberpunk Stylized Conductor)
    # Phần thân / Áo măng-tô Cyberpunk Trench Coat (Collar & Shoulders)
    coat_color = (20, 20, 28)
    shoulder_y = height - 100
    # Thân dưới
    draw.polygon(
        [
            (width // 2 - 140, height),
            (width // 2 - 110, shoulder_y + 30),
            (width // 2 - 60, shoulder_y),
            (width // 2 - 40, shoulder_y - 25),  # Cổ áo trái
            (width // 2, shoulder_y + 15),       # Cổ áo V
            (width // 2 + 40, shoulder_y - 25),  # Cổ áo phải
            (width // 2 + 60, shoulder_y),
            (width // 2 + 110, shoulder_y + 30),
            (width // 2 + 140, height),
        ],
        fill=coat_color,
        outline=(255, 30, 64),
    )

    # Cà vạt / Ve áo Crimson Neon
    draw.polygon(
        [
            (width // 2 - 12, shoulder_y + 15),
            (width // 2 + 12, shoulder_y + 15),
            (width // 2 + 8, height - 20),
            (width // 2, height),
            (width // 2 - 8, height - 20),
        ],
        fill=(180, 15, 40),
        outline=(255, 30, 64),
    )

    # Cổ (Neck)
    neck_x1, neck_x2 = width // 2 - 25, width // 2 + 25
    neck_y1, neck_y2 = shoulder_y - 45, shoulder_y + 10
    draw.rectangle([neck_x1, neck_y1, neck_x2, neck_y2], fill=(45, 45, 55))

    # Khuôn mặt (Face Silhouette)
    face_cx, face_cy = width // 2, shoulder_y - 85
    face_rx, face_ry = 48, 65
    draw.ellipse(
        [face_cx - face_rx, face_cy - face_ry, face_cx + face_rx, face_cy + face_ry],
        fill=(60, 60, 75),
        outline=(255, 50, 80),
        width=2,
    )

    # Cyberpunk Visor / Neural Glasses (Kính thực tế tăng cường Neon Crimson)
    visor_y = face_cy - 12
    visor_w = 46
    visor_h = 16
    draw.rounded_rectangle(
        [face_cx - visor_w, visor_y - visor_h // 2, face_cx + visor_w, visor_y + visor_h // 2],
        radius=4,
        fill=(255, 30, 64),
        outline=(255, 120, 150),
        width=2,
    )
    # Lằn sáng qua kính
    draw.line(
        [(face_cx - visor_w + 6, visor_y), (face_cx + visor_w - 6, visor_y)],
        fill=(255, 255, 255),
        width=2,
    )

    # Tóc Cyberpunk Slicked-back / Undercut
    hair_color = (24, 24, 32)
    hair_points = [
        (face_cx - 52, face_cy - 20),
        (face_cx - 50, face_cy - 70),
        (face_cx - 20, face_cy - 92),
        (face_cx + 15, face_cy - 96),
        (face_cx + 50, face_cy - 80),
        (face_cx + 54, face_cy - 20),
        (face_cx + 42, face_cy - 50),
        (face_cx + 10, face_cy - 72),
        (face_cx - 30, face_cy - 68),
        (face_cx - 45, face_cy - 40),
    ]
    draw.polygon(hair_points, fill=hair_color)

    # Cybernetic Neural Interface Lines (Mạch điện neon bên má & cổ)
    neon_red = (255, 30, 64)
    # Đường vi mạch bên má phải
    draw.line([(face_cx + 25, face_cy + 10), (face_cx + 38, face_cy + 18), (face_cx + 38, face_cy + 40)], fill=neon_red, width=2)
    draw.ellipse([face_cx + 36, face_cy + 40, face_cx + 40, face_cy + 44], fill=neon_red)

    # Vòng hào quang HUD / Reticle Cybernetic
    draw.arc([face_cx - 90, face_cy - 90, face_cx + 90, face_cy + 90], start=210, end=330, fill=neon_red, width=2)
    draw.arc([face_cx - 90, face_cy - 90, face_cx + 90, face_cy + 90], start=30, end=150, fill=neon_red, width=2)

    # Chỉ số HUD xung quanh
    draw.text((20, 20), "CHIEF CONDUC: HOANG_PHI", fill=(255, 30, 64))
    draw.text((20, 36), "SYSTEM: AI COMPANY OS", fill=(180, 180, 200))
    draw.text((width - 125, 20), "NEURAL: ACTIVE", fill=(255, 30, 64))
    draw.text((width - 125, 36), "STATUS: 100%", fill=(0, 255, 180))

    # Lưu ảnh
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=95)
    return output_path


def prepare_image_for_ascii(
    image_path: str,
    target_width: int = 70,
    aspect_ratio_correction: float = 0.52,
    contrast: float = 1.9,
    sharpness: float = 2.0,
) -> Image.Image:
    """
    Xử lý ảnh đầu vào:
    1. Tải ảnh (hoặc tạo ảnh demo nếu chưa có)
    2. Chuyển sang Grayscale
    3. Cân bằng tương phản và làm nét viền
    4. Resize theo tỉ lệ ký tự font monospace (chiều cao ký tự xấp xỉ gấp đôi chiều rộng)
    """
    if not os.path.exists(image_path):
        # Tự động tạo ảnh mẫu nếu đường dẫn không tồn tại
        generate_demo_hero_avatar(image_path)

    img = Image.open(image_path).convert("L")

    # Tự động crop theo tâm hình vuông hoặc chân dung nếu kích thước quá lệch
    w, h = img.size
    if h > w * 1.5:
        # Cắt bớt phần chân nếu ảnh quá dài
        img = img.crop((0, 0, w, int(w * 1.35)))
    elif w > h:
        # Cắt tâm nếu ảnh ngang
        offset = (w - h) // 2
        img = img.crop((offset, 0, offset + h, h))

    # Tăng cường độ tương phản (Contrast)
    enhancer_contrast = ImageEnhance.Contrast(img)
    img = enhancer_contrast.enhance(contrast)

    # Tăng cường độ sắc nét (Sharpness)
    enhancer_sharp = ImageEnhance.Sharpness(img)
    img = enhancer_sharp.enhance(sharpness)

    # Tính toán kích thước mới
    w, h = img.size
    target_height = int(target_width * (h / w) * aspect_ratio_correction)
    img_resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

    return img_resized


if __name__ == "__main__":
    demo_path = os.path.join(os.path.dirname(__file__), "..", "data", "hero.png")
    os.makedirs(os.path.dirname(demo_path), exist_ok=True)
    generate_demo_hero_avatar(demo_path)
    print(f"[OK] Đã khởi tạo ảnh demo hero tại: {demo_path}")
