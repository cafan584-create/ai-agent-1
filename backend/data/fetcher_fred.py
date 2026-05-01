import httpx
from backend.utils.cache import get, set
from backend.config import get_settings

settings = get_settings()

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

SERIES = {
    "interest_rate": "FEDFUNDS",
    "unemployment_rate": "UNRATE",
    "money_supply_m1": "M1SL",
    "money_supply_m2": "M2SL",
    "inflation_cpi": "CPIAUCSL",
    "treasury_10y": "DGS10",
    "treasury_2y": "DGS2",
    "industrial_production": "INDPRO",
    "personal_income": "PCPI",
    "consumer_sentiment": "UMCSENT",
}


def _fetch_series(series_id: str, api_key: str) -> list:
    cache_key = f"fred_{series_id}"
    cached = get(cache_key, ttl=86400)
    if cached is not None:
        return cached

    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 12,
    }
    try:
        r = httpx.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        data = r.json().get("observations", [])
        set(cache_key, data)
        return data
    except Exception:
        return []


def fetch_all() -> dict:
    api_key = settings.fred_api_key
    if not api_key:
        return {}

    results = {}
    for name, series_id in SERIES.items():
        try:
            observations = _fetch_series(series_id, api_key)
            if observations:
                latest = next((o for o in observations if o.get("value") != "."), None)
                if latest:
                    results[name] = {
                        "value": float(latest["value"]),
                        "date": latest["date"],
                        "source": "fred",
                    }
        except Exception:
            continue
    return results
