from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import createToken, ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import datetime, timedelta

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    userFake = {
        "username": form_data.username,
        "role": "student" if form_data.username != "admin" else "admin"
    }
    access_token = createToken(
        data={"sub": userFake["username"], "role": userFake["role"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return { 
        "acces_token": access_token, 
        "token_type": "bearer", 
        "role": userFake["role"] 
    }
78