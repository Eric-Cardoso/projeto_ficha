from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import usuario_schema
from models.usuario_model import Usuario
from core.seguranca import bcrypt_context, validar_senha
from repos import repo_usuario

async def verificar_fichas(usuario: Usuario) -> None:
    # Verifica se a quantidade de fichas veio como um valor Nulo
    if usuario.quantidade_fichas is None:
        usuario.quantidade_fichas = 0

async def criar_usuario(
    dados: usuario_schema.CriarUsuario, 
    sessao: AsyncSession
) -> Usuario:
    
    # Verifica se ja existe um usuário com o mesmo email no banco
    usuario_existe = await sessao.scalar(
        select(Usuario)
        .where(Usuario.email == dados.email)
    )

    # Verifica se o usuário foi encontrado
    if usuario_existe:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail='Já existe um usuário com este email'
        )
    
    # Pega os dados em forma de dict
    dict_dados = dados.model_dump()

    # Valida a senha do usuário
    validar_senha(senha=dict_dados['senha'])
    
    # Criptografa a senha do usuário
    dict_dados['senha'] = bcrypt_context.hash(dict_dados['senha'])

    # pega os dados em forma de objeto
    db_usuario = Usuario(**dict_dados)

    # Salva o usuário no banco
    await repo_usuario.criar_usuario(usuario=db_usuario, sessao=sessao)

    # Verifica se a quantidade de fichas está vindo como um valor Nulo
    verificar_fichas(usuario=db_usuario)

    return db_usuario

