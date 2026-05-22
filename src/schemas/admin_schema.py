from pydantic import BaseModel
from schemas.usuario_schema import UsuarioPublico
from schemas.ficha_schema import FichaPublica
from typing import Optional

class ListarUsuarios(BaseModel):
    usuarios: list[UsuarioPublico]

class AtualizarUsuario(BaseModel):
    ativo: Optional[bool] = None
    admin: Optional[bool] = None

class UsuarioPublico(BaseModel):
    id: int
    nome: str
    email: str
    quantidade_fichas: int
    ativo: bool
    admin: bool

class ListarFichas(BaseModel):
    usuario: UsuarioPublico
    fichas: list[FichaPublica]