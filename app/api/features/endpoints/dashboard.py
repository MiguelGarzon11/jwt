from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()

@router.get("/dashboard")
def dashboard(user=Depends(get_current_user)):
    return {"msg": f"Bienvenido"}