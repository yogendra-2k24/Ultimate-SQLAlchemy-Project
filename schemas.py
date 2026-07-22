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


class UserBase(BaseModel):
    username: str
    email: EmailStr    

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    user_id: int