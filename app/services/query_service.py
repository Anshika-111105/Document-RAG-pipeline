"""
Query service for retrieving answers from documents.
Orchestrates: retrieval → LLM chain → source citation
"""

import logging
from typing import List, Dict, Tuple
import time

logger = logging.getLogger(__name__)


class QueryService:
    """Service for document querying and answer generation."""
    
    def __init__(self, vector_store, llm_chain):
        """
        Initialize query service.
        
        Args:
            vector_store: Vector store adapter (FAISS/Chroma)
            llm_chain: LLM RetrievalQA chain
        """
        self.vector_store = vector_store
        self.llm_chain = llm_chain
    
    def retrieve_sources(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Retrieve relevant documents from vector store.
        
        Args:
            query: User query
            top_k: Number of sources to retrieve
            
        Returns:
            List of source documents with scores
        """
        try:
            results = self.vector_store.similarity_search_with_score(query, k=top_k)
            sources = []
            for doc, score in results:
                sources.append({
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                    "score": score,
                })
            return sources
        except Exception as e:
            logger.error(f"Retrieval failed: {str(e)}")
            return []
    
    def generate_answer(self, query: str, sources: List[Dict]) -> str:
        """
        Generate answer using LLM chain with retrieved sources.
        
        Args:
            query: User query
            sources: Retrieved source documents
            
        Returns:
            Generated answer with source citations
        """
        try:
            answer = self.llm_chain.run(
                input_documents=sources,
                question=query,
            )
            return answer
        except Exception as e:
            logger.error(f"Answer generation failed: {str(e)}")
            return "Could not generate answer."
    
    def query(self, query: str, top_k: int = 5) -> Tuple[str, List[Dict], float]:
        """
        Process a query: retrieve → generate → return answer + sources.
        
        Args:
            query: User query
            top_k: Number of sources to retrieve
            
        Returns:
            Tuple of (answer, sources, processing_time_ms)
        """
        start_time = time.time()
        
        try:
            # Retrieve sources
            sources = self.retrieve_sources(query, top_k)
            
            # Generate answer
            if sources:
                answer = self.generate_answer(query, sources)
            else:
                answer = "No relevant documents found."
            
            processing_time_ms = (time.time() - start_time) * 1000
            
            return answer, sources, processing_time_ms
            
        except Exception as e:
            logger.error(f"Query processing failed: {str(e)}")
            processing_time_ms = (time.time() - start_time) * 1000
            return "Error processing query.", [], processing_time_ms
