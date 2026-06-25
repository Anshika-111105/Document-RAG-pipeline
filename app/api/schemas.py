"""
Pydantic models for API request/response validation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class UploadDocumentRequest(BaseModel):
    """Request model for document upload."""
    filename: str = Field(..., description="Name of the document file")


class DocumentMetadata(BaseModel):
    """Metadata for a document."""
    doc_id: str
    filename: str
    page_count: Optional[int] = None
    upload_date: str


class QueryRequest(BaseModel):
    """Request model for querying documents."""
    query: str = Field(..., min_length=1, description="Query text")
    top_k: int = Field(default=5, ge=1, le=20, description="Number of sources to retrieve")


class SourceDocument(BaseModel):
    """Source document reference in answer."""
    filename: str
    page: Optional[int] = None
    content: str
    score: float = Field(..., ge=0.0, le=1.0, description="Relevance score")


class QueryResponse(BaseModel):
    """Response model for query results."""
    query: str
    answer: str
    sources: List[SourceDocument]
    processing_time_ms: float


class DocumentsListResponse(BaseModel):
    """Response model for listing documents."""
    documents: List[DocumentMetadata]
    total_count: int


class HealthResponse(BaseModel):
    """Response model for health check."""
    status: str
    version: str
    vector_store_ready: bool
