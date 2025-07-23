from fastapi import APIRouter

from .movie_routes import router as movie_router
from .watchlist_routes import router as watchlist_router

router = APIRouter()
router.include_router(movie_router)
router.include_router(watchlist_router)
