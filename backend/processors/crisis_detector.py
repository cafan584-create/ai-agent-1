from typing import Optional

CRISIS_TYPES = [
    "currency_collapse",
    "debt_default",
    "hyperinflation",
    "bank_run",
    "recession",
    "trade_crisis",
]


def detect_currency_collapse(data: dict) -> dict | None:
    currency_change = data.get("currency_change_pct", 0)
    reserves = data.get("forex_reserves", 100)
    rates = data.get("interest_rate", 5)
    if currency_change < -10 and reserves < 50 and rates > 15:
        return {
            "type": "currency_collapse",
            "severity": "critical",
            "title": "Currency Collapse Warning",
            "description": f"Currency down {currency_change}% with low reserves and high rates",
            "confidence": 85.0,
        }
    return None


def detect_debt_default(data: dict) -> dict | None:
    debt = data.get("gov_debt", 0)
    reserves = data.get("forex_reserves", 100)
    if debt > 100 and reserves < 40:
        return {
            "type": "debt_default",
            "severity": "critical",
            "title": "Debt Default Risk",
            "description": f"Debt-to-GDP {debt}% with depleted reserves",
            "confidence": 80.0,
        }
    return None


def detect_hyperinflation(data: dict) -> dict | None:
    inflation = data.get("inflation", 0)
    money_supply_growth = data.get("money_supply_growth", 0)
    if inflation > 50 and money_supply_growth > 20:
        return {
            "type": "hyperinflation",
            "severity": "critical",
            "title": "Hyperinflation Alert",
            "description": f"Inflation {inflation}% with money supply growth {money_supply_growth}%",
            "confidence": 90.0,
        }
    return None


def detect_bank_run(data: dict) -> dict | None:
    banking_health = data.get("banking_health", 60)
    if banking_health < 30:
        return {
            "type": "bank_run",
            "severity": "high",
            "title": "Bank Run Risk",
            "description": f"Banking system health critically low at {banking_health}",
            "confidence": 70.0,
        }
    return None


def detect_recession(data: dict) -> dict | None:
    gdp_growth = data.get("gdp_growth", 0)
    if gdp_growth < -2:
        return {
            "type": "recession",
            "severity": "high",
            "title": "Recession Warning",
            "description": f"GDP growth negative at {gdp_growth}%",
            "confidence": 75.0,
        }
    return None


def detect_trade_crisis(data: dict) -> dict | None:
    trade_balance = data.get("trade_balance", 0)
    currency_change = data.get("currency_change_pct", 0)
    if trade_balance < -20 and currency_change < -5:
        return {
            "type": "trade_crisis",
            "severity": "high",
            "title": "Trade Crisis",
            "description": f"Trade deficit with currency depreciation",
            "confidence": 70.0,
        }
    return None


DETECTORS = {
    "currency_collapse": detect_currency_collapse,
    "debt_default": detect_debt_default,
    "hyperinflation": detect_hyperinflation,
    "bank_run": detect_bank_run,
    "recession": detect_recession,
    "trade_crisis": detect_trade_crisis,
}


def scan(country_code: str, data: dict) -> list:
    alerts = []
    for crisis_type, detector in DETECTORS.items():
        try:
            alert = detector(data)
            if alert:
                alert["country_code"] = country_code
                alerts.append(alert)
        except Exception:
            continue
    return alerts
