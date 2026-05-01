from typing import Optional

WEIGHTS = {
    "gdp_growth": 0.08,
    "inflation_stability": 0.07,
    "debt_to_gdp": 0.08,
    "forex_reserves": 0.06,
    "trade_balance": 0.05,
    "currency_stability": 0.06,
    "stock_market": 0.05,
    "employment": 0.05,
    "interest_rate_env": 0.05,
    "money_supply_growth": 0.04,
    "banking_health": 0.05,
    "real_estate": 0.04,
    "credit_rating": 0.05,
    "foreign_investment": 0.04,
    "gov_budget": 0.04,
    "crypto_impact": 0.03,
    "economic_freedom": 0.03,
    "geopolitical_risk": 0.03,
}


def _score_inflation(inflation: Optional[float]) -> float:
    if inflation is None:
        return 50
    if 2 <= inflation <= 4:
        return 100
    if inflation < 0:
        return 40
    if inflation <= 2:
        return 80 + (inflation - 0) * 10
    if inflation <= 6:
        return 80 - (inflation - 4) * 20
    if inflation <= 15:
        return 40 - (inflation - 6) * 3
    return 10


def _score_debt(debt_to_gdp: Optional[float]) -> float:
    if debt_to_gdp is None:
        return 50
    if debt_to_gdp <= 30:
        return 100
    if debt_to_gdp <= 60:
        return 100 - (debt_to_gdp - 30) * 1.5
    if debt_to_gdp <= 100:
        return 55 - (debt_to_gdp - 60) * 0.8
    return 20


def _score_gdp_growth(growth: Optional[float]) -> float:
    if growth is None:
        return 50
    if growth >= 5:
        return 100
    if growth >= 2:
        return 60 + (growth - 2) * 13.3
    if growth >= 0:
        return 40 + growth * 10
    if growth >= -2:
        return 40 + growth * 10
    return 10


def _score_unemployment(rate: Optional[float]) -> float:
    if rate is None:
        return 50
    if rate <= 3:
        return 100
    if rate <= 6:
        return 100 - (rate - 3) * 13.3
    if rate <= 12:
        return 60 - (rate - 6) * 5
    return 20


def calculate(data: dict) -> dict:
    scores = {}
    scores["gdp_growth"] = _score_gdp_growth(data.get("gdp_growth"))
    scores["inflation_stability"] = _score_inflation(data.get("inflation"))
    scores["debt_to_gdp"] = _score_debt(data.get("gov_debt"))
    scores["forex_reserves"] = 60
    scores["trade_balance"] = 60 if data.get("trade_balance", 0) >= 0 else 40
    scores["currency_stability"] = 70
    scores["stock_market"] = 65
    scores["employment"] = _score_unemployment(data.get("unemployment"))
    scores["interest_rate_env"] = 65
    scores["money_supply_growth"] = 60
    scores["banking_health"] = 60
    scores["real_estate"] = 60
    scores["credit_rating"] = 75
    scores["foreign_investment"] = 60
    scores["gov_budget"] = 60 if data.get("gov_debt", 0) < 100 else 40
    scores["crypto_impact"] = 70
    scores["economic_freedom"] = 65
    scores["geopolitical_risk"] = 60

    overall = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS if k in scores)
    overall = round(min(100, max(0, overall)), 2)

    return {
        "overall_score": overall,
        "breakdown": scores,
        "trend": "stable",
    }
