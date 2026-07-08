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