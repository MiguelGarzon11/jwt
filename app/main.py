from fastapi import FastAPI
from app.api.auth.endpoints import login, register
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(login.router, prefix="/auth", tags=["auth"])
app.include_router(register.router, prefix="/auth", tags=["auth"])