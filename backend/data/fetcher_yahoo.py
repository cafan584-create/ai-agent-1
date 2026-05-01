from backend.utils.cache import get, set

MAJOR_INDICES = {
    "US": "^GSPC",
    "US_TECH": "^IXIC",
    "UK": "^FTSE",
    "JP": "^N225",
    "CN": "000001.SS",
    "DE": "^GDAXI",
    "IN": "^BSESN",
    "BR": "^BVSP",
    "AU": "^AXJO",
    "KR": "^KS11",
}


def fetch_index(symbol: str) -> dict:
    cache_key = f"yahoo_{symbol}"
    cached = get(cache_key, ttl=900)
    if cached is not None:
        return cached

    try:
        import yfinance as yf
        ticker = yf.Ticker(symbol)
        info = ticker.info
        hist = ticker.history(period="2d")
        if hist.empty:
            return None
        current = float(hist["Close"].iloc[-1])
        prev = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else current
        change = current - prev
        change_pct = (change / prev * 100) if prev else 0
        volume = int(hist["Volume"].iloc[-1]) if "Volume" in hist.columns else 0

        result = {
            "symbol": symbol,
            "name": info.get("longName") or info.get("shortName", symbol),
            "value": current,
            "change": change,
            "change_percent": round(change_pct, 4),
            "volume": volume,
            "currency": info.get("currency", "USD"),
        }
        set(cache_key, result)
        return result
    except Exception:
        return None


def fetch_all_indices() -> dict:
    results = {}
    for country, symbol in MAJOR_INDICES.items():
        data = fetch_index(symbol)
        if data:
            results[country] = data
    return results
