from models.usuario_model import Usuario
from models.ficha_model import Ficha
from fastapi import Depends, HTTPException, status
from dependencias import verificar_token, sessao
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import ficha_schema
from repos import repo_ficha

async def criar_ficha(
    dados: ficha_schema.CriarFicha,
    usuario: Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> Ficha:
    
    # Obtém os dados em forma de dict
    dict_dados = dados.model_dump()

    # Define a qual usuário a ficha pertence
    dict_dados['id_usuario'] = usuario.id

    # Obtém a ficha em forma de objeto
    db_ficha = Ficha(**dict_dados)

    # Verifica se o usuário excedeu o limite máximo de criar fichas
    if usuario.quantidade_fichas >= 20:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Você já atingiu o limite de criação fichas'
        )
    
    # Atualiza a quantidade de fichas que o usuário possuí
    usuario.quantidade_fichas += 1

    # Salva no banco
    await repo_ficha.criar_ficha(ficha=db_ficha, sessao=sessao)

    return db_ficha

