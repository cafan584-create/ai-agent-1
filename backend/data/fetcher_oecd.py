import httpx
from backend.utils.cache import get, set

BASE_URL = "https://data.oecd.org/api/jsonstat/1.0/en"

DATASETS = {
    "gdp_growth": "QNA",
    "unemployment": "LFS_UNECHR",
    "inflation": "PRICES_CPI",
    "house_price": "HOU_PRIC",
    "trade": "MEI_TRD",
}


def _fetch_jsonstat(dataset: str, params: dict) -> list:
    cache_key = f"oecd_{dataset}_{str(params)}"
    cached = get(cache_key, ttl=86400)
    if cached is not None:
        return cached

    url = f"{BASE_URL}/{dataset}"
    try:
        r = httpx.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        set(cache_key, data)
        return data
    except Exception:
        return []


def fetch_gdp_growth(country_code: str = "USA") -> dict:
    data = _fetch_jsonstat("QNA", {"filter": f"LOCATION:{country_code}"})
    if data and isinstance(data, list) and data:
        latest = data[-1]
        return {
            "value": latest.get("value", 0),
            "year": int(latest.get("year", 0)),
            "source": "oecd",
        }
    return {}


def fetch_unemployment(country_code: str = "USA") -> dict:
    data = _fetch_jsonstat("LFS_UNECHR", {"filter": f"LOCATION:{country_code}"})
    if data and isinstance(data, list) and data:
        latest = data[-1]
        return {
            "value": latest.get("value", 0),
            "year": int(latest.get("year", 0)),
            "source": "oecd",
        }
    return {}


def fetch_for_country(country_code: str) -> dict:
    results = {}
    try:
        u = fetch_unemployment(country_code)
        if u:
            results["unemployment_oecd"] = u
    except Exception:
        pass
    return results
