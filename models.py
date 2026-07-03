from sqlalchemy import String, Integer, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from datetime import date
from sqlalchemy import Date, func, CheckConstraint, ForeignKey

from database import Base

class Book(Base):

    __tablename__ = "books"


    book_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    
    author: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100)
    )

    price: Mapped[Decimal] = mapped_column(
        DECIMAL(10, 2)
    )

    pages: Mapped[int] = mapped_column(
        Integer
    )

    edition: Mapped[int] = mapped_column(
        Integer
    )

    available_copies: Mapped[int] = mapped_column(
        Integer
    )

    issued_books = relationship("IssuedBook", back_populates="book")

    def __repr__(self):
        return f"Book(id={self.book_id}, title='{self.title}', author='{self.author}')"
    
class Member(Base):

    __tablename__ = "members"

    member_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(15),
    )

    membership_date: Mapped[date] = mapped_column(
        Date,
        server_default=func.current_date()
    )

    issued_books = relationship("IssuedBook", back_populates="meber")

class IssuedBook(Base):

    __tablename__ = "issued_books"

    __table_args__ = (
        CheckConstraint(
            "status IN ('Issued', 'Returned')",
            name="check_status"
        ),
    )

    issue_id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True
    )

    book_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("books.book_id")
    )

    member_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("members.member_id")
    )

    issue_date: Mapped[date] = mapped_column(
        Date,
        server_default=func.current_date()
    )

    return_date: Mapped[date] = mapped_column(
        Date
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable= False
    )

    book = relationship("Book", back_populates="issued_books")

    member = relationship("Member", back_populates="issued_books")