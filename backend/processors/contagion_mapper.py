from typing import Optional

TRADE_WEIGHT = 0.4
FINANCIAL_WEIGHT = 0.3
GEOGRAPHIC_WEIGHT = 0.2
SUPPLY_CHAIN_WEIGHT = 0.1

CRISIS_IMPACTS = {
    "currency_collapse": {"trade": 0.6, "financial": 0.8, "geographic": 0.4, "supply": 0.3},
    "debt_default": {"trade": 0.7, "financial": 0.9, "geographic": 0.3, "supply": 0.2},
    "hyperinflation": {"trade": 0.5, "financial": 0.6, "geographic": 0.3, "supply": 0.4},
    "bank_run": {"trade": 0.4, "financial": 0.9, "geographic": 0.3, "supply": 0.2},
    "recession": {"trade": 0.6, "financial": 0.5, "geographic": 0.3, "supply": 0.5},
    "trade_crisis": {"trade": 0.9, "financial": 0.4, "geographic": 0.3, "supply": 0.6},
}


def get_country_exposure(country_code: str) -> dict:
    exposure = {
        "USA": {"trade": 0.6, "financial": 0.8, "geographic": 0.3, "supply": 0.5},
        "CHN": {"trade": 0.9, "financial": 0.5, "geographic": 0.4, "supply": 0.8},
        "DEU": {"trade": 0.8, "financial": 0.6, "geographic": 0.7, "supply": 0.5},
        "JPN": {"trade": 0.7, "financial": 0.6, "geographic": 0.5, "supply": 0.6},
        "GBR": {"trade": 0.6, "financial": 0.7, "geographic": 0.4, "supply": 0.4},
    }
    return exposure.get(country_code, {"trade": 0.3, "financial": 0.3, "geographic": 0.2, "supply": 0.2})


def calculate_impact(source_country: str, crisis_type: str, target_country: str) -> float:
    impacts = CRISIS_IMPACTS.get(crisis_type, {})
    source_exposure = get_country_exposure(source_country)
    target_exposure = get_country_exposure(target_country)

    score = 0.0
    score += impacts.get("trade", 0) * source_exposure["trade"] * TRADE_WEIGHT
    score += impacts.get("financial", 0) * source_exposure["financial"] * FINANCIAL_WEIGHT
    score += impacts.get("geographic", 0) * source_exposure["geographic"] * GEOGRAPHIC_WEIGHT
    score += impacts.get("supply", 0) * source_exposure["supply"] * SUPPLY_CHAIN_WEIGHT

    return round(min(1.0, score), 3)


def predict_spread(source_country: str, crisis_type: str, all_countries: list, threshold: float = 0.3) -> list:
    results = []
    for country in all_countries:
        if country == source_country:
            continue
        impact = calculate_impact(source_country, crisis_type, country)
        if impact >= threshold:
            results.append({
                "source": source_country,
                "target": country,
                "crisis_type": crisis_type,
                "impact_score": impact,
                "risk_level": "high" if impact > 0.6 else "medium" if impact > 0.4 else "low",
            })
    return sorted(results, key=lambda x: x["impact_score"], reverse=True)
