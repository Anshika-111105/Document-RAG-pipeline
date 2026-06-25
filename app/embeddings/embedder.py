"""
Embeddings factory and wrapper.
Supports: OpenAI, HuggingFace embeddings
"""

import logging
from typing import List, Literal
from app.config import settings

logger = logging.getLogger(__name__)


class EmbeddingFactory:
    """Factory for creating embedding models."""
    
    @staticmethod
    def create(provider: Literal["openai", "huggingface"] = None, **kwargs):
        """
        Create an embedding model.
        
        Args:
            provider: Embedding provider ("openai" or "huggingface")
            **kwargs: Provider-specific arguments
            
        Returns:
            Embedding model instance
        """
        provider = provider or settings.embedding_provider
        
        try:
            if provider == "openai":
                from langchain.embeddings import OpenAIEmbeddings
                return OpenAIEmbeddings(
                    api_key=settings.openai_api_key,
                    model=settings.embedding_model,
                    **kwargs
                )
            
            elif provider == "huggingface":
                from langchain.embeddings import HuggingFaceEmbeddings
                return HuggingFaceEmbeddings(
                    model_name=settings.embedding_model,
                    **kwargs
                )
            
            else:
                raise ValueError(f"Unknown embedding provider: {provider}")
        
        except Exception as e:
            logger.error(f"Failed to create embedder: {str(e)}")
            raise


class Embedder:
    """Thin wrapper around embedding models."""
    
    def __init__(self, model=None):
        """Initialize embedder."""
        self.model = model or EmbeddingFactory.create()
    
    def embed_text(self, text: str) -> List[float]:
        """
        Embed a single text string.
        
        Args:
            text: Text to embed
            
        Returns:
            Embedding vector
        """
        return self.model.embed_query(text)
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Embed multiple texts.
        
        Args:
            texts: List of texts to embed
            
        Returns:
            List of embedding vectors
        """
        return self.model.embed_documents(texts)
