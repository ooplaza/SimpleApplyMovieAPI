from fastapi import FastAPI

from app.api.v1.routes import router as api_router

app = FastAPI(title="Movie API")
app.include_router(api_router, prefix="/api/v1")
