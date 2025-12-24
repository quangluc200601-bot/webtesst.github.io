# -*- coding: utf-8 -*-
import re

file_path = r"c:\Users\Hi\Downloads\web mới\marketplace.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Thay thế URL ảnh bằng emoji
replacements = {
    "image: 'https://picsum.photos/seed/mmo1/400/300'": "image: '📱'",
    "image: 'https://picsum.photos/seed/ads2/400/300'": "image: '📢'",
    "image: 'https://picsum.photos/seed/seo3/400/300'": "image: '🔍'",
    "image: 'https://picsum.photos/seed/btc4/400/300'": "image: '₿'",
    "image: 'https://picsum.photos/seed/bo10/400/300'": "image: '📊'",
    "image: 'https://picsum.photos/seed/forex35/400/300'": "image: '💱'",
    "image: 'https://picsum.photos/seed/gold28/400/300'": "image: '💹'",
    "image: 'https://picsum.photos/seed/stock53/400/300'": "image: '📈'",
    "image: 'https://picsum.photos/seed/lottery7/400/300'": "image: '🎲'",
    "image: 'https://picsum.photos/seed/bingo8/400/300'": "image: '🎰'",
    "image: 'https://picsum.photos/seed/go889/400/300'": "image: '🎮'",
    "image: 'https://picsum.photos/seed/stats12/400/300'": "image: '📈'",
    "image: 'https://picsum.photos/seed/casino13/400/300'": "image: '🃏'",
    "image: 'https://picsum.photos/seed/cards36/400/300'": "image: '♠️'",
    "image: 'https://picsum.photos/seed/fish37/400/300'": "image: '🐟'",
    "image: 'https://picsum.photos/seed/soccer34/400/300'": "image: '⚽'",
    "image: 'https://picsum.photos/seed/tiki5/400/300'": "image: '🛍️'",
    "image: 'https://picsum.photos/seed/flight30/400/300'": "image: '✈️'",
    "image: 'https://picsum.photos/seed/hotel32/400/300'": "image: '🏨'",
    "image: 'https://picsum.photos/seed/dating31/400/300'": "image: '💋'",
    "image: 'https://picsum.photos/seed/love38/400/300'": "image: '💕'",
    "image: 'https://picsum.photos/seed/adult39/400/300'": "image: '🔞'",
    "image: 'https://picsum.photos/seed/credit6/400/300'": "image: '💳'",
    "image: 'https://picsum.photos/seed/bank11/400/300'": "image: '🏦'",
    "image: 'https://picsum.photos/seed/loan40/400/300'": "image: '💰'",
    "image: 'https://picsum.photos/seed/shop19/400/300'": "image: '🛒'",
    "image: 'https://picsum.photos/seed/ecom24/400/300'": "image: '📦'",
    "image: 'https://picsum.photos/seed/charity22/400/300'": "image: '❤️'",
    "image: 'https://picsum.photos/seed/tax21/400/300'": "image: '🏛️'",
    "image: 'https://picsum.photos/seed/debt41/400/300'": "image: '📋'",
    "image: 'https://picsum.photos/seed/labor42/400/300'": "image: '🌏'",
    "image: 'https://picsum.photos/seed/labor43/400/300'": "image: '✈️'",
    "image: 'https://picsum.photos/seed/farm44/400/300'": "image: '🐷'",
    "image: 'https://picsum.photos/seed/chicken45/400/300'": "image: '🐔'",
    "image: 'https://picsum.photos/seed/chat46/400/300'": "image: '💬'",
    "image: 'https://picsum.photos/seed/karaoke47/400/300'": "image: '🎤'",
    "image: 'https://picsum.photos/seed/delivery16/400/300'": "image: '🚚'",
    "image: 'https://picsum.photos/seed/bike48/400/300'": "image: '🏍️'",
    "image: 'https://picsum.photos/seed/service33/400/300'": "image: '🛠️'",
    "image: 'https://picsum.photos/seed/multi49/400/300'": "image: '⚡'",
    "image: 'https://picsum.photos/seed/ai18/400/300'": "image: '🤖'",
    "image: 'https://picsum.photos/seed/deepfake29/400/300'": "image: '🎭'",
    "image: 'https://picsum.photos/seed/staff17/400/300'": "image: '👥'",
    "image: 'https://picsum.photos/seed/time50/400/300'": "image: '⏰'",
    "image: 'https://picsum.photos/seed/fishing51/400/300'": "image: '🎣'",
    "image: 'https://picsum.photos/seed/support52/400/300'": "image: '📞'"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã thay thế tất cả URL ảnh thành emoji!")
