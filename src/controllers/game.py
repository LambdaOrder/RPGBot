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
    
    async def get_all(self):
        async with self.async_session() as session:
            games = await session.execute(select(Game))

        game_list = games.all()
        return game_list

    async def get_by_nome(self, nome:str):
        async with self.async_session() as session:
            games = await session.execute(select(Game).where(Game.nome==nome))

        game_list = games.all()
        return game_list

    async def get_by_id(self, id:int):
        async with self.async_session() as session:
            games = await session.execute(select(Game).where(Game.id==id))

        game = games.all()
        return game

