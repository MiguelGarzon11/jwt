from fastapi import APIRouter, Depends, HTTPException, status

from app.db.schemas import UserCreate
from app.db.models import User
from app.core.security import hash_password
from app.db.session import get_db

from sqlalchemy.orm import Session



router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User (
        username = user.username,
        password = hash_password(user.password)
    )

    username_exist = db.query(User).filter(User.username == user.username).first()

    if username_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already in use"
        )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

