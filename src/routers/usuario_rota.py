from fastapi import APIRouter, status, Depends
from schemas import usuario_schema
from sqlalchemy.ext.asyncio import AsyncSession
from dependencias import sessao
from services import usuario_service
from models import usuario_model

# Configura a rota de usuário
usuario_rota = APIRouter(prefix='/usuarios', tags=['usuários'])

@usuario_rota.post(
    path='/criar', 
    response_model=usuario_schema.UsuarioPublic, 
    status_code=status.HTTP_201_CREATED
)
async def criar_usuario(
    dados: usuario_schema.CriarUsuario, 
    sessao: AsyncSession = Depends(sessao)
) -> usuario_model.Usuario:
    
    return await usuario_service.criar_usuario(dados=dados, sessao=sessao)