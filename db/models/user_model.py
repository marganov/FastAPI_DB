from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
#from typing import Optional

class UserBase(BaseModel):
    full_name: str = Field(..., description="Full user name")
    email: EmailStr = Field(..., description="User email")

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True