from typing import List, Dict, Any

from utils.logger import get_logger

logger = get_logger(__name__)


class HTMLParser:
    """
    HTML document parser.
    
    TODO: Implement HTML parsing with BeautifulSoup.
    """
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initialize HTML parser.
        
        Args:
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        logger.info(f"HTMLParser initialized (chunk_size={chunk_size})")
    
    def parse(self, html_path: str) -> List[Dict[str, Any]]:
        """
        Parse HTML into chunks with metadata.
        
        Args:
            html_path: Path to HTML file
        
        Returns:
            List of chunks with metadata
        
        TODO: Implement HTML parsing and chunking.
        """
        logger.info(f"Parsing HTML: {html_path}")
        
        # TODO: Extract text from HTML
        # TODO: Split into chunks
        # TODO: Add metadata
        
        return []
