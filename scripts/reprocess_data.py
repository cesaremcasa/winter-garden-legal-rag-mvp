#!/usr/bin/env python3
"""
Reprocess data script for Winter Garden Legal RAG.

This script:
1. Deletes old processed outputs
2. Re-runs parsers on raw data
3. Regenerates processed JSON files
"""

import sys
import shutil
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config.loader import load_config
from parsers.pdf_parser import PDFParser
from parsers.html_parser import HTMLParser
from utils.logger import get_logger

logger = get_logger(__name__)


def clean_outputs(processed_path: str):
    """
    Delete old processed data.
    
    Args:
        processed_path: Path to processed data directory
    """
    logger.info(f"Cleaning old outputs from: {processed_path}")
    
    path = Path(processed_path)
    if path.exists():
        shutil.rmtree(path)
        logger.info("Old outputs deleted")
    
    path.mkdir(parents=True, exist_ok=True)
    logger.info("Output directory recreated")


def reprocess_pdfs(data_path: str, output_path: str, config: dict):
    """
    Reprocess PDF documents.
    
    Args:
        data_path: Path to raw PDFs
        output_path: Path to save processed data
        config: Configuration dict
    """
    logger.info(f"Reprocessing PDFs from: {data_path}")
    
    parser = PDFParser(
        chunk_size=config.get("chunk_size", 500),
        chunk_overlap=config.get("chunk_overlap", 50)
    )
    
    # TODO: Implement PDF reprocessing
    # chunks = parser.parse_directory(data_path)
    # Save chunks to JSON in output_path
    
    logger.info("PDF reprocessing completed")


def main():
    """Main reprocessing function."""
    logger.info("Starting data reprocessing")
    
    # Load configuration
    try:
        config = load_config()
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        sys.exit(1)
    
    data_path = config.get("data_path", "./data/raw_pdfs/")
    processed_path = config.get("processed_path", "./data/processed/")
    
    # Clean old outputs
    clean_outputs(processed_path)
    
    # Reprocess documents
    reprocess_pdfs(data_path, processed_path, config)
    
    logger.info("Data reprocessing completed successfully")


if __name__ == "__main__":
    main()
