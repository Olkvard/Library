from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    """Schema for creating a new book."""
    title: str
    author: str
    isbn: str
    notes: Optional[str] = None

class BookRead(BaseModel):
    """Schema for reading book information."""
    id: int
    title: str
    author: str
    isbn: str
    status: str

    class Config:
        from_attributes = True