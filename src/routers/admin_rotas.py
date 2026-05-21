from fastapi import APIRouter, status, Depends, Response
from schemas import admin_schema, usuario_schema
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

@admin_rota.get(
    path='/usuario/{id_usuario}',
    response_model=usuario_schema.UsuarioPublico, 
    status_code=status.HTTP_200_OK
)
async def listar_usuario(
    id_usuario: int,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> usuario_schema.UsuarioPublico:
    
    return await admin_service.listar_usuario(
        id_usuario=id_usuario,
        usuario=usuario, 
        sessao=sessao
    )

@admin_rota.patch(
    path='/usuario/{id_usuario}',
    response_model=admin_schema.UsuarioPublico, 
    status_code=status.HTTP_200_OK
)
async def atualizar_usuario(
    id_usuario: int,
    dados: admin_schema.AtualizarUsuario,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> admin_schema.UsuarioPublico:
    
    return await admin_service.atualizar_usuario(
        id_usuario=id_usuario,
        dados=dados,
        usuario=usuario, 
        sessao=sessao
    )

@admin_rota.delete(
    path='/usuario/{id_usuario}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def deletar_usuario(
    id_usuario: int,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> Response:
    
    return await admin_service.deletar_usuario(
        id_usuario=id_usuario,
        usuario=usuario, 
        sessao=sessao
    )