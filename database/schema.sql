-- ============================================================
-- SOVEREIGN — Global Financial Intelligence Agent
-- Database Schema (PostgreSQL / Supabase)
-- ============================================================
-- Run this entire file in Supabase SQL Editor
-- Project -> SQL Editor -> New Query -> Paste -> Run
-- ============================================================

-- 1. COUNTRY MASTER TABLE
CREATE TABLE IF NOT EXISTS countries (
    id              SERIAL PRIMARY KEY,
    code            VARCHAR(3)  NOT NULL UNIQUE,
    name            VARCHAR(100) NOT NULL,
    full_name       VARCHAR(200),
    region          VARCHAR(50),
    sub_region      VARCHAR(50),
    iso_numeric     VARCHAR(3),
    capital         VARCHAR(100),
    currency_code   VARCHAR(3),
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    updated_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_countries_code ON countries(code);
CREATE INDEX idx_countries_region ON countries(region);


-- 2. ECONOMIC INDICATORS
CREATE TABLE IF NOT EXISTS economic_indicators (
    id              SERIAL PRIMARY KEY,
    country_code    VARCHAR(3)    NOT NULL REFERENCES countries(code),
    indicator_type  VARCHAR(50)   NOT NULL,
    value           NUMERIC(20,4),
    unit            VARCHAR(20)   DEFAULT 'usd',
    frequency       VARCHAR(20)   DEFAULT 'annual',
    year            INT,
    quarter         VARCHAR(2),
    month           INT,
    source          VARCHAR(50),
    fetched_at      TIMESTAMPTZ   DEFAULT NOW(),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_indicators_country ON economic_indicators(country_code);
CREATE INDEX idx_indicators_type ON economic_indicators(indicator_type);
CREATE INDEX idx_indicators_year ON economic_indicators(year);
CREATE INDEX idx_indicators_fetched ON economic_indicators(fetched_at);


-- 3. STOCK MARKET INDICES
CREATE TABLE IF NOT EXISTS stock_indices (
    id              SERIAL PRIMARY KEY,
    country_code    VARCHAR(3)    NOT NULL REFERENCES countries(code),
    index_name      VARCHAR(100)  NOT NULL,
    value           NUMERIC(20,4) NOT NULL,
    open_price      NUMERIC(20,4),
    high_price      NUMERIC(20,4),
    low_price       NUMERIC(20,4),
    close_price     NUMERIC(20,4),
    change_percent  NUMERIC(10,4),
    volume          BIGINT,
    timestamp       TIMESTAMPTZ   NOT NULL,
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_stocks_country ON stock_indices(country_code);
CREATE INDEX idx_stocks_timestamp ON stock_indices(timestamp);
CREATE INDEX idx_stocks_name ON stock_indices(index_name);


-- 4. CRYPTOCURRENCY DATA
CREATE TABLE IF NOT EXISTS crypto_data (
    id              SERIAL PRIMARY KEY,
    symbol          VARCHAR(20)   NOT NULL,
    name            VARCHAR(100),
    price_usd       NUMERIC(20,4) NOT NULL,
    market_cap      NUMERIC(20,2),
    volume_24h      NUMERIC(20,2),
    change_1h       NUMERIC(10,4),
    change_24h      NUMERIC(10,4),
    change_7d       NUMERIC(10,4),
    circulating_supply NUMERIC(20,4),
    total_supply    NUMERIC(20,4),
    timestamp       TIMESTAMPTZ   DEFAULT NOW(),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_crypto_symbol ON crypto_data(symbol);
CREATE INDEX idx_crypto_timestamp ON crypto_data(timestamp);


-- 5. EXCHANGE RATES
CREATE TABLE IF NOT EXISTS exchange_rates (
    id              SERIAL PRIMARY KEY,
    base_currency   VARCHAR(3)    NOT NULL DEFAULT 'USD',
    target_currency VARCHAR(3)    NOT NULL,
    rate            NUMERIC(20,8) NOT NULL,
    source          VARCHAR(50)   DEFAULT 'frankfurter',
    timestamp       TIMESTAMPTZ   DEFAULT NOW(),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_exchange_target ON exchange_rates(target_currency);
CREATE INDEX idx_exchange_timestamp ON exchange_rates(timestamp);


-- 6. COUNTRY HEALTH SCORES
CREATE TABLE IF NOT EXISTS health_scores (
    id              SERIAL PRIMARY KEY,
    country_code    VARCHAR(3)    NOT NULL REFERENCES countries(code),
    overall_score   NUMERIC(5,2)  NOT NULL CHECK (overall_score >= 0 AND overall_score <= 100),
    gdp_growth      NUMERIC(5,2),
    inflation       NUMERIC(5,2),
    debt_to_gdp     NUMERIC(5,2),
    forex_reserves  NUMERIC(5,2),
    trade_balance   NUMERIC(5,2),
    currency_stability NUMERIC(5,2),
    stock_market    NUMERIC(5,2),
    employment      NUMERIC(5,2),
    interest_rates  NUMERIC(5,2),
    money_supply    NUMERIC(5,2),
    banking_health  NUMERIC(5,2),
    real_estate     NUMERIC(5,2),
    credit_rating   NUMERIC(5,2),
    foreign_investment NUMERIC(5,2),
    government_budget NUMERIC(5,2),
    crypto_impact   NUMERIC(5,2),
    economic_freedom NUMERIC(5,2),
    geopolitical_risk NUMERIC(5,2),
    trend           VARCHAR(10)   DEFAULT 'stable' CHECK (trend IN ('up', 'down', 'stable')),
    previous_score  NUMERIC(5,2),
    score_change    NUMERIC(5,2),
    calculated_at   TIMESTAMPTZ   DEFAULT NOW(),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_health_country ON health_scores(country_code);
CREATE INDEX idx_health_calculated ON health_scores(calculated_at);
CREATE INDEX idx_health_overall ON health_scores(overall_score DESC);


-- 7. CRISIS ALERTS
CREATE TABLE IF NOT EXISTS crisis_alerts (
    id              SERIAL PRIMARY KEY,
    country_code    VARCHAR(3)    NOT NULL REFERENCES countries(code),
    alert_type      VARCHAR(50)   NOT NULL,
    severity        VARCHAR(10)   NOT NULL CHECK (severity IN ('low', 'medium', 'high', 'critical')),
    title           VARCHAR(200),
    description     TEXT,
    confidence      NUMERIC(5,2)  CHECK (confidence >= 0 AND confidence <= 100),
    historical_match VARCHAR(100),
    indicators      JSONB,
    is_active       BOOLEAN       DEFAULT TRUE,
    resolved_at     TIMESTAMPTZ,
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_alerts_country ON crisis_alerts(country_code);
CREATE INDEX idx_alerts_active ON crisis_alerts(is_active);
CREATE INDEX idx_alerts_severity ON crisis_alerts(severity);
CREATE INDEX idx_alerts_created ON crisis_alerts(created_at);


-- 8. ANOMALIES
CREATE TABLE IF NOT EXISTS anomalies (
    id              SERIAL PRIMARY KEY,
    country_code    VARCHAR(3)    NOT NULL REFERENCES countries(code),
    anomaly_type    VARCHAR(50)   NOT NULL,
    description     TEXT,
    data_source     VARCHAR(50),
    severity        VARCHAR(10)   CHECK (severity IN ('low', 'medium', 'high')),
    expected_value  NUMERIC(20,4),
    actual_value    NUMERIC(20,4),
    deviation_pct   NUMERIC(10,2),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_anomalies_country ON anomalies(country_code);
CREATE INDEX idx_anomalies_created ON anomalies(created_at);


-- 9. NEWS
CREATE TABLE IF NOT EXISTS news (
    id              SERIAL PRIMARY KEY,
    title           VARCHAR(500)  NOT NULL,
    description     TEXT,
    url             TEXT,
    source          VARCHAR(100),
    country_codes   TEXT,
    category        VARCHAR(50),
    sentiment       VARCHAR(20),
    published_at    TIMESTAMPTZ,
    fetched_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_news_source ON news(source);
CREATE INDEX idx_news_fetched ON news(fetched_at);
CREATE INDEX idx_news_category ON news(category);


-- 10. AI BRIEFINGS
CREATE TABLE IF NOT EXISTS briefings (
    id              SERIAL PRIMARY KEY,
    briefing_type   VARCHAR(20)   NOT NULL CHECK (briefing_type IN ('hourly', 'daily', 'event')),
    title           VARCHAR(200),
    content         TEXT          NOT NULL,
    countries_covered TEXT,
    generated_at    TIMESTAMPTZ   DEFAULT NOW(),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_briefings_type ON briefings(briefing_type);
CREATE INDEX idx_briefings_generated ON briefings(generated_at);


-- 11. CORRELATIONS
CREATE TABLE IF NOT EXISTS correlations (
    id              SERIAL PRIMARY KEY,
    indicator_a     VARCHAR(100)  NOT NULL,
    indicator_b     VARCHAR(100)  NOT NULL,
    country_code    VARCHAR(3)    REFERENCES countries(code),
    correlation_coeff NUMERIC(5,4),
    sample_size     INT,
    confidence      NUMERIC(5,2),
    discovered_at   TIMESTAMPTZ   DEFAULT NOW(),
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_correlations_country ON correlations(country_code);
CREATE INDEX idx_correlations_discovered ON correlations(discovered_at);


-- 12. PREDICTIONS
CREATE TABLE IF NOT EXISTS predictions (
    id              SERIAL PRIMARY KEY,
    country_code    VARCHAR(3)    NOT NULL REFERENCES countries(code),
    prediction_type VARCHAR(50)   NOT NULL,
    predicted_value NUMERIC(20,4),
    confidence      NUMERIC(5,2),
    target_date     DATE,
    model_used      VARCHAR(50),
    actual_value    NUMERIC(20,4),
    is_resolved     BOOLEAN       DEFAULT FALSE,
    created_at      TIMESTAMPTZ   DEFAULT NOW(),
    resolved_at     TIMESTAMPTZ
);

CREATE INDEX idx_predictions_country ON predictions(country_code);
CREATE INDEX idx_predictions_target ON predictions(target_date);
CREATE INDEX idx_predictions_resolved ON predictions(is_resolved);


-- 13. API FETCH LOG
CREATE TABLE IF NOT EXISTS fetch_logs (
    id              SERIAL PRIMARY KEY,
    data_source     VARCHAR(50)   NOT NULL,
    endpoint        VARCHAR(200),
    status_code     INT,
    records_fetched INT           DEFAULT 0,
    duration_ms     INT,
    error_message   TEXT,
    fetched_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_fetch_logs_source ON fetch_logs(data_source);
CREATE INDEX idx_fetch_logs_fetched ON fetch_logs(fetched_at);


-- 14. USER ALERTS
CREATE TABLE IF NOT EXISTS user_alerts (
    id              SERIAL PRIMARY KEY,
    telegram_chat_id BIGINT,
    alert_rule      VARCHAR(100)  NOT NULL,
    country_code    VARCHAR(3)    REFERENCES countries(code),
    indicator_type  VARCHAR(50),
    condition       VARCHAR(10)   CHECK (condition IN ('above', 'below', 'equals', 'crosses')),
    threshold_value NUMERIC(20,4),
    is_active       BOOLEAN       DEFAULT TRUE,
    triggered_count INT           DEFAULT 0,
    last_triggered  TIMESTAMPTZ,
    created_at      TIMESTAMPTZ   DEFAULT NOW()
);

CREATE INDEX idx_user_alerts_chat ON user_alerts(telegram_chat_id);
CREATE INDEX idx_user_alerts_active ON user_alerts(is_active);


-- ============================================================
-- HELPER VIEWS
-- ============================================================

CREATE OR REPLACE VIEW v_latest_health_scores AS
SELECT DISTINCT ON (hs.country_code)
    hs.country_code,
    c.name AS country_name,
    c.region,
    hs.overall_score,
    hs.trend,
    hs.previous_score,
    hs.score_change,
    hs.calculated_at
FROM health_scores hs
JOIN countries c ON c.code = hs.country_code
ORDER BY hs.country_code, hs.calculated_at DESC;


CREATE OR REPLACE VIEW v_active_alerts_summary AS
SELECT
    country_code,
    COUNT(*) AS alert_count,
    MAX(severity) AS max_severity,
    MAX(created_at) AS latest_alert
FROM crisis_alerts
WHERE is_active = TRUE
GROUP BY country_code;


-- ============================================================
-- UPDATE TIMESTAMP TRIGGER
-- ============================================================

CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_countries_updated_at
    BEFORE UPDATE ON countries
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
