from sqlalchemy.orm import relationship
from .base import Base

class Game(Base):
    __tablename__ = "games"

    personagens = relationship("Personagem", back_populates="game")
