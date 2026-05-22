from fastapi import APIRouter, status, Depends, Response
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

@ficha_rota.get(
    path='/listar', 
    response_model=ficha_schema.ListarFichas, 
    status_code=status.HTTP_200_OK
)
async def listar_fichas(
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> ficha_schema.ListarFichas:
    
    return await ficha_service.listar_fichas(
        usuario=usuario, 
        sessao=sessao
    )

@ficha_rota.get(
    path='/{id_ficha}', 
    response_model=ficha_schema.FichaPublica, 
    status_code=status.HTTP_200_OK
)
async def listar_ficha(
    id_ficha: int,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> ficha_schema.FichaPublica:
    
    return await ficha_service.listar_ficha(
        id_ficha=id_ficha,
        usuario=usuario, 
        sessao=sessao
    )

@ficha_rota.put(
    path='/{id_ficha}', 
    response_model=ficha_schema.FichaPublica, 
    status_code=status.HTTP_200_OK
)
async def atualizar_ficha(
    id_ficha: int,
    dados: ficha_schema.AtualizarFicha,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> ficha_schema.FichaPublica:
    
    return await ficha_service.atualizar_ficha(
        id_ficha=id_ficha,
        dados=dados,
        usuario=usuario, 
        sessao=sessao
    )

@ficha_rota.patch(
    path='/{id_ficha}', 
    response_model=ficha_schema.FichaPublica, 
    status_code=status.HTTP_200_OK
)
async def atualizar_parcial_ficha(
    id_ficha: int,
    dados: ficha_schema.AtualizarParcialFicha,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> ficha_schema.FichaPublica:
    
    return await ficha_service.atualizar_parcial_ficha(
        id_ficha=id_ficha,
        dados=dados,
        usuario=usuario, 
        sessao=sessao
    )

@ficha_rota.delete(
    path='/{id_ficha}', 
    status_code=status.HTTP_204_NO_CONTENT
)
async def deletar_ficha(
    id_ficha: int,
    usuario: usuario_model.Usuario = Depends(verificar_token), 
    sessao: AsyncSession = Depends(sessao)
) -> Response:
    
    return await ficha_service.deletar_ficha(
        id_ficha=id_ficha,
        usuario=usuario, 
        sessao=sessao
    )