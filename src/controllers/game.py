from sqlalchemy import select, update
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

    async def update(self, id:int, **kwargs):
        async with self.async_session() as session:
            game = self.get_by_id(id)
            if game:
                await session.execute(update(Game).where(Game.id==id).values(**kwargs))
                await session.commit()


