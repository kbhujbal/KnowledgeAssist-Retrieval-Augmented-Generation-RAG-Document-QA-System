from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # API Configuration
    app_name: str = "Knowledge Assist RAG API"
    app_version: str = "1.0.0"
    api_prefix: str = "/api/v1"
    debug: bool = False

    # CORS
    allowed_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    # File Upload
    max_upload_size: int = 10 * 1024 * 1024  # 10MB
    allowed_extensions: set[str] = {".pdf", ".txt", ".docx"}
    upload_dir: str = "app/storage/uploads"

    # Vector Store
    chroma_persist_dir: str = "app/storage/chroma_db"
    collection_name: str = "documents"

    # Embeddings
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # LLM Configuration
    llm_provider: str = "anthropic"  # or "openai"
    anthropic_api_key: str = ""
    openai_api_key: str = ""
    llm_model: str = "claude-3-5-sonnet-20241022"  # or "gpt-4-turbo"
    llm_temperature: float = 0.0
    max_tokens: int = 2000

    # RAG Configuration
    chunk_size: int = 1000
    chunk_overlap: int = 200
    retrieval_k: int = 4  # Number of chunks to retrieve

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Cached settings instance."""
    return Settings()
