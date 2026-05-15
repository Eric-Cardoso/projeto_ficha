from fastapi import APIRouter, status, Depends
from schemas import usuario_schema
from sqlalchemy.ext.asyncio import AsyncSession
from dependencias import sessao
from services import usuario_service
from models import usuario_model
from dependencias import verificar_token

# Configura a rota de usuário
usuario_rota = APIRouter(prefix='/usuarios', tags=['usuários'])

@usuario_rota.post(
    path='/criar', 
    response_model=usuario_schema.UsuarioPublico, 
    status_code=status.HTTP_201_CREATED
)
async def criar_usuario(
    dados: usuario_schema.CriarUsuario, 
    sessao: AsyncSession = Depends(sessao)
) -> usuario_model.Usuario:
    
    return await usuario_service.criar_usuario(dados=dados, sessao=sessao)

@usuario_rota.get(
    path='/me', 
    response_model=usuario_schema.UsuarioPublico, 
    status_code=status.HTTP_200_OK
)
async def listar_usuario(
    usuario: usuario_model.Usuario = Depends(verificar_token)
):
    
    return await usuario_service.listar_usuario(usuario=usuario)

@usuario_rota.patch(
    path='/me', 
    response_model=usuario_schema.UsuarioPublico, 
    status_code=status.HTTP_200_OK
)
async def atualizar_usuario(
    dados: usuario_schema.AtualizarUsuario, 
    usuario: usuario_model.Usuario = Depends(verificar_token),
    sessao: AsyncSession = Depends(sessao),
    
) -> usuario_model.Usuario:
    
    return await usuario_service.atualizar_usuario(
        usuario=usuario, 
        sessao=sessao, 
        dados=dados
    )