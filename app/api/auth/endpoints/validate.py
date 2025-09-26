from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from app.db.models import User


router = APIRouter()

@router.get("/validate")
def read_current_user(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"detail": "User authenticated"}
    