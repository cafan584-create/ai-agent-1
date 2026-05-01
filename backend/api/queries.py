from fastapi import APIRouter, Depends
from backend.ai.query_handler import answer_question
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


@router.post("/api/query")
def query_ai(body: dict, conn=Depends(get_db)):
    question = body.get("question", "")
    context = body.get("context", {})
    if not context:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM health_scores ORDER BY calculated_at DESC LIMIT 10")
        context["recent_scores"] = cur.fetchall()
        cur.execute("SELECT * FROM crisis_alerts WHERE is_active = TRUE LIMIT 10")
        context["active_alerts"] = cur.fetchall()
    answer = answer_question(question, context)
    return {"question": question, "answer": answer}
