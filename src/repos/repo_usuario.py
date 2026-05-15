from models.usuario_model import Usuario
from sqlalchemy.ext.asyncio import AsyncSession

async def criar_usuario(usuario: Usuario, sessao: AsyncSession) -> None:
    # Adiciona o usuário ao banco
    sessao.add(usuario)

    # Salva no banco as alterações
    await sessao.commit()

    # Atualiza o objeto
    await sessao.refresh(usuario)

async def atualizar_usuario(usuario: Usuario, sessao: AsyncSession) -> None:
    # Salva no banco as alterações
    await sessao.commit()

    # Atualiza o objeto
    await sessao.refresh(usuario)

async def deletar_usuario(usuario: Usuario, sessao: AsyncSession) -> None:
    # Deleta o usuário
    await sessao.delete(usuario)

    # Salva no banco as alterações
    await sessao.commit()

