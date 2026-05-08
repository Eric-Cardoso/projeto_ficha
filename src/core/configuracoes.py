from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker
)

# Estabelece o banco que será utilizado e o nome do arquivo do banco
DATABASE_URL = 'sqlite+aiosqlite:///fichas.db'

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
