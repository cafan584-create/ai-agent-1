from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.config import get_settings
from backend.api import countries, health_scores, alerts, queries, briefings, comparisons

settings = get_settings()

app = FastAPI(
    title="SOVEREIGN",
    description="Global Financial Intelligence Agent",
    version="0.1.0",
)

app.include_router(countries.router)
app.include_router(health_scores.router)
app.include_router(alerts.router)
app.include_router(queries.router)
app.include_router(briefings.router)
app.include_router(comparisons.router)


@app.get("/")
async def root():
    return {
        "name": "SOVEREIGN",
        "description": "Global Financial Intelligence Agent",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# Mount static files for frontend (added later)
try:
    app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
except Exception:
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=settings.app_port,
        reload=settings.app_env == "development",
    )