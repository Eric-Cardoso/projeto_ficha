from models.ficha_model import Ficha
from sqlalchemy.ext.asyncio import AsyncSession

async def criar_ficha(ficha: Ficha, sessao: AsyncSession) -> None:
    # Adiciona a ficha ao banco
    sessao.add(ficha)

    # Salva no banco as alterações
    await sessao.commit()

    # Atualiza o objeto
    await sessao.refresh(ficha)

async def atualizar_ficha(ficha: Ficha, sessao: AsyncSession) -> None:
    # Salva no banco as alterações
    await sessao.commit()

    # Atualiza o objeto
    await sessao.refresh(ficha)

async def deletar_ficha(ficha: Ficha, sessao: AsyncSession) -> None:
    # Deleta a ficha do banco
    await sessao.delete(ficha)
    
    # Salva no banco as alterações
    await sessao.commit()


async def deletar_fichas(fichas: list[Ficha], sessao: AsyncSession) -> None:
    # Deleta todas as fichas que pertenciam ao usuário deletado
    for ficha in fichas:
        await sessao.delete(ficha)

    # Salva no banco as alterações
    await sessao.commit()
