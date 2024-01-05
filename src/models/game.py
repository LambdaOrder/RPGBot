from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import Base

class Game(Base):
    __tablename__ = "games"
    nome = Column(String)

    personagens = relationship("Personagem", back_populates="game")
    
    def __repr__(self) -> str:
        return f"ID:{self.id}, Nome:{self.nome}"
