from pyrogram import Client
from database_config.db import init_db
from database_config.config import API_ID, API_HASH, SESSION_STRING

app = Client("my_session", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)

async def main():
    await init_db()
    print("Успешный вход в Telegram!")

if __name__ == "__main__":
    app.run(main())
