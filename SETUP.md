# 🔴 HƯỚNG DẪN TRIỂN KHAI GITHUB PROFILE CYBERPUNK CRIMSON
### DÀNH CHO FOUNDER HOÀNG PHI (CHIEF CONDUCTOR)

Tài liệu này hướng dẫn chi tiết cách sử dụng, tùy biến ảnh chân dung thực tế và đẩy toàn bộ profile phong cách **Cyberpunk Crimson (Red & Black Edition)** lên trang cá nhân GitHub [phith752003/phith752003](https://github.com/phith752003).

---

## 📁 1. Cấu Trúc Thư Mục Dự Án

```
founder-github-profile/
├── .github/
│   └── workflows/
│       └── update.yml           # GitHub Actions tự động cập nhật profile mỗi ngày
├── data/
│   └── hero.png                 # Ảnh chân dung gốc (mặc định là avatar cyberpunk mẫu)
├── scripts/
│   ├── requirements.txt         # Thư viện phụ thuộc (Pillow, requests)
│   ├── prep_photo.py            # Xử lý ảnh (Contrast, Sharpness, CLAHE S-curve)
│   ├── make_ascii_svg.py        # Chuyển ảnh thành ASCII Matrix Terminal Crimson Neon
│   ├── make_info_card.py        # Render Neofetch Terminal Card thông số Conductor
│   ├── render_heatmap_svg.py    # Render biểu đồ đóng góp 53 tuần Cyberpunk
│   └── generate_all.py          # Script tổng hợp chạy 1 lệnh tạo trọn bộ assets
├── banner-capsule.svg           # Banner Cinematic Capsule Venom Đỏ - Đen
├── founder-ascii.svg            # Card ma trận chân dung ASCII (430x510)
├── info-card.svg                # Card Neofetch Terminal System Specs (430x510)
├── contrib-heatmap.svg          # Ma trận đóng góp 5 cấp độ màu Đỏ Neon (890x240)
├── README.md                    # File Profile Readme chính thức
└── SETUP.md                     # Tài liệu hướng dẫn này
```

---

## ⚡ 2. Cài Đặt Môi Trường Ban Đầu

Mở **PowerShell** hoặc **Terminal** tại thư mục dự án và chạy:

```bash
# 1. Chuyển vào thư mục dự án
cd "C:\Users\Admin\Desktop\all companies\founder-github-profile"

# 2. Cài đặt các thư viện phụ thuộc
pip install -r scripts/requirements.txt
```

---

## 📸 3. Cách Đổi Ảnh Chân Dung Thật

Mặc định, hệ thống đã sinh sẵn một ảnh avatar Cyberpunk Vector tại `data/hero.png`. Khi Founder muốn sử dụng ảnh chân dung thật:

1. **Chuẩn bị ảnh:** Chọn một bức ảnh chân dung góc chụp rõ mặt (nền tối hoặc nền đơn sắc sẽ cho kết quả ASCII đẹp nhất).
2. **Cách 1 - Ghi đè file:**
   - Đổi tên ảnh chân dung của bạn thành `hero.png`.
   - Copy đè vào thư mục `data/hero.png`.
   - Chạy lệnh tổng hợp:
     ```bash
     python scripts/generate_all.py
     ```
3. **Cách 2 - Chỉ định đường dẫn ảnh bất kỳ:**
   ```bash
   python scripts/generate_all.py --image "C:\duong-dan\toi\anh-cua-ban.jpg"
   ```
4. **Kết quả:** Script sẽ tự động cân bằng độ sáng, tăng tương phản, áp dụng bộ lọc hạt ma trận và xuất ra file `founder-ascii.svg` mới toanh với độ chi tiết cao và hiệu ứng quét tia CRT rực rỡ.

---

## 🛠️ 4. Tùy Biến Thông Số Trong `info-card.svg`

Nếu Founder muốn cập nhật thêm kỹ năng, chức danh hoặc thông số kỹ thuật Neofetch:
- Mở file `scripts/make_info_card.py`.
- Chỉnh sửa các dòng trong mục `Chi tiết Thông Số Neofetch` (Founder, Role, OS, Kernel, Stack, Mission...).
- Chạy lại:
  ```bash
  python scripts/make_info_card.py
  ```

---

## 🚀 5. Đẩy Lên GitHub Cá Nhân (`phith752003/phith752003`)

Để biến giao diện này thành trang chủ GitHub Profile của bạn:

### Bước 5.1: Special Repository trên GitHub
1. Đăng nhập vào [GitHub](https://github.com) với tài khoản **phith752003**.
2. Truy cập [New Repository](https://github.com/new).
3. Tại ô **Repository name**, nhập chính xác: `phith752003`.
   - GitHub sẽ hiển thị thông báo: *"✨ You found a secret! phith752003/phith752003 is a special repository that you can use to add a README.md to your GitHub profile."*
4. Đặt chế độ **Public** (Bắt buộc để hiển thị trên profile).
5. Không cần tích "Add a README file" (vì đã có sẵn bộ này).
6. Nhấn **Create repository**.

### Bước 5.2: Khởi tạo Git và Push từ máy tính
Chạy các lệnh sau trong thư mục `founder-github-profile`:

```bash
# Khởi tạo git local
git init

# Đổi nhánh mặc định thành main
git branch -M main

# Thêm remote SSH chính thức
git remote add origin git@github.com:phith752003/phith752003.git
# Hoặc nếu dùng HTTPS:
# git remote set-url origin https://github.com/phith752003/phith752003.git

# Thêm toàn bộ file
git add .

# Commit
git commit -m "feat: Cyberpunk Crimson GitHub Profile for Hoang Phi (@phith752003)"

# Đẩy lên GitHub
git push -u origin main
```

---

## 🤖 6. Cơ Chế Tự Động Cập Nhật (GitHub Actions)

File `.github/workflows/update.yml` đã được cấu hình sẵn:
- **Tần suất chạy:** 00:00 UTC mỗi ngày (tự động cập nhật heatmap và stats mới nhất).
- **Thao tác thủ công:** Có thể vào tab **Actions** trên GitHub và nhấn **Run workflow** bất cứ lúc nào.
- **Quyền hạn cần thiết:** Trên GitHub repo, vào **Settings** ➔ **Actions** ➔ **General** ➔ mục **Workflow permissions**, chọn **"Read and write permissions"** rồi nhấn **Save**.

---

## 🎨 7. Bảng Mã Màu Cyberpunk Crimson Chuẩn

| Vai Trò | Mã Màu Hex | Mô Tả |
| :--- | :--- | :--- |
| **Nền Đen Tuyệt Đối** | `#08080C` | Dark Matte OLED chống mỏi mắt |
| **Đỏ Crimson Neon** | `#FF1E40` | Màu chủ đạo cho viền, tiêu đề & điểm nhấn |
| **Đỏ Rực Neon** | `#FF0033` | Cấp độ commit cao nhất và hiệu ứng cảnh báo |
| **Hồng Ngọc Neon** | `#FF4D6D` | Dùng cho text highlight và tiến trình năng lượng |
| **Đỏ Nhung Trầm** | `#990022` | Khối màu mức trung bình và hoa văn chìm |
| **Đỏ Bóng Đêm** | `#4D0012` | Nền thanh header và đường kẻ vi mạch |
| **Xanh Sinh Thái Cyber** | `#00FF88` | Đèn tín hiệu trạng thái LIVE / ACTIVE |

---

*Hệ thống được phát triển bởi **dev_coder** — Đội ngũ kỹ sư tự hành của **AI Company OS**.*
