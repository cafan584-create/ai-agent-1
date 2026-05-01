import httpx
from backend.utils.cache import get, set

BASE_URL = "https://api.coingecko.com/api/v3"

TOP_COINS = [
    "bitcoin", "ethereum", "tether", "binancecoin", "solana",
    "ripple", "usd-coin", "cardano", "dogecoin", "avalanche",
    "polkadot", "tron", "chainlink", "polygon", "shiba-inu",
]


def fetch_crypto_prices(coin_ids: list = None) -> list:
    ids = coin_ids or TOP_COINS
    cache_key = f"coingecko_prices_{','.join(sorted(ids))}"
    cached = get(cache_key, ttl=300)
    if cached is not None:
        return cached

    ids_str = ",".join(ids)
    url = f"{BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ids_str,
        "order": "market_cap_desc",
        "per_page": len(ids),
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h,7d",
    }
    r = httpx.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()
    set(cache_key, data)
    return data


def fetch_global_data() -> dict:
    cache_key = "coingecko_global"
    cached = get(cache_key, ttl=300)
    if cached is not None:
        return cached

    url = f"{BASE_URL}/global"
    r = httpx.get(url, timeout=30)
    r.raise_for_status()
    data = r.json().get("data", {})
    set(cache_key, data)
    return data


def normalize_for_db(prices: list) -> list:
    result = []
    for c in prices:
        result.append({
            "symbol": c.get("symbol", "").upper(),
            "name": c.get("name", ""),
            "price_usd": c.get("current_price", 0),
            "market_cap": c.get("market_cap", 0),
            "volume_24h": c.get("total_volume", 0),
            "change_24h": c.get("price_change_percentage_24h", 0),
            "change_7d": c.get("price_change_percentage_7d_in_currency", 0) if c.get("price_change_percentage_7d_in_currency") else 0,
        })
    return result
