from fastapi import Depends, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from dependencias import sessao, verificar_token
from services import auth_service
from schemas import auth_schema
from models import usuario_model

# Configura a rota de autenticação
auth_rota = APIRouter(prefix='/auth', tags=['auth'])

@auth_rota.post(
    path='/login', 
    response_model=auth_schema.TokenPublico, 
    status_code=status.HTTP_200_OK
)
async def login_usuario(
    usuario: OAuth2PasswordRequestForm = Depends(), 
    sessao: AsyncSession = Depends(sessao)
) -> dict:
    
    return await auth_service.login_usuario(usuario=usuario, sessao=sessao)


@auth_rota.get(
    path='/refresh', 
    response_model=auth_schema.RefreshPublico, 
    status_code=status.HTTP_200_OK
)
async def refresh(usuario: usuario_model.Usuario = Depends(verificar_token)
) -> dict:
    
    return await auth_service.refresh(usuario=usuario)
