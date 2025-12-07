#!/bin/bash

# Winter Garden Legal RAG - API Startup Script
# Usage: ./run_api.sh [port]

set -e

# Get port from argument or environment variable or default to 8000
PORT=${1:-${PORT:-8000}}

echo "Starting Winter Garden Legal RAG API on port $PORT..."

# Check if uvicorn is installed
if ! command -v uvicorn &> /dev/null; then
    echo "Error: uvicorn not found. Install it with: pip install uvicorn"
    exit 1
fi

# Check if config exists
if [ ! -f "config/config.yaml" ]; then
    echo "Warning: config/config.yaml not found"
fi

# Start API
uvicorn api.routes:app --reload --host 0.0.0.0 --port "$PORT"
