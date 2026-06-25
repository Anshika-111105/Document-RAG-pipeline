"""
RetrievalQA chain for generating answers with source citations.
Integrates: retriever + LLM + source tracking
"""

import logging
from typing import List
from app.config import settings

logger = logging.getLogger(__name__)


class RetrievalQAChain:
    """RetrievalQA chain for document question answering."""
    
    def __init__(self, llm, retriever, prompt_template: str = None):
        """
        Initialize RetrievalQA chain.
        
        Args:
            llm: Language model instance
            retriever: Vector store retriever
            prompt_template: Custom prompt template (optional)
        """
        self.llm = llm
        self.retriever = retriever
        self.prompt_template = prompt_template or self._default_prompt()
    
    def _default_prompt(self) -> str:
        """Default prompt template for QA."""
        return """
You are a helpful assistant answering questions based on provided documents.
Answer the question based on the context below. Include specific references to the source documents.

Context:
{context}

Question: {question}

Answer:"""
    
    def run(self, question: str, input_documents: List = None, **kwargs) -> str:
        """
        Run the QA chain.
        
        Args:
            question: User question
            input_documents: Retrieved documents for context
            **kwargs: Additional arguments
            
        Returns:
            Generated answer with source citations
        """
        try:
            # Prepare context from documents
            context = self._prepare_context(input_documents)
            
            # Format prompt
            prompt = self.prompt_template.format(
                context=context,
                question=question
            )
            
            # Generate answer
            answer = self.llm.invoke(prompt)
            
            return answer.content if hasattr(answer, 'content') else str(answer)
            
        except Exception as e:
            logger.error(f"Chain execution failed: {str(e)}")
            raise
    
    def _prepare_context(self, documents: List) -> str:
        """Prepare context string from documents."""
        if not documents:
            return "No documents available."
        
        context_parts = []
        for i, doc in enumerate(documents, 1):
            if isinstance(doc, dict):
                content = doc.get("content", str(doc))
                metadata = doc.get("metadata", {})
                filename = metadata.get("source", "Unknown")
                context_parts.append(f"[{i}] (from {filename}):\n{content}")
            else:
                context_parts.append(f"[{i}]:\n{doc.page_content}")
        
        return "\n\n".join(context_parts)


class LLMFactory:
    """Factory for creating LLM instances."""
    
    @staticmethod
    def create(provider: str = None, **kwargs):
        """
        Create an LLM instance.
        
        Args:
            provider: LLM provider ("openai", "huggingface", etc.)
            **kwargs: Provider-specific arguments
            
        Returns:
            LLM instance
        """
        provider = provider or settings.llm_provider
        
        try:
            if provider == "openai":
                from langchain.llms import OpenAI
                return OpenAI(
                    api_key=settings.openai_api_key,
                    model_name=settings.openai_model,
                    **kwargs
                )
            
            elif provider == "huggingface":
                from langchain.llms import HuggingFaceHub
                return HuggingFaceHub(**kwargs)
            
            else:
                raise ValueError(f"Unknown LLM provider: {provider}")
        
        except Exception as e:
            logger.error(f"Failed to create LLM: {str(e)}")
            raise
