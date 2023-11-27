from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base

engine = create_engine(getenv("DATABASE_URL"), echo=True)
session = Session(engine)
Base.metadata.create_all(engine)
