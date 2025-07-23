from fastapi import APIRouter

from app.api.v1.schema.movie import MovieResponse, WatchlistAddRequest
from app.api.v1.services.watchlist_service import (
    async_add_movie,
    async_get_movies_by_ids,
    async_get_watchlist,
    async_remove_movie,
)

router = APIRouter()


@router.get("/watchlist/{user_id}", response_model=list[MovieResponse])
async def get_user_watchlist(user_id: str):
    """
    Get user's watchlist.
    """
    movie_ids = await async_get_watchlist(user_id)
    watchlist_movies = await async_get_movies_by_ids(movie_ids)
    return watchlist_movies


@router.post("/watchlist/{user_id}")
async def add_to_watchlist(user_id: str, add_request: WatchlistAddRequest):
    """
    Add a movie to user's watchlist.
    """
    updated_watchlist = await async_add_movie(user_id, add_request.movie_id)
    return {
        "message": "Movie added",
        "watchlist": updated_watchlist,
    }


@router.delete("/watchlist/{user_id}/{movie_id}")
async def remove_from_watchlist(user_id: str, movie_id: str):
    """
    Remove movie from user's watchlist.
    """
    updated_watchlist = await async_remove_movie(user_id, movie_id)
    return {
        "message": "Movie removed",
        "watchlist": updated_watchlist,
    }
