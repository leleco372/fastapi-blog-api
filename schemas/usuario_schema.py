from typing import Optional, List

from pydantic import BaseModel, EmailStr, ConfigDict

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False


class UsuarioSchemaCreate(UsuarioSchemaBase):

    senha: str


class UsuarioSchemasArtigos(UsuarioSchemaBase):

    artigos: Optional[List[ArtigoSchema]] = None


class UsuarioSchemaUp(UsuarioSchemaBase):

    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    eh_admin: Optional[bool] = None