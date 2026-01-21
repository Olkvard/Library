from app.db.session import engine
from app.models import user, book, loan  # Import all models to register them with Base
from app.db.base import Base

def init_db():
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)
    print("Created tables: ")

if __name__ == "__main__":
    init_db()