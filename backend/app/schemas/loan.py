from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LoanCreate(BaseModel):
    """Schema for creating a new loan."""
    user_id: int
    book_id: int

class LoanRead(BaseModel):
    """Schema for reading loan information."""
    id: int
    user_id: int
    book_id: int
    loan_date: datetime
    return_date: Optional[datetime] = None

    class Config:
        from_attributes = True