#!/usr/bin/env python3
"""
Build index script for Winter Garden Legal RAG.

This script:
1. Loads configuration
2. Parses documents from data_path
3. Generates chunks
4. Creates FAISS and BM25 indexes
5. Saves indexes to configured paths
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.loader import load_config
from parsers.pdf_parser import PDFParser
from retrieval.bm25 import BM25Retrieval
from retrieval.faiss_store import FaissRetrieval
from utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Main index building function."""
    logger.info("Starting index build process")
    
    # Load configuration
    try:
        config = load_config()
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        sys.exit(1)
    
    data_path = config.get("data_path", "./data/raw_pdfs/")
    faiss_index_path = config.get("faiss_index_path", "./data/index/faiss/")
    bm25_index_path = config.get("bm25_index_path", "./data/index/bm25/")
    chunk_size = config.get("chunk_size", 500)
    chunk_overlap = config.get("chunk_overlap", 50)
    
    logger.info(f"Configuration loaded: data_path={data_path}")
    
    # Create output directories
    Path(faiss_index_path).mkdir(parents=True, exist_ok=True)
    Path(bm25_index_path).mkdir(parents=True, exist_ok=True)
    
    # Parse documents
    logger.info("Parsing documents...")
    parser = PDFParser(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    
    # TODO: Implement parsing
    # chunks = parser.parse_directory(data_path)
    # logger.info(f"Parsed {len(chunks)} chunks")
    
    # Build FAISS index
    logger.info("Building FAISS index...")
    faiss_retriever = FaissRetrieval(faiss_index_path)
    # TODO: Build and save FAISS index
    # faiss_retriever.build_index(embeddings, chunks, faiss_index_path)
    
    # Build BM25 index
    logger.info("Building BM25 index...")
    bm25_retriever = BM25Retrieval(bm25_index_path)
    # TODO: Build and save BM25 index
    # bm25_retriever.build_index(documents, bm25_index_path)
    
    logger.info("Index build completed successfully")


if __name__ == "__main__":
    main()
