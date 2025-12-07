Winter Garden Legal RAG Backend (MVP Architecture)

A modular, architecture-first backend for a Legal Retrieval-Augmented Generation (RAG) system built over the City of Winter Garden, FL legal code.
This MVP focuses on clean structure, correct layering, and production-style design, providing a clear blueprint for how a full legal RAG backend is engineered.

It is intentionally implementation-light: components exist as functional scaffolds (API, logging, configuration, module boundaries), ready for incremental extension into a fully operational RAG pipeline.

1. Overview

This backend defines a complete architectural skeleton for a legal RAG system:

A FastAPI service exposing /query, /index, and /health

A modular retrieval subsystem (BM25, FAISS, Hybrid)

Parsing layer for PDFs and HTML

LLM client wrapper with multi-provider structure

Grounding and citation validation stubs

Structured JSON logging with request tracing

External configuration via YAML

Operational scripts for index building and data processing

Basic API contract tests

The project highlights engineering discipline: separation of concerns, type-safe interfaces, predictable module boundaries, and reproducible operational workflows.

2. Current Capabilities

This MVP ships with the operational surface and architectural layout of a real RAG service.
Today it provides:

API

/health — reports service status

/query — accepts a natural language query, returns structured stub response

/index — triggers index rebuild workflow

Automatic request IDs via header or UUID

Measured latency per request

Logging

JSON-formatted logs

Structured fields: timestamp, level, message, request_id, latency, query

Single shared logger across modules

Configuration

Central YAML configuration (config/config.yaml)

Paths, models, retrieval parameters, and API settings

Safe loading and error handling

Execution Scripts

build_index.py — orchestrates ingestion and index initialization

reprocess_data.py — resets processed directory and prepares inputs

run_api.sh — launches the service with optional port configuration

Testing

FastAPI TestClient tests for endpoint correctness and request ID handling

Establishes the contract for future integration tests

3. Architectural Intent

This MVP serves as a blueprint for a full legal RAG system.
All layers are defined, isolated, and extensible:

Retrieval Layer

Files:

bm25.py

faiss_store.py

hybrid.py

Interfaces and class structures are complete.
Future work fills in BM25 ranking, vector embeddings, FAISS index building, and hybrid fusion.

Parsing Layer

Files:

pdf_parser.py

html_parser.py

Signatures, configuration parameters, and directory-level traversal are defined.
Extraction and chunking logic remains to be implemented.

LLM Layer

File: llm/client.py

Includes:

Provider enum

Unified API

Stubs for answer and citation generation

Designed to support OpenAI, Anthropic, and local models.

Validation Layer

File: validators/grounding.py

Defines:

Answer grounding interface

Citation validation hook

Ready for factuality checks once retrieval and LLM integration are in place.

4. Project Structure
.
├── api/                  # FastAPI routes and request models
├── config/               # YAML config + loader
├── data/                 # Raw PDFs, processed chunks, index placeholders
├── llm/                  # LLM client scaffolding
├── parsers/              # PDF / HTML parsing skeletons
├── retrieval/            # BM25, FAISS, Hybrid retrieval interfaces
├── scripts/              # Index build + data processing orchestration
├── tests/                # API contract tests
├── utils/                # Structured JSON logging
├── validators/           # Grounding and citation validation stubs
└── run_api.sh            # Service startup script


This layout mirrors production RAG systems where each subsystem evolves independently.

5. Installation

Python 3.10+

pip install -r requirements.txt

6. Running the API
Using the startup script:
./run_api.sh 8000

Or with Uvicorn directly:
uvicorn api.routes:app --reload --host 0.0.0.0 --port 8000

7. Reprocessing and Index Building
Reprocess documents:
python scripts/reprocess_data.py

Initialize index directory and pipeline:
python scripts/build_index.py


Both scripts run end-to-end and load configuration/logging correctly, preparing the operational environment for future embedding + indexing logic.

8. Current Status (MVP Scope)

This project is in Phase 1: Architectural Scaffolding.

Operational boundaries, interfaces, folders, scripts, and execution paths are complete.
The following subsystems intentionally use stub implementations:

Retrieval (retrieve() returns empty lists)

Parsers (no PDF/HTML extraction yet)

LLM generation (placeholder strings)

Grounding validation (always passes)

Index building (no embeddings or FAISS index written yet)

This approach makes the system safe to share publicly, while clearly showcasing the engineering structure of a real RAG backend.

9. Roadmap

Next steps for completing a production-grade system:

Document ingestion

Extract PDF text

Parse HTML

Implement chunking with overlap

Retrieval

Generate embeddings

Build FAISS index

Implement BM25 ranking

Add hybrid fusion (RRF, weighted sum)

LLM integration

Connect LLMClient to OpenAI/Anthropic

Build RAG prompt templates

Generate answers with citations

Validation

Grounding checks

Citation verification

Confidence scoring

Testing and Observability

Integration tests

Stress tests

Telemetry and monitoring hooks

10. License

MIT License
