from typing import Optional

THRESHOLDS = {
    "gdp_growth_min": -15,
    "gdp_growth_max": 25,
    "inflation_min": -5,
    "inflation_max": 100,
    "unemployment_min": 0,
    "unemployment_max": 50,
    "debt_to_gdp_max": 300,
    "currency_change_max": 30,
}


def check_outlier(value: Optional[float], min_val: float, max_val: float, label: str, country_code: str) -> dict | None:
    if value is None:
        return None
    if value < min_val or value > max_val:
        return {
            "country_code": country_code,
            "anomaly_type": "outlier",
            "description": f"{label} value {value} outside expected range [{min_val}, {max_val}]",
            "data_source": "internal_check",
            "severity": "high" if abs(value) > max_val * 1.5 else "medium",
        }
    return None


def detect(data: dict, country_code: str) -> list:
    anomalies = []

    anomalies.append(check_outlier(
        data.get("gdp_growth"), THRESHOLDS["gdp_growth_min"], THRESHOLDS["gdp_growth_max"],
        "GDP growth", country_code
    ))

    anomalies.append(check_outlier(
        data.get("inflation"), THRESHOLDS["inflation_min"], THRESHOLDS["inflation_max"],
        "Inflation", country_code
    ))

    anomalies.append(check_outlier(
        data.get("unemployment"), THRESHOLDS["unemployment_min"], THRESHOLDS["unemployment_max"],
        "Unemployment", country_code
    ))

    anomalies.append(check_outlier(
        data.get("gov_debt"), 0, THRESHOLDS["debt_to_gdp_max"],
        "Debt-to-GDP", country_code
    ))

    currency_change = data.get("currency_change_pct")
    if currency_change and abs(currency_change) > THRESHOLDS["currency_change_max"]:
        anomalies.append({
            "country_code": country_code,
            "anomaly_type": "currency_shock",
            "description": f"Currency change {currency_change}% exceeds normal range",
            "data_source": "exchange_rate",
            "severity": "high",
        })

    if data.get("gdp_growth", 0) > 10 and data.get("unemployment", 0) > 15:
        anomalies.append({
            "country_code": country_code,
            "anomaly_type": "contradiction",
            "description": "High GDP growth with very high unemployment is contradictory",
            "data_source": "cross_check",
            "severity": "medium",
        })

    return [a for a in anomalies if a is not None]
