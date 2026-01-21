from sqlalchemy.orm import declarative_base

# SQLAlchemy Base class for models
Base = declarative_base()
metadata = Base.metadata
metadata.schema = "public"
