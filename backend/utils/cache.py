import json
import os
import time
from pathlib import Path
from typing import Any, Optional

CACHE_DIR = Path(__file__).parent.parent / "cache"
CACHE_TTL_DEFAULT = 3600


def _ensure_cache_dir():
    CACHE_DIR.mkdir(exist_ok=True)


def _cache_path(key: str) -> Path:
    safe_key = key.replace("/", "_").replace("\\", "_")
    return CACHE_DIR / f"{safe_key}.json"


def get(key: str, ttl: int = CACHE_TTL_DEFAULT) -> Optional[Any]:
    _ensure_cache_dir()
    path = _cache_path(key)
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if time.time() - data.get("timestamp", 0) > ttl:
            return None
        return data.get("value")
    except Exception:
        return None


def set(key: str, value: Any):
    _ensure_cache_dir()
    path = _cache_path(key)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"timestamp": time.time(), "value": value}, f, ensure_ascii=False, default=str)


def delete(key: str):
    path = _cache_path(key)
    if path.exists():
        path.unlink()


def clear():
    _ensure_cache_dir()
    for f in CACHE_DIR.iterdir():
        if f.suffix == ".json":
            f.unlink()
