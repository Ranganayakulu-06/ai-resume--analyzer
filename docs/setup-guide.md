# Setup Guide

## Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL 12+
- OpenAI or Claude API key

## Full Stack Setup

### 1. Clone Repository
```bash
git clone <repo-url>
cd ai-resume-analyzer
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

# Configure .env
# IMPORTANT: Update DATABASE_URL, API keys, etc

alembic upgrade head
uvicorn app.main:app --reload
```

### 3. Frontend Setup
```bash
cd ../frontend
npm install
cp .env.example .env

# Configure .env
# IMPORTANT: Update VITE_API_URL if needed

npm run dev
```

### 4. Access Application
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Docker Setup

```bash
docker-compose up -d
```
