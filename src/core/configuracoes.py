from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker
)
from dotenv import load_dotenv
import os
import redis.asyncio as redis

# Carrega as variáveis de ambiente
load_dotenv()

# Estabelece o banco que será utilizado e o nome do arquivo do banco
DATABASE_URL = 'sqlite+aiosqlite:///fichas.db'

# Obter o valor da variável de ambiente CHAVE_SECRETA
CHAVE_SECRETA = os.getenv('CHAVE_SECRETA')

# Obter o valor da variável de ambiente ALGORITMO
ALGORITMO = os.getenv('ALGORITMO')

# Obter o valor da variável de ambiente TEMPO_EXPIRACAO_TOKEN
TEMPO_EXPIRACAO_TOKEN = int(os.getenv('TEMPO_EXPIRACAO_TOKEN'))

# Cria a engine
engine = create_async_engine(DATABASE_URL)

# Cria a sessão local
SessionLocal = async_sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    autoflush=False, 
    autocommit=False
)

# Cria o Base
Base = declarative_base()

# Configura o Redis
cache = redis.Redis()
