from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata = Base.metadata
metadata.schema = "public"
