from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """Schema for creating a new user."""
    name: str
    email: EmailStr
    password: str

class UserRead(BaseModel):
    """Schema for reading user information."""
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True