from core.configuracoes import Base
from sqlalchemy import Column, String, Integer

# Configura a tabela de usuarios
class Usuario(Base):
    # Define o nome da tabela
    __tablename__ = 'usuarios'

    # Configura cada campo da tabela
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    quantidade_fichas = Column(Integer, nullable=False, default=0)
