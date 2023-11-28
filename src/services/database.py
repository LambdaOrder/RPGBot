from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base
from models.personagem import Antecedente, Raca, Classe, Personagem
from models.game import Game

engine = create_engine(getenv("DATABASE_URL"), echo=True)
session = Session(engine)
Base.metadata.create_all(engine)
