import pytest
from fastapi import HTTPException

from app.api.v1.services import movie_service, watchlist_service

# Remove artificial delay for faster testing
movie_service.WATCHLIST_DELAY = 0


@pytest.fixture
def sample_movies():
    return [
        movie_service.MovieResponse(
            id="1", title="Movie One", year=2020, genres=["Action"], plot="Plot 1"
        ),
        movie_service.MovieResponse(
            id="2", title="Movie Two", year=2021, genres=["Drama"], plot="Plot 2"
        ),
    ]


@pytest.mark.asyncio
async def test_get_watchlist_returns_empty():
    result = await watchlist_service.async_get_watchlist("user1")
    assert result == []


@pytest.mark.asyncio
async def test_add_movie_success(monkeypatch, sample_movies):
    monkeypatch.setattr(watchlist_service, "load_movies_data", lambda: sample_movies)

    result = await watchlist_service.async_add_movie("user1", "1")

    assert result == ["1"]
    assert watchlist_service.USERS_WATCHLISTS["user1"] == ["1"]


@pytest.mark.asyncio
async def test_add_movie_invalid_id(monkeypatch, sample_movies):
    monkeypatch.setattr(watchlist_service, "load_movies_data", lambda: sample_movies)

    with pytest.raises(HTTPException) as exc_info:
        await watchlist_service.async_add_movie("user1", "999")

    assert exc_info.value.status_code == 404
    assert "does not exist" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_remove_movie_success(monkeypatch, sample_movies):
    monkeypatch.setattr(watchlist_service, "load_movies_data", lambda: sample_movies)
    await watchlist_service.async_add_movie("user1", "1")

    result = await watchlist_service.async_remove_movie("user1", "1")

    assert result == []
    assert movie_service.USERS_WATCHLISTS["user1"] == []


@pytest.mark.asyncio
async def test_remove_movie_user_not_found():
    with pytest.raises(HTTPException) as exc_info:
        await watchlist_service.async_remove_movie("nonexistent_user", "1")

    assert exc_info.value.status_code == 404
    assert "No watchlist found" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_remove_movie_id_not_in_watchlist(monkeypatch, sample_movies):
    monkeypatch.setattr(watchlist_service, "load_movies_data", lambda: sample_movies)
    await watchlist_service.async_add_movie("user1", "1")

    with pytest.raises(HTTPException) as exc_info:
        await watchlist_service.async_remove_movie("user1", "2")

    assert exc_info.value.status_code == 404
    assert "not found in user's watchlist" in str(exc_info.value.detail)


@pytest.mark.asyncio
async def test_get_movies_by_ids(monkeypatch, sample_movies):
    monkeypatch.setattr(watchlist_service, "load_movies_data", lambda: sample_movies)

    result = await watchlist_service.async_get_movies_by_ids(["1", "2", "999"])

    assert len(result) == 2
    ids = [movie.id for movie in result]
    assert "1" in ids and "2" in ids
