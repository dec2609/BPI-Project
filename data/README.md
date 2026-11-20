# Danh mục & Tài liệu Hướng dẫn Dữ liệu (Data Documentation)

Thư mục này chứa toàn bộ các tập dữ liệu phục vụ nghiên cứu **Chỉ số Hiệu quả Kinh tế tư nhân (BPI)** và **Câu hỏi nghiên cứu 3 (RQ3 - PCI, FDI & Phát triển Doanh nghiệp Tư nhân)**.

---

## 1. Cấu trúc thư mục dữ liệu

```
data/
├── raw/            # Dữ liệu thô gốc (bất biến)
├── interim/        # Dữ liệu trung gian trong quá trình chuyển đổi
├── processed/      # DỮ LIỆU ĐÃ XỬ LÝ SẴN SÀNG CHO MÔ HÌNH HÓA
│   ├── rq3_provincial_panel_pre_merger_2021_2025.csv
│   └── rq3_provincial_panel_post_merger_2021_2025.csv
└── README.md       # Tài liệu mô tả chi tiết phương pháp luận và từ điển biến
```

---

## 2. Mô tả 2 Tệp Dữ liệu Bảng (Panel Datasets)

### Tệp 1: `rq3_provincial_panel_pre_merger_2021_2025.csv`
* **Phạm vi không gian:** **63 tỉnh, thành phố trực thuộc Trung ương** trước đợt sắp xếp, sáp nhập năm 2025.
* **Thời gian:** 5 năm liên tục (**2021 – 2025**).
* **Quy mô:** **315 dòng quan sát** (63 tỉnh $\times$ 5 năm), **38 cột chỉ số**.
* **Đặc điểm:** Giữ nguyên địa giới hành chính lịch sử; phản ánh đầy đủ 10 chỉ số thành phần PCI truyền thống (2021–2024) và dữ liệu vĩ mô cấp tỉnh.

### Tệp 2: `rq3_provincial_panel_post_merger_2021_2025.csv`
* **Phạm vi không gian:** **34 đơn vị hành chính cấp tỉnh mới** (gồm 6 thành phố trực thuộc Trung ương và 28 tỉnh).
* **Thời gian:** 5 năm liên tục (**2021 – 2025**).
* **Quy mô:** **170 dòng quan sát** (34 tỉnh $\times$ 5 năm), **37 cột chỉ số**.
* **Đặc điểm:** Tái lập chuỗi thời gian lịch sử trên không gian 34 tỉnh bằng phương pháp **bình quân gia quyền chuẩn thống kê** (gia quyền theo dân số cho biến đầu người/tỷ suất; gia quyền theo số lượng doanh nghiệp hoạt động cho chỉ số PCI/BPI; cộng dồn $\sum$ cho các biến quy mô). Cung cấp đầy đủ **9 chỉ số thành phần của phiên bản PCI 2.0**.

---

## 3. Từ điển Dữ liệu (Data Dictionary)

### Nhóm 1: Định danh, Không gian & Phân loại
| Tên cột | Kiểu | Đơn vị | Mô tả |
| :--- | :--- | :--- | :--- |
| `province_key` | Chuỗi | - | Mã định danh chuẩn hóa của tỉnh (chỉ có ở file trước sáp nhập) |
| `province_name` | Chuỗi | - | Tên tỉnh/thành phố trước sáp nhập |
| `post_merger_province` | Chuỗi | - | Tên tỉnh/thành phố sau sáp nhập (34 tỉnh) |
| `year` | Số nguyên | Năm | Năm quan sát (2021, 2022, 2023, 2024, 2025) |
| `region_7` | Chuỗi | - | 7 vùng kinh tế - văn hóa xã hội (ĐBSH, TDMNPB, BTB, DHNTB, TN, ĐNB, ĐBSCL) |
| `merger_status` | Chuỗi | - | Phân loại: `Không biến động (Giữ nguyên)` (11 tỉnh) hoặc `Có biến động (Sáp nhập)` (23 tỉnh) |
| `constituent_provinces` | Chuỗi | - | Danh sách các tỉnh cũ cấu thành (chỉ có ở file sau sáp nhập) |
| `constituent_provinces_count` | Số nguyên | Tỉnh | Số lượng tỉnh cũ hợp thành (1, 2 hoặc 3 tỉnh) |

### Nhóm 2: Kinh tế Vĩ mô & Dân số
| Tên cột | Kiểu | Đơn vị | Mô tả | Nguồn gốc |
| :--- | :--- | :--- | :--- | :--- |
| `population_thousand` | Số thực | Nghìn người | Dân số trung bình trong năm của địa phương | Niên giám TCTK |
| `grdp_per_capita_million_vnd` | Số thực | Triệu VNĐ | Tổng sản phẩm trên địa bàn (GRDP) bình quân đầu người | Niên giám TCTK |
| `grdp_total_billion_vnd` | Số thực | Tỷ VNĐ | Tổng giá trị GRDP trên địa bàn | Tính toán: $(\text{GRDP/người} \times \text{Dân số})/1000$ |

### Nhóm 3: Đầu tư Trực tiếp Nước ngoài (FDI) & Đầu tư Công
| Tên cột | Kiểu | Đơn vị | Mô tả | Nguồn gốc |
| :--- | :--- | :--- | :--- | :--- |
| `fdi_registered_total_musd` | Số thực | Triệu USD | Tổng vốn FDI đăng ký cấp mới, tăng thêm và góp vốn mua CP | Cục Đầu tư nước ngoài (FIA) / TCTK |
| `fdi_new_projects` | Số nguyên | Dự án | Số lượng dự án FDI được cấp phép mới trong năm | Niên giám TCTK / FIA |
| `fdi_per_1000_enterprises_musd` | Số thực | Triệu USD/1000 DN | Vốn FDI đăng ký trên 1.000 doanh nghiệp đang hoạt động | Tính toán: $(\text{FDI} / \text{DN hoạt động}) \times 1000$ |
| `public_investment_billion_vnd` | Số thực | Tỷ VNĐ | Vốn đầu tư phát triển từ nguồn NSNN do địa phương quản lý | Quyết toán NSNN & Niên giám TCTK |

### Nhóm 4: Di cư & Lực lượng Lao động
| Tên cột | Kiểu | Đơn vị | Mô tả | Nguồn gốc |
| :--- | :--- | :--- | :--- | :--- |
| `in_migration_rate_permille` | Số thực | Phần nghìn (‰) | Tỷ suất nhập cư (số người nhập cư trên 1.000 dân) | Niên giám TCTK / Báo cáo Di cư |
| `out_migration_rate_permille` | Số thực | Phần nghìn (‰) | Tỷ suất xuất cư (số người rời đi trên 1.000 dân) | Niên giám TCTK / Báo cáo Di cư |
| `net_migration_rate_permille` | Số thực | Phần nghìn (‰) | Tỷ suất di cư thuần = Nhập cư trừ Xuất cư | Tính toán |
| `total_labor_in_enterprises` | Số nguyên | Người | Tổng số lao động làm việc trong các doanh nghiệp hoạt động | Niên giám TCTK (mục Doanh nghiệp) |

### Nhóm 5: Cấu trúc Quy mô Doanh nghiệp
| Tên cột | Kiểu | Đơn vị | Mô tả quy mô (Nghị định 80/2021/NĐ-CP) |
| :--- | :--- | :--- | :--- |
| `enterprises_active_total` | Số nguyên | Doanh nghiệp | Tổng số DN đang hoạt động tại thời điểm 31/12 hàng năm |
| `enterprises_newly_registered` | Số nguyên | Doanh nghiệp | Số doanh nghiệp đăng ký thành lập mới trong năm |
| `enterprises_micro` | Số nguyên | Doanh nghiệp | Doanh nghiệp siêu nhỏ (< 10 lao động) |
| `enterprises_small` | Số nguyên | Doanh nghiệp | Doanh nghiệp nhỏ (10 đến 49 lao động) |
| `enterprises_medium` | Số nguyên | Doanh nghiệp | Doanh nghiệp quy mô vừa (50 đến 299 lao động) |
| `enterprises_sme_total` | Số nguyên | Doanh nghiệp | **Tổng số doanh nghiệp SME** = Siêu nhỏ + Nhỏ + Vừa (< 300 người) |
| `enterprises_large` | Số nguyên | Doanh nghiệp | Doanh nghiệp quy mô lớn ($\ge 300$ lao động) |

> **Bảo toàn thống kê:** `enterprises_sme_total` + `enterprises_large` = `enterprises_active_total`.

### Nhóm 6: Bộ Chỉ số Năng lực Cạnh tranh (PCI 2.0 - 9 Chỉ số thành phần)
*(Xuất hiện trong file sau sáp nhập 34 tỉnh)*:
* `pci_2_composite_score`: Điểm PCI tổng hợp (0 – 100).
* `pci2_1_market_entry`: Gia nhập thị trường (1 – 10).
* `pci2_2_resource_access`: Tiếp cận nguồn lực (đất đai, mặt bằng, tín dụng) (1 – 10).
* `pci2_3_transparency`: Tính minh bạch & công khai thông tin (1 – 10).
* `pci2_4_administrative_compliance`: Chi phí tuân thủ thủ tục hành chính & thanh tra (1 – 10).
* `pci2_5_informal_charges`: Chi phí không chính thức (bôi trơn) (1 – 10).
* `pci2_6_fair_competition`: Cạnh tranh bình đẳng (giữa tư nhân với DNNN/FDI) (1 – 10).
* `pci2_7_business_support`: Chính sách hỗ trợ doanh nghiệp & xúc tiến (1 – 10).
* `pci2_8_legal_institutions`: Thiết chế pháp lý & an ninh trật tự (1 – 10).
* `pci2_9_enabling_governance`: Chính quyền kiến tạo, năng động & tháo gỡ (1 – 10).

*(Trong file trước sáp nhập, gồm `pci_total` và 10 chỉ số thành phần `pci_1` đến `pci_10` theo chuẩn VCCI 2021–2024).*

### Nhóm 7: Chỉ số Hiệu quả Kinh tế tư nhân (BPI - Business Performance Index)
* `bpi_private_sector_growth`: Chiều cạnh 1 - Sự phát triển của khu vực tư nhân (mật độ DN trên dân số, tỷ lệ tăng trưởng DN, khả năng tạo việc làm).
* `bpi_innovation`: Chiều cạnh 2 - Đổi mới sáng tạo & Chuyển đổi số khu vực tư nhân (ứng dụng công nghệ, năng lực R&D).
* `bpi_composite`: Chỉ số BPI tổng hợp = $0,55 \times \text{Tăng trưởng} + 0,45 \times \text{Đổi mới}$.

---

## 4. Phương pháp luận Tổng hợp Không gian (Aggregation Methodology)

Khi chuyển dịch từ 63 tỉnh cũ sang 34 tỉnh mới cho các năm lịch sử (2021–2024), quy tắc bảo toàn được áp dụng:

1. **Biến tổng lượng (Extensive sums):**
   $$\text{Biến tổng}_{\text{cụm}} = \sum_{i \in \text{cụm}} \text{Biến tổng}_i$$
   *(Đảm bảo tổng toàn quốc của 34 tỉnh bằng chính xác 100% tổng của 63 tỉnh cũ).*

2. **Biến cường độ / bình quân đầu người (Population-weighted averages):**
   $$\text{GRDP/người}_{\text{cụm}} = \frac{\sum_{i} (\text{GRDP/người}_i \times \text{Dân số}_i)}{\sum_i \text{Dân số}_i}$$

3. **Biến điểm số khảo sát doanh nghiệp (Firm-weighted averages):**
   $$\text{PCI}_{\text{cụm}} = \sum_{i} \left( \text{PCI}_i \times \frac{\text{Số DN hoạt động}_i}{\sum \text{Số DN hoạt động}} \right)$$

---

## 5. Hướng dẫn Đọc dữ liệu mẫu

### Python (pandas)
```python
import pandas as pd

# 1. Đọc dữ liệu 34 tỉnh sau sáp nhập
df_post = pd.read_csv("data/processed/rq3_provincial_panel_post_merger_2021_2025.csv")

# Xem tương quan giữa 9 chỉ số PCI 2.0 và BPI tổng hợp năm 2025
pci_cols = [c for c in df_post.columns if c.startswith("pci2_")]
corrs = df_post[df_post["year"] == 2025][pci_cols + ["bpi_composite"]].corr()["bpi_composite"]
print(corrs.sort_values(ascending=False))
```

### R
```r
library(tidyverse)
df_post <- read_csv("data/processed/rq3_provincial_panel_post_merger_2021_2025.csv")
glimpse(df_post)
```
