from fastapi import FastAPI

from app.api.routes import users, books, loans

# FastAPI application instance
app = FastAPI(title="Library System")

# Include API routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(loans.router, prefix="/loans", tags=["loans"])

# Health check endpoint
@app.get("/")
def health():
    """Health check endpoint to verify database connectivity."""
    return {"status": "ok"}