# main.py - Điểm khởi đầu của hệ thống Ticketing API

from fastapi import FastAPI
from ticketing_app import routes  # Import phần định nghĩa API routes (các đường dẫn)

# Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title="Ticketing API",           # Tên hiển thị trong Swagger UI
    description="API cho hệ thống mua vé và quản lý vé", 
    version="1.0.0"
)

# Đăng ký router (nơi định nghĩa các API endpoint)
# Router được viết trong file routes.py
app.include_router(routes.router, prefix="/api", tags=["Ticketing"])

# Nếu chạy trực tiếp file main.py thì khởi động server
# uvicorn sẽ là web server chạy FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("ticketing_app.main:_
