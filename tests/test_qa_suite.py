import os
import sys
import glob
import py_compile
import xml.etree.ElementTree as ET

# Đảm bảo UTF-8 cho Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_tests():
    print("==================================================================")
    print("      QA SQUAD INDEPENDENT TEST SUITE - AI COMPANY OS")
    print("      Project: Founder GitHub Profile Cyberpunk Crimson")
    print("==================================================================")

    failures = []

    # 1. Kiểm tra cấu trúc thư mục và file bắt buộc
    print("\n[TEST 1] Kiểm tra sự tồn tại của các file bắt buộc...")
    required_files = [
        "scripts/requirements.txt",
        "scripts/prep_photo.py",
        "scripts/make_ascii_svg.py",
        "scripts/make_info_card.py",
        "scripts/render_heatmap_svg.py",
        "scripts/generate_all.py",
        "README.md",
        "SETUP.md",
        ".github/workflows/update.yml",
        "founder-ascii.svg",
        "info-card.svg",
        "contrib-heatmap.svg",
        "banner-capsule.svg"
    ]
    for rf in required_files:
        p = os.path.join(PROJECT_DIR, rf)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            print(f"  [PASS] File tồn tại ({os.path.getsize(p):>6} bytes): {rf}")
        else:
            msg = f"Thiếu file hoặc file rỗng: {rf}"
            print(f"  [FAIL] {msg}")
            failures.append(msg)

    # 2. Cú pháp Python của toàn bộ scripts
    print("\n[TEST 2] Kiểm tra cú pháp biên dịch Python (py_compile)...")
    py_files = glob.glob(os.path.join(PROJECT_DIR, "scripts", "*.py"))
    for pf in sorted(py_files):
        rel = os.path.relpath(pf, PROJECT_DIR)
        try:
            py_compile.compile(pf, doraise=True)
            print(f"  [PASS] Cú pháp Python hợp lệ: {rel}")
        except Exception as e:
            msg = f"Lỗi cú pháp Python tại {rel}: {e}"
            print(f"  [FAIL] {msg}")
            failures.append(msg)

    # 3. Phân tích cú pháp XML/SVG bằng xml.etree.ElementTree
    print("\n[TEST 3] Kiểm tra tính hợp lệ cú pháp XML/SVG (ElementTree)...")
    svg_files = ["banner-capsule.svg", "founder-ascii.svg", "info-card.svg", "contrib-heatmap.svg"]
    dims = {}
    for sf in svg_files:
        sp = os.path.join(PROJECT_DIR, sf)
        try:
            tree = ET.parse(sp)
            root = tree.getroot()
            tag = root.tag
            if not tag.endswith("svg"):
                msg = f"Root tag của {sf} không phải là svg: {tag}"
                print(f"  [FAIL] {msg}")
                failures.append(msg)
                continue
            w = root.attrib.get("width")
            h = root.attrib.get("height")
            vb = root.attrib.get("viewBox")
            dims[sf] = {"width": w, "height": h, "viewBox": vb}
            print(f"  [PASS] {sf:20} -> XML Well-formed! width={w}, height={h}, viewBox={vb}")
        except Exception as e:
            msg = f"Lỗi parse XML {sf}: {e}"
            print(f"  [FAIL] {msg}")
            failures.append(msg)

    # 4. Kiểm tra kích thước Dual Terminal (founder-ascii vs info-card)
    print("\n[TEST 4] Kiểm tra cân đối tỷ lệ hiển thị Dual Terminal...")
    f_info = dims.get("founder-ascii.svg", {})
    i_info = dims.get("info-card.svg", {})
    f_w, f_h = f_info.get("width"), f_info.get("height")
    i_w, i_h = i_info.get("width"), i_info.get("height")
    print(f"  founder-ascii.svg dimensions: {f_w}x{f_h}")
    print(f"  info-card.svg     dimensions: {i_w}x{i_h}")
    if f_w == "430" and f_h == "510" and i_w == "430" and i_h == "510":
        print("  [PASS] Cả hai card đều đạt chuẩn kích thước 430x510 tuyệt đối cân bằng!")
    else:
        msg = f"Sai lệch kích thước: founder-ascii ({f_w}x{f_h}) vs info-card ({i_w}x{i_h})"
        print(f"  [FAIL] {msg}")
        failures.append(msg)

    # 5. Kiểm tra cú pháp YAML của GitHub Actions
    print("\n[TEST 5] Kiểm tra cấu hình .github/workflows/update.yml...")
    wf_path = os.path.join(PROJECT_DIR, ".github", "workflows", "update.yml")
    try:
        import yaml
        with open(wf_path, "r", encoding="utf-8") as f:
            ydata = yaml.safe_load(f)
        job_names = list(ydata.get("jobs", {}).keys())
        print(f"  [PASS] YAML cú pháp chuẩn. Tên: '{ydata.get('name')}', Jobs: {job_names}")
    except ImportError:
        with open(wf_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        has_name = any(line.startswith("name:") for line in lines)
        has_jobs = any(line.startswith("jobs:") for line in lines)
        if has_name and has_jobs:
            print("  [PASS] update.yml cấu trúc hợp lệ (kiểm tra dòng cơ bản)")
        else:
            msg = "update.yml thiếu khai báo name hoặc jobs"
            print(f"  [FAIL] {msg}")
            failures.append(msg)
    except Exception as e:
        msg = f"Lỗi phân tích YAML update.yml: {e}"
        print(f"  [FAIL] {msg}")
        failures.append(msg)

    # 6. Kiểm tra bảng màu Cyberpunk Crimson Red & Dark Black
    print("\n[TEST 6] Kiểm tra mã màu Cyberpunk Crimson (#FF1E40 / #FF0033)...")
    for sf in svg_files:
        sp = os.path.join(PROJECT_DIR, sf)
        with open(sp, "r", encoding="utf-8") as f:
            content = f.read().upper()
        has_crimson = ("#FF1E40" in content) or ("#FF0033" in content)
        has_dark = any(k in content for k in ["#08080C", "#0A0A0C", "#14060B", "#17040A", "#0D0206", "#000"])
        if has_crimson and has_dark:
            print(f"  [PASS] {sf:20} -> Đạt chuẩn màu Crimson Red & Dark Black")
        else:
            msg = f"{sf} không chứa đầy đủ màu Crimson hoặc nền tối chuẩn (Crimson: {has_crimson}, Dark: {has_dark})"
            print(f"  [FAIL] {msg}")
            failures.append(msg)

    # 7. Kiểm tra liên kết trong README.md
    print("\n[TEST 7] Kiểm tra cấu trúc liên kết và hình ảnh trong README.md...")
    rm_path = os.path.join(PROJECT_DIR, "README.md")
    with open(rm_path, "r", encoding="utf-8") as f:
        rm_text = f.read()

    for sf in svg_files:
        ref_tag = f"./{sf}"
        if ref_tag in rm_text:
            print(f"  [PASS] README.md liên kết chính xác tới: {ref_tag}")
        else:
            msg = f"README.md thiếu liên kết tới {ref_tag}"
            print(f"  [FAIL] {msg}")
            failures.append(msg)

    # Kiểm tra các khối cấu trúc bắt buộc trong README.md
    expected_sections = [
        "banner-capsule.svg",
        "DUAL TERMINAL COMMAND DECK",
        "C-SUITE AUTONOMOUS SWARMS",
        "NEURAL ARMORY & TECH STACK",
        "AUTONOMOUS CONTRIBUTION TELEMETRY",
        "MISSION & ARCHITECTURE PHILOSOPHY",
        "NEURAL CHANNELS & TRANSMISSION NODES"
    ]
    for sec in expected_sections:
        if sec in rm_text:
            print(f"  [PASS] README.md có phân mục: '{sec}'")
        else:
            msg = f"README.md thiếu phân mục quan trọng: '{sec}'"
            print(f"  [FAIL] {msg}")
            failures.append(msg)

    # TỔNG KẾT
    print("\n==================================================================")
    if not failures:
        print(">>> KẾT QUẢ: 100% PASS - TẤT CẢ TIÊU CHÍ KIỂM ĐỊNH HOÀN TOÀN ĐẠT CHUẨN! <<<")
        print("==================================================================")
        return 0
    else:
        print(f">>> KẾT QUẢ: FAIL ({len(failures)} lỗi phát hiện) <<<")
        for f in failures:
            print(f"  - {f}")
        print("==================================================================")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
