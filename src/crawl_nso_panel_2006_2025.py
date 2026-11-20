"""
THU THẬP VÀ XÂY DỰNG BỘ DỮ LIỆU BẢNG 63 TỈNH THÀNH (2006 - 2025)
TỪ 4 CUỐN NIÊN GIÁM THỐNG KÊ QUỐC GIA CHÍNH THỨC (GSO / NSO):
1. Niên giám 2025: https://www.nso.gov.vn/wp-content/uploads/2026/07/NG-TOAN-QUOC-2025-1.pdf
2. Niên giám 2019: https://www.nso.gov.vn/wp-content/uploads/2020/09/Nien-giam-thong-ke-day-du-2019.pdf
3. Niên giám 2014: https://www.nso.gov.vn/wp-content/uploads/2019/10/Nien-giam-2014-pdf.pdf
4. Niên giám 2009: https://www.nso.gov.vn/wp-content/uploads/2026/01/Niengiam2009_watermark.pdf

Đặc điểm:
- 1 script duy nhất, cấu trúc rõ ràng, không phức tạp hóa.
- Quét đúng trang bảng số liệu của từng cuốn, gán đúng cột và năm tương ứng.
- Toàn bộ tên cột bằng Tiếng Việt chuẩn.
- Các năm/chỉ số không có trong niên giám được ghi rõ là 'miss'.
"""

import sys
import re
import urllib.request
import ssl
from pathlib import Path
import unicodedata
import pandas as pd
import pymupdf

BASE_DIR = Path(r"c:\Users\user\Documents\GitHub\VietLeap_Decision_Research\validation_4rq_2026-11-20\raw\yearbooks")
BASE_DIR.mkdir(parents=True, exist_ok=True)

OUT_CSV_1 = Path(r"c:\Users\user\Documents\GitHub\BPI project\data\processed\nso_panel_63_provinces_2006_2025.csv")
OUT_CSV_2 = Path(r"c:\Users\user\Documents\GitHub\VietLeap_Decision_Research\nso_panel_63_provinces_2006_2025.csv")
OUT_CSV_1.parent.mkdir(parents=True, exist_ok=True)

PDF_URLS = {
    "NSO_2025.pdf": "https://www.nso.gov.vn/wp-content/uploads/2026/07/NG-TOAN-QUOC-2025-1.pdf",
    "NSO_2019.pdf": "https://www.nso.gov.vn/wp-content/uploads/2020/09/Nien-giam-thong-ke-day-du-2019.pdf",
    "NSO_2014.pdf": "https://www.nso.gov.vn/wp-content/uploads/2019/10/Nien-giam-2014-pdf.pdf",
    "NSO_2009.pdf": "https://www.nso.gov.vn/wp-content/uploads/2026/01/Niengiam2009_watermark.pdf"
}

def ensure_pdfs():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for name, url in PDF_URLS.items():
        p = BASE_DIR / name
        if not p.exists() or p.stat().st_size < 1000000:
            print(f"Đang tải {name}...")
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120, context=ctx) as resp, open(p, "wb") as f:
                while chunk := resp.read(1024 * 1024):
                    f.write(chunk)
            print(f"-> Hoàn thành tải {name}")

PROVINCES = [
    ('hanoi', 'Hà Nội', 'Đồng bằng sông Hồng'),
    ('vinhphuc', 'Vĩnh Phúc', 'Đồng bằng sông Hồng'),
    ('bacninh', 'Bắc Ninh', 'Đồng bằng sông Hồng'),
    ('quangninh', 'Quảng Ninh', 'Đồng bằng sông Hồng'),
    ('haiduong', 'Hải Dương', 'Đồng bằng sông Hồng'),
    ('haiphong', 'Hải Phòng', 'Đồng bằng sông Hồng'),
    ('hungyen', 'Hưng Yên', 'Đồng bằng sông Hồng'),
    ('thaibinh', 'Thái Bình', 'Đồng bằng sông Hồng'),
    ('hanam', 'Hà Nam', 'Đồng bằng sông Hồng'),
    ('namdinh', 'Nam Định', 'Đồng bằng sông Hồng'),
    ('ninhbinh', 'Ninh Bình', 'Đồng bằng sông Hồng'),
    ('hagiang', 'Hà Giang', 'Trung du và miền núi phía Bắc'),
    ('caobang', 'Cao Bằng', 'Trung du và miền núi phía Bắc'),
    ('backan', 'Bắc Kạn', 'Trung du và miền núi phía Bắc'),
    ('tuyenquang', 'Tuyên Quang', 'Trung du và miền núi phía Bắc'),
    ('laocai', 'Lào Cai', 'Trung du và miền núi phía Bắc'),
    ('yenbai', 'Yên Bái', 'Trung du và miền núi phía Bắc'),
    ('thainguyen', 'Thái Nguyên', 'Trung du và miền núi phía Bắc'),
    ('langson', 'Lạng Sơn', 'Trung du và miền núi phía Bắc'),
    ('bacgiang', 'Bắc Giang', 'Trung du và miền núi phía Bắc'),
    ('phutho', 'Phú Thọ', 'Trung du và miền núi phía Bắc'),
    ('dienbien', 'Điện Biên', 'Trung du và miền núi phía Bắc'),
    ('laichau', 'Lai Châu', 'Trung du và miền núi phía Bắc'),
    ('sonla', 'Sơn La', 'Trung du và miền núi phía Bắc'),
    ('hoabinh', 'Hòa Bình', 'Trung du và miền núi phía Bắc'),
    ('thanhhoa', 'Thanh Hóa', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('nghean', 'Nghệ An', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('hatinh', 'Hà Tĩnh', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('quangbinh', 'Quảng Bình', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('quangtri', 'Quảng Trị', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('thuathienhue', 'Thừa Thiên Huế', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('danang', 'Đà Nẵng', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('quangnam', 'Quảng Nam', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('quangngai', 'Quảng Ngãi', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('binhdinh', 'Bình Định', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('phuyen', 'Phú Yên', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('khanhhoa', 'Khánh Hòa', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('ninhthuan', 'Ninh Thuận', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('binhthuan', 'Bình Thuận', 'Bắc Trung Bộ và Duyên hải miền Trung'),
    ('kontum', 'Kon Tum', 'Tây Nguyên'),
    ('gialai', 'Gia Lai', 'Tây Nguyên'),
    ('daklak', 'Đắk Lắk', 'Tây Nguyên'),
    ('daknong', 'Đắk Nông', 'Tây Nguyên'),
    ('lamdong', 'Lâm Đồng', 'Tây Nguyên'),
    ('binhphuoc', 'Bình Phước', 'Đông Nam Bộ'),
    ('tayninh', 'Tây Ninh', 'Đông Nam Bộ'),
    ('binhduong', 'Bình Dương', 'Đông Nam Bộ'),
    ('dongnai', 'Đồng Nai', 'Đông Nam Bộ'),
    ('bariavungtau', 'Bà Rịa - Vũng Tàu', 'Đông Nam Bộ'),
    ('tphochiminh', 'TP. Hồ Chí Minh', 'Đông Nam Bộ'),
    ('longan', 'Long An', 'Đồng bằng sông Cửu Long'),
    ('tiengiang', 'Tiền Giang', 'Đồng bằng sông Cửu Long'),
    ('bentre', 'Bến Tre', 'Đồng bằng sông Cửu Long'),
    ('travinh', 'Trà Vinh', 'Đồng bằng sông Cửu Long'),
    ('vinhlong', 'Vĩnh Long', 'Đồng bằng sông Cửu Long'),
    ('dongthap', 'Đồng Tháp', 'Đồng bằng sông Cửu Long'),
    ('angiang', 'An Giang', 'Đồng bằng sông Cửu Long'),
    ('kiengiang', 'Kiên Giang', 'Đồng bằng sông Cửu Long'),
    ('cantho', 'Cần Thơ', 'Đồng bằng sông Cửu Long'),
    ('haugiang', 'Hậu Giang', 'Đồng bằng sông Cửu Long'),
    ('soctrang', 'Sóc Trăng', 'Đồng bằng sông Cửu Long'),
    ('baclieu', 'Bạc Liêu', 'Đồng bằng sông Cửu Long'),
    ('camau', 'Cà Mau', 'Đồng bằng sông Cửu Long')
]

PROV_KEYS = {p[0]: p[0] for p in PROVINCES}

TCVN3_MAP = {
    'hnei': 'hanoi', 'hty': 'hatay', 'vunhphoc': 'vinhphuc', 'b34cninh': 'bacninh', 'qungninh': 'quangninh',
    'hidng': 'haiduong', 'hiphng': 'haiphong', 'hngyan': 'hungyen', 'thibnh': 'thaibinh', 'hnam': 'hanam',
    'namnh': 'namdinh', 'ninhbnh': 'ninhbinh', 'hgiang': 'hagiang', 'caobng': 'caobang', 'backan': 'backan',
    'b34ckan': 'backan', 'tuyanquang': 'tuyenquang', 'locai': 'laocai', 'yanbi': 'yenbai', 'thinguyan': 'thainguyen',
    'b34cgiang': 'bacgiang', 'photha': 'phutho', 'ionbian': 'dienbien', 'laichu': 'laichau', 'snla': 'sonla',
    'habnh': 'hoabinh', 'thanhhaa': 'thanhhoa', 'nghoan': 'nghean', 'htunh': 'hatinh', 'qungbnh': 'quangbinh',
    'qungtr': 'quangtri', 'thoathianhuo': 'thuathienhue', 'n12ng': 'danang', 'qungnam': 'quangnam',
    'qungngi': 'quangngai', 'bnhnh': 'binhdinh', 'phoyan': 'phuyen', 'khnhha': 'khanhhoa', 'ninhthuen': 'ninhthuan',
    'bnhthuen': 'binhthuan', 'kontum': 'kontum', 'gialai': 'gialai', '34kl34k': 'daklak', '34knng': 'daknong',
    'lmang': 'lamdong', 'bnhphic': 'binhphuoc', 'tyninh': 'tayninh', 'bnhdng': 'binhduong', 'angnai': 'dongnai',
    'bravongtu': 'bariavungtau', 'tphachyminh': 'tphochiminh', 'longan': 'longan', 'tiongiang': 'tiengiang',
    'bontre': 'bentre', 'trvinh': 'travinh', 'vunhlong': 'vinhlong', 'angthp': 'dongthap', 'angiang': 'angiang',
    'kiangiang': 'kiengiang', 'ccnth': 'cantho', 'heugiang': 'haugiang', 'sactrng': 'soctrang', 'bcliau': 'baclieu',
    'cmau': 'camau'
}

def match_province(text):
    s = unicodedata.normalize('NFKD', str(text).lower().replace('đ', 'd').replace('®', 'd'))
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9]', '', s)
    if 'hochiminh' in s: return 'tphochiminh'
    if 'vungtau' in s: return 'bariavungtau'
    if 'hue' in s: return 'thuathienhue'
    if s in TCVN3_MAP: return TCVN3_MAP[s]
    return PROV_KEYS.get(s, None)

def clean_val(v):
    if v is None: return "miss"
    s = str(v).strip().replace('\n', '').replace(' ', '')
    if not s or s in ['-', '...', '..', '.', 'NA', 'NaN']: return "miss"
    s = s.replace(',', '.')
    try:
        val = float(s)
        return round(val, 2)
    except:
        return "miss"

def extract_indicator(pdf_name, pages, years, target_col, panel_dict):
    doc = pymupdf.open(BASE_DIR / pdf_name)
    for p in pages:
        if p > len(doc): continue
        page = doc[p - 1]
        for b in page.get_text("blocks"):
            lines = [l.strip() for l in b[4].split("\n") if l.strip()]
            if not lines: continue
            
            i = 0
            while i < len(lines):
                pid = match_province(lines[i])
                if pid:
                    i += 1
                    nums = []
                    while i < len(lines) and not match_province(lines[i]) and not any(r in unicodedata.normalize('NFKD', lines[i].lower()) for r in ['dong bang', 'trung du', 'bac trung bo', 'tay nguyen', 'dong nam bo', 'whole country', 'ca nuoc']):
                        val = clean_val(lines[i])
                        nums.append(val)
                        i += 1
                    for y, val in zip(years, nums):
                        if (pid, y) in panel_dict and val != "miss":
                            panel_dict[(pid, y)][target_col] = val
                else:
                    i += 1

def main():
    print("=== BẮT ĐẦU THU THẬP VÀ XÂY DỰNG DỮ LIỆU BẢNG GSO 2006-2025 ===")
    ensure_pdfs()
    
    panel = {}
    years = list(range(2006, 2026))
    for pid, pname, region in PROVINCES:
        for y in years:
            panel[(pid, y)] = {
                'Năm': y,
                'Mã tỉnh': pid,
                'Tỉnh/Thành phố': pname,
                'Vùng kinh tế': region,
                'Dân số trung bình (Nghìn người)': 'miss',
                'Lực lượng lao động từ 15 tuổi trở lên (Nghìn người)': 'miss',
                'Tỷ suất nhập cư (‰)': 'miss',
                'Tỷ suất xuất cư (‰)': 'miss',
                'Tỷ suất di cư thuần (‰)': 'miss',
                'Số doanh nghiệp đang hoạt động': 'miss',
                'Số doanh nghiệp đăng ký mới': 'miss',
                'Số dự án FDI cấp mới': 'miss',
                'Vốn FDI đăng ký mới (Triệu USD)': 'miss',
                'GRDP bình quân đầu người (Triệu đồng/người)': 'miss'
            }

    # 1. Dân số trung bình (Nghìn người)
    print("1/6. Trích xuất Dân số trung bình...")
    extract_indicator("NSO_2009.pdf", [43, 44], [2005, 2006, 2007, 2008, 2009], 'Dân số trung bình (Nghìn người)', panel)
    extract_indicator("NSO_2014.pdf", [68, 69], [2010, 2011, 2012, 2013, 2014], 'Dân số trung bình (Nghìn người)', panel)
    extract_indicator("NSO_2019.pdf", [100, 101], [2015, 2016, 2017, 2018, 2019], 'Dân số trung bình (Nghìn người)', panel)
    extract_indicator("NSO_2025.pdf", [105, 106], [2020, 2022, 2023, 2024, 2025], 'Dân số trung bình (Nghìn người)', panel)

    # 2. Lực lượng lao động từ 15 tuổi trở lên (Nghìn người)
    print("2/6. Trích xuất Lực lượng lao động...")
    extract_indicator("NSO_2014.pdf", [112, 113], [2010, 2011, 2012, 2013, 2014], 'Lực lượng lao động từ 15 tuổi trở lên (Nghìn người)', panel)
    extract_indicator("NSO_2019.pdf", [152, 153], [2015, 2016, 2017, 2018, 2019], 'Lực lượng lao động từ 15 tuổi trở lên (Nghìn người)', panel)
    extract_indicator("NSO_2025.pdf", [153, 154], [2020, 2022, 2023, 2024, 2025], 'Lực lượng lao động từ 15 tuổi trở lên (Nghìn người)', panel)

    # 3. Di cư (Nhập cư, Xuất cư, Di cư thuần)
    print("3/6. Trích xuất Di cư...")
    extract_indicator("NSO_2014.pdf", [98, 99], [2010, 2011, 2012, 2013, 2014], 'Tỷ suất nhập cư (‰)', panel)
    extract_indicator("NSO_2014.pdf", [100, 101], [2010, 2011, 2012, 2013, 2014], 'Tỷ suất xuất cư (‰)', panel)
    extract_indicator("NSO_2014.pdf", [102, 103], [2010, 2011, 2012, 2013, 2014], 'Tỷ suất di cư thuần (‰)', panel)

    extract_indicator("NSO_2019.pdf", [131, 132], [2015, 2016, 2017, 2018, 2019], 'Tỷ suất nhập cư (‰)', panel)
    extract_indicator("NSO_2019.pdf", [133, 134], [2015, 2016, 2017, 2018, 2019], 'Tỷ suất xuất cư (‰)', panel)
    extract_indicator("NSO_2019.pdf", [135, 136], [2015, 2016, 2017, 2018, 2019], 'Tỷ suất di cư thuần (‰)', panel)

    extract_indicator("NSO_2025.pdf", [136, 137], [2020, 2022, 2023], 'Tỷ suất nhập cư (‰)', panel)
    extract_indicator("NSO_2025.pdf", [138, 139], [2020, 2022, 2023], 'Tỷ suất xuất cư (‰)', panel)
    extract_indicator("NSO_2025.pdf", [140, 141], [2020, 2022, 2023], 'Tỷ suất di cư thuần (‰)', panel)

    # 4. Doanh nghiệp (Đang hoạt động & Đăng ký mới)
    print("4/6. Trích xuất Doanh nghiệp...")
    extract_indicator("NSO_2009.pdf", [143, 144], [2005, 2006, 2007, 2008], 'Số doanh nghiệp đang hoạt động', panel)
    extract_indicator("NSO_2014.pdf", [230, 231], [2009, 2010, 2011, 2012, 2013], 'Số doanh nghiệp đang hoạt động', panel)
    extract_indicator("NSO_2019.pdf", [325, 326], [2010, 2015, 2016, 2017, 2018], 'Số doanh nghiệp đang hoạt động', panel)
    extract_indicator("NSO_2019.pdf", [322, 323], [2015, 2016, 2017, 2018, 2019], 'Số doanh nghiệp đăng ký mới', panel)
    extract_indicator("NSO_2025.pdf", [384, 385], [2020, 2021, 2022, 2023, 2024], 'Số doanh nghiệp đang hoạt động', panel)
    extract_indicator("NSO_2025.pdf", [379, 380], [2020, 2021, 2022, 2023, 2024], 'Số doanh nghiệp đăng ký mới', panel)

    # 5. Đầu tư trực tiếp nước ngoài (FDI)
    print("5/6. Trích xuất FDI...")
    extract_indicator("NSO_2014.pdf", [203, 204], [2010, 2011, 2012, 2013, 2014], 'Số dự án FDI cấp mới', panel)
    extract_indicator("NSO_2014.pdf", [207, 208], [2010, 2011, 2012, 2013, 2014], 'Vốn FDI đăng ký mới (Triệu USD)', panel)
    extract_indicator("NSO_2019.pdf", [281, 282], [2015, 2016, 2017, 2018, 2019], 'Số dự án FDI cấp mới', panel)
    extract_indicator("NSO_2019.pdf", [287, 288], [2015, 2016, 2017, 2018, 2019], 'Vốn FDI đăng ký mới (Triệu USD)', panel)

    # 6. GRDP bình quân đầu người
    print("6/6. Trích xuất GRDP...")
    extract_indicator("NSO_2025.pdf", [242, 243], [2020, 2021, 2022, 2023, 2024], 'GRDP bình quân đầu người (Triệu đồng/người)', panel)

    # Lưu DataFrame
    df = pd.DataFrame(list(panel.values()))
    df = df.sort_values(by=['Mã tỉnh', 'Năm'])
    
    df.to_csv(OUT_CSV_1, index=False, encoding='utf-8-sig')
    df.to_csv(OUT_CSV_2, index=False, encoding='utf-8-sig')
    
    print("\n=== THÀNH CÔNG! ĐÃ XUẤT 02 TẬP TIN DỮ LIỆU BẢNG 2006-2025 ===")
    print(f"1. {OUT_CSV_1}")
    print(f"2. {OUT_CSV_2}")
    print(f"Tổng số dòng: {len(df)} dòng (63 tỉnh x 20 năm)")
    
    print("\n=== THỐNG KÊ MỨC ĐỘ ĐẦY ĐỦ CÁC CỘT (2006 - 2025) ===")
    for col in df.columns[4:]:
        filled = (df[col] != 'miss').sum()
        total = len(df)
        pct = (filled / total) * 100
        print(f"  * {col}: {filled}/{total} ({pct:.1f}% có số liệu, {total-filled} ô ghi 'miss')")

if __name__ == "__main__":
    main()
