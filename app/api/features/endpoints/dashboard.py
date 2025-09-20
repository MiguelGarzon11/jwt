from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.get("/dashboard")
def dashboard(token: str = Depends(oauth2_scheme), user=Depends(get_current_user)):
    return {"msg": f"Bienvenido"}