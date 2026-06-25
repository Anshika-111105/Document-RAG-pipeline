# Document RAG Pipeline

A production-ready Retrieval-Augmented Generation (RAG) pipeline for document ingestion, semantic search, and LLM-powered question answering.

## Features

- **📄 Multi-format Document Support**: PDF, TXT, DOCX ingestion
- **🔍 Semantic Search**: FAISS/Chroma vector stores with OpenAI/HuggingFace embeddings
- **🤖 LLM Integration**: GPT-3.5, GPT-4, and open-source model support
- **🚀 FastAPI Backend**: Async, scalable REST API
- **⚛️ React Frontend**: Modern UI with Vite
- **🐳 Docker**: Full containerization with Postgres + Redis
- **✅ Production Ready**: Testing, CI/CD, logging, error handling

## Project Structure

```
app/
├── config.py                 # Settings from .env
├── api/
│   ├── routes.py            # FastAPI endpoints
│   └── schemas.py           # Pydantic models
├── services/
│   ├── document_service.py  # Ingestion pipeline
│   └── query_service.py     # Query orchestration
├── embeddings/
│   └── embedder.py          # Embedding factory
├── vector_store/
│   └── store.py             # FAISS/Chroma adapters
└── llm/
    └── chain.py             # RetrievalQA chain

data/
├── raw_documents/           # Uploaded files
└── processed_chunks/        # Chunk exports

vector_db/                   # FAISS indexes

frontend/
├── src/
│   ├── App.jsx
│   ├── components/          # React components
│   └── api/
│       └── client.js        # Axios client
└── package.json

tests/
├── conftest.py              # Pytest fixtures
├── test_ingest.py
└── test_query.py

.github/workflows/
└── ci.yml                   # GitHub Actions
```

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- OpenAI API key (or HuggingFace token)

### Installation

1. **Clone & Setup**
   ```bash
   cd document-rag-pipeline
   
   # Python backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirement.txt
   
   # Frontend
   cd frontend
   npm install
   cd ..
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and settings
   ```

3. **Run Services**

   **Option A: Docker Compose (Recommended)**
   ```bash
   docker-compose up -d
   ```

   **Option B: Local Development**
   ```bash
   # Terminal 1: Backend
   python -m uvicorn main:app --reload --port 8000
   
   # Terminal 2: Frontend
   cd frontend
   npm run dev
   ```

4. **Access**
   - API: http://localhost:8000/docs (Swagger UI)
   - Frontend: http://localhost:3000
   - Health: http://localhost:8000/api/health

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/upload` | POST | Upload document |
| `/api/query` | POST | Query documents |
| `/api/documents` | GET | List documents |
| `/api/documents/{id}` | DELETE | Delete document |

### Example Requests

**Upload Document**
```bash
curl -X POST "http://localhost:8000/api/upload" \
  -F "file=@document.pdf"
```

**Query Documents**
```bash
curl -X POST "http://localhost:8000/api/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the main topic?", "top_k": 5}'
```

## Testing

```bash
# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=app --cov-report=html
```

## Configuration

Edit `.env` to customize:
- LLM provider (OpenAI, HuggingFace)
- Vector store (FAISS, Chroma)
- Chunk size & overlap
- Database URLs
- API settings

## Development

- **Linting**: `ruff check app tests main.py --fix`
- **Code Format**: `black app tests main.py`
- **Type Check**: `mypy app --ignore-missing-imports`

## Deployment

### Docker
```bash
docker-compose -f docker-compose.yml up -d
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

### Cloud
- **AWS**: Deploy to ECS/Lambda
- **GCP**: Use Cloud Run + Vertex AI
- **Azure**: App Service + Cognitive Search

## Performance Tips

- Use `FAISS` for large-scale (100k+ embeddings)
- Use `Chroma` for smaller datasets with metadata filtering
- Set `CHUNK_SIZE` to 1000-2000 tokens
- Use `text-embedding-3-small` for cost efficiency
- Enable Redis caching for frequent queries

## Troubleshooting

**Vector store not found**
- Initialize: `python -c "from app.vector_store.store import VectorStoreFactory; ..."`

**API returns 500**
- Check logs: `docker-compose logs backend`
- Verify .env variables

**Slow queries**
- Increase `top_k` retrieval in config
- Check vector store size
- Monitor database connections

## Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -am 'Add feature'`
4. Push: `git push origin feature/my-feature`
5. Open Pull Request

## License

MIT

## Support

- 📧 Email: support@example.com
- 💬 Issues: GitHub Issues
- 📚 Docs: [Full Documentation](https://docs.example.com)

## Roadmap

- [ ] Multi-language support
- [ ] Fine-tuned embedding models
- [ ] GraphRAG integration
- [ ] Agent-based querying
- [ ] Advanced analytics dashboard
- [ ] API authentication (OAuth2)
- [ ] Rate limiting & quotas
