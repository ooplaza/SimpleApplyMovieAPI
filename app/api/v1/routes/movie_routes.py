import asyncio

from fastapi import APIRouter

from app.api.v1.schema.movie import MovieResponse
from app.api.v1.services.movie_service import load_movies_data

router = APIRouter()


@router.get("/movies", response_model=list[MovieResponse])
async def get_all_movies():
    """Return a list of available movies."""
    await asyncio.sleep(1)
    return load_movies_data()
