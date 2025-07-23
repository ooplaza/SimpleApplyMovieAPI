import asyncio
import json

from fastapi import FastAPI
from pydantic import BaseModel


# Data Models
class Movie(BaseModel):
    id: str
    title: str
    year: int
    genres: list[str]
    plot: str


class WatchlistAddRequest(BaseModel):
    movie_id: str


# Database (In-Memory)
with open("movies.json") as f:
    MOVIES_DATA: list[Movie] = [Movie.model_validate(m) for m in json.load(f)]

# A simple in-memory "database" to store user watchlists.
# The key is a user_id (string), and the value is a list of movie IDs (strings).
WATCHLISTS: dict[str, list[str]] = {}

# API Endpoints
# TODO: Implement the following endpoints.
app = FastAPI()


@app.get("/movies")
async def get_all_movies() -> list[Movie]:
    """
    Returns a list of all available movies.
    """

    # Simulate network latency
    await asyncio.sleep(1)

    return MOVIES_DATA


@app.get("/watchlist/{user_id}")
async def get_watchlist(user_id: str):
    """
    Retrieves the watchlist for a given user.
    """
    raise NotImplementedError


@app.post("/watchlist/{user_id}")
async def add_to_watchlist(user_id: str, add_request: WatchlistAddRequest):
    """
    Adds a movie to a user's watchlist.
    """
    raise NotImplementedError


@app.delete("/watchlist/{user_id}/{movie_id}")
async def remove_from_watchlist(user_id: str, movie_id: str):
    """
    Removes a movie from a user's watchlist.
    """
    raise NotImplementedError
