"""
Initialize database connection and verify all tables exist.
Run: python scripts/init_db.py
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

TABLES = [
    "countries",
    "economic_indicators",
    "stock_indices",
    "crypto_data",
    "exchange_rates",
    "health_scores",
    "crisis_alerts",
    "anomalies",
    "news",
    "briefings",
    "correlations",
    "predictions",
    "fetch_logs",
    "user_alerts",
]


def check_tables(db_url: str):
    """Connect to database and check all required tables exist."""
    import psycopg2

    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

        cur.execute(
            """
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name
            """
        )
        existing = {row[0] for row in cur.fetchall()}

        print("\n=== DATABASE CONNECTION: OK ===\n")
        print(f"Existing tables: {len(existing)}")

        missing = []
        for table in TABLES:
            if table in existing:
                print(f"  [OK]   {table}")
            else:
                print(f"  [MISSING] {table}")
                missing.append(table)

        if missing:
            print(f"\nWARNING: {len(missing)} tables missing!")
            print("Run database/schema.sql in Supabase SQL Editor first.")
            return False
        else:
            print(f"\nAll {len(TABLES)} tables verified OK.")
            return True

    except Exception as e:
        print(f"\nDATABASE CONNECTION FAILED: {e}")
        print("Check your SUPABASE_DB_URL in .env file.")
        return False


if __name__ == "__main__":
    db_url = os.getenv("SUPABASE_DB_URL")
    if not db_url:
        print("ERROR: SUPABASE_DB_URL not set in .env file")
        sys.exit(1)

    success = check_tables(db_url)
    sys.exit(0 if success else 1)
