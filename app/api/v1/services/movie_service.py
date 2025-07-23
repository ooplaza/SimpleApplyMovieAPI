import json
from pathlib import Path

from fastapi import HTTPException
from pydantic import ValidationError

from app.api.v1.schema.movie import MovieResponse

MOVIES_JSON_PATH = Path(__file__).resolve().parent.parent / "models" / "movies.json"
USERS_WATCHLISTS: dict[str, list[str]] = {}


def load_movies_data() -> list[MovieResponse]:
    try:
        with MOVIES_JSON_PATH.open() as file:
            raw_movies = json.load(file)
            return [MovieResponse.model_validate(movie) for movie in raw_movies]
    except ValidationError as ve:
        raise HTTPException(
            status_code=422, detail=f"Invalid movie data: {ve.errors()}"
        )
    except (FileNotFoundError, json.JSONDecodeError) as error:
        raise HTTPException(status_code=400, detail=f"Error loading movies: {error}")
