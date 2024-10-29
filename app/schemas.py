from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class PostCreate(BaseModel):
    title: str
    content: str
    owner_id: int

class PostRead(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
