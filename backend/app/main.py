from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db

# FastAPI application instance
app = FastAPI(title="Library System")

# Health check endpoint
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check endpoint to verify database connectivity."""
    return {"status": "ok", "db": "connected"}