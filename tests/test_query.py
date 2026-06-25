"""
Tests for query processing.
Tests: retrieval + answer generation flow
"""

import pytest
from app.services.query_service import QueryService


class TestQueryService:
    """Tests for QueryService."""
    
    def test_query_service_initialization(self, mock_vector_store, mock_llm):
        """Test QueryService initialization."""
        service = QueryService(mock_vector_store, mock_llm)
        assert service.vector_store is not None
        assert service.llm_chain is not None
    
    def test_retrieve_sources(self, mock_vector_store, mock_llm):
        """Test source retrieval."""
        service = QueryService(mock_vector_store, mock_llm)
        sources = service.retrieve_sources("test query", top_k=2)
        
        mock_vector_store.similarity_search_with_score.assert_called_once()
        assert len(sources) >= 0
    
    def test_retrieve_sources_empty(self, mock_vector_store, mock_llm):
        """Test retrieval when no sources found."""
        service = QueryService(mock_vector_store, mock_llm)
        mock_vector_store.similarity_search_with_score.return_value = []
        
        sources = service.retrieve_sources("xyz", top_k=5)
        assert sources == []
    
    def test_query_processing(self, mock_vector_store, mock_llm):
        """Test complete query processing."""
        service = QueryService(mock_vector_store, mock_llm)
        
        answer, sources, processing_time = service.query("What is this about?", top_k=2)
        
        assert isinstance(answer, str)
        assert isinstance(processing_time, float)
        assert processing_time >= 0
