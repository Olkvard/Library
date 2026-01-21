from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# SQLAlchemy engine instance
engine = create_engine(settings.DATABASE_URL, echo=True)

# SQLAlchemy session factory 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)