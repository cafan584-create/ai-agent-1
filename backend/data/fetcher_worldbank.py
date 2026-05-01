import httpx
from backend.utils.cache import get, set
from backend.config import get_settings

settings = get_settings()

BASE_URL = "https://api.worldbank.org/v2"
INDICATORS = {
    "gdp": "NY.GDP.MKTP.CD",
    "gdp_per_capita": "NY.GDP.PCAP.CD",
    "gdp_growth": "NY.GDP.MKTP.KD.ZG",
    "inflation": "FP.CPI.TOTL.ZG",
    "unemployment": "SL.UEM.TOTL.ZS",
    "gov_debt": "GC.DOD.TOTL.GD.ZS",
    "exports": "NE.EXP.GNFS.CD",
    "imports": "NE.IMP.GNFS.CD",
    "fdi_inflow": "BX.KLT.DINV.CD.WD",
    "trade_balance": "BN.GSR.GNFS.CD",
}

def _fetch(indicator_code: str, country_code: str = "all") -> list:
    cache_key = f"worldbank_{indicator_code}_{country_code}"
    cached = get(cache_key, ttl=86400)
    if cached is not None:
        return cached

    url = f"{BASE_URL}/country/{country_code}/indicator/{indicator_code}"
    params = {"format": "json", "per_page": 1000, "date": "2015:2030"}
    results = []
    page = 1
    while True:
        params["page"] = page
        r = httpx.get(url, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        if not data[1]:
            break
        results.extend(data[1])
        if len(data[1]) < 1000:
            break
        page += 1

    set(cache_key, results)
    return results


def fetch_for_country(country_code: str) -> dict:
    indicators = {}
    for name, code in INDICATORS.items():
        try:
            data = _fetch(code, country_code)
            if data:
                latest = next((d for d in data if d.get("value") is not None), None)
                if latest:
                    indicators[name] = {
                        "value": latest["value"],
                        "year": int(latest["date"]),
                        "source": "worldbank",
                    }
        except Exception:
            continue
    return indicators


def fetch_all_countries() -> list:
    cache_key = "worldbank_countries"
    cached = get(cache_key, ttl=86400)
    if cached is not None:
        return cached

    url = f"{BASE_URL}/country"
    params = {"format": "json", "per_page": 500}
    r = httpx.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()
    set(cache_key, data[1])
    return data[1]
