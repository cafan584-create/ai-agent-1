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


@router.get("/api/health-scores")
def get_health_scores(conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT hs.*, c.name, c.region
        FROM health_scores hs
        JOIN countries c ON c.code = hs.country_code
        WHERE hs.calculated_at = (
            SELECT MAX(calculated_at) FROM health_scores WHERE country_code = hs.country_code
        )
        ORDER BY hs.overall_score DESC
    """)
    return cur.fetchall()


@router.get("/api/health-scores/{code}")
def get_country_score(code: str, conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM health_scores WHERE country_code = %s ORDER BY calculated_at DESC LIMIT 30", (code,))
    return cur.fetchall()
