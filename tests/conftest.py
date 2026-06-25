"""
Pytest configuration and shared fixtures.
Mock embeddings and vector stores for testing.
"""

import pytest
from unittest.mock import Mock, MagicMock
from langchain.schema import Document


@pytest.fixture
def mock_embeddings():
    """Mock embedding model for testing."""
    embedder = Mock()
    embedder.embed_query = Mock(return_value=[0.1] * 384)
    embedder.embed_documents = Mock(return_value=[[0.1] * 384] * 3)
    return embedder


@pytest.fixture
def mock_vector_store():
    """Mock vector store for testing."""
    store = Mock()
    store.similarity_search = Mock(return_value=[
        Document(page_content="Test document 1", metadata={"source": "test1.pdf"}),
        Document(page_content="Test document 2", metadata={"source": "test2.pdf"}),
    ])
    store.similarity_search_with_score = Mock(return_value=[
        (Document(page_content="Test document 1", metadata={"source": "test1.pdf"}), 0.95),
        (Document(page_content="Test document 2", metadata={"source": "test2.pdf"}), 0.87),
    ])
    store.add_documents = Mock()
    return store


@pytest.fixture
def sample_documents():
    """Sample documents for testing."""
    return [
        Document(
            page_content="Paragraph 1: This is the first test document.",
            metadata={"source": "test1.pdf", "page": 1}
        ),
        Document(
            page_content="Paragraph 2: This is the second test document.",
            metadata={"source": "test1.pdf", "page": 2}
        ),
        Document(
            page_content="Paragraph 3: This is the third test document.",
            metadata={"source": "test2.pdf", "page": 1}
        ),
    ]


@pytest.fixture
def mock_llm():
    """Mock LLM for testing."""
    llm = Mock()
    llm.invoke = Mock(return_value=Mock(content="This is a test answer based on the documents."))
    return llm
