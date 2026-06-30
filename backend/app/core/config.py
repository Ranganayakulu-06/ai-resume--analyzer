"""Application configuration using Pydantic Settings."""
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # App
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    PROJECT_NAME: str = "AI Resume Analyzer"
    VERSION: str = "1.0.0"

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/ai_resume_analyzer"

    # API Keys
    OPENAI_API_KEY: str = ""
    CLAUDE_API_KEY: str = ""

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    # File Upload
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_FILE_TYPES: List[str] = ["pdf", "docx"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
