from models.usuario_model import Usuario
from sqlalchemy.ext.asyncio import AsyncSession

async def criar_usuario(usuario: Usuario, sessao: AsyncSession) -> None:
    # Adiciona o usuário ao banco
    sessao.add(usuario)

    # Salva no banco as alterações
    await sessao.commit()

    # Atualiza o objeto
    await sessao.refresh(usuario)
