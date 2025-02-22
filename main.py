import asyncio
from pyrogram import Client
from database_config.db import init_db
from database_config.config import API_ID, API_HASH

app = Client("my_session", api_id=API_ID, api_hash=API_HASH)

async def main():
    await init_db()

    async with app:
        print("Успешный вход в Telegram!")
        await app.idle()


if __name__ == "__main__":
    asyncio.run(main())

