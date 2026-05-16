from fastapi import APIRouter, status, Depends
from schemas import ficha_schema
from sqlalchemy.ext.asyncio import AsyncSession
from dependencias import sessao
from services import ficha_service
from models import ficha_model, usuario_model
from dependencias import verificar_token

# Configura a rota de ficha
ficha_rota = APIRouter(prefix='/fichas', tags=['fichas'])

@ficha_rota.post(
    path='/criar', 
    response_model=ficha_schema.FichaPublica, 
    status_code=status.HTTP_201_CREATED
)
async def criar_ficha(
    dados: ficha_schema.CriarFicha, 
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> ficha_model.Ficha:
    
    return await ficha_service.criar_ficha(
        dados=dados, 
        usuario=usuario, 
        sessao=sessao
    )