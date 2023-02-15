from fastapi import FastAPI, APIRouter
from authenticator import authenticator
from routers import accounts
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(authenticator.router)
app.include_router(accounts.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
