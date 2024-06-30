# Knowledge Assist RAG - Backend

FastAPI-based backend for the Knowledge Assist RAG application.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run the server:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Visit `http://localhost:8000/docs` for interactive Swagger documentation.

## Directory Structure

- `app/api/` - API routes and request/response models
- `app/services/` - Business logic (RAG, document processing, vector store)
- `app/core/` - Core utilities and dependencies
- `app/storage/` - File and vector database storage

## Key Services

### Document Processor
Handles loading and chunking of PDF, TXT, and DOCX files.

### Vector Store Service
Manages ChromaDB vector database operations.

### RAG Service
Orchestrates the retrieval-augmented generation pipeline using LangChain.

## Testing

Run tests:
```bash
pytest
```

With coverage:
```bash
pytest --cov=app tests/
```
