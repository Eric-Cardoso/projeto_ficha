from core.configuracoes import SessionLocal, CHAVE_SECRETA, ALGORITMO
from core.seguranca import oauth2_schema
from fastapi import Depends, status, HTTPException
from models.usuario_model import Usuario
from jose import jwt, JWTError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# Empresta a sessao do banco de dados sempre que necessário
async def sessao():
    async with SessionLocal() as sessao: 
        yield sessao
  
async def verificar_token(
    token: str = Depends(oauth2_schema), 
    sessao: AsyncSession = Depends(sessao)
) -> Usuario:
    
    try:
        # Decodifica o token
        dict_info = jwt.decode(
            token=token, 
            key=CHAVE_SECRETA, 
            algorithms=[ALGORITMO]
        )

        # Obtém o id do usuário
        id_usuario = int(dict_info.get('sub'))

        # Tenta obter o usuário de acordo com o id
        db_usuario = await sessao.scalar(
            select(Usuario).where(Usuario.id == id_usuario)
        )
        
        # Verifica se o usuário foi encontrado
        if not db_usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Usuário não encontrado',
            )
        
        return db_usuario

    # Levanta uma exceção caso ocorra algum erro ao descodificar o token
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais inválidas',
        )
    