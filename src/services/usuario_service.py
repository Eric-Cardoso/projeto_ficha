from fastapi import HTTPException, status, Response
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

async def listar_usuario(usuario: Usuario):
    return usuario

async def atualizar_usuario(
    usuario: Usuario, 
    sessao: AsyncSession, 
    dados: usuario_schema.AtualizarUsuario
) -> Usuario:
    
    # Tenta obter o usuário de acordo com o id
    db_usuario = await sessao.scalar(
        select(Usuario)
        .where(Usuario.id == usuario.id)
    )

    # Verifica se o usuário foi encontrado
    if not db_usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Usuário não encontrado'
        )
    
    # Obtém em dict os dados enviados
    dict_dados = dados.model_dump()

    # Atualiza os dados do usuário
    for campo, valor in dict_dados.items():
        setattr(db_usuario, campo, valor)

    # Salva as alterações no banco
    await repo_usuario.atualizar_usuario(usuario=db_usuario, sessao=sessao)

    return db_usuario

async def deletar_usuario(usuario: Usuario, sessao: AsyncSession) -> Response:
    # Deleta o usuário
    await repo_usuario.deletar_usuario(usuario=usuario, sessao=sessao)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


