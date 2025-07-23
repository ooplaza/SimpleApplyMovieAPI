# Python Developer Take-Home Challenge: Movie Watchlist API

Welcome to our take-home programming challenge! This exercise is designed to assess your skills in building a simple, yet functional, RESTful API using Python. We're looking for clean, well-structured, and maintainable code that demonstrates your understanding of core software engineering principles.

## The Challenge

Your task is to complete a "Movie Watchlist" service. This service will allow users to manage a list of movies they want to watch. We have provided a boilerplate with a predefined list of movies and a simple in-memory database.

### Core Features

1. **Retrieve a User's Watchlist:**
  * Create an API endpoint that retrieves all the movies on a user's watchlist from the database.

2. **Add a Movie to a Watchlist:**
  * Create an API endpoint that adds a movie to a user's watchlist.

3. **Remove a Movie from a Watchlist:**
  * Create an API endpoint that removes a movie from a user's watchlist.

### Technical Requirements

* **Framework:** Use [FastAPI](https://fastapi.tiangolo.com/) to build the API.
* **Asynchronous Programming:** Use `asyncio` for all I/O-bound operations.
* **Data Modeling:** Use [Pydantic](https://docs.pydantic.dev/) to define the data models for your API requests and responses.
* **Dependencies:** List all project dependencies in a `requirements.txt` file.

### Getting Started

We have provided a basic project structure to get you started:

* `main.py`: A minimal FastAPI application with endpoint stubs for you to complete.
* `movies.json`: A file containing the movie data for the service.
* `requirements.txt`: A file containing the project's dependencies.

You will need to:

1. Install the required dependencies: `pip install -r requirements.txt`
2. Run the application: `uvicorn main:app --reload`
3. Implement the logic for the API endpoints in `main.py` (look for the `NotImplementedError`).

### Optional Requirements

* **Containerization:** Create a `Dockerfile` and a corresponding `docker-compose.yml` file to allow the application to be run in a container.
* **Unit Tests:** Write unit tests for the API endpoints. We recommend using `pytest`, but you are free to use any testing framework you are comfortable with.

### What We're Looking For

* **Correctness:** The application should work as described in the feature requirements.
* **Code Quality:** Your code should be clean, well-organized, and easy to understand.
* **Best Practices:** We're interested in seeing your approach to error handling and API design.
* **Problem-Solving:** How you structure your code and solve the given problem.

### Submission

Please submit your solution as a link to a Git repository (e.g., on GitHub or GitLab). Make sure the repository is public so we can access it.

Good luck! We look forward to seeing your work.
