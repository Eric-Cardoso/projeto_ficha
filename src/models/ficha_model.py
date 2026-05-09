from core.configuracoes import Base
from sqlalchemy import Column, String, Integer, ForeignKey

# Configura a tabela de fichas
class Ficha(Base):
    # Define o nome da tabela
    __tablename__ = 'fichas'

    # Configura cada campo da tabela
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(ForeignKey('usuarios.id'))
    nome_personagem = Column(String, nullable=True)
    nome_jogador = Column(String, nullable=True)
    vida = Column(Integer, nullable=True, default=20)
    sanidade = Column(Integer, nullable=True, default=10)
    classe = Column(String, nullable=True)
    forca = Column(Integer, nullable=True, default=1)
    agilidade = Column(Integer, nullable=True, default=1)
    intelecto = Column(Integer, nullable=True, default=1)
    presenca = Column(Integer, nullable=True, default=1)
    vigor = Column(Integer, nullable=True, default=1)
    inventario = Column(String, nullable=True)
    descricao = Column(String, nullable=True)
    defesa = Column(Integer, nullable=True, default=1)
    armas = Column(String, nullable=True)
    