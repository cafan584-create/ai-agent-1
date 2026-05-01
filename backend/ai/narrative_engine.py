import os
from backend.ai.prompt_templates import COUNTRY_BRIEFING, COMPARE_COUNTRIES, CRISIS_ANALYSIS
from backend.config import get_settings

settings = get_settings()


def call_groq(prompt: str) -> str:
    api_key = settings.groq_api_key
    if not api_key:
        return "[AI disabled: set GROQ_API_KEY in .env]"

    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "system", "content": prompt}],
            max_tokens=200,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[AI error: {str(e)}]"


def generate_country_briefing(country_code: str, country_name: str, health_score: float, trend: str, indicators: dict, alerts: list) -> str:
    prompt = COUNTRY_BRIEFING.format(
        country_name=country_name,
        country_code=country_code,
        health_score=health_score,
        trend=trend,
        gdp_growth=indicators.get("gdp_growth", "N/A"),
        inflation=indicators.get("inflation", "N/A"),
        unemployment=indicators.get("unemployment", "N/A"),
        debt_to_gdp=indicators.get("gov_debt", "N/A"),
        trade_balance=indicators.get("trade_balance", "N/A"),
        alerts=", ".join(a.get("title", "") for a in alerts) if alerts else "None",
    )
    return call_groq(prompt)


def generate_comparison(comparison_data: list) -> str:
    data_str = "\n".join(
        f"{c['code']}: Score={c.get('score', 'N/A')}, GDP Growth={c.get('gdp_growth', 'N/A')}%, Inflation={c.get('inflation', 'N/A')}%"
        for c in comparison_data
    )
    prompt = COMPARE_COUNTRIES.format(comparison_data=data_str)
    return call_groq(prompt)


def analyze_crisis(country_name: str, alert: dict) -> str:
    prompt = CRISIS_ANALYSIS.format(
        country_name=country_name,
        alert_type=alert.get("alert_type", ""),
        severity=alert.get("severity", ""),
        description=alert.get("description", ""),
        confidence=alert.get("confidence", 0),
    )
    return call_groq(prompt)
