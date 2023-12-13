from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Text
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


    # testes de resistencia
    resistencia_forca = Column(Boolean, default=False)
    resistencia_destreza = Column(Boolean, default=False)
    resistencia_constituicao = Column(Boolean, default=False)
    resistencia_inteligencia = Column(Boolean, default=False)
    resistencia_sabedoria = Column(Boolean, default=False)
    resistencia_carisma = Column(Boolean, default=False)

    personagens = relationship(
        "Personagem", secondary=personagens_classes_association_table, back_populates="classes")


class Personagem(Base,  Atributos):
    __tablename__ = "personagens"

    game_id = Column(Integer, ForeignKey("games.id"))
    game = relationship("Game", back_populates="personagens")
    jogador_telegram_id = Column(String)

    nome = Column(String)
    raca_id = Column(Integer, ForeignKey("racas.id"))
    raca = relationship("Raca", back_populates="personagens")
    tendencia = Column(String)
    experiencia = Column(Integer)
    inspiracao = Column(Boolean)
    proficiencia = Column(String)
    iniciativa = Column(Integer)
    pontos_de_vida_atuais = Column(Integer)
    pontos_de_vida_temporarios = Column(Integer)

    #Personalidade
    traits = Column(Text)
    ideais = Column(Text)
    vinculos = Column(Text)
    defeitos = Column(Text)

    #  Pericias
    acrobacia = Column(Boolean, default=False)
    adestrar_animais = Column(Boolean, default=False)
    arcanismo = Column(Boolean, default=False)
    atletismo = Column(Boolean, default=False)
    atuacao = Column(Boolean, default=False)
    enganacao = Column(Boolean, default=False)
    furtividade = Column(Boolean, default=False)
    historia = Column(Boolean, default=False)
    intimidacao = Column(Boolean, default=False)
    intuicao = Column(Boolean, default=False)
    investigacao = Column(Boolean, default=False)
    medicina = Column(Boolean, default=False)
    natureza = Column(Boolean, default=False)
    percepcao = Column(Boolean, default=False)
    persuasao = Column(Boolean, default=False)
    prestidigitacao = Column(Boolean, default=False)
    religiao = Column(Boolean, default=False)
    sobrevivencia = Column(Boolean, default=False)
    

    

    classes = relationship(
        "Classe", secondary=personagens_classes_association_table, back_populates="personagens")
