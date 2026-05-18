from models.usuario_model import Usuario
from models.ficha_model import Ficha
from fastapi import Depends, HTTPException, status
from dependencias import verificar_token, sessao
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import ficha_schema
from repos import repo_ficha
from services import redis_service
from core.configuracoes import cache

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

async def listar_fichas(
    usuario: Usuario, 
    sessao: AsyncSession
) -> ficha_schema.ListarFichas:
    
    # Obtém todas as fichas que pertencem ao usuário logado
    db_fichas = await sessao.scalars(
        select(Ficha)
        .where(Ficha.id_usuario == usuario.id)
    )

    return {
        'fichas': db_fichas.all()
    }

async def listar_ficha(
    id_ficha: int, 
    usuario: Usuario, 
    sessao: AsyncSession
) -> Ficha:
    
    # Tenta obter os dados da ficha de acordo com o id
    cache_ficha = await redis_service.buscar_ficha(id_ficha=id_ficha)

    # Verifica se os dados foram encontrados
    if not cache_ficha:
        # Tenta obter a ficha de acordo com o id
        db_ficha = await sessao.scalar(
            select(Ficha)
            .where(Ficha.id == id_ficha)
        )

        # Verifica se a ficha foi encontrada
        if not db_ficha:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='Ficha não encontrada'
            )
        
        # Verifica se a ficha pertence ao usuário logado
        if usuario.id != db_ficha.id_usuario:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail='Acesso negado'
            )

        # Obtém os dados da ficha em forma de dict
        dados_ficha = {
            k: v 
            for k, v in db_ficha.__dict__.items()
            if not k.startswith('_')        
        }
        
        # Atualiza o cache
        await redis_service.atualizar_cache(ficha=db_ficha, dados_ficha=dados_ficha)

        return db_ficha
    
    # Obtém os dados da ficha em forma de dict
    dict_ficha = redis_service.obter_ficha(cache_ficha=cache_ficha)

    # Verifica se a ficha pertence ao usuário logado
    if usuario.id != dict_ficha['id_usuario']:
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, 
                detail='Acesso negado'
            )
    
    # Obtém a ficha em forma de objeto
    db_ficha = Ficha(**dict_ficha)

    return db_ficha

async def atualizar_ficha(
    id_ficha: int,
    dados: ficha_schema.AtualizarFicha, 
    usuario: Usuario, 
    sessao: AsyncSession
) -> Ficha:
    
    # Tenta obter a ficha de acordo com o id
    db_ficha = await sessao.scalar(select(Ficha).where(Ficha.id == id_ficha))

    # Verifica se a ficha foi encontrada
    if not db_ficha:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Ficha não encontrada'
        )
    
    # Verifica se a ficha pertence ao usuário logado
    if usuario.id != db_ficha.id_usuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Obtém os dados enviados em forma de dict
    dict_dados = dados.model_dump()

    # Atualiza os dados da ficha
    for campo, valor in dict_dados.items():
        setattr(db_ficha, campo, valor)

    # Salva no banco
    await repo_ficha.atualizar_ficha(ficha=db_ficha, sessao=sessao)

    # Deleta a ficha do cache
    await redis_service.deletar_ficha(id_ficha=db_ficha.id)

    return db_ficha

async def atualizar_parcial_ficha(
    id_ficha: int,
    dados: ficha_schema.AtualizarParcialFicha, 
    usuario: Usuario, 
    sessao: AsyncSession
) -> Ficha:
    
    # Tenta obter a ficha de acordo com o id
    db_ficha = await sessao.scalar(select(Ficha).where(Ficha.id == id_ficha))

    # Verifica se a ficha foi encontrada
    if not db_ficha:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Ficha não encontrada'
        )
    
    # Verifica se a ficha pertence ao usuário logado
    if usuario.id != db_ficha.id_usuario:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail='Acesso negado'
        )
    
    # Obtém os dados enviados em forma de dict
    dict_dados = dados.model_dump(exclude_unset=True, exclude_none=True)

    # Atualiza os dados da ficha
    for campo, valor in dict_dados.items():
        setattr(db_ficha, campo, valor)

    # Salva no banco
    await repo_ficha.atualizar_ficha(ficha=db_ficha, sessao=sessao)

    # Deleta a ficha do cache
    await redis_service.deletar_ficha(id_ficha=db_ficha.id)

    return db_ficha
