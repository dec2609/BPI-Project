# BPI Project: Business Performance Index & Provincial Economic Analytics

Nghiên cứu định lượng về **Chỉ số Hiệu quả Kinh tế tư nhân (BPI)** và mối liên hệ giữa cải thiện các chỉ số thành phần năng lực cạnh tranh (**PCI / PCI 2.0**) với kết quả kinh tế khu vực tư nhân tại Việt Nam (giai đoạn 2021–2025).

---

## 1. Dữ liệu Nghiên cứu Chính (Key Datasets)

Bộ dữ liệu bảng đã xử lý hoàn chỉnh nằm tại `data/processed/`:

* **[Tệp 1 - Trước sáp nhập (63 tỉnh/thành, 2021–2025)](data/processed/rq3_provincial_panel_pre_merger_2021_2025.csv):**
  * `315` dòng quan sát (63 tỉnh $\times$ 5 năm), `38` biến số.
  * Địa giới hành chính lịch sử; đầy đủ 10 chỉ số thành phần PCI cũ (2021–2024), GRDP đầu người, FDI, di cư & lao động, đầu tư công, cấu trúc quy mô DN (SME, lớn).

* **[Tệp 2 - Sau sáp nhập (34 tỉnh/thành, 2021–2025)](data/processed/rq3_provincial_panel_post_merger_2021_2025.csv):**
  * `170` dòng quan sát (34 đơn vị hành chính mới $\times$ 5 năm), `37` biến số.
  * Tái lập không gian 34 tỉnh bằng phương pháp bình quân gia quyền theo quy mô doanh nghiệp và dân số.
  * Bao gồm đầy đủ **9 chỉ số thành phần của phiên bản PCI 2.0** (`pci2_1_market_entry` đến `pci2_9_enabling_governance`) và 2 chiều cạnh đo lường của **Chỉ số BPI** (`bpi_private_sector_growth`, `bpi_innovation`, `bpi_composite`).

> Xem hướng dẫn chi tiết và từ điển biến tại **[data/README.md](data/README.md)**.

---

## 2. Cấu trúc thư mục dự án

```
BPI project/
├── data/
│   ├── processed/
│   │   ├── rq3_provincial_panel_pre_merger_2021_2025.csv
│   │   └── rq3_provincial_panel_post_merger_2021_2025.csv
│   └── README.md              # Từ điển biến & phương pháp luận chi tiết
├── src/
│   ├── build_rq3_data.py      # ETL pipeline tái lập tự động từ NSO/VCCI
│   ├── data_loader.py
│   ├── processing.py
│   └── utils.py
├── notebooks/                 # Phân tích mô tả & hồi quy bảng (Panel regression)
├── tests/                     # Kiểm thử tính toàn vẹn dữ liệu
└── requirements.txt
```

---

## 3. Khởi chạy nhanh (Quickstart)

1. Thiết lập môi trường ảo:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```
2. Cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy lại pipeline dữ liệu nếu cần trích xuất cập nhật:
   ```bash
   python src/build_rq3_data.py
   ```
