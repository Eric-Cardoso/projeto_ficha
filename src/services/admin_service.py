from models.usuario_model import Usuario
from models.ficha_model import Ficha
from fastapi import HTTPException, status, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import admin_schema
from repos import repo_admin

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
    
    # Obtém o usuário de acordo com o id
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.id == id_usuario)
    )
    
    # Verifica se o usuário foi encontrado
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado'
        )
    
    return db_usuario

async def atualizar_usuario(
    id_usuario: int,
    dados: admin_schema.AtualizarUsuario, 
    usuario: Usuario, 
    sessao: AsyncSession
) -> Usuario:
    
    # Verifica se o usuário logado é admin
    if not usuario.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Busca o usuário pelo id
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.id == id_usuario)
    )

    # Verifica se o usuário foi encontrado
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado'
        )
    
    # Obtém os dados enviados em forma de dict
    dict_dados = dados.model_dump(exclude_unset=True, exclude_none=True)

    # Atualiza os dados do usuário
    for campo, valor in dict_dados.items():
        setattr(db_usuario, campo, valor)

    # Salva no banco
    await repo_admin.atualizar_usuario(usuario=db_usuario, sessao=sessao)

    return db_usuario

async def deletar_usuario(
    id_usuario: int, 
    usuario: Usuario, 
    sessao: AsyncSession
) -> Response:
    
    # Verifica se o usuário logado é admin
    if not usuario.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Busca o usuário pelo id
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.id == id_usuario)
    )

    # Verifica se o usuário foi encontrado
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado'
        )
    
    # Deleta o usuário do banco
    await repo_admin.deletar_usuario(usuario=db_usuario, sessao=sessao)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

async def listar_fichas(
    id_usuario: int, 
    usuario: Usuario, 
    sessao: AsyncSession
) -> admin_schema.ListarFichas:
    
    # Verifica se o usuário logado é admin
    if not usuario.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Busca o usuário pelo id
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.id == id_usuario)
    )

    # Verifica se o usuário foi encontrado
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado'
        )
    
    # Obtém todas as fichas pertencentes ao usuário buscado
    db_fichas = await sessao.scalars(
        select(Ficha)
        .where(Ficha.id_usuario == db_usuario.id)
    )

    return {
        'usuario': db_usuario,
        'fichas': db_fichas.all()
    }

    
