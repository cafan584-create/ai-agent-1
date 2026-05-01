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


@router.get("/api/compare")
def compare_countries(countries: str = "", conn=Depends(get_db)):
    codes = [c.strip().upper() for c in countries.split(",") if c.strip()]
    if not codes:
        return {"error": "Provide country codes via ?countries=US,CN,IN"}

    cur = conn.cursor(cursor_factory=RealDictCursor)
    placeholders = ",".join(["%s"] * len(codes))
    cur.execute(f"""
        SELECT
            hs.*,
            c.name,
            c.region,
            (SELECT json_agg(row_to_json(ei)) FROM (
                SELECT * FROM economic_indicators WHERE country_code = hs.country_code ORDER BY year DESC LIMIT 5
            ) ei) as indicators
        FROM health_scores hs
        JOIN countries c ON c.code = hs.country_code
        WHERE hs.country_code IN ({placeholders})
        AND hs.calculated_at = (
            SELECT MAX(calculated_at) FROM health_scores WHERE country_code = hs.country_code
        )
    """, codes)
    return cur.fetchall()
