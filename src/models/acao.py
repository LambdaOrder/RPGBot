import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Text, Enum, ARRAY
from .base import Base
from sqlalchemy.orm import relationship


class TipoAcao(enum.Enum):
    simples = 0
    bonus = 1
    reacao = 2
    longo = 3


class TipoAtaque(enum.Enum):
    melee = 0
    ranged = 1


class TipoDano(enum.Enum):
    acido = 0
    concussao = 1
    gelo = 2
    fogo = 3
    força = 4
    relampago = 5
    necrotico = 6
    penetrante = 7
    veneno = 8
    psiquico = 9
    radiante = 10
    corte = 11
    trovao = 12
    arco_curto = 13
    arco_longo = 14
    melee_uma_mao = 15
    melee_duas_maos = 16
    natural = 17
    desarmado = 18


class TipoAreaDeEfeito(enum.Enum):
    cilindro = 0
    cone = 1
    cubo = 2
    esfera = 3
    linha = 4


class AtributoEnum(enum.Enum):
    # TODO: dar um jeito nesse negocio aqui pq foi um copia e cola da classe de personagens
    forca = 0
    destreza = 1
    constituicao = 2
    inteligencia = 3
    sabedoria = 4
    carisma = 5


class Efeitos(enum.Enum):
    cegueira = 0
    charme = 1
    surdes = 2
    exaustao = 3
    amedrontar = 4
    agarrar = 5
    incapacitar = 6
    invisibilidade = 7
    paralisia = 8
    petrificar = 9
    envenenar = 10
    atordoar = 11
    derrubar = 12
    conter = 13
    desmaiar = 14


class EscolasMagia(enum.Enum):
    abjuracao = 0
    adivinhacao = 1
    conjuracao = 2
    encantamento = 3
    evocacao = 4
    ilusao = 5
    necromancia = 6
    transmutacao = 7


class Componentes(enum.Enum):
    V = 0
    S = 1
    M = 2


class Magia(Base):
    __tablename__ = "magias"

    nome = Column(String)
    nivel = Column(Integer)
    descricao = Column(Text)
    componentes = Column(Enum(Componentes))
    escola = Column(Enum(EscolasMagia))
    tipo = Column(Enum(TipoAtaque))
    tipo_dano = Column(Enum(TipoDano))
    efeitos = Column(ARRAY(Enum(Efeitos)))
    concentracao = Column(Boolean)
    ritual = Column(Boolean)
    area_efeito = Column(Enum(TipoAreaDeEfeito))
    duracao = Column(Integer)
    tipo_acao = Column(Enum(TipoAcao))
    tempo_conjuracao = Column(Integer)
    alcance = Column(Integer)
    atributo = Column(ARRAY(Enum(AtributoEnum)))
