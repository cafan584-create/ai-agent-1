from telegram import Update
from telegram.ext import ContextTypes
import httpx
from backend.config import get_settings

API_BASE = "http://localhost:8000/api"

settings = get_settings()


async def health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = context.args[0].upper() if context.args else "USA"
    try:
        r = await httpx.AsyncClient().get(f"{API_BASE}/countries/{code}")
        data = r.json()
        score = data.get("health_score", {}).get("overall_score", "N/A")
        await update.message.reply_text(f"{data.get('name', code)} Health Score: {score}/100")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def crisis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = await httpx.AsyncClient().get(f"{API_BASE}/alerts")
        alerts = r.json()[:5]
        if not alerts:
            await update.message.reply_text("No active crisis alerts.")
            return
        msg = "🚨 Active Crisis Alerts:\n\n" + "\n".join(
            f"• {a['title']} ({a['country_code']}) - {a['severity']}" for a in alerts
        )
        await update.message.reply_text(msg)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def compare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /compare US CN IN")
        return
    codes = ",".join(context.args).upper()
    try:
        r = await httpx.AsyncClient().get(f"{API_BASE}/compare?countries={codes}")
        data = r.json()
        msg = "📊 Comparison:\n\n" + "\n".join(
            f"• {c['name']}: {c.get('overall_score', 'N/A')}/100" for c in data
        )
        await update.message.reply_text(msg)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def top5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = await httpx.AsyncClient().get(f"{API_BASE}/health-scores")
        data = r.json()[:5]
        msg = "🏆 Top 5 Healthiest:\n\n" + "\n".join(
            f"{i+1}. {c['name']}: {c['overall_score']}/100" for i, c in enumerate(data)
        )
        await update.message.reply_text(msg)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def bottom5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = await httpx.AsyncClient().get(f"{API_BASE}/health-scores")
        data = r.json()[-5:][::-1]
        msg = "⚠️ Top 5 At-Risk:\n\n" + "\n".join(
            f"{i+1}. {c['name']}: {c['overall_score']}/100" for i, c in enumerate(data)
        )
        await update.message.reply_text(msg)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def briefing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = await httpx.AsyncClient().get(f"{API_BASE}/briefings/latest")
        data = r.json()
        if not data or not data.get("content"):
            await update.message.reply_text("No briefing available yet.")
            return
        await update.message.reply_text(f"📄 Latest Briefing:\n\n{data['content'][:400]}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = " ".join(context.args)
    if not q:
        await update.message.reply_text("Usage: /query <your question>")
        return
    try:
        r = await httpx.AsyncClient().post(
            f"{API_BASE}/query",
            json={"question": q}
        )
        data = r.json()
        await update.message.reply_text(data.get("answer", "No answer."))
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "SOVEREIGN Bot\n\n"
        "Commands:\n"
        "/health <CODE> - Country health score\n"
        "/crisis - Active alerts\n"
        "/compare US CN IN - Compare countries\n"
        "/top5 - Top 5 healthiest\n"
        "/bottom5 - Top 5 at-risk\n"
        "/briefing - Latest AI report\n"
        "/query <question> - Ask AI"
    )
