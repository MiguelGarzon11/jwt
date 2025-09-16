from fastapi import APIRouter, Depends,  HTTPException, status
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import createToken, ACCESS_TOKEN_EXPIRE_MINUTES, hash_password, verify_password
from app.db.schemas import UserCreate
from app.db.session import get_db
from app.db.models import User


from datetime import datetime, timedelta

router = APIRouter()

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    
    user_exist = db.query(User).filter(User.username == user.username).first()

    if user_exist:
        if (verify_password(user.password, user_exist.password)):
            raise HTTPException(
                status_code=status.HTTP_202_ACCEPTED,
                detail="Login successfully"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect password"
            )
    else: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user does not exist"
        )
