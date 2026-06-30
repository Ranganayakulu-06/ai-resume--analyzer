# AI Resume Analyzer - Backend

FastAPI backend for AI Resume Analyzer application.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL 12+
- pip or Poetry

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Setup database**
   ```bash
   alembic upgrade head
   ```

5. **Run development server**
   ```bash
   uvicorn app.main:app --reload
   ```

Server will be available at `http://localhost:8000`

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📁 Project Structure

```
app/
├── api/             # API routes
├── core/            # Configuration & security
├── crud/            # Database operations
├── db/              # Database models
├── models/          # Pydantic schemas
├── services/        # Business logic
└── tests/           # Test suite
```

## 🧪 Testing

```bash
pytest
```

## 🐳 Docker

```bash
docker build -t ai-resume-analyzer-backend .
docker run -p 8000:8000 ai-resume-analyzer-backend
```
