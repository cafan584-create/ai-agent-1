from fastapi import APIRouter, Depends
from psycopg2.extras import RealDictCursor
from backend.config import get_settings
import psycopg2

router = APIRouter()

def get_db():
    settings = get_settings()
    conn = psycopg2.connect(settings.supabase_db_url)
    try:
        yield conn
    finally:
        conn.close()


@router.get("/api/countries")
def list_countries(conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM countries ORDER BY name")
    return cur.fetchall()


@router.get("/api/countries/{code}")
def get_country(code: str, conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM countries WHERE code = %s", (code,))
    country = cur.fetchone()
    if country:
        cur.execute("SELECT * FROM economic_indicators WHERE country_code = %s ORDER BY year DESC LIMIT 20", (code,))
        country["indicators"] = cur.fetchall()
        cur.execute("SELECT * FROM health_scores WHERE country_code = %s ORDER BY calculated_at DESC LIMIT 1", (code,))
        country["health_score"] = cur.fetchone()
    return country
