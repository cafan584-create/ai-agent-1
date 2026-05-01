import httpx
from xml.etree import ElementTree as ET
from datetime import datetime
from backend.utils.cache import get, set

RSS_FEEDS = {
    "Reuters": "https://feeds.reuters.com/reuters/businessNews",
    "Bloomberg": "https://www.bloomberg.com/feed/podcast/etf-iq.xml",
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "Financial Times": "https://www.ft.com/rss/world",
    "Yahoo Finance": "https://finance.yahoo.com/news/rssindex",
}


def _parse_date(date_str: str) -> str:
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S GMT", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.strptime(date_str.strip(), fmt).isoformat()
        except Exception:
            continue
    return date_str


def fetch_feed(source_name: str, url: str, limit: int = 10) -> list:
    cache_key = f"rss_{source_name}"
    cached = get(cache_key, ttl=3600)
    if cached is not None:
        return cached

    try:
        r = httpx.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        root = ET.fromstring(r.text)
        items = []
        for item in root.findall(".//item")[:limit]:
            title = item.findtext("title", "").strip()
            description = item.findtext("description", "").strip()[:500]
            link = item.findtext("link", "")
            pub_date = item.findtext("pubDate") or item.findtext("published", "")
            items.append({
                "title": title,
                "description": description,
                "url": link,
                "source": source_name,
                "published_at": _parse_date(pub_date) if pub_date else None,
            })
        set(cache_key, items)
        return items
    except Exception:
        return []


def fetch_all_news(limit_per_feed: int = 10) -> list:
    cache_key = "rss_all_news"
    cached = get(cache_key, ttl=1800)
    if cached is not None:
        return cached

    all_news = []
    for source, url in RSS_FEEDS.items():
        articles = fetch_feed(source, url, limit_per_feed)
        all_news.extend(articles)

    all_news.sort(key=lambda x: x.get("published_at") or "", reverse=True)
    set(cache_key, all_news)
    return all_news
