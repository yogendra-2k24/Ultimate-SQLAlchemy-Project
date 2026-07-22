from database import get_db
from models import User
from fastapi import FastAPI, Depends, HTTPException
from schemas import BookCreate, BookResponse, UserCreate, UserResponse
import crud, auth
from sqlalchemy.orm import Session
from auth import verify_password, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

# This method is called from crud.py for viwing books

# books = view_books()

# for book in books:
#     print(book)


# book = add_book("Think Python","Allen Downey", "Programming", 750.00, 450, 2, 8)

# print(book)

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Welcome to Library Management API"}


@app.get("/about")
def about():
    return {
        "message": "Library Management System Backend"
    }


@app.get("/books", response_model=list[BookResponse])
def get_books(
    category: str | None = None,
    min_price: float | None = None,
    sort_by: str = "book_id",
    order: str = "asc",
    skip: int = 0,
    limit: int = 10
):
    return crud.get_books(category, min_price, sort_by, order, skip, limit)


@app.get("/books/filter", response_model=list[BookResponse])
def filter_books(category: str):

    return crud.filter_books(category)


@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate, current_user: User = Depends(get_current_user)):

    return crud.add_book(book)

@app.get("/books/{book_id}")
def view_book(book_id: int):

    return crud.get_book(book_id)

@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: BookCreate):

    return crud.update_book(book_id, book_data)

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    return crud.delete_book(book_id)


@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = auth.authenticate_user(db, form_data.username)

    if db_user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    if not verify_password(
        form_data.password, db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    access_token = auth.create_access_token(
        data = {
            "sub": str(db_user.user_id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/me", response_model=UserResponse)
def me(
    current_user: User = Depends(get_current_user)
):
    return {
        "user_id": current_user.user_id,
        "username": current_user.username,
        "email": current_user.email
    }

@app.post("/return/{issue_id}")
def return_book(issue_id: int):
    return crud.return_book(issue_id)


@app.get("/member/{member_id}")
def get_member(member_id: int):
    member = crud.get_member(member_id)
    # print(member.issued_books)
    return member