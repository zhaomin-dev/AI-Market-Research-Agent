# AI Market Research Agent (MVP - Stage A)

## 📌 Project Overview

This project is a **modular AI Agent system** designed to automate market research workflows.
It collects data from multiple sources, processes it, and outputs structured insights.

> Current Stage: **Stage A – MVP (Data Aggregation Agent)**
> Goal: Build a minimal working agent with input → data fetching → processing → output pipeline.

---

## 🎯 Objectives (Stage A)

* Build a minimal Agent pipeline (Input → Action → Brain → Output)
* Fetch data from multiple sources (API / mock data)
* Perform basic data processing and structuring
* Output JSON results + simple summary
* Ensure the system runs with **0 cost (mock-first design)**

---

## 🧠 System Architecture

```
User Input → Action (Data Fetching) → Brain (Processing) → Output (Report)
```

### Modules:

* **Input**: CLI input handling
* **Action**: Data fetching (API / mock)
* **Brain**: Data processing & simple logic
* **Output**: Structured report generation

---

## 📂 Project Structure

```
ai-market-research-agent/
├── input/
├── action/
├── brain/
├── output/
├── data/
├── outputs/
├── logs/
├── run.py
├── config.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python 3.12.10
* requests / aiohttp (API calls)
* python-dotenv (config management)

---

## 🚀 How to Run (MVP)

```bash
# 1. Clone repo
git clone <https://github.com/zhaomin-dev/AI-Market-Research-Agent.git>

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env

# 5. Run
python run.py
```

---

## 🔧 Configuration

This project uses `.env` for configuration:

* `USE_MOCK_DATA=true` → Run without real APIs
* `USE_LLM=false` → Disable LLM (Stage A)

---

## 📊 Current Status

* [x] Project initialization
* [x] Modular structure setup
* [x] Config & environment setup
* [ ] Input module
* [ ] API integration
* [ ] Data processing
* [ ] Output generation

---

## 🧩 Future Plans

### Stage B

* Multi-API integration (real data)
* LLM-based summarization
* Structured report generation

### Stage C

* Automation pipeline
* Scheduling & workflow
* Advanced analysis & decision support

---

## 💡 Design Philosophy

* **Mock-first development** (0 cost, fast iteration)
* **Modular architecture** (scalable & maintainable)
* **Incremental development** (build → test → extend)

---

## 👤 Author

* Independent AI Agent Developer
* Focus: AI Automation / Agent Systems / Market Intelligence
