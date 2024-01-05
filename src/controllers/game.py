from sqlalchemy import select
from models.game import Game


class GameController:
    def __init__(self, async_session):
        self.async_session = async_session

    async def create(self, nome:str):
        new_game = Game(nome=nome)
        async with self.async_session() as session:
            async with session.begin():
                session.add(new_game)
                await session.commit()

        return new_game
