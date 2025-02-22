from database_config.db import save_message
from main import app
from pyrogram import filters
import re

KEYWORDS = ['MAZDA3', 'MAZDA 3', 'MERCEDES BENZ C CLASS', 'MERCEDES-BENZ C CLASS',
            'MERCEDES BENZ', 'MERCEDES', 'MERCEDES BENZ C-CLASS', 'MERCEDES-BENZ C-CLASS' ]
PRICE_PATTERN = re.compile(r"Итоговая стоимость:?\s*([\d.,]+₽)")

def search_price(text: str) -> str:
    price = PRICE_PATTERN.search(text)
    return price.group(1) if price else "Не указана"



@app.on_message(filters.chat("auto_zakazz25"))
async def handle_channel_messages(client, message):
    text = message.text if message.text else message.caption
    if not text:
        return
    car = next((brand for brand in KEYWORDS if brand in text.upper()), None)
    if not car:
        return
    tg_url = f"https://t.me/{message.chat.username}/{message.id}"
    price = search_price(text)
    await save_message(car, text, tg_url, price)
