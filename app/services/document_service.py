"""
Document ingestion pipeline service.
Handles: loading → chunking → embedding → vector store insertion
"""

import logging
from typing import List
from pathlib import Path
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import settings

logger = logging.getLogger(__name__)


class DocumentService:
    """Service for document ingestion and processing."""
    
    def __init__(self):
        self.chunk_size = settings.chunk_size
        self.chunk_overlap = settings.chunk_overlap
        self.raw_docs_path = Path(settings.raw_documents_path)
        self.processed_chunks_path = Path(settings.processed_chunks_path)
        
        # Ensure directories exist
        self.raw_docs_path.mkdir(parents=True, exist_ok=True)
        self.processed_chunks_path.mkdir(parents=True, exist_ok=True)
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )
    
    def load_document(self, file_path: str):
        """
        Load a document from file.
        Supports: PDF, TXT, DOCX
        """
        file_path = Path(file_path)
        
        if file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
            return loader.load()
        elif file_path.suffix.lower() == ".txt":
            loader = TextLoader(str(file_path))
            return loader.load()
        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")
    
    def chunk_documents(self, documents):
        """Split documents into chunks."""
        return self.text_splitter.split_documents(documents)
    
    def ingest_pipeline(self, file_path: str):
        """
        Complete ingestion pipeline:
        1. Load document
        2. Chunk into smaller pieces
        3. Embed chunks
        4. Store in vector DB
        """
        try:
            logger.info(f"Starting ingestion pipeline for: {file_path}")
            
            # Load
            documents = self.load_document(file_path)
            logger.info(f"Loaded {len(documents)} documents")
            
            # Chunk
            chunks = self.chunk_documents(documents)
            logger.info(f"Created {len(chunks)} chunks")
            
            # Return chunks for embedding/storage
            return chunks
            
        except Exception as e:
            logger.error(f"Ingestion pipeline failed: {str(e)}")
            raise
