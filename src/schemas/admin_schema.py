from pydantic import BaseModel
from schemas.usuario_schema import UsuarioPublico

class ListarUsuarios(BaseModel):
    usuarios: list[UsuarioPublico]