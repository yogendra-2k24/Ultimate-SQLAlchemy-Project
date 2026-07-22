from pydantic import BaseModel, EmailStr, Field


class BookBase(BaseModel):
    title: str
    author: str
    category: str
    price: float = Field(gt=0)
    pages: int = Field(gt=0)
    edition: int = Field(gt=0)
    available_copies: int = Field(ge=0)

class BookCreate(BookBase):
   pass

class BookResponse(BookBase):

    book_id: int

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