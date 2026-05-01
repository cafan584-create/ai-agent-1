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


@router.get("/api/alerts")
def get_alerts(conn=Depends(get_db)):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT ca.*, c.name FROM crisis_alerts ca
        JOIN countries c ON c.code = ca.country_code
        WHERE ca.is_active = TRUE
        ORDER BY
            CASE severity WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END,
            created_at DESC
    """)
    return cur.fetchall()


@router.post("/api/alerts")
def create_alert(body: dict, conn=Depends(get_db)):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO user_alerts (telegram_chat_id, country_code, indicator_type, condition, threshold_value)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (
        body.get("telegram_chat_id"),
        body.get("country_code"),
        body.get("indicator_type"),
        body.get("condition"),
        body.get("threshold_value"),
    ))
    conn.commit()
    return {"id": cur.fetchone()[0], "status": "created"}
