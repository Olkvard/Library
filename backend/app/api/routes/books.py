from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookRead

router = APIRouter()

@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Create a new book.
    Args:
        book (BookCreate): The book data to create.
        db (Session, optional): The database session. Defaults to Depends(get_db).
    Returns:
        BookRead: The created book.
    """
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book