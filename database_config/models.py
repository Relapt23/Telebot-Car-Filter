from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime


class Base(DeclarativeBase):
    pass


class InfoCars(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    car: Mapped[str]
    text: Mapped[str]
    price: Mapped[str]
    tg_url: Mapped[str]
    date_create: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)