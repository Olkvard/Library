from app.db.session import engine
from app.models import user, book, loan  # Import all models to register them with Base
from app.db.base import Base

def init_db():
    print("Before create_all: ", Base.metadata.tables)
    Base.metadata.create_all(bind=engine)
    print("After create_all: ", Base.metadata.tables)

if __name__ == "__main__":
    init_db()