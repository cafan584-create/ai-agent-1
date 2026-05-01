CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    code VARCHAR(3) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    region VARCHAR(50),
    sub_region VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS economic_indicators (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) REFERENCES countries(code),
    indicator_type VARCHAR(50) NOT NULL,
    value NUMERIC(20,4),
    unit VARCHAR(20) DEFAULT 'usd',
    frequency VARCHAR(20) DEFAULT 'annual',
    year INT,
    source VARCHAR(50),
    fetched_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS stock_indices (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) REFERENCES countries(code),
    index_name VARCHAR(100) NOT NULL,
    value NUMERIC(20,4) NOT NULL,
    change_percent NUMERIC(10,4),
    volume BIGINT,
    timestamp TIMESTAMPTZ NOT NULL
);

CREATE TABLE IF NOT EXISTS crypto_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    name VARCHAR(100),
    price_usd NUMERIC(20,4) NOT NULL,
    market_cap NUMERIC(20,2),
    volume_24h NUMERIC(20,2),
    change_24h NUMERIC(10,4),
    change_7d NUMERIC(10,4),
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS exchange_rates (
    id SERIAL PRIMARY KEY,
    base_currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    target_currency VARCHAR(3) NOT NULL,
    rate NUMERIC(20,8) NOT NULL,
    source VARCHAR(50) DEFAULT 'frankfurter',
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS health_scores (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) REFERENCES countries(code),
    overall_score NUMERIC(5,2) NOT NULL,
    trend VARCHAR(10) DEFAULT 'stable',
    previous_score NUMERIC(5,2),
    score_change NUMERIC(5,2),
    calculated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS crisis_alerts (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) REFERENCES countries(code),
    alert_type VARCHAR(50) NOT NULL,
    severity VARCHAR(10) NOT NULL,
    title VARCHAR(200),
    description TEXT,
    confidence NUMERIC(5,2),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS anomalies (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) REFERENCES countries(code),
    anomaly_type VARCHAR(50) NOT NULL,
    description TEXT,
    data_source VARCHAR(50),
    severity VARCHAR(10),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS news (
    id SERIAL PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    url TEXT,
    source VARCHAR(100),
    category VARCHAR(50),
    published_at TIMESTAMPTZ,
    fetched_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS briefings (
    id SERIAL PRIMARY KEY,
    briefing_type VARCHAR(20) NOT NULL,
    title VARCHAR(200),
    content TEXT NOT NULL,
    generated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS correlations (
    id SERIAL PRIMARY KEY,
    indicator_a VARCHAR(100) NOT NULL,
    indicator_b VARCHAR(100) NOT NULL,
    country_code VARCHAR(3) REFERENCES countries(code),
    correlation_coeff NUMERIC(5,4),
    discovered_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) REFERENCES countries(code),
    prediction_type VARCHAR(50) NOT NULL,
    predicted_value NUMERIC(20,4),
    confidence NUMERIC(5,2),
    target_date DATE,
    actual_value NUMERIC(20,4),
    is_resolved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    resolved_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS fetch_logs (
    id SERIAL PRIMARY KEY,
    data_source VARCHAR(50) NOT NULL,
    status_code INT,
    records_fetched INT DEFAULT 0,
    error_message TEXT,
    fetched_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS user_alerts (
    id SERIAL PRIMARY KEY,
    telegram_chat_id BIGINT,
    country_code VARCHAR(3) REFERENCES countries(code),
    indicator_type VARCHAR(50),
    condition VARCHAR(10),
    threshold_value NUMERIC(20,4),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_indicators_country ON economic_indicators(country_code);
CREATE INDEX idx_stocks_country ON stock_indices(country_code);
CREATE INDEX idx_crypto_timestamp ON crypto_data(timestamp);
CREATE INDEX idx_health_country ON health_scores(country_code);
CREATE INDEX idx_alerts_country ON crisis_alerts(country_code);
CREATE INDEX idx_fetch_logs_source ON fetch_logs(data_source);