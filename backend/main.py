from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.config import get_settings
from backend.api import countries, health_scores, alerts, queries, briefings, comparisons

settings = get_settings()
templates = Jinja2Templates(directory="frontend/templates")

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


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/alerts")
async def alerts_page(request: Request):
    return templates.TemplateResponse("alerts.html", {"request": request})


@app.get("/compare")
async def compare_page(request: Request):
    return templates.TemplateResponse("compare.html", {"request": request})


@app.get("/briefing")
async def briefing_page(request: Request):
    return templates.TemplateResponse("briefing.html", {"request": request})


@app.get("/country")
async def country_page(request: Request, code: str = "USA"):
    return templates.TemplateResponse("country.html", {"request": request, "code": code})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=settings.app_port,
        reload=settings.app_env == "development",
    )