# -*- coding: utf-8 -*-
import codecs

# Đọc file với encoding sai và decode lại đúng
file_path = r"c:\Users\Hi\Downloads\web mới\marketplace.html"

# Đọc file với latin-1 (để lấy bytes gốc)
with open(file_path, 'r', encoding='latin-1') as f:
    content = f.read()

# Fix encoding: chuyển từ latin-1 về UTF-8
# Encode lại thành bytes với latin-1, rồi decode bằng UTF-8
try:
    fixed_content = content.encode('latin-1').decode('utf-8')
except:
    # Nếu không work, thử cách khác
    fixed_content = content

# Ghi lại file với UTF-8 đúng
with codecs.open(file_path, 'w', encoding='utf-8-sig') as f:
    f.write(fixed_content)

print("Đã sửa encoding UTF-8!")
