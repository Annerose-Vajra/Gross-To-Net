import subprocess
import webbrowser
import time

# Khởi chạy uvicorn bằng subprocess
process = subprocess.Popen(["uvicorn", "src.api.main:app", "--reload"])

# Chờ 1-2 giây để server khởi động (hoặc lâu hơn nếu cần)
time.sleep(2)

# Mở trình duyệt tại địa chỉ Swagger UI
webbrowser.open("http://127.0.0.1:8000/docs")

# Đợi process uvicorn chạy mãi
process.wait()
