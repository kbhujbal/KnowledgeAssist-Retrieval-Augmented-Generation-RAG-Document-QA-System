# Knowledge Assist RAG

A full-stack Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask questions about them using AI. The system uses LangChain, ChromaDB for vector storage, and supports both Anthropic and OpenAI LLMs.

## Features

- **Document Upload**: Upload PDF, TXT, and DOCX files with drag-and-drop support
- **Smart Chunking**: Automatically splits documents into optimal chunks for retrieval
- **Vector Search**: Uses ChromaDB for fast semantic search across documents
- **AI-Powered Answers**: Leverages Claude or GPT models for context-aware responses
- **Source Citations**: Every answer includes references to source documents with page numbers
- **Conversation Memory**: Maintains conversation context for follow-up questions
- **Beautiful UI**: Modern React interface with real-time updates

## Technology Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **LangChain**: RAG pipeline orchestration
- **ChromaDB**: Vector database for embeddings
- **Sentence Transformers**: Local embedding generation
- **Anthropic/OpenAI**: LLM providers

### Frontend
- **React 18**: Modern UI library
- **TypeScript**: Type-safe development
- **Vite**: Fast build tool
- **Axios**: HTTP client
- **React Dropzone**: File upload with drag & drop
- **React Markdown**: Render formatted responses

## Project Structure

```
KnowledgeAssist RAG/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/               # API routes and models
│   │   ├── services/          # Business logic
│   │   ├── core/              # Core functionality
│   │   └── storage/           # File and vector storage
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── services/          # API client
│   │   ├── types/             # TypeScript types
│   │   └── styles/            # CSS files
│   ├── package.json
│   └── tsconfig.json
│
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+
- API key from Anthropic or OpenAI

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file from example:
```bash
cp .env.example .env
```

5. Edit `.env` and add your API key:
```bash
# For Anthropic (Claude)
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-api-key-here

# OR for OpenAI (GPT)
LLM_PROVIDER=openai
OPENAI_API_KEY=your-api-key-here
```

6. Run the server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for interactive API documentation.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file (optional - defaults to localhost:8000):
```bash
cp .env.example .env
```

4. Start the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:5173`.

## Usage

1. **Upload Documents**:
   - Drag and drop PDF, TXT, or DOCX files into the upload area
   - Wait for processing (you'll see the number of chunks created)

2. **Ask Questions**:
   - Type your question in the chat input
   - Press Enter or click Send
   - The AI will respond with an answer based on your documents

3. **View Sources**:
   - Click on the sources toggle to see which document chunks were used
   - Each source shows the document name, page number, and relevant text

4. **Follow-up Questions**:
   - Continue the conversation naturally
   - The system maintains context for related questions

## API Endpoints

### Upload
- `POST /api/v1/upload/` - Upload a single file
- `POST /api/v1/upload/batch` - Upload multiple files

### Chat
- `POST /api/v1/chat/` - Send a question and get an answer
- `DELETE /api/v1/chat/conversation/{id}` - Clear conversation history

### Documents
- `GET /api/v1/documents/` - List uploaded documents
- `DELETE /api/v1/documents/{id}` - Delete a document

## Configuration

### Backend Configuration (`.env`)

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM_PROVIDER` | AI provider (anthropic/openai) | anthropic |
| `ANTHROPIC_API_KEY` | Anthropic API key | - |
| `OPENAI_API_KEY` | OpenAI API key | - |
| `CHUNK_SIZE` | Text chunk size | 1000 |
| `CHUNK_OVERLAP` | Overlap between chunks | 200 |
| `RETRIEVAL_K` | Number of chunks to retrieve | 4 |
| `MAX_UPLOAD_SIZE` | Max file size in bytes | 10485760 |

### Frontend Configuration (`.env`)

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_BASE_URL` | Backend API URL | http://localhost:8000 |

## Development

### Backend Development

Run tests:
```bash
cd backend
pytest
```

Format code:
```bash
black app/
```

### Frontend Development

Type checking:
```bash
cd frontend
npm run build
```

Linting:
```bash
npm run lint
```

## Production Deployment

### Backend

1. Set up a production database (PostgreSQL recommended for document metadata)
2. Use a production-grade vector store (Pinecone, Weaviate, or managed ChromaDB)
3. Add authentication and rate limiting
4. Use a reverse proxy (Nginx)
5. Set up HTTPS

Example with Docker:
```bash
cd backend
docker build -t rag-backend .
docker run -p 8000:8000 --env-file .env rag-backend
```

### Frontend

1. Build for production:
```bash
cd frontend
npm run build
```

2. Serve the `dist` folder with a static file server or CDN

3. Update `VITE_API_BASE_URL` to point to your production API

## Troubleshooting

### Backend Issues

**Problem**: ChromaDB initialization fails
- **Solution**: Delete `backend/app/storage/chroma_db/` and restart

**Problem**: Out of memory when loading embeddings
- **Solution**: Use a smaller embedding model or reduce batch size

### Frontend Issues

**Problem**: CORS errors
- **Solution**: Ensure backend `ALLOWED_ORIGINS` includes your frontend URL

**Problem**: File upload fails
- **Solution**: Check file size limits and supported file types

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Vector storage by [ChromaDB](https://www.trychroma.com/)
- Embeddings by [Sentence Transformers](https://www.sbert.net/)
- UI components by [Lucide Icons](https://lucide.dev/)

## Support

For issues and questions:
- Open an issue on GitHub
- Check the [API documentation](http://localhost:8000/docs)
- Review the architecture diagram in this README

---

Made with ❤️ using FastAPI, React, and LangChain
