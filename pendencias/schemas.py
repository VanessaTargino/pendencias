from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDB(UserSchema):
    id: int


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class PendenciaCreate(BaseModel):
    titulo: str
    descricao: str
    usuario_id: int


class Pendencia(BaseModel):
    id: int
    titulo: str
    descricao: str
    usuario_id: int
    concluida: bool = False
