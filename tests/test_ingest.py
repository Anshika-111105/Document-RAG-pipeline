"""
Tests for document ingestion pipeline.
Tests: load → chunk → embed flow
"""

import pytest
from app.services.document_service import DocumentService


class TestDocumentService:
    """Tests for DocumentService."""
    
    def test_initialization(self):
        """Test DocumentService initialization."""
        service = DocumentService()
        assert service.chunk_size > 0
        assert service.chunk_overlap >= 0
        assert service.raw_docs_path.exists()
        assert service.processed_chunks_path.exists()
    
    def test_chunk_documents(self, sample_documents):
        """Test document chunking."""
        service = DocumentService()
        chunks = service.chunk_documents(sample_documents)
        
        assert len(chunks) > 0
        assert all(hasattr(chunk, 'page_content') for chunk in chunks)
    
    def test_ingest_pipeline_with_mock(self, tmp_path, monkeypatch):
        """Test ingestion pipeline with mocked file loading."""
        service = DocumentService()
        
        # Mock the load_document method
        mock_documents = [
            {"page_content": "Test content 1", "metadata": {}},
            {"page_content": "Test content 2", "metadata": {}},
        ]
        monkeypatch.setattr(
            service,
            "load_document",
            lambda x: mock_documents
        )
        
        # Run pipeline
        chunks = service.ingest_pipeline("test.pdf")
        assert isinstance(chunks, list)
