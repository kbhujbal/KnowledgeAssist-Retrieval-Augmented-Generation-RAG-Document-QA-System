from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)
from pathlib import Path
import logging
from typing import Optional

from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class DocumentProcessor:
    """Process and chunk documents."""

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )

    def load_document(self, file_path: str, filename: str) -> list[Document]:
        """
        Load a document based on file extension.

        Args:
            file_path: Path to the file
            filename: Original filename

        Returns:
            List of Document objects
        """
        file_extension = Path(filename).suffix.lower()

        try:
            if file_extension == ".pdf":
                loader = PyPDFLoader(file_path)
            elif file_extension == ".txt":
                loader = TextLoader(file_path, encoding='utf-8')
            elif file_extension == ".docx":
                loader = Docx2txtLoader(file_path)
            else:
                raise ValueError(f"Unsupported file type: {file_extension}")

            documents = loader.load()
            logger.info(f"Loaded {len(documents)} pages from {filename}")

            # Add filename to metadata
            for doc in documents:
                doc.metadata["filename"] = filename
                doc.metadata["source"] = file_path

            return documents

        except Exception as e:
            logger.error(f"Error loading document {filename}: {e}")
            raise

    def chunk_documents(
        self,
        documents: list[Document],
        filename: str
    ) -> list[Document]:
        """
        Split documents into chunks.

        Args:
            documents: List of Document objects
            filename: Original filename for metadata

        Returns:
            List of chunked Document objects
        """
        chunks = self.text_splitter.split_documents(documents)

        # Add chunk index to metadata
        for idx, chunk in enumerate(chunks):
            chunk.metadata["chunk_index"] = idx
            chunk.metadata["filename"] = filename

        logger.info(f"Created {len(chunks)} chunks from {filename}")
        return chunks

    def process_file(
        self,
        file_path: str,
        filename: str
    ) -> list[Document]:
        """
        Complete processing pipeline: load and chunk.

        Args:
            file_path: Path to the file
            filename: Original filename

        Returns:
            List of chunked Document objects ready for embedding
        """
        documents = self.load_document(file_path, filename)
        chunks = self.chunk_documents(documents, filename)

        return chunks
