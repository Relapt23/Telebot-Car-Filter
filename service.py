from database_config.db import save_message
from main import app
from pyrogram import filters
import re

KEYWORDS = ['MAZDA3', 'MAZDA 3', 'MERCEDES BENZ C CLASS', 'MERCEDES-BENZ C CLASS',
            'MERCEDES BENZ', 'MERCEDES', 'MERCEDES BENZ C-CLASS', 'MERCEDES-BENZ C-CLASS' ]
PRICE_PATTERN = re.compile(r"Итоговая стоимость:?\s*([\d.,]+₽)")
YEAR_PATTERN = re.compile(r"(\d{4})г")
ENGINE_PATTERN = re.compile(r"Объем\s*([\d.]+)")
RATING_PATTERN = re.compile(r"Оценка\s*([\d.]+)")

def search_price(text: str) -> str:
    price = PRICE_PATTERN.search(text)
    return price.group(1) if price else "Не указана"

def search_year(text: str) -> str:
    year = YEAR_PATTERN.search(text)
    return year.group(1) if year else "Не указано"

def search_engine(text: str) -> str:
    engine_capacity = ENGINE_PATTERN.search(text)
    return engine_capacity.group(1) if engine_capacity else "Не указан"

def search_rating(text: str) -> str:
    rating = RATING_PATTERN.search(text)
    return rating.group(1) if rating else "Не указана"



def append_keyword(text:str) -> str:
    if text in KEYWORDS:
        return f"Марка машины '{text}' уже есть в списке!"
    KEYWORDS.append(text)
    return f"Добавлена новая марка машины для поиска"

def delete_keyword(text:str) -> str:
    if text not in KEYWORDS:
        return f"Введенная марка машины {text} не найдена"
    KEYWORDS.remove(text)
    return f"Марка {text} успешно удалена из фильтров поиска"


@app.on_message(filters.channel("auto_zakazz25"))
async def handle_channel_messages(client, message):
    text = message.text if message.text else message.caption
    if not text:
        return
    car = next((brand for brand in KEYWORDS if brand in text.upper()), None)
    if not car:
        return
    tg_url = f"https://t.me/{message.chat.username}/{message.id}"
    price = search_price(text)
    year = search_year(text)
    engine_capacity = search_engine(text)
    rating = search_rating(text)
    await save_message(car, text, tg_url, price, year, engine_capacity, rating)

@app.on_message(filters.text & ~filters.command("del"))
async def handle_message(client, message):
    res = append_keyword(message.text)
    await message.reply(res)

@app.on_message(filters.command("del"))
async def handle_delete(client, message):
    if len(message.command) < 2:
        await message.reply("Укажите ключевое слово для удаления! Пример: `/del BMW X5`")
        return
    delete_car_model = " ".join(message.command[1:])
    res = delete_keyword(delete_car_model)
    await message.reply(res)
