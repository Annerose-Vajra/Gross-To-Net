# Gross-To-Net

**Gross-To-Net** là một ứng dụng Python được phát triển trong khuôn khổ chương trình thực tập tại AvePoint. Dự án này nhằm mục đích tính toán lương **net** (lương thực nhận) từ lương **gross** (lương tổng) dựa trên các quy định về thuế và bảo hiểm tại Việt Nam.

## 📁 Cấu trúc thư mục
```
Gross-To-Net/ ├── src/ │ └── ... # Mã nguồn chính
              ├── run_and_open.py # Script chính để chạy ứng dụng 
              ├── output_with_net_salary.xlsx # Kết quả xuất ra dưới dạng Excel
              ├── .env # Biến môi trường (ví dụ: cấu hình) 
              ├── pyproject.toml # Cấu hình dự án (sử dụng Poetry)
```
## 🚀 Hướng dẫn sử dụng

### 1. Cài đặt Poetry (nếu chưa có)

```bash
pip install poetry
poetry install
poetry run python run_and_open.py
```
⚙️ Các tính năng chính
Tính toán lương net từ lương gross dựa trên các khoản khấu trừ như:

Bảo hiểm xã hội (Social Insurance)

Bảo hiểm y tế (Health Insurance)

Bảo hiểm thất nghiệp (Unemployment Insurance)

Thuế thu nhập cá nhân (Personal Income Tax)

Xuất kết quả ra file Excel để dễ dàng theo dõi và chia sẻ.

🧪 Môi trường phát triển
Python 3.11

Poetry (quản lý gói và môi trường ảo)

Các thư viện khác được liệt kê trong pyproject.toml
