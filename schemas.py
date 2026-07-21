from pydantic import BaseModel, EmailStr

class BookCreate(BaseModel):
    title: str
    author: str
    category: str
    price: float
    pages: int
    edition: int
    available_copies: int

class BookResponse(BaseModel):

    title: str
    author: str
    category: str
    price: float
    pages: int
    edition: int
    available_copies: int

    model_config = {
    "from_attributes": True
    }

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str