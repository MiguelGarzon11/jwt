from fastapi import FastAPI
from app.api.auth.endpoints import login, register
from app.api.features.endpoints import dashboard
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(login.router, prefix="/auth", tags=["auth"])
app.include_router(register.router, prefix="/auth", tags=["auth"])
app.include_router(dashboard.router)