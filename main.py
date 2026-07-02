from database import SessionLocal
from models import Book
from crud import view_books

# This method is called from crud.py for viwing books

books = view_books()

for book in books:
    print(book)