from sqlalchemy import Column, ForeignKey, Integer, String, Table
from .base import Base
from sqlalchemy.orm import relationship
class Personagem(Base):
    __tablename__ = "personagens"
    name = Column(String)

    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="personagens")


