<div align="center">

<img src="https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge" alt="Version"/>
<img src="https://img.shields.io/badge/status-active-success?style=for-the-badge" alt="Status"/>
<img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License"/>
<img src="https://img.shields.io/badge/python-3.14-blue?style=for-the-badge&logo=python" alt="Python"/>
<img src="https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js" alt="Next.js"/>

<br/>
<br/>

```
 ██████╗ ███╗   ███╗ █████╗ ██████╗ ████████╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
██╔════╝ ████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
╚█████╗  ██╔████╔██║███████║██████╔╝   ██║   ██████╔╝██║   ██║██║     ███████╗█████╗  
 ╚═══██╗ ██║╚██╔╝██║██╔══██║██╔══██╗   ██║   ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
██████╔╝ ██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   ██║     ╚██████╔╝███████╗███████║███████╗
╚═════╝  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
```

# 🇱🇰 SLTDA SmartPulse
### *AI-Powered Tourism Business Intelligence Platform*

<h3>
  <em>"The Intelligence Behind Sri Lanka Tourism"</em>
</h3>

<br/>

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Visit_Now-2C5282?style=for-the-badge)](https://sltda-smartpulse.vercel.app)
[![API Docs](https://img.shields.io/badge/📚_API_Docs-Swagger_UI-0D6E6E?style=for-the-badge)](https://sltda-smartpulse-api.railway.app/docs)
[![GitHub Stars](https://img.shields.io/github/stars/NelushaNethmina/SLTDA-SmartPulse?style=for-the-badge&color=C6A84B)](https://github.com/NelushaNethmina/SLTDA-SmartPulse/stargazers)

<br/>

---

</div>

## 📋 Table of Contents

- [🎯 What is SmartPulse?](#-what-is-smartpulse)
- [🚨 The Problem](#-the-problem)
- [✨ Features — 26 Total](#-features--26-total)
- [🏗️ System Architecture](#️-system-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [🗄️ Database Design](#️-database-design)
- [📊 Dashboard Pages](#-dashboard-pages)
- [🔐 Security & RBAC](#-security--rbac)
- [🌍 Competitive Analysis](#-competitive-analysis)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [🔌 API Reference](#-api-reference)
- [📈 ML Models](#-ml-models)
- [💰 Business Model](#-business-model)
- [🗺️ Roadmap](#️-roadmap)
- [👨‍💻 Developer](#-developer)

---

## 🎯 What is SmartPulse?

**SLTDA SmartPulse** is a production-grade, AI-powered Business Intelligence platform built exclusively for the **Sri Lanka Tourism Development Authority (SLTDA)**.

It transforms Sri Lanka's fragmented tourism data into a **unified, real-time intelligence hub** — enabling evidence-based policy decisions, forward-looking demand forecasting, and sustainable commercial revenue.

```
Before SmartPulse:                    After SmartPulse:
─────────────────                     ────────────────
📄 PDF reports (monthly)        →     📊 Real-time interactive dashboard
🔍 Manual Excel analysis        →     🤖 AI-powered automated insights  
🌐 English reviews only         →     🌍 12-language multilingual NLP
📉 Historical data only         →     ✈️  Forward-looking flight demand signals
💸 Zero commercial revenue      →     💰 SaaS API monetisation tier
```

> **Built by:** Nelusha Nethmina | Uva Wellassa University | BSc (Hons) ICT — Business Intelligence

---

## 🚨 The Problem

Sri Lanka's tourism sector contributes **12%+ to national GDP** and employs **2.1+ million people** — yet SLTDA operates with:

| Gap | Current Reality | Impact |
|-----|----------------|--------|
| 📄 Data Fragmentation | Monthly PDF bulletins, no live dashboard | Policy decisions delayed by weeks |
| 🔮 Zero Forecasting | No ML model — purely reactive planning | Cannot pre-position marketing spend |
| 🌐 English-Only Sentiment | 72% of reviews in other languages ignored | Russian, Chinese, German voices unheard |
| ✈️ No Forward Signals | Historical data only — no flight intent data | Misses 3-6 month demand signals |
| 💸 No Revenue Generation | All analytics locked inside government | Significant SaaS opportunity untapped |
| 🗺️ No District Intelligence | National aggregates only — no district drill-down | Cannot identify underperforming regions |

---

## ✨ Features — 26 Total

<details>
<summary><b>🔵 Core BI Analytics (F-01 to F-05)</b></summary>

| ID | Feature | Description |
|----|---------|-------------|
| F-01 | Tourist Arrival Analytics | Interactive time-series by country, season, entry point |
| F-02 | Hotel & Accommodation Intelligence | Occupancy gaps, ADR, RevPAR by district |
| F-03 | Tourist Spending Pattern Analysis | Sector breakdown — accommodation, food, transport |
| F-04 | Tourist Flow & Route Mapping | Internal travel corridors across 25 districts |
| F-05 | Accommodation Gap Analysis | Supply vs demand by star category and district |

</details>

<details>
<summary><b>🤖 AI / ML Intelligence (F-06 to F-13)</b></summary>

| ID | Feature | Technology |
|----|---------|-----------|
| F-06 | 90-Day Demand Forecasting | Facebook Prophet |
| F-07 | ✨ Amadeus Hybrid Forward Demand | Amadeus API + Prophet (60/40 blend) |
| F-08 | Tourist Review Sentiment | VADER NLP |
| F-09 | ✨ Multilingual Sentiment — 12 Languages | langdetect + deep-translator + VADER |
| F-10 | Tourist Persona Clustering | K-Means (Scikit-learn) |
| F-11 | Anomaly Detection | Isolation Forest |
| F-12 | Monsoon Impact Intelligence | Custom seasonal model |
| F-13 | ✨ Economic Impact & Sector Analysis | World Bank API + CBSL data |

</details>

<details>
<summary><b>⚡ Advanced Features (F-14 to F-22)</b></summary>

| ID | Feature | Description |
|----|---------|-------------|
| F-14 | AI Chatbot | Claude API (claude-sonnet-4-6) natural language queries |
| F-15 | ✨ AI Itinerary Planner | Claude API + live DB context injection |
| F-16 | Revenue Optimization Engine | Pricing recommendations by season + source market |
| F-17 | Geo-Spatial Heatmap | Leaflet.js — all 25 Sri Lanka districts |
| F-18 | Travel Agent B2B Portal | TAASL/SLAITO member data exchange |
| F-19 | Regional Benchmarking | Compare Sri Lanka vs Thailand, Maldives, Vietnam |
| F-20 | Source Market Analyzer | Diversification opportunities by nationality |
| F-21 | Seasonal Campaign Planner | AI-assisted marketing calendar |
| F-22 | ✨ Smart Alert System | APScheduler + SMTP — Prophet-driven notifications |

</details>

<details>
<summary><b>🔒 Security, Operations & Commercial (F-23 to F-26)</b></summary>

| ID | Feature | Description |
|----|---------|-------------|
| F-23 | Role-Based Access Control | 22 accounts, 14 roles, bcrypt + JWT |
| F-24 | Problem Tracking Workflow | Closed-loop complaint management |
| F-25 | False Review Detection | 3-method ML detection system |
| F-26 | ✨ Premium API Tier System | Free / Starter / Pro / Enterprise SaaS |

</details>

> ✨ = Version 1.0 new features

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                           │
│  Next.js 15 + TypeScript + Tailwind CSS 4 + shadcn/ui              │
│  Recharts │ Leaflet.js │ React Query │ 10 Dashboard Pages           │
└─────────────────────────┬───────────────────────────────────────────┘
                          │ HTTP/REST (JSON)
┌─────────────────────────▼───────────────────────────────────────────┐
│                          API LAYER                                   │
│  FastAPI (Python) │ JWT Auth │ RBAC │ Rate Limiting │ Swagger UI    │
│  8 Routers │ Pydantic v2 Validation │ CORS                          │
└──────────┬──────────────┬──────────────────────────────────────────-┘
           │              │
┌──────────▼──────┐  ┌────▼─────────────────────────────────────────┐
│   AI/ML ENGINE  │  │              DATA LAYER                       │
│  Prophet        │  │  PostgreSQL 18 (Star Schema)                  │
│  VADER + NLP    │  │  Redis (Cache)                                │
│  K-Means        │  │  Supabase (Auth + RLS)                        │
│  Isolation Forest│  │  13 Tables │ Indexes │ Triggers               │
│  Amadeus API    │  └──────────────────────────────────────────────-┘
│  Claude API     │
└──────────┬──────┘
           │
┌──────────▼──────────────────────────────────────────────────────────┐
│                        DATA SOURCES (14)                             │
│  SLTDA PDFs │ Amadeus API │ OpenWeatherMap │ World Bank              │
│  Google Reviews │ TripAdvisor │ Booking.com │ CBSL Reports           │
│  AviationStack │ ExchangeRate API │ REST Countries                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| Next.js | 15 (React 19) | SSR Framework |
| TypeScript | 5.x | Type Safety |
| Tailwind CSS | 4.x | Styling |
| shadcn/ui | Latest | UI Components |
| Recharts | Latest | Data Charts |
| Leaflet.js | 1.9 | District Maps |

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| FastAPI | 0.115+ | API Framework |
| Python | 3.14 | Language |
| SQLAlchemy | 2.0 | ORM |
| Pydantic | v2 | Validation |
| bcrypt | 4.0.1 | Password Hashing |
| python-jose | 3.x | JWT Tokens |

### AI / ML
| Technology | Purpose |
|-----------|---------|
| Facebook Prophet | Demand Forecasting |
| VADER Sentiment | Review Analysis |
| Scikit-learn | Clustering + Anomaly |
| deep-translator | 12-Language NLP |
| Claude API | AI Chatbot + Itinerary |
| Amadeus API | Flight Demand Signals |

### Infrastructure
| Technology | Purpose | Cost |
|-----------|---------|------|
| PostgreSQL 18 | Database | Free (local) |
| Redis | Caching | Free |
| Vercel | Frontend Hosting | Free |
| Railway | Backend Hosting | ~$5/month |
| Supabase | Auth + RLS | Free tier |
| GitHub Actions | CI/CD | Free |

---

## 🗄️ Database Design

**Star Schema — Optimised for BI Analytics**

```
                    dim_country
                         │
         dim_time ───────┼────── dim_location
                         │
              fact_visitor_trips (CENTRAL)
                         │
         dim_accommodation ── dim_weather
                         │
              dim_review ── dim_problem
```

**13 Tables Total:**

| Table | Type | Records |
|-------|------|---------|
| fact_visitor_trips | FACT | Growing |
| dim_country | Dimension | 50+ countries |
| dim_location | Dimension | 250+ locations |
| dim_time | Dimension | Date dimension |
| dim_accommodation | Dimension | All star categories |
| dim_weather | Dimension | 9 provinces |
| dim_review | Dimension | 3,750+ reviews |
| dim_problem | Dimension | Problem tracking |
| tourism_locations | Extended | 250+ locations |
| reviews | Extended | 3,750+ reviews |
| tourist_arrivals | Extended | 2010-2024 data |
| tourism_problems | Extended | Issue tracker |
| users | Auth | 22 accounts |

---

## 📊 Dashboard Pages

| Page | Title | Key Visualisations |
|------|-------|-------------------|
| 1 | Executive Overview | KPI cards, active alerts, top countries |
| 2 | Arrival Analytics | Time-series, YoY comparison, filters |
| 3 | District Intelligence | Leaflet heatmap, 25 districts, time-slider |
| 4 | Demand Forecasting | Prophet + Amadeus chart, confidence bands |
| 5 | Sentiment & Reviews | 12-language breakdown, false review panel |
| 6 | Tourist Personas & Flow | K-Means clusters, Sankey flow chart |
| 7 | Economic Impact | Revenue by district, GDP contribution |
| 8 | Problem Tracker | Priority queue, resolution workflow |
| 9 | AI Assistant | Claude chatbot + itinerary planner |
| 10 | Admin Panel | User management, ETL status, audit logs |

---

## 🔐 Security & RBAC

```
Authentication Flow:
──────────────────
POST /api/auth/login
    ↓ bcrypt verify (cost factor 12)
    ↓ JWT create (HS256, 60min expiry)
    ↓ Token returned
    ↓ All subsequent requests: Authorization: Bearer <token>
    ↓ RBAC enforced at DB query level
```

**22 User Accounts — 14 Roles:**

| Role | Access Level |
|------|-------------|
| `director` | Full platform — all 10 pages |
| `research` | Data warehouse + ML outputs |
| `marketing` | Personas + sentiment + campaigns |
| `it_admin` | User management + system health |
| `admin` | Full admin panel |
| `ministry` | Read-only executive KPIs |
| `regional` (×9) | Own province data only |
| `wildlife` | Nature tourism metrics |
| `archaeology` | Heritage site data |
| `agent` | B2B portal + forecasts |
| `hotel` | Occupancy + local sentiment |
| `tour_guide` | Trending routes + nationalities |
| `restaurant` | Food sector spending |
| `transport` | Tourist flow mapping |

---

## 🌍 Competitive Analysis

| Capability | SLTDA Current | Thailand TAT | Maldives | **SmartPulse** |
|-----------|:---:|:---:|:---:|:---:|
| Live Dashboard | ❌ | ✅ | ✅ | ✅ |
| AI Forecasting | ❌ | ✅ | ⚠️ | ✅ |
| Flight Demand Signals | ❌ | ⚠️ | ❌ | ✅ |
| Multilingual NLP (12 lang) | ❌ | ❌ | ❌ | ✅ |
| Economic Sector Breakdown | ❌ | ⚠️ | ❌ | ✅ |
| AI Chatbot | ❌ | ❌ | ❌ | ✅ |
| AI Itinerary Planner | ❌ | ❌ | ❌ | ✅ |
| False Review Detection | ❌ | ❌ | ❌ | ✅ |
| Commercial SaaS API | ❌ | ❌ | ❌ | ✅ |
| 25-District Heatmap | ❌ | ❌ | ❌ | ✅ |

> SmartPulse surpasses every regional competitor across all 10 capability dimensions.

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required
Python 3.11+        # Backend
Node.js 18+         # Frontend  
PostgreSQL 18       # Database
Git                 # Version control
```

### 1. Clone Repository

```bash
git clone https://github.com/NelushaNethmina/SLTDA-SmartPulse.git
cd SLTDA-SmartPulse
```

### 2. Backend Setup

```bash
# Create virtual environment
python -m venv .venv --without-pip
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Mac/Linux

# Install pip
.venv\Scripts\python.exe -m ensurepip --upgrade

# Install libraries
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Environment Setup

```bash
# Copy example env
cp .env.example .env

# Edit .env with your credentials
# DB_URL, SECRET_KEY, API keys
```

### 4. Database Setup

```bash
# Run schema in pgAdmin or psql
psql -U postgres -d sltda_smartpulse -f database/schema.sql
```

### 5. Start Backend

```bash
uvicorn backend.main:app --reload --port 8000
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### 6. Start Frontend

```bash
cd frontend
yarn install
yarn dev
# Dashboard: http://localhost:3000
```

### 7. Login

```
URL:      http://localhost:3000/login
Email:    director.general@sltda.gov.lk
Password: DG@SLTDA#2026!Director
```

---

## 📁 Project Structure

```
SLTDA-SmartPulse/
│
├── 🐍 backend/                  # FastAPI Server
│   ├── main.py                  # App entry point
│   ├── config.py                # Settings (.env reader)
│   ├── database.py              # PostgreSQL connection
│   ├── routers/                 # API endpoints
│   │   ├── auth.py              # POST /api/auth/login
│   │   ├── arrivals.py          # GET /api/arrivals
│   │   ├── forecast.py          # GET /api/forecast
│   │   ├── sentiment.py         # POST /api/sentiment/analyze
│   │   ├── chatbot.py           # POST /api/chat
│   │   ├── problems.py          # GET/POST /api/problems
│   │   ├── forward_demand.py    # GET /api/demand
│   │   └── economic_impact.py   # GET /api/economic
│   └── services/                # Business Logic
│       ├── ml_service.py        # Prophet + K-Means
│       ├── alert_service.py     # Smart alerts
│       └── multilingual_sentiment.py
│
├── ⚛️ frontend/                  # Next.js 15 Dashboard
│   └── src/
│       ├── app/                 # Pages (App Router)
│       ├── components/          # Reusable UI
│       └── lib/                 # API helpers
│
├── 🗄️ database/                  # DB Files
│   ├── schema.sql               # Table definitions
│   └── seeds/                   # Sample data
│
├── 🔄 etl/                       # Data Pipeline
│   ├── collectors/              # Download scripts
│   ├── processors/              # Data cleaning
│   └── loaders/                 # DB insert
│
├── 🤖 models/                    # ML Model Files
│   ├── prophet/
│   ├── clustering/
│   └── sentiment/
│
├── 🧪 tests/                     # Test Suite
├── 🚀 deployment/                # Docker + Nginx
├── 📚 docs/                      # Documentation
│
├── .env                         # 🔒 Secrets (not in git)
├── .env.example                 # Template for .env
├── .gitignore                   # Git exclusions
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🔌 API Reference

**Base URL:** `http://localhost:8000`
**Auth:** Bearer JWT Token (from login)

| Method | Endpoint | Description | Auth |
|--------|---------|-------------|------|
| POST | `/api/auth/login` | Login → JWT token | ❌ |
| GET | `/api/arrivals` | Tourist arrivals data | ✅ |
| GET | `/api/forecast` | 90-day ML forecast | ✅ |
| POST | `/api/sentiment/analyze` | Analyze review text | ✅ |
| GET | `/api/sentiment/language-breakdown` | By nationality | ✅ |
| POST | `/api/chat` | AI chatbot query | ✅ |
| GET | `/api/problems` | Problem list | ✅ |
| GET | `/api/demand/flight-demand` | Amadeus signals | ✅ |
| GET | `/api/economic/spending-analysis` | Economic impact | ✅ |
| GET | `/api/economic/gdp-contribution` | GDP % trend | ✅ |

> 📚 Full interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📈 ML Models

### Prophet — Demand Forecasting
```python
# 90-day forward forecast
# Trained on: 2010-2024 SLTDA arrival data
# Inputs: historical arrivals by country + month
# Output: predicted arrivals + confidence interval
# Accuracy target: MAPE < 8%
```

### Amadeus Hybrid Model
```python
# 60% Amadeus flight search signal
# 40% Prophet historical pattern
# Horizon: 3-6 months forward
# Advantage: Real human intent data
```

### VADER Multilingual Sentiment
```python
# langdetect → detect language (95%+ accuracy)
# deep-translator → translate to English (free)
# VADER → sentiment score (-1 to +1)
# Languages: EN, RU, ZH, DE, FR, JA, KO, AR, ES, IT, NL, HI
```

### K-Means Tourist Clustering
```python
# Features: spending, LOS, purpose, nationality
# Output: 5 tourist personas
# Beach Luxury | Cultural Explorer | Adventure Seeker
# Budget Backpacker | Business Traveller
```

---

## 💰 Business Model

| Tier | Target | Price | Access |
|------|--------|-------|--------|
| 🆓 Free | SLTDA + Universities | LKR 0 | Full internal platform |
| 🥈 Starter | Tour guides, guesthouses | ~LKR 14,500/mo | National aggregates |
| 🥇 Pro | Hotels, tour operators | ~LKR 43,500/mo | District + forecasts |
| 💎 Enterprise | Cinnamon, Jetwing, airlines | Custom | Full data + AI APIs |

> **Revenue Potential:** 10 Starter + 5 Pro = **LKR 362,500/month** recurring

---

## 🗺️ Roadmap

- [x] Database design (star schema, 13 tables)
- [x] User authentication (bcrypt + JWT + RBAC)
- [x] Project structure setup
- [ ] FastAPI backend — all 8 routers
- [ ] Frontend — login page
- [ ] Dashboard pages 1-5
- [ ] Dashboard pages 6-10
- [ ] Prophet ML integration
- [ ] Multilingual NLP pipeline
- [ ] Amadeus API integration
- [ ] Smart Alert system
- [ ] Docker deployment
- [ ] Vercel + Railway production deploy
- [ ] SLTDA presentation

---

## 👨‍💻 Developer

<div align="center">

**Nelusha Nethmina**

*2nd Year, BSc (Hons) ICT — Business Intelligence*
*Uva Wellassa University of Sri Lanka*
*Faculty of Science and Technology*

[![GitHub](https://img.shields.io/badge/GitHub-NelushaNethmina-181717?style=for-the-badge&logo=github)](https://github.com/NelushaNethmina)
[![University](https://img.shields.io/badge/University-Uva_Wellassa-1B3A6B?style=for-the-badge)](https://www.uwu.ac.lk)

</div>

---

<div align="center">

**Built with ❤️ for Sri Lanka Tourism**

*© 2026 SLTDA SmartPulse — Uva Wellassa University*

⭐ **Star this repo if you find it useful!** ⭐

</div>
