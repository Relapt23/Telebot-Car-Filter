from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from database_config.config import DB_CONFIG
from database_config.models import Base, InfoCars
from sqlalchemy import select

engine = create_async_engine(f"postgresql+asyncpg://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}", echo=True)
sess = async_sessionmaker(engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def save_message(car: str, text: str, tg_url: str, price: str, year: str, engine_capacity: str, rating: str):
    async with sess() as session:
        response = await session.execute(select(InfoCars).where(tg_url==InfoCars.tg_url))
        res = response.scalars().all()
        if not res:
            right_message = InfoCars(car=car, text=text, tg_url=tg_url,price=price,
                                     year=year, engine_capacity=engine_capacity, rating=rating)
            session.add(right_message)
            await session.commit()