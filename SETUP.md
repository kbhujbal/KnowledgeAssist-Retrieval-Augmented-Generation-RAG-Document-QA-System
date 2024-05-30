# Quick Setup Guide

Follow these steps to get the Knowledge Assist RAG application running on your machine.

## Prerequisites

Before you begin, ensure you have:
- Python 3.9 or higher installed
- Node.js 18 or higher installed
- An API key from either Anthropic or OpenAI

## Step 1: Backend Setup

Open a terminal and run:

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
```

Now edit the `.env` file and add your API key:

```bash
# Open .env in your favorite editor
# For Anthropic Claude:
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx

# OR for OpenAI:
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-xxxxxxxxxxxxx
```

Start the backend server:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

Keep this terminal open and running.

## Step 2: Frontend Setup

Open a **new terminal** window and run:

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# (Optional) Create environment file
cp .env.example .env

# Start the development server
npm run dev
```

You should see:
```
  VITE v5.0.11  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

## Step 3: Open the Application

Open your browser and navigate to:
```
http://localhost:5173
```

You should see the Knowledge Assist RAG interface!

## Step 4: Test the Application

1. **Upload a document**:
   - Drag and drop a PDF, TXT, or DOCX file into the upload area
   - Wait for the processing to complete (you'll see "Success" status)

2. **Ask a question**:
   - Type a question about your document in the chat input
   - Press Enter or click Send
   - Wait for the AI response

3. **View sources**:
   - Click on the "sources" button to see which parts of your document were used

## Troubleshooting

### Backend won't start

**Error**: `ModuleNotFoundError`
- **Solution**: Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

**Error**: `chromadb initialization failed`
- **Solution**: Delete the `backend/app/storage/chroma_db` folder and restart

### Frontend won't start

**Error**: `ENOENT: no such file or directory`
- **Solution**: Make sure you're in the `frontend` directory and ran `npm install`

**Error**: `Cannot connect to backend`
- **Solution**: Ensure the backend is running on port 8000

### API Errors

**Error**: `Invalid API key`
- **Solution**: Check that you've correctly set your API key in `backend/.env`

**Error**: `Rate limit exceeded`
- **Solution**: You've hit your API provider's rate limit. Wait a few minutes and try again.

## Next Steps

- Read the main [README.md](README.md) for detailed documentation
- Check the API documentation at `http://localhost:8000/docs`
- Explore the example queries below

## Example Questions to Try

After uploading a document, try these questions:

1. "What are the main topics discussed in this document?"
2. "Can you summarize the key points?"
3. "What does the document say about [specific topic]?"
4. "List the important dates or numbers mentioned."
5. "What conclusions does the author draw?"

## Stopping the Application

To stop the servers:

1. **Backend**: Press `Ctrl+C` in the backend terminal
2. **Frontend**: Press `Ctrl+C` in the frontend terminal

To deactivate the Python virtual environment:
```bash
deactivate
```

---

Enjoy using Knowledge Assist RAG! 🚀
