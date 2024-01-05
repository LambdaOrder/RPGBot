import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from services.envvars import DATABASE_URL
from models.base import Base
from models.personagem import Antecedente, Raca, Classe, Personagem
from models.game import Game

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
