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


@router.get("/api/briefings/latest")
def get_latest_briefing(conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM briefings ORDER BY generated_at DESC LIMIT 1")
    return cur.fetchone()


@router.get("/api/briefings/{briefing_id}")
def get_briefing(briefing_id: int, conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM briefings WHERE id = %s", (briefing_id,))
    return cur.fetchone()
