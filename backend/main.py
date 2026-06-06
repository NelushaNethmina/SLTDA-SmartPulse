from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import auth


app = FastAPI(
    title="SLTDA SmartPulse",
    description="AI-Powered Tourism Business Intelligence Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth.router, 
    prefix="/api/auth", 
    tags=["Authentication"]
)


@app.get("/")
async def root():
    return {
        "system": settings.app_name,
        "status": "operational",
        "version": "1.0.0",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected",
    }
    
    