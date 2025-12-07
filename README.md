# Winter Garden Legal RAG Backend (MVP Architecture)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Status](https://img.shields.io/badge/Status-MVP-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A modular, architecture-first backend for a **Legal Retrieval-Augmented Generation (RAG)** system built on the *City of Winter Garden, Florida* legal code.

This MVP focuses on **correct engineering structure**, **clean subsystem boundaries**, and **production-style organization**, serving as a blueprint for how a real legal RAG backend is built.  
It is intentionally implementation-light so the architecture can be evaluated safely and clearly.

---

## 1. Overview

The system defines all essential layers required in a modern RAG backend:

- FastAPI service (`/query`, `/index`, `/health`)
- Modular retrieval subsystem (BM25, FAISS, Hybrid)
- Parsing layer for PDFs and HTML
- Configurable LLM client wrapper
- Grounding & citation validation stubs
- Structured JSON logging with request tracing
- Centralized YAML configuration
- Operational scripts for indexing & data processing
- API contract tests (using FastAPI TestClient)

This project demonstrates **engineering discipline**, not raw capability:
clean separation of concerns, explicit interfaces, reproducible scripts, and an extendable design.

---

## 2. Current Capabilities (MVP Scope)

### API
- `/health` — returns service status  
- `/query` — accepts natural language queries, returns structured placeholder answers  
- `/index` — scaffolding for index rebuild workflows  
- Automatic request ID propagation  
- Per-request latency tracking  

### Logging
- Shared JSON structured logger  
- Fields: `timestamp`, `level`, `message`, `request_id`, `latency`, `query`  

### Configuration
- Central `config/config.yaml`  
- Defines paths, models, retrieval parameters, and API settings  
- Error-safe loading (`loader.py`)  

### Scripts
- `scripts/build_index.py` — orchestrates ingestion + future embedding/index building  
- `scripts/reprocess_data.py` — resets processed directory  

### Tests
- API contract tests ensuring:
  - Endpoint stability  
  - Header propagation  
  - Response structure  

---

## 3. Architectural Intent

This MVP establishes the **blueprint** for a full legal RAG pipeline.  
All subsystems exist in their production form — only logic is missing, by design.

### Retrieval Layer (`retrieval/`)
- `bm25.py`, `faiss_store.py`, `hybrid.py`  
- Interfaces defined  
- Methods stubbed for future:
  - Sparse BM25 retrieval  
  - Dense FAISS vector search  
  - Hybrid ranking/fusion strategies  

### Parsing Layer (`parsers/`)
- `pdf_parser.py`, `html_parser.py`  
- Directory traversal + signatures defined  
- Extraction & chunking are TODO  

### LLM Layer (`llm/client.py`)
- Provider enum (OpenAI, Anthropic, local models)  
- Unified LLM interface  
- Stubbed answer + citation generation  

### Validation Layer (`validators/grounding.py`)
- Grounding interface  
- Citation check hook  

Ready for RAG hallucination prevention once retrieval + LLM integration exist.

---

## 4. Project Structure

```
├── api/                  # FastAPI routes and request models
├── config/               # YAML config + loader
├── data/                 # Raw PDFs, processed chunks, index placeholders
├── llm/                  # LLM client scaffolding
├── parsers/              # PDF / HTML parsing skeletons
├── retrieval/            # BM25, FAISS, Hybrid retrieval scaffolding
├── scripts/              # Index build + data processing orchestration
├── tests/                # API contract tests
├── utils/                # JSON structured logging
├── validators/           # Grounding / citation validation stubs
└── run_api.sh            # Startup script
```

This mirrors real production RAG services where each subsystem evolves independently.

---

## 5. Installation

Requires **Python 3.10+**.

```bash
pip install -r requirements.txt
```

---

## 6. Running the API

### Using the startup script
```bash
./run_api.sh 8000
```

### Using Uvicorn directly
```bash
uvicorn api.routes:app --reload --host 0.0.0.0 --port 8000
```

---

## 7. Reprocessing and Index Building

### Reset processed data
```bash
python scripts/reprocess_data.py
```

### Initialize index structure
```bash
python scripts/build_index.py
```

Both scripts validate configuration & logging pipelines and set up the environment for future
embedding + retrieval logic.

---

## 8. Current Status (MVP Reality)

This repository is in **Phase 1 — Architectural Scaffolding**.

Functional components intentionally remain unimplemented:

| Subsystem        | Current Behavior |
|------------------|------------------|
| Retrieval        | Returns empty lists |
| Parsers          | No PDF/HTML extraction |
| LLM generation   | Returns placeholder strings |
| Grounding        | Always passes |
| Index building   | No embeddings or FAISS index |

This design ensures the project is safe for public portfolio use while highlighting real engineering practices.

---

## 9. Roadmap (Production Path)

### Document ingestion
- Extract text from PDFs (pdfplumber / PyPDF2)
- Parse HTML (BeautifulSoup)
- Implement chunking (size + overlap)

### Retrieval
- Generate embeddings (sentence-transformers)
- Build FAISS index
- Implement BM25
- Hybrid fusion (RRF, weighted sum)

### LLM Integration
- Connect to OpenAI/Anthropic
- Build RAG prompts
- Generate answers w/ citations

### Validation
- Citation verification  
- Hallucination detection  
- Confidence scoring  

### Observability + Testing
- Metrics  
- Tracing  
- Integration tests  
- Stress tests  

---

## 10. License

MIT License
