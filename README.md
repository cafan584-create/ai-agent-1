# SOVEREIGN — Global Financial Intelligence Agent

An autonomous AI agent that tracks, analyzes, and predicts the financial health of every country on Earth in real-time. **100% free to run.**

---

## 📁 Project Structure

```
ai-agent-1/
│
├── .env.example                  # Template for all API keys & config
├── .gitignore                    # Git ignore rules
├── requirements.txt              # All Python dependencies
├── docker-compose.yml            # Local development setup
│
├── backend/                      # Python FastAPI backend server
│   ├── main.py                   # Application entry point (FastAPI app)
│   ├── config.py                 # Environment config loader (Supabase, Redis, API keys)
│   │
│   ├── data/                     # DATA COLLECTION LAYER — fetches live data from free APIs
│   │   ├── __init__.py
│   │   ├── fetcher_worldbank.py  # GDP, trade balance, debt, forex reserves, inflation (no API key)
│   │   ├── fetcher_fred.py       # US interest rates, money supply, bond yields, employment (needs FRED API key)
│   │   ├── fetcher_yahoo.py      # Stock market indices, forex pairs, commodities (no API key via yfinance)
│   │   ├── fetcher_coingecko.py  # Crypto prices, market cap, volume, DeFi TVL (no API key)
│   │   ├── fetcher_oecd.py       # Employment rates, housing prices, productivity, trade data (no API key)
│   │   ├── fetcher_imf.py        # IMF debt data, balance of payments, SDR allocations (no API key)
│   │   ├── fetcher_bis.py        # Banking system health, credit growth, property prices (no API key)
│   │   ├── fetcher_defillama.py  # DeFi total value locked, stablecoin market data (no API key)
│   │   ├── fetcher_exchange.py   # Real-time currency exchange rates (free, needs ExchangeRate-API key)
│   │   └── fetcher_rss.py        # Financial news from RSS feeds — Reuters, Bloomberg, CNBC (no API key, no limits)
│   │
│   ├── processors/               # INTELLIGENCE ENGINES — processes raw data into insights
│   │   ├── __init__.py
│   │   ├── normalizer.py         # Cleans, validates, and standardizes all fetched data into uniform format
│   │   ├── health_scorer.py      # Country Health Score algorithm — combines 18 indicators into 0-100 score
│   │   ├── crisis_detector.py    # Early warning system — detects patterns matching historical crises (currency collapse, debt default, hyperinflation, bank runs)
│   │   ├── anomaly_detector.py   # Flags impossible/improbable data — cross-references sources for contradictions, detects data manipulation
│   │   ├── contagion_mapper.py   # Cross-country impact analysis — maps trade/financial relationships, predicts crisis spread
│   │   ├── correlation_engine.py # Auto-discovers hidden relationships between indicators across countries
│   │   └── prediction_engine.py  # Forecasts future trends using ARIMA time series models + historical patterns
│   │
│   ├── ai/                       # AI ANALYSIS LAYER — generates natural language insights
│   │   ├── __init__.py
│   │   ├── narrative_engine.py   # Auto-generates financial briefings — daily/hourly/event-driven reports in plain English
│   │   ├── query_handler.py      # Natural language Q&A — users ask questions in plain English, AI answers from database
│   │   └── prompt_templates.py   # System prompts for AI models — pre-built templates for different analysis types
│   │
│   ├── api/                      # REST API ENDPOINTS — serves data to frontend and bots
│   │   ├── __init__.py
│   │   ├── countries.py          # GET /api/countries (list all), GET /api/countries/{code} (single country profile)
│   │   ├── health_scores.py      # GET /api/health-scores (all ranked), GET /api/health-scores/{code} (score history)
│   │   ├── alerts.py             # GET /api/alerts (active alerts), POST /api/alerts (create custom alert)
│   │   ├── queries.py            # POST /api/query (natural language question → AI answer)
│   │   ├── briefings.py          # GET /api/briefings/latest (latest AI report), GET /api/briefings/{id} (specific report)
│   │   └── comparisons.py        # GET /api/compare?countries=US,CN,IN (compare 2+ countries side by side)
│   │
│   ├── scheduler/                # AUTOMATED DATA UPDATES — runs fetchers on schedule
│   │   ├── __init__.py
│   │   └── tasks.py              # APScheduler jobs — crypto every 5min, stocks 15min, news hourly, economic data daily, health scores daily
│   │
│   └── utils/                    # HELPER UTILITIES
│       ├── __init__.py
│       ├── cache.py              # File-based JSON cache — caches API responses to avoid re-fetching
│       └── formatters.py         # Data formatting — number formatting, date parsing, currency display
│
├── database/                     # DATABASE SETUP
│   ├── schema.sql                # Full PostgreSQL schema — all table definitions (run in Supabase SQL editor)
│   └── seed_countries.py         # Seeds 195 countries with ISO codes, names, regions into database
│
├── frontend/                     # WEB DASHBOARD — lightweight HTML/CSS/JS served by FastAPI
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css         # Global styles, responsive design, dark theme
│   │   ├── js/
│   │   │   ├── app.js            # Main application logic
│   │   │   ├── world-map.js      # Interactive world map visualization (color-coded by health score)
│   │   │   ├── charts.js         # Trend charts using Chart.js — health score history, indicator graphs
│   │   │   └── alerts.js         # Live crisis alert feed with auto-refresh
│   │   └── img/
│   │       └── logo.svg          # SOVEREIGN logo
│   └── templates/
│       ├── base.html             # Base HTML template with navigation
│       ├── index.html            # Home page — world map overview, top 5 healthiest, top 5 at-risk
│       ├── country.html          # Country detail page — full profile, all indicators, score breakdown, history
│       ├── compare.html          # Comparison page — side-by-side country comparison with charts
│       ├── alerts.html           # Alerts page — all active crisis alerts, severity breakdown
│       └── briefing.html         # Briefing page — latest AI-generated financial report
│
├── bots/                         # CHAT PLATFORM BOTS
│   └── telegram/
│       ├── bot.py                # Telegram bot main — connects to Telegram API, handles incoming messages
│       └── commands.py           # Bot commands: /health, /crisis, /compare, /alert, /query, /top5, /bottom5, /briefing
│
├── scripts/                      # UTILITY SCRIPTS
│   ├── init_db.py                # Initialize database connection and verify tables exist
│   ├── seed_data.py              # Initial bulk data load — fetches historical data for all countries
│   └── test_apis.py              # Tests all API connections — verifies every data source is working
│
├── deploy/                       # DEPLOYMENT CONFIGS
│   ├── render.yaml               # Render.com deployment config (free tier)
│   └── vercel.json               # Vercel frontend config (free tier)
│
├── deploy.sh                     # One-click deploy script for Render
└── README.md                     # This file
```

---

## 🏗️ Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                        USER LAYER                                 │
│                                                                   │
│   ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│   │  Web Browser │  │  Telegram    │  │  Discord (future)     │  │
│   │  (Dashboard) │  │  Bot         │  │                       │  │
│   └──────┬───────┘  └──────┬───────┘  └───────────┬───────────┘  │
│          │                  │                      │              │
└──────────┼──────────────────┼──────────────────────┼──────────────┘
           │                  │                      │
┌──────────▼──────────────────▼──────────────────────▼──────────────┐
│                     API LAYER (FastAPI)                           │
│                                                                   │
│   GET  /api/countries          →  List all countries             │
│   GET  /api/countries/{code}   →  Single country profile         │
│   GET  /api/health-scores      →  All countries ranked           │
│   GET  /api/alerts             →  Active crisis alerts           │
│   POST /api/query              →  Natural language AI question   │
│   GET  /api/briefings/latest   →  Latest AI financial report     │
│   GET  /api/compare            →  Compare 2+ countries           │
│                                                                   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    INTELLIGENCE ENGINE                          │
│                                                                   │
│   ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│   │ Health       │  │ Crisis       │  │ Anomaly               │  │
│   │ Scorer       │  │ Detector     │  │ Detector              │  │
│   │ (18 factors) │  │ (6 patterns) │  │ (cross-reference)     │  │
│   └──────────────┘  └──────────────┘  └───────────────────────┘  │
│   ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐  │
│   │ Contagion    │  │ Correlation  │  │ Prediction            │  │
│   │ Mapper       │  │ Engine       │  │ Engine                │  │
│   └──────────────┘  └──────────────┘  └───────────────────────┘  │
│                                                                   │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    DATA COLLECTION LAYER                        │
│                                                                   │
│   World Bank │ FRED │ CoinGecko │ Yahoo │ OECD │ IMF │ BIS      │
│   Frankfurter │ DeFiLlama │ RSS Feeds │ ExchangeRate-API        │
│                                                                   │
│   Update schedule:                                               │
│   • Crypto: every 5 minutes                                      │
│   • Stocks: every 15 minutes (market hours)                      │
│   • Exchange rates: every hour                                   │
│   • News: every hour                                             │
│   • Economic indicators: daily (when released)                   │
│   • Health scores: recalculated daily                            │
│   • Crisis alerts: evaluated on every new data point             │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    STORAGE LAYER                                │
│                                                                   │
│   ┌──────────────────────┐    ┌─────────────────────────────┐    │
│   │ Supabase (PostgreSQL)│    │ JSON File Cache             │    │
│   │                      │    │ (local disk, zero service)  │    │
│   │ • countries          │    │                             │    │
│   │ • economic_indicators│    │ • API response cache        │    │
│   │ • stock_indices      │    │ • Rate limiting             │    │
│   │ • crypto_data        │    │ • Temporary computation     │    │
│   │ • health_scores      │    │                             │    │
│   │ • crisis_alerts      │    │                             │    │
│   │ • anomalies          │    │                             │    │
│   │ • news               │    │                             │    │
│   │ • briefings          │    │                             │    │
│   │ • correlations       │    │                             │    │
│   └──────────────────────┘    └─────────────────────────────┘    │
│                                                                   │
│   Supabase: 100% FREE (email signup only)                        │
│   File Cache: BUILT-IN — no external service needed              │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🔧 What Data It Tracks

### **Macroeconomic Indicators**
- GDP (nominal & PPP), GDP growth rate, GDP per capita
- Inflation (CPI, PPI, core inflation)
- Unemployment rate, labor force participation
- National debt, debt-to-GDP ratio
- Government budget balance, deficit/surplus
- Money supply (M1, M2, M3)

### **Financial Markets**
- Stock market indices (S&P 500, FTSE, Nikkei, Shanghai, BSE, all major)
- Cryptocurrency prices (top 100 by market cap)
- Currency exchange rates (all major & emerging market currencies)
- Bond yields, yield curves
- Interest rates (central bank policy rates)
- Foreign exchange reserves
- Gold reserves

### **Trade & Commerce**
- Import volumes, export volumes
- Trade balance (surplus/deficit)
- Top trading partners
- Current account balance
- Foreign direct investment (FDI)
- DeFi total value locked (TVL)

### **Banking & Credit**
- Banking system stability metrics
- Credit growth rate
- Non-performing loan ratios
- Property price indices
- Mortgage rates

### **Real-Time Events**
- Financial news (Reuters, Bloomberg, CNBC via RSS)
- Breaking economic events
- Central bank announcements
- Geopolitical events affecting markets

---

## 🧮 Country Health Score Algorithm

Every country gets a **0-100 score** calculated from 18 weighted indicators:

| Indicator | Weight | What It Measures |
|---|---|---|
| GDP Growth | 8% | Economic expansion/contraction |
| Inflation Stability | 7% | Price stability (2-4% is ideal) |
| Debt-to-GDP Ratio | 8% | National debt burden |
| Forex Reserves | 6% | Ability to defend currency, pay debts |
| Trade Balance | 5% | Export competitiveness |
| Currency Stability | 6% | Exchange rate volatility |
| Stock Market Health | 5% | Investor confidence, market performance |
| Employment Rate | 5% | Labor market strength |
| Interest Rate Environment | 5% | Monetary policy effectiveness |
| Money Supply Growth | 4% | Inflation risk indicator |
| Banking System Health | 5% | Financial system stability |
| Real Estate Stability | 4% | Housing market health |
| Credit Rating | 5% | International confidence |
| Foreign Investment | 4% | Capital attractiveness |
| Government Budget | 4% | Fiscal responsibility |
| Crypto Adoption/Impact | 3% | Digital economy integration |
| Economic Freedom Index | 3% | Business environment quality |
| Geopolitical Risk | 3% | Political stability impact |

**Score interpretation:**
- **80-100:** Strong & stable economy
- **60-79:** Moderate, some risks
- **40-59:** Vulnerable, watch closely
- **20-39:** High risk, crisis possible
- **0-19:** Critical, crisis likely

---

## 🔔 Crisis Detection Patterns

The system detects 6 types of economic crises by pattern-matching against historical data:

1. **Currency Collapse** — Rapid depreciation + falling reserves + rising interest rates
2. **Debt Default** — Debt-to-GDP spike + falling reserves + credit downgrade
3. **Hyperinflation** — CPI growth >50% month-over-month + money supply explosion
4. **Bank Run** — Deposit withdrawals + banking sector stress + liquidity crunch
5. **Recession** — Two consecutive quarters of negative GDP growth
6. **Trade Crisis** — Export collapse + currency depreciation + reserve depletion

Each detection includes **confidence percentage** and **historical similarity match** (e.g., "This pattern matches Turkey 2018 at 87% similarity").

---

## 💰 100% Free — Zero Cost Forever

| Service | Purpose | Cost |
|---|---|---|
| **Supabase** | PostgreSQL database | Free (email signup only) |
| **JSON File Cache** | Caching layer | Built-in, no service needed |
| **World Bank API** | Economic data | Free, no key |
| **FRED API** | US financial data | Free (need API key) |
| **CoinGecko** | Crypto data | Free, no key |
| **yfinance** | Stock data | Free, no key |
| **OECD API** | Employment, trade data | Free, no key |
| **IMF API** | Debt, reserves data | Free, no key |
| **BIS API** | Banking data | Free, no key |
| **DeFi Llama** | DeFi data | Free, no key |
| **Frankfurter API** | Exchange rates | Free, no key |
| **RSS Feeds** | Financial news | Free, no key |
| **Telegram Bot API** | Chat bot | Free (need bot token) |
| **Render** | Backend hosting | Free tier |
| **Vercel** | Frontend hosting | Free tier |
| **Groq** (optional) | AI processing | Free tier |

---

## 🚀 Setup Guide (Coming Soon)

### Prerequisites
- Python 3.10+
- Free Supabase account (email only, no payment method)
- Free API keys (FRED, ExchangeRate-API)

### Quick Start
```bash
# 1. Clone the repo
git clone https://github.com/cafan584-create/ai-agent-1.git
cd ai-agent-1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env with your Supabase URL and API keys

# 4. Initialize database
python scripts/init_db.py

# 5. Seed countries
python scripts/seed_countries.py

# 6. Load initial data
python scripts/seed_data.py

# 7. Run the server
uvicorn backend.main:app --reload

# 8. Open dashboard
http://localhost:8000
```

---

## 📊 Data Sources (No API Key Required)

| Source | Data | URL |
|---|---|---|
| World Bank | GDP, trade, debt, reserves | `api.worldbank.org/v2` |
| CoinGecko | Crypto prices, market cap | `api.coingecko.com/api/v3` |
| yfinance | Stock indices, forex | Python library |
| OECD | Employment, housing, trade | `data.oecd.org/api` |
| IMF | Debt, balance of payments | `api.imf.org` |
| BIS | Banking, credit, property | `data.bis.org` |
| DeFi Llama | DeFi TVL, stablecoins | `api.llama.fi` |
| Frankfurter | Exchange rates | `api.frankfurter.app` |
| RSS Feeds | Financial news | Various RSS URLs |

### Data Sources (Free API Key Required)

| Source | Data | Get Key At |
|---|---|---|
| FRED | US rates, money supply, employment | `fred.stlouisfed.org/docs/api/api_key.html` |
| ExchangeRate-API | Real-time currency rates | `www.exchangerate-api.com` |
| NewsAPI | Financial news (backup to RSS) | `newsapi.org` |

---

## 📈 Update Schedule

| Data Type | Frequency | Source |
|---|---|---|
| Crypto prices | Every 5 minutes | CoinGecko |
| Stock indices | Every 15 minutes (market hours) | yfinance |
| Exchange rates | Every hour | Frankfurter / ExchangeRate-API |
| Financial news | Every hour | RSS feeds |
| Economic indicators | Daily | World Bank, OECD, IMF, BIS, FRED |
| Health scores | Recalculated daily | All data sources |
| Crisis alerts | Real-time (evaluated on each new data point) | All processors |
| AI briefings | Every 3 hours or on major events | Narrative engine |

---

## 🛤️ Development Roadmap

- [x] Step 1: Project structure + config
- [x] Step 2: Database schema (Supabase PostgreSQL)
- [x] Step 3: File-based JSON cache layer
- [x] Step 4: World Bank data fetcher
- [x] Step 5: CoinGecko crypto fetcher
- [x] Step 6: Yahoo Finance stock fetcher
- [x] Step 7: OECD data fetcher
- [x] Step 8: FRED data fetcher
- [x] Step 9: Exchange rate fetcher
- [x] Step 10: RSS news fetcher
- [x] Step 11: Country Health Score engine
- [x] Step 12: Crisis Detection engine
- [x] Step 13: Anomaly Detection engine
- [x] Step 14: Contagion Mapper
- [x] Step 15: Correlation Engine
- [x] Step 16: AI Narrative Engine
- [x] Step 17: REST API endpoints
- [x] Step 18: Web dashboard
- [x] Step 19: Telegram bot
- [x] Step 20: Data scheduler
- [x] Step 21: Deployment
- [x] Step 22: Documentation

---

## 📜 License

MIT License — Free to use, modify, and distribute.
