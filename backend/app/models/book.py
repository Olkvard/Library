from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Book(Base):
    """SQLAlchemy model for books."""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=False, unique=True)
    notes = Column(String, nullable=True)
    status = Column(String, nullable=False, default="available")