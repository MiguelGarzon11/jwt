from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel

from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import createToken, hash_password, verify_password
from app.db.schemas import UserCreate
from app.db.session import get_db
from app.db.models import User


from datetime import datetime, timedelta

router = APIRouter()

class LoginData(BaseModel):
    username: str 
    password: str 

@router.post("/login")
def login(user: LoginData, response: Response ,db: Session = Depends(get_db)):
    
    user_exist = db.query(User).filter(User.username == user.username).first()

    if user_exist:
        if (verify_password(user.password, user_exist.password)):
            token = createToken(
                {"sub": user.username, "per": ["test1", "test2"]}
            )

            response.set_cookie(
                key="access_token",
                value=token,
                httponly=True,
                secure=False
            )
            
            return {
                "msg": "Login successfully",
                "access_token": token,
                "token_type": "bearer"
            }
        
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
