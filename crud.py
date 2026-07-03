from database import SessionLocal
from models import Book, Member, IssuedBook


# For viewing the books

def view_books():

    session = SessionLocal()

    try:

        books = session.query(Book).all()

        return books

    finally:

        session.close()


# For Adding the books

def add_book(title, author, category, price, pages, edition, available_copies):

    session = SessionLocal()

    try:
        new_book = Book(
            title = title,
            author = author,
            category = category,
            price = price,
            pages = pages,
            edition = edition,
            available_copies = available_copies
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