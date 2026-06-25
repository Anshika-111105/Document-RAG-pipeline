"""
Configuration module using Pydantic Settings.
Loads environment variables from .env file.
"""

from pydantic_settings import BaseSettings
from typing import Optional, Literal


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Configuration
    api_title: str = "Document RAG Pipeline"
    api_version: str = "0.1.0"
    debug: bool = False
    
    # LLM Configuration
    llm_provider: Literal["openai", "huggingface"] = "openai"
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-3.5-turbo"
    
    # Embedding Configuration
    embedding_provider: Literal["openai", "huggingface"] = "openai"
    embedding_model: str = "text-embedding-3-small"
    
    # Vector Store Configuration
    vector_store_type: Literal["faiss", "chroma"] = "faiss"
    vector_db_path: str = "./vector_db"
    
    # Document Processing
    chunk_size: int = 1000
    chunk_overlap: int = 200
    
    # Data paths
    raw_documents_path: str = "./data/raw_documents"
    processed_chunks_path: str = "./data/processed_chunks"
    
    # Database
    postgres_url: Optional[str] = None
    redis_url: Optional[str] = "redis://localhost:6379"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Singleton instance
settings = Settings()
