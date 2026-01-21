from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.api.deps import get_db
from app.models.loan import Loan
from app.models.book import Book
from app.schemas.loan import LoanCreate, LoanRead

router = APIRouter()

@router.post("/", response_model=LoanRead)
def loan_book(data: LoanCreate, db: Session = Depends(get_db)):
    """Create a new loan for a book.
    Args:
        data (LoanCreate): The loan data to create.
        db (Session, optional): The database session. Defaults to Depends(get_db).
    Returns:
        LoanRead: The created loan.
    """
    book = db.get(Book, data.book_id)
    if not book or book.status != "available":
        raise HTTPException(status_code=400, detail="Book is not available for loan.")
    
    book.status = "loaned"
    loan = Loan(user_id=data.user_id, book_id=data.book_id)
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

@router.post("/{loan_id}/return")
def return_book(loan_id: int, db: Session = Depends(get_db)):
    """Return a loaned book.
    Args:
        loan_id (int): The ID of the loan to return.
        db (Session, optional): The database session. Defaults to Depends(get_db).
    Returns:
        dict: A message indicating the book has been returned.
    """
    loan = db.get(Loan, loan_id)
    if not loan or loan.return_date is not None:
        raise HTTPException(status_code=400, detail="Invalid loan ID or book already returned.")
    
    loan.return_date = datetime.utcnow()
    loan.book.status = "available"
    db.commit()
    return {"status": "returned"}