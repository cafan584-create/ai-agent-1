from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import logging

logger = logging.getLogger(__name__)


def fetch_crypto():
    try:
        from backend.data.fetcher_coingecko import fetch_crypto_prices, normalize_for_db
        from backend.config import get_settings
        import psycopg2

        prices = fetch_crypto_prices()
        rows = normalize_for_db(prices)
        settings = get_settings()
        conn = psycopg2.connect(settings.supabase_db_url)
        cur = conn.cursor()
        for r in rows:
            cur.execute(
                "INSERT INTO crypto_data (symbol, name, price_usd, market_cap, volume_24h, change_24h, change_7d) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (r["symbol"], r["name"], r["price_usd"], r["market_cap"], r["volume_24h"], r["change_24h"], r["change_7d"])
            )
        conn.commit()
        conn.close()
        logger.info(f"Crypto: updated {len(rows)} coins")
    except Exception as e:
        logger.error(f"Crypto fetch error: {e}")


def fetch_stocks():
    try:
        from backend.data.fetcher_yahoo import fetch_all_indices
        from backend.config import get_settings
        import psycopg2

        indices = fetch_all_indices()
        settings = get_settings()
        conn = psycopg2.connect(settings.supabase_db_url)
        cur = conn.cursor()
        for country, data in indices.items():
            cur.execute(
                "INSERT INTO stock_indices (country_code, index_name, value, change_percent, volume, timestamp) VALUES (%s,%s,%s,%s,%s,NOW())",
                (country, data["name"], data["value"], data["change_percent"], data["volume"])
            )
        conn.commit()
        conn.close()
        logger.info(f"Stocks: updated {len(indices)} indices")
    except Exception as e:
        logger.error(f"Stock fetch error: {e}")


def fetch_exchange_rates():
    try:
        from backend.data.fetcher_exchange import fetch_rates, normalize_for_db
        from backend.config import get_settings
        import psycopg2

        rates = fetch_rates("USD")
        rows = normalize_for_db(rates)
        settings = get_settings()
        conn = psycopg2.connect(settings.supabase_db_url)
        cur = conn.cursor()
        for r in rows:
            cur.execute(
                "INSERT INTO exchange_rates (base_currency, target_currency, rate, source, timestamp) VALUES (%s,%s,%s,%s,NOW())",
                (r["base_currency"], r["target_currency"], r["rate"], r["source"])
            )
        conn.commit()
        conn.close()
        logger.info(f"Exchange: updated {len(rows)} rates")
    except Exception as e:
        logger.error(f"Exchange fetch error: {e}")


def fetch_news():
    try:
        from backend.data.fetcher_rss import fetch_all_news
        from backend.config import get_settings
        import psycopg2

        articles = fetch_all_news()
        settings = get_settings()
        conn = psycopg2.connect(settings.supabase_db_url)
        cur = conn.cursor()
        for a in articles[:50]:
            cur.execute(
                "INSERT INTO news (title, description, url, source, category, published_at, fetched_at) VALUES (%s,%s,%s,%s,%s,%s,NOW()) ON CONFLICT DO NOTHING",
                (a["title"][:500], a["description"][:500], a["url"], a["source"], "general", a.get("published_at"))
            )
        conn.commit()
        conn.close()
        logger.info(f"News: updated {len(articles)} articles")
    except Exception as e:
        logger.error(f"News fetch error: {e}")


def calculate_health_scores():
    try:
        from backend.processors.health_scorer import calculate
        from backend.config import get_settings
        import psycopg2
        from psycopg2.extras import RealDictCursor

        settings = get_settings()
        conn = psycopg2.connect(settings.supabase_db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT code FROM countries")
        countries = cur.fetchall()

        for c in countries:
            code = c["code"]
            cur.execute("SELECT indicator_type, value FROM economic_indicators WHERE country_code = %s ORDER BY year DESC LIMIT 20", (code,))
            indicators = {r["indicator_type"]: r["value"] for r in cur.fetchall()}
            result = calculate(indicators)
            cur.execute(
                "INSERT INTO health_scores (country_code, overall_score, trend, previous_score, score_change, calculated_at) VALUES (%s,%s,%s,0,0,NOW())",
                (code, result["overall_score"], result["trend"])
            )
        conn.commit()
        conn.close()
        logger.info(f"Health scores: recalculated for {len(countries)} countries")
    except Exception as e:
        logger.error(f"Health score error: {e}")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_crypto, IntervalTrigger(minutes=5), id='crypto')
    scheduler.add_job(fetch_stocks, IntervalTrigger(minutes=15), id='stocks')
    scheduler.add_job(fetch_exchange_rates, IntervalTrigger(hours=1), id='exchange')
    scheduler.add_job(fetch_news, IntervalTrigger(hours=1), id='news')
    scheduler.add_job(calculate_health_scores, IntervalTrigger(hours=24), id='health_scores')
    scheduler.start()
    logger.info("Scheduler started - crypto:5min, stocks:15min, exchange:1h, news:1h, health:24h")
