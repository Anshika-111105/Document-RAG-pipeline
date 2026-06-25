"""
Vector store adapters for FAISS and Chroma.
Factory pattern for abstraction.
"""

import logging
from typing import List, Literal
from pathlib import Path
from app.config import settings

logger = logging.getLogger(__name__)


class FAISSAdapter:
    """FAISS vector store adapter."""
    
    def __init__(self, embeddings, index_path: str = None):
        """
        Initialize FAISS adapter.
        
        Args:
            embeddings: Embedding model instance
            index_path: Path to FAISS index
        """
        self.embeddings = embeddings
        self.index_path = index_path or settings.vector_db_path
        Path(self.index_path).mkdir(parents=True, exist_ok=True)
        self.vectorstore = None
        self._load_or_create_index()
    
    def _load_or_create_index(self):
        """Load existing index or create new one."""
        try:
            from langchain.vectorstores import FAISS
            index_file = Path(self.index_path) / "index.faiss"
            
            if index_file.exists():
                self.vectorstore = FAISS.load_local(
                    self.index_path,
                    self.embeddings,
                    allow_dangerous_deserialization=True
                )
                logger.info("Loaded existing FAISS index")
            else:
                logger.info("Creating new FAISS index")
                # Will be created on first add_documents call
                
        except Exception as e:
            logger.error(f"FAISS initialization failed: {str(e)}")
            raise
    
    def add_documents(self, documents):
        """Add documents to FAISS index."""
        try:
            from langchain.vectorstores import FAISS
            if self.vectorstore is None:
                self.vectorstore = FAISS.from_documents(
                    documents,
                    self.embeddings
                )
            else:
                self.vectorstore.add_documents(documents)
            
            self.vectorstore.save_local(self.index_path)
            logger.info(f"Added {len(documents)} documents to FAISS")
        except Exception as e:
            logger.error(f"Failed to add documents: {str(e)}")
            raise
    
    def similarity_search(self, query: str, k: int = 5):
        """Search for similar documents."""
        if self.vectorstore is None:
            return []
        return self.vectorstore.similarity_search(query, k=k)
    
    def similarity_search_with_score(self, query: str, k: int = 5):
        """Search with relevance scores."""
        if self.vectorstore is None:
            return []
        return self.vectorstore.similarity_search_with_score(query, k=k)


class ChromaAdapter:
    """Chroma vector store adapter."""
    
    def __init__(self, embeddings, collection_name: str = "documents"):
        """
        Initialize Chroma adapter.
        
        Args:
            embeddings: Embedding model instance
            collection_name: Chroma collection name
        """
        self.embeddings = embeddings
        self.collection_name = collection_name
        self.vectorstore = None
        self._initialize()
    
    def _initialize(self):
        """Initialize Chroma vector store."""
        try:
            from langchain.vectorstores import Chroma
            self.vectorstore = Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embeddings,
                persist_directory="./vector_db/chroma"
            )
            logger.info("Initialized Chroma vector store")
        except Exception as e:
            logger.error(f"Chroma initialization failed: {str(e)}")
            raise
    
    def add_documents(self, documents):
        """Add documents to Chroma."""
        try:
            self.vectorstore.add_documents(documents)
            logger.info(f"Added {len(documents)} documents to Chroma")
        except Exception as e:
            logger.error(f"Failed to add documents: {str(e)}")
            raise
    
    def similarity_search(self, query: str, k: int = 5):
        """Search for similar documents."""
        return self.vectorstore.similarity_search(query, k=k)
    
    def similarity_search_with_score(self, query: str, k: int = 5):
        """Search with relevance scores."""
        return self.vectorstore.similarity_search_with_score(query, k=k)


class VectorStoreFactory:
    """Factory for creating vector stores."""
    
    @staticmethod
    def create(
        embeddings,
        store_type: Literal["faiss", "chroma"] = None,
        **kwargs
    ):
        """
        Create a vector store.
        
        Args:
            embeddings: Embedding model
            store_type: Vector store type ("faiss" or "chroma")
            **kwargs: Store-specific arguments
            
        Returns:
            Vector store instance
        """
        store_type = store_type or settings.vector_store_type
        
        try:
            if store_type == "faiss":
                return FAISSAdapter(embeddings, **kwargs)
            elif store_type == "chroma":
                return ChromaAdapter(embeddings, **kwargs)
            else:
                raise ValueError(f"Unknown vector store type: {store_type}")
        except Exception as e:
            logger.error(f"Failed to create vector store: {str(e)}")
            raise
