from fastapi import FastAPI

app = FastAPI(title="Habit Tracker API")


# @app.get("/health")
def health() -> dict[str, str]:
    """Tell clients the API process is up and answering requests."""
    return {"status": "ok"}
