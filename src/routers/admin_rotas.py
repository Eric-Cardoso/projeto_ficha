from fastapi import APIRouter, status, Depends
from schemas import admin_schema
from sqlalchemy.ext.asyncio import AsyncSession
from dependencias import sessao
from services import admin_service
from models import usuario_model
from dependencias import verificar_token

# Configura a rota de admin
admin_rota = APIRouter(prefix='/admin', tags=['admin'])

@admin_rota.get(
    path='/usuarios',
    response_model=admin_schema.ListarUsuarios, 
    status_code=status.HTTP_200_OK
)
async def listar_usuarios(
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao),
    offset: int = 0,
    limit: int = 100
) -> admin_schema.ListarUsuarios:
    
    return await admin_service.listar_usuarios(
        usuario=usuario, 
        sessao=sessao, 
        offset=offset, 
        limit=limit
    )