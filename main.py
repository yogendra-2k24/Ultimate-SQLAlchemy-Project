from database import SessionLocal
from models import Book
from crud import view_books, add_book
from fastapi import FastAPI
from schemas import BookCreate, BookResponse
import crud

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
def get_book():
    books = crud.view_books()
    return books

@app.get("/books", response_model=list[BookResponse])
def get_books(
    category: str | None = None,
    min_price: float | None = None
):
    return crud.get_books(category, min_price)


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
