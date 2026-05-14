from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.usuario_model import Usuario
from core.seguranca import bcrypt_context, gerar_token
from datetime import timedelta

async def login_usuario(
    sessao: AsyncSession,
    usuario: OAuth2PasswordRequestForm,
) -> dict:
    
    # Tenta obter o usuário de acordo com o email
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.email == usuario.username)
    )

    # Verifica se o email está correto
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Credenciais inválidas'
        )

    # Verifica se a senha está correta
    if not bcrypt_context.verify(usuario.password, db_usuario.senha ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Credenciais inválidas'
        )
    
    # Cria o token de acesso
    access_token = gerar_token(id_usuario=db_usuario.id)

    # Cria o token de refresh
    refresh_token = gerar_token(
        id_usuario=db_usuario.id, 
        tempo_expiracao_token=timedelta(days=7)
    )

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'token_type': 'bearer'
    }

async def refresh(usuario: Usuario) -> dict:
    # Cria o token de acesso
    access_token = gerar_token(id_usuario=usuario.id)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }

    