from database import SessionLocal
from models import Book, Member, IssuedBook
from schemas import BookCreate
from fastapi import HTTPException


# For viewing the books

def view_books():

    session = SessionLocal()

    try:

        books = session.query(Book).all()

        return books

    finally:

        session.close()


# For Adding the books

def add_book(book_data: BookCreate):

    session = SessionLocal()

    try:
        new_book = Book(
            title = book_data.title,
            author = book_data.author,
            category = book_data.category,
            price = book_data.price,
            pages = book_data.pages,
            edition = book_data.edition,
            available_copies = book_data.available_copies
        )

        session.add(new_book)

        session.commit()

        session.refresh(new_book)

        return new_book
    
    finally:

        session.close()



# For Updating the price of the book


def update_book_price(title, new_price):

    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            Book.title == title
        ).first()

        if book:

            book.price = new_price

            session.commit()

            session.refresh(book)

            return book
        
        return None
    
    except Exception:

        session.rollback()

        raise

    finally:

        session.close()


# For deleting the book

def delete_book(title):

    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            Book.title == title
        ).first()

        if book:

            session.delete(book)

            session.commit()

            return True
    
        return False

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()


def issue_book(book_id, member_id):

    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            Book.book_id == book_id
        ).first()

        if not book:
            return "Book Not Found"
        
        if book.available_copies == 0:
            return "Book Not Available"
        

        member = session.query(Member).filter(
            Member.member_id == member_id
        ).first()

        if not member:
            return "Member not Found!"
        
        total_books = session.query(IssuedBook).filter(
            IssuedBook.member_id == member_id,
            IssuedBook.status == 'Issued'
        ).count()

        if total_books >= 3:
            return "Maximum Issue Limit Reached"
        
        new_issue = IssuedBook(
            book_id = book.book_id,
            member_id = member.member_id,
            status = 'Issued'
        )

        session.add(new_issue)

        book.available_copies -= 1

        session.commit()

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()

def get_book(book_id: int):

    session = SessionLocal()

    try:

        book = session.query(Book).filter( 
            Book.book_id == book_id
        ).first()

        if book is None:

            raise HTTPException(
                status_code=404,
                detail="Book Not Found"
            )
        
        return book
    
    finally:

        session.close()


def update_book(book_id: int, book_data: BookCreate):
    
    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            Book.book_id == book_id
        ).first()

        if book is None:

            raise HTTPException(
                status_code=404,
                detail="Book Not Found"
            )
        
        book.title = book_data.title
        book.author = book_data.author
        book.category = book_data.category
        book.price = book_data.price
        book.pages = book_data.pages
        book.edition = book_data.edition
        book.available_copies = book_data.available_copies

        session.commit()

        session.refresh(book)

        return book
    
    finally:

        session.close()

def delete_book(book_id: int):

    session = SessionLocal

    try:

        book = session.query(Book).filter(
            Book.book_id == book_id
        ).first()

        if book is None:

            raise HTTPException(
                status_code=404,
                detail="Book Not Found"
            )
        
        session.delete(book)

        session.commit()

        return {
            "message" : "Book deleted Successfully"
        }

    finally:

        session.close()


def filter_books(category: str):

    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            Book.category == category
        ).all()

        return book
    
    finally:

        session.close()


def get_books(
        category: str | None = None,
        min_price: float | None = None,
        skip: int = 0,
        limit: int = 10
):
    session = SessionLocal()

    try:

        query = session.query(Book)

        if category is not None:

            query = query.filter(Book.category == category)

        if min_price is not None:

            query = query.filter(Book.price >= min_price)

        query = query.offset(skip)

        query = query.limit(limit)

        books = query.all()

        return books
    
    finally:

        session.close()