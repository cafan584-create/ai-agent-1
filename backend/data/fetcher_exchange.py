import httpx
from backend.utils.cache import get, set

FRANKFURTER_URL = "https://api.frankfurter.app"
EXCHANGERATE_URL = "https://v6.exchangerate-api.com/v6"


def fetch_frankfurter(base: str = "USD", symbols: list = None) -> dict:
    cache_key = f"frankfurter_{base}_{','.join(symbols or [])}"
    cached = get(cache_key, ttl=3600)
    if cached is not None:
        return cached

    params = {"from": base}
    if symbols:
        params["to"] = ",".join(symbols)

    try:
        r = httpx.get(f"{FRANKFURTER_URL}/latest", params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        set(cache_key, data)
        return data.get("rates", {})
    except Exception:
        return {}


def fetch_exchangerate_api(base: str = "USD") -> dict:
    from backend.config import get_settings
    settings = get_settings()

    if not settings.exchangerate_api_key:
        return {}

    cache_key = f"exchangerate_{base}"
    cached = get(cache_key, ttl=3600)
    if cached is not None:
        return cached

    url = f"{EXCHANGERATE_URL}/{settings.exchangerate_api_key}/latest/{base}"
    try:
        r = httpx.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        result = data.get("conversion_rates", {})
        set(cache_key, result)
        return result
    except Exception:
        return {}


def fetch_rates(base: str = "USD", symbols: list = None) -> dict:
    rates = fetch_frankfurter(base, symbols)
    if not rates:
        rates = fetch_exchangerate_api(base)
    return rates


def normalize_for_db(rates: dict, base: str = "USD") -> list:
    return [
        {
            "base_currency": base,
            "target_currency": currency,
            "rate": rate,
            "source": "frankfurter" if rates else "exchangerate-api",
        }
        for currency, rate in rates.items()
    ]
