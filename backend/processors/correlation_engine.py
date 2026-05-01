from typing import Optional
from datetime import datetime


def calculate_correlation(values_a: list, values_b: list) -> Optional[float]:
    if not values_a or not values_b or len(values_a) != len(values_b):
        return None
    n = len(values_a)
    if n < 2:
        return None

    mean_a = sum(values_a) / n
    mean_b = sum(values_b) / n

    cov = sum((a - mean_a) * (b - mean_b) for a, b in zip(values_a, values_b))
    var_a = sum((a - mean_a) ** 2 for a in values_a)
    var_b = sum((b - mean_b) ** 2 for b in values_b)

    if var_a == 0 or var_b == 0:
        return None

    return round(cov / (var_a ** 0.5 * var_b ** 0.5), 4)


def discover_pairs(indicators: dict) -> list:
    keys = [k for k in indicators if isinstance(indicators[k], (int, float))]
    correlations = []
    for i, key_a in enumerate(keys):
        for key_b in keys[i + 1:]:
            corr = calculate_correlation(
                [indicators[key_a]] if isinstance(indicators[key_a], (int, float)) else [],
                [indicators[key_b]] if isinstance(indicators[key_b], (int, float)) else [],
            )
            if corr is not None and abs(corr) > 0.5:
                correlations.append({
                    "indicator_a": key_a,
                    "indicator_b": key_b,
                    "correlation_coeff": corr,
                    "country_code": None,
                    "discovered_at": datetime.utcnow().isoformat(),
                })
    return correlations


def analyze_trend(values: list) -> str:
    if not values or len(values) < 2:
        return "stable"
    recent = values[-3:]
    if all(recent[i] < recent[i + 1] for i in range(len(recent) - 1)):
        return "rising"
    if all(recent[i] > recent[i + 1] for i in range(len(recent) - 1)):
        return "falling"
    return "volatile"
