from fastapi import FastAPI, HTTPException

app = FastAPI(title="Habit Tracker API")

# Temporary in-memory data until phase 2 adds a database.
# It resets every time the server restarts.
HABITS: list[dict] = [
    {"id": 1, "name": "Drink water", "done": True},
    {"id": 2, "name": "Read 10 pages", "done": False},
    {"id": 3, "name": "Walk 20 minutes", "done": False},
]


@app.get("/health")
def health() -> dict[str, str]:
    """Tell clients the API process is up and answering requests."""
    return {"status": "ok"}


@app.get("/habits")
def list_habits(done: bool | None = None) -> list[dict]:
    """List habits; ?done=true or ?done=false keeps only matching ones."""
    if done is None:
        return HABITS
    return [habit for habit in HABITS if habit["done"] == done]


@app.get("/habits/{habit_id}")
def get_habit(habit_id: int) -> dict:
    """Return one habit by id, or 404 if it does not exist."""
    for habit in HABITS:
        if habit["id"] == habit_id:
            return habit
    raise HTTPException(status_code=404, detail="Habit not found")
