from models.usuario_model import Usuario
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import admin_schema

async def listar_usuarios(
    usuario: Usuario, 
    sessao: AsyncSession, 
    offset: int, 
    limit: int
) -> admin_schema.ListarUsuarios:
    
    # Verifica se o usuário logado é admin
    if not usuario.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Obtém os usuários salvos no banco
    db_usuarios = await sessao.scalars(
        select(Usuario)
        .offset(offset=offset)
        .limit(limit=limit)
    )

    return {
        'usuarios': db_usuarios.all()
    }

async def listar_usuario(
    id_usuario: int,
    usuario: Usuario, 
    sessao: AsyncSession
) -> Usuario:
    
    # Verifica se o usuário logado é admin
    if not usuario.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Obtém os usuários salvos no banco
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.id == id_usuario)
    )

    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado'
        )
    
    return db_usuario
    
