# Telegram Bot + Web System

## Cấu trúc dự án

### Frontend (GitHub Pages)
- `index.html` - Trang chủ câu chuyện
- `vip1.html` - Gallery 1
- `vip2.html` - Gallery 2  
- `vip3.html` - Trang bảo trì
- `login.html` - Đăng nhập
- `admin.html` - Quản lý keys

### Backend (Railway/Render/PythonAnywhere)
- `bot.py` - Telegram bot + HTTP server + API

## Deploy Backend

### Railway.app (Đề xuất)
1. Tạo tài khoản tại [railway.app](https://railway.app)
2. New Project → Deploy from GitHub repo
3. Chọn repo này
4. Railway tự động detect Python và chạy

### Render.com
1. Tạo tài khoản tại [render.com](https://render.com)
2. New → Web Service
3. Connect GitHub repo
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python bot.py`

### PythonAnywhere
1. Tạo tài khoản tại [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload code
3. Setup Web App với Python 3.11
4. Configure WSGI

## Cấu hình

1. Lấy URL backend sau khi deploy (VD: `https://your-app.railway.app`)
2. Cập nhật API endpoint trong các file HTML từ `http://localhost:3000` → URL backend
3. Deploy frontend lên GitHub Pages

## Chạy local

```bash
python bot.py
```

Server chạy tại: http://localhost:3000
