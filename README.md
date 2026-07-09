# 📄 Document RAG Pipeline

A **Retrieval-Augmented Generation (RAG)** pipeline for querying documents using natural language. Instead of relying purely on an LLM's parametric knowledge, the system will retrieve relevant chunks from a vector database and inject them into the prompt to produce grounded, context-aware answers — reducing hallucinations and enabling Q&A over private/custom document collections.

> **Status: 🚧 Early development.** The ingestion step (PDF loading) and the vector database service are in place. Chunking, embedding, retrieval, and LLM-based answer generation are in progress — see [Roadmap](#roadmap) below.

---

## Current Functionality

Right now the pipeline can:

- Load a PDF document (`PEFT.pdf`) using LangChain's `PyPDFLoader`
- Parse it into per-page `Document` objects
- Spin up a **Qdrant** vector database instance via Docker for upcoming embedding storage

```python
from pathlib import Path
from langchain.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "PEFT.pdf"
loader = PyPDFLoader(file_path=pdf_path)
documents = loader.load()

print(documents[5].page_content)
```

## Roadmap

The end-to-end pipeline this project is building toward:

```
 Documents (PDF)
       │
       ▼
 Document Loader (PyPDFLoader)  ✅ done
       │
       ▼
 Text Chunking                  ⬜ planned
       │
       ▼
 Embedding Model                ⬜ planned
       │
       ▼
 Vector Store (Qdrant)          🟡 service scaffolded, not yet wired up
       │
       ▼
 Similarity Search / Retrieval  ⬜ planned
       │
       ▼
 LLM Answer Generation          ⬜ planned
       │
       ▼
 Context-Aware Answer
```

Planned additions:

- [ ] Recursive/character-based text chunking (LangChain text splitters)
- [ ] Embedding generation (OpenAI / HuggingFace / local models)
- [ ] Store & query embeddings in Qdrant
- [ ] Similarity search + context retrieval
- [ ] LLM integration (OpenAI GPT / Ollama) for grounded answer generation
- [ ] REST API (FastAPI) to expose upload + query endpoints
- [ ] Support for multiple documents and file types (DOCX, TXT)
- [ ] Response citations pointing back to source chunks

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Document Loading / Framework | LangChain (`langchain-classic`, `langchain-community`, `langchain-text-splitters`) |
| PDF Parsing | `pypdf` |
| Vector Database | [Qdrant](https://qdrant.tech/) (via Docker) |
| Config | `python-dotenv` |
| Planned: Embeddings | OpenAI Embeddings / HuggingFace |
| Planned: LLM | OpenAI GPT / Ollama |
| Planned: API | FastAPI |

## Project Structure

```
Document-RAG-pipeline/
├── PEFT.pdf              # Sample source document used for ingestion
├── index.py               # Entry point: loads and parses the PDF
├── docker-compose.yml      # Spins up the Qdrant vector database
├── requirement.txt        # Python dependencies
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (for the vector database)

### 1. Clone the repository

```bash
git clone https://github.com/Anshika-111105/Document-RAG-pipeline.git
cd Document-RAG-pipeline
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Start the vector database

```bash
docker-compose up -d
```

This starts Qdrant, accessible at `http://localhost:6333`.

### 5. Run the ingestion script

```bash
python index.py
```

This loads `PEFT.pdf`, parses it page by page, and prints the content of page 6 (index `5`) to the console as a sanity check that the loader works.

---

## Environment Variables

Not required yet for the current script. Once LLM/embedding integration is added, a `.env` file will be needed, e.g.:

```
OPENAI_API_KEY=your_api_key
VECTOR_DB_URL=http://localhost:6333
```

---

## Contributing

This is an actively evolving learning/portfolio project. Issues and PRs that move items on the [Roadmap](#roadmap) forward are welcome.

## License

This project is licensed under the MIT License.
