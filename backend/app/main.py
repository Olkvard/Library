from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db

app = FastAPI(title="Library System")

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "ok", "db": "connected"}