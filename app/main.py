from fastapi import FastAPI
from app.api.auth.endpoints import login, register


app = FastAPI()

app.include_router(login.router, prefix="/auth", tags=["auth"])
app.include_router(register.router, prefix="/auth", tags=["auth"])