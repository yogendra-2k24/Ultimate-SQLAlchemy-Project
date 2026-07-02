from database import SessionLocal
from models import Book

def view_books():

    session = SessionLocal()

    try:

        books = session.query(Book).all()

        return books

    finally:

        session.close()