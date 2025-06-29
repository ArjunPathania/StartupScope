# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.database import Base, engine
from app.models.company import Company

# Correct way to create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StartupScope",
    description="Backend service for StartupScope.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the versioned API router
app.include_router(api_router, prefix="/api/v1")
