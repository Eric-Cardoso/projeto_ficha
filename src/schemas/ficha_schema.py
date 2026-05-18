from pydantic import BaseModel, Field
from typing import Optional

class CriarFicha(BaseModel): 
    nome_personagem: Optional[str] = None
    nome_jogador: Optional[str] = None
    vida: Optional[int] = Field(default=20)
    sanidade: Optional[int] = Field(default=10)
    classe: Optional[str] = None
    forca: Optional[int] = Field(default=1)
    agilidade: Optional[int] = Field(default=1)
    intelecto: Optional[int] = Field(default=1)
    presenca: Optional[int] = Field(default=1)
    vigor: Optional[int] = Field(default=1)
    inventario: Optional[str] = None
    descricao: Optional[str] = None
    defesa: Optional[int] = Field(default=1)
    armas: Optional[str] = None

class FichaPublica(BaseModel):
    id: int
    id_usuario: int 
    nome_personagem: Optional[str] = None
    nome_jogador: Optional[str] = None
    vida: int
    sanidade:int
    classe: Optional[str] = None
    forca: int
    agilidade: int
    intelecto: int
    presenca: int
    vigor: int
    inventario: Optional[str] = None
    descricao: Optional[str] = None
    defesa: int
    armas: Optional[str] = None

class ListarFichas(BaseModel):
    fichas: list[FichaPublica]

class AtualizarFicha(BaseModel):
    nome_personagem: str
    nome_jogador: str
    vida: int = Field(default=20)
    sanidade: int = Field(default=10)
    classe: str
    forca: int = Field(default=1)
    agilidade: int = Field(default=1)
    intelecto: int = Field(default=1)
    presenca: int = Field(default=1)
    vigor: int = Field(default=1)
    inventario: str
    descricao: str
    defesa: int = Field(default=1)
    armas: str

class AtualizarParcialFicha(BaseModel):
    nome_personagem: Optional[str] = None
    nome_jogador: Optional[str] = None
    vida: Optional[int] = Field(default=20)
    sanidade: Optional[int] = Field(default=10)
    classe: Optional[str] = None
    forca: Optional[int] = Field(default=1)
    agilidade: Optional[int] = Field(default=1)
    intelecto: Optional[int] = Field(default=1)
    presenca: Optional[int] = Field(default=1)
    vigor: Optional[int] = Field(default=1)
    inventario: Optional[str] = None
    descricao: Optional[str] = None
    defesa: Optional[int] = Field(default=1)
    armas: Optional[str] = None