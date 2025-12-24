# -*- coding: utf-8 -*-
import os
import sys

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

marketplace_path = r"c:\Users\Hi\Downloads\web mới\marketplace.html"

# Read corrupted file as latin-1 then decode properly
try:
    with open(marketplace_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Delete old file
    os.remove(marketplace_path)
    print("Deleted corrupted file")
except:
    print("File not found or error reading")

# Create new clean file
html = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marketplace - Cửa hàng số 1 Việt Nam</title>
</head>
<body>
    <h1>Test: Chứng khoán - Tài Xỉu - Xổ Số</h1>
    <p>🛍️ 📱 🎰 ₿</p>
</body>
</html>"""

with open(marketplace_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Created new marketplace.html successfully!")
print("File saved with UTF-8 encoding")
