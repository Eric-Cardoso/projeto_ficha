from fastapi import Depends, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from dependencias import sessao
from services import auth_service
from schemas import auth_schema

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
