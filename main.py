from database import SessionLocal
from models import Book
from crud import view_books, add_book
from fastapi import FastAPI

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

@app.get("/books")
def get_book():
    return {"message": "List of Books"}

@app.post("/books")
def create_book():
    return {"message": "Book Created Successfully"}