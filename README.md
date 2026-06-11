# 📄 Document RAG Pipeline with LangChain & Vector Database

##  Overview

The **Document RAG (Retrieval-Augmented Generation) Pipeline** is an AI-powered application that enables users to query large document collections using natural language. Instead of relying solely on a Large Language Model (LLM), the system retrieves relevant information from uploaded documents and provides context-aware, accurate responses.

This project leverages **LangChain**, **Vector Databases (FAISS/ChromaDB)**, and **Large Language Models (OpenAI/Ollama)** to build an intelligent document question-answering system.

---

##  Objectives

* Build a document-aware AI assistant.
* Implement Retrieval-Augmented Generation (RAG).
* Enable semantic search over large document collections.
* Reduce LLM hallucinations using contextual retrieval.
* Create a scalable foundation for enterprise knowledge systems.

---

##  Features

* 📂 Document Upload & Processing
* ✂️ Automatic Text Chunking
* 🔍 Semantic Search using Vector Embeddings
* 🧠 Context-Aware Question Answering
* ⚡ FastAPI REST API Integration
* 🗄️ Vector Database Storage (FAISS/ChromaDB)
* 🔄 Modular LangChain Pipeline
* 🤖 Support for OpenAI and Ollama Models
* 📊 Easy Scalability for Large Document Collections

---

##  System Architecture

```text
                 ┌──────────────────┐
                 │    Documents     │
                 │ (PDF, TXT, DOCX) │
                 └─────────┬────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Document Loader     │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Text Chunking       │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Embedding Model     │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Vector Database     │
                │ (FAISS/ChromaDB)    │
                └─────────┬───────────┘
                          │
──────────────────────────┼─────────────────────────
                          │
                          ▼
                 User Query
                          │
                          ▼
                ┌─────────────────────┐
                │ Query Embedding     │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Similarity Search   │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Retrieved Context   │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ LLM (OpenAI/Ollama) │
                └─────────┬───────────┘
                          │
                          ▼
                   Generated Answer
```

---

## 🛠️ Technology Stack

| Layer                  | Technology                      |
| ---------------------- | ------------------------------- |
| Frontend               | React.js (Optional)             |
| Backend                | FastAPI                         |
| Programming Language   | Python                          |
| AI Framework           | LangChain                       |
| Vector Database        | FAISS / ChromaDB                |
| Embedding Models       | OpenAI Embeddings / HuggingFace |
| LLM                    | OpenAI GPT / Ollama             |
| Document Processing    | PyPDF, Unstructured             |
| API Testing            | Postman                         |
| Environment Management | dotenv                          |

---

##  Project Structure

```bash
document-rag-pipeline/
│
├── app/
│   ├── api/
│   ├── services/
│   ├── embeddings/
│   ├── vector_store/
│   └── llm/
│
├── data/
│   ├── raw_documents/
│   └── processed_documents/
│
├── vector_db/
│
├── tests/
│
├── requirements.txt
├── main.py
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/document-rag-pipeline.git

cd document-rag-pipeline
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key

MODEL_NAME=gpt-4o-mini

VECTOR_DB=faiss
```

For Ollama:

```env
OLLAMA_MODEL=llama3
```

---

## Running the Application

### Start FastAPI Server

```bash
uvicorn main:app --reload
```

Server runs at:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

##  Workflow

### Step 1: Upload Documents

* PDF
* DOCX
* TXT

### Step 2: Process Documents

* Load document
* Clean text
* Split into chunks
* Generate embeddings

### Step 3: Store Embeddings

* Save vectors in FAISS or ChromaDB

### Step 4: Query Documents

User submits a question:

```text
What are the key objectives mentioned in the report?
```

### Step 5: Retrieve Context

Relevant chunks are fetched from the vector database.

### Step 6: Generate Response

The retrieved context is passed to the LLM for grounded answer generation.

---

##  Scalability Considerations

* Modular pipeline architecture
* Swappable vector databases
* Batch embedding generation
* Support for cloud deployment
* Easy migration to distributed RAG systems
* Can be extended with Redis queues and worker nodes

---

##  Future Enhancements

* Multi-document collections
* Hybrid Search (BM25 + Vector Search)
* Response Citation Support
* User Authentication
* Redis-Based Task Queue
* Document Versioning
* Feedback and Evaluation Metrics
* Kubernetes Deployment

---

##  Real-World Applications

### Enterprise Knowledge Assistant

Search company policies, SOPs, and internal documentation.

### Educational Q&A System

Allow students to ask questions from textbooks and notes.

### Legal Document Analysis

Retrieve information from contracts and legal documents.

### Research Assistant

Query research papers and technical reports.

### Customer Support Knowledge Base

Provide AI-powered responses using support documentation.

---

##  Learning Outcomes

By completing this project, you will gain hands-on experience with:

* Retrieval-Augmented Generation (RAG)
* LangChain Framework
* Vector Databases
* Embedding Models
* Large Language Models
* FastAPI Development
* Semantic Search Systems
* AI Application Architecture

---

##  Authors

Developed as part of a Project-Based Learning initiative focused on Full Stack Development and Generative AI Systems.

---

##  License

This project is licensed under the MIT License.
