import asyncio
from typing import List

from fastapi import HTTPException

from app.api.v1.schema.movie import MovieResponse
from app.api.v1.services.movie_service import USERS_WATCHLISTS, load_movies_data

WATCHLIST_DELAY = 1


async def _simulate_io():
    await asyncio.sleep(WATCHLIST_DELAY)


async def async_get_watchlist(user_id: str) -> List[str]:
    """Fetches a user's watchlist (I/O-bound)"""
    await _simulate_io()
    return USERS_WATCHLISTS.get(user_id, [])


async def async_get_movies_by_ids(movie_ids: List[str]) -> List[MovieResponse]:
    """Fetches movie objects by ID (loads fresh data)"""
    await _simulate_io()
    movies = load_movies_data()
    return [movie for movie in movies if movie.id in movie_ids]


async def async_add_movie(user_id: str, movie_id: str) -> List[str]:
    """Adds a movie to a user's watchlist (I/O-bound). Raises an error if movie doesn't exist."""
    await _simulate_io()

    # Validate that the movie exists
    movies = load_movies_data()
    if not any(movie.id == movie_id for movie in movies):
        raise HTTPException(
            status_code=404, detail=f"Movie ID '{movie_id}' does not exist"
        )

    # Proceed to add movie to user's watchlist
    user_watchlist = USERS_WATCHLISTS.setdefault(user_id, [])
    if movie_id not in user_watchlist:
        user_watchlist.append(movie_id)

    return user_watchlist


async def async_remove_movie(user_id: str, movie_id: str) -> List[str]:
    """
    Removes a movie from a user's watchlist (I/O-bound). Raises an error if movie not found.
    """

    await _simulate_io()
    user_watchlist = USERS_WATCHLISTS.get(user_id)

    if user_watchlist is None:
        raise HTTPException(
            status_code=404, detail=f"No watchlist found for user '{user_id}'"
        )

    if movie_id not in user_watchlist:
        raise HTTPException(
            status_code=404,
            detail=f"Movie ID '{movie_id}' not found in user's watchlist",
        )

    user_watchlist.remove(movie_id)
    return user_watchlist
