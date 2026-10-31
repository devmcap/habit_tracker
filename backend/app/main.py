from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query

app = FastAPI(title="Habit Tracker API")

# Temporary in-memory data until phase 2 adds a database.
# It resets every time the server restarts.
HABITS: list[dict] = [
    {"id": 1, "name": "Drink water", "done": True},
    {"id": 2, "name": "Read 10 pages", "done": False},
    {"id": 3, "name": "Walk 20 minutes", "done": False},
]


def get_habit_store() -> list[dict]:
    """Provide the habits that endpoints read; tests can replace it with an override."""
    return HABITS


@app.get("/health")
def health() -> dict[str, str]:
    """Tell clients the API process is up and answering requests."""
    return {"status": "ok"}


@app.get("/habits")
def list_habits(
        store: Annotated[list[dict], Depends(get_habit_store)],
        done: Annotated[
            bool | None,
            Query(description="Shows only done (true) or pending (false) habits. Omit it to get all habits."),
        ] = None,
        limit: Annotated[
            int | None,
            Query(ge=1, description="Maximum number of habits to return."),
        ] = None,
) -> list[dict]:
    """List habits."""
    habits = store
    if done is not None:
        habits = [habit for habit in store if habit["done"] == done]
    return habits[:limit]


@app.get("/habits/{habit_id}")
def get_habit(
        habit_id: int,
        store: Annotated[list[dict], Depends(get_habit_store)],
) -> dict:
    """Return one habit by id, or 404 if it does not exist."""
    for habit in store:
        if habit["id"] == habit_id:
            return habit
    raise HTTPException(status_code=404, detail="Habit not found")
