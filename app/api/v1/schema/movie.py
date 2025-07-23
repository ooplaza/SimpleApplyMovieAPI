from typing import List

from pydantic import BaseModel, ConfigDict


class WatchlistAddRequest(BaseModel):
    movie_id: str

    model_config = ConfigDict(extra="forbid")


class MovieResponse(BaseModel):
    id: str
    title: str
    year: int
    genres: List[str]
    plot: str


class WatchlistResponse(BaseModel):
    message: str
    watchlist: List[str]
