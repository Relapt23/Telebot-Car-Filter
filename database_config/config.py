import os
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

app = Client("my_session", api_id=API_ID, api_hash=API_HASH)

with app:
    print("Успешный вход в Telegram!")


@app.on_message(filters.chat("auto_zakazz25"))
async def handle_channel_messages(client, message):
    print(f"Новое сообщение в канале: {message.text}")

app.run()