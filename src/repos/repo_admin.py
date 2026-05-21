from models.usuario_model import Usuario
from sqlalchemy.ext.asyncio import AsyncSession

async def atualizar_usuario(usuario: Usuario, sessao: AsyncSession) -> None:
    # Salva no banco as alterações
    await sessao.commit()

    # Atualiza o objeto
    await sessao.refresh(usuario)
