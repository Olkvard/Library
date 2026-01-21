from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user.
    Args:
        user (UserCreate): The user data to create.
        db (Session, optional): The database session. Defaults to Depends(get_db).
    Returns:
        UserRead: The created user.
    """
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=user.password  # In a real app, hash the password!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user