from database import SessionLocal, get_db
from models import Book
from crud import view_books, add_book, create_access_token
from fastapi import FastAPI, Depends, HTTPException
from schemas import BookCreate, BookResponse, UserCreate, UserLogin
import crud
from sqlalchemy.orm import Session
from auth import verify_password

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


@app.post("/books")
def create_book(book: BookCreate):

    return crud.add_book(book)

@app.get("/books/{book_id}")
def view_book(book_id: int):

    return crud.get_book(book_id)

@app.post("/books/{book_id}")
def update_book(book_id: int, book_data: BookCreate):

    return crud.update_book(book_id, book_data)

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    return crud.delete_book(book_id)


@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/login")
def login(login_user: UserLogin, db: Session = Depends(get_db)):

    db_user = crud.authenticate_user(db, login_user.username)

    if db_user is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    if not verify_password(
        login_user.password, db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    
    access_token = create_access_token(
        data = {
            "sub": db_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

