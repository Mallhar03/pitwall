# PitWall

PitWall is a production-style Formula 1 race-data backend that ingests timing and telemetry-derived data from verified public sources, stores it reliably in PostgreSQL, serves it via a secured FastAPI REST API, replays races over WebSockets/event streams, and serves baseline tyre degradation models.

## Project Structure

```
pitwall/
├── PROJECT_GUIDE.md        # The stable rulebook and engineering guide
├── PROJECT_STATE.md        # The live status, decisions, and task tracker
├── README.md               # Setup and development guide
├── pyproject.toml          # Project metadata and tool configuration
├── .env.example            # Environment variables template
├── docs/                   # Documentation, data source research, glossary, design notes
├── spikes/                 # Exploratory spike scripts (P0.3 source evaluations)
├── src/pitwall/            # Core application source code
└── tests/                  # Unit and integration test suite
```

## Quickstart & Environment Setup

### 1. Prerequisites
- Python 3.11+
- Git

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install in Editable Mode with Dev Dependencies
```bash
pip install -e ".[dev]"
```

### 4. Run Smoke Tests
```bash
pytest
```
