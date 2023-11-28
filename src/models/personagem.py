from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text, column
from .base import Base
from sqlalchemy.orm import relationship


class Atributos():
    __tablename__ = "atributos"

    forca = Column(Integer, default=0)
    destreza = Column(Integer, default=0)
    constituicao = Column(Integer, default=0)
    inteligencia = Column(Integer, default=0)
    sabedoria = Column(Integer, default=0)
    carisma = Column(Integer, default=0)


class Antecedente(Base):
    __tablename__ = "antecedentes"
    nome = Column(String)
    descricao = Column(Text)
    idade_max = Column(Integer)
    idade_adulta = Column(Integer)
    tendencia = Column(String)

    # tamanho medio em centimetros pra individuos dessa raça
    tamanho = Column(Integer)
    deslocamento = Column(String)



class Raca(Atributos, Base):
    __tablename__ = "racas"
    nome = Column(String)
    idioma = Column(String)

    personagens = relationship("Personagem", back_populates="raca")


personagens_classes_association_table = Table(
    "personagens_classes_association_table",
    Base.metadata,
    Column("personagem_id", ForeignKey("personagens.id")),
    Column("classe_id", ForeignKey("classes.id"))
)


class Classe(Atributos, Base):
    __tablename__ = "classes"
    nome = Column(String)
    level = Column(Integer)

    personagens = relationship(
        "Personagem", secondary=personagens_classes_association_table, back_populates="classes")


class Personagem(Base):
    __tablename__ = "personagens"

    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="personagens")
    jogador_telegram_id = Column(String)

    nome = Column(String)
    raca_id = Column(Integer, ForeignKey("racas.id"))
    raca = relationship("Raca", back_populates="personagens")
    tendencia = Column(String)
    experiencia = Column(Integer)

    inspiracao = Column(String)
    proficiencia = Column(String)
    

    classes = relationship(
        "Classe", secondary=personagens_classes_association_table, back_populates="personagens")
