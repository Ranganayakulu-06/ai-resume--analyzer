# AI Resume Analyzer

🤖 An intelligent application that analyzes resumes, compares them with job descriptions, and provides actionable feedback to improve ATS compatibility.

## 🎯 Features

- 📄 **Resume Upload** - Support for PDF and DOCX formats
- 💼 **Job Description Input** - Paste or upload job requirements
- 🔍 **Skills Extraction** - Automatic extraction of candidate skills
- ⚠️ **Missing Skills Identification** - Highlights skills gaps
- 🎯 **ATS Compatibility Score** - Scoring for Applicant Tracking Systems
- 📋 **Resume Summary** - AI-powered resume overview
- 📊 **Section-wise Feedback** - Detailed feedback for Education, Experience, Skills, Projects
- 💡 **Suggested Keywords** - Keywords to improve ATS matching
- 📥 **Downloadable Reports** - Generate and download analysis reports
- 📚 **Analysis History** - Store and review previous analyses

## 🏗️ Architecture

```
┌─────────────────────────────────┐
│     React Frontend (JSX)        │
│  - Resume Upload                │
│  - Job Description Input        │
│  - Analysis Report Display      │
│  - History Management           │
└────────────┬────────────────────┘
             │ HTTP/REST
┌────────────▼────────────────────┐
│     FastAPI Backend (Python)    │
│  - Document Processing          │
│  - AI Analysis (OpenAI/Claude)  │
│  - ATS Scoring                  │
│  - Report Generation            │
└────────────┬────────────────────┘
             │ SQL
┌────────────▼────────────────────┐
│   PostgreSQL Database           │
│  - Users                        │
│  - Resumes                      │
│  - Job Descriptions             │
│  - Analysis Results             │
└─────────────────────────────────┘
```

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - ORM for database operations
- **PyMuPDF/pdfplumber** - PDF text extraction
- **python-docx** - DOCX file parsing
- **OpenAI/Anthropic API** - AI analysis
- **Alembic** - Database migrations
- **Pydantic** - Data validation

### Frontend
- **React 18+** - UI library
- **Vite** - Build tool
- **React Router** - Routing
- **Axios** - HTTP client
- **CSS3** - Styling

## 📁 Project Structure

```
ai-resume-analyzer/
├── backend/                 # FastAPI backend
├── frontend/                # React frontend
├── docs/                    # Documentation
└── README.md
```

## 🔧 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL 12+
- OpenAI/Claude API key

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Configure .env with your database and API keys
alembic upgrade head
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## 📖 API Documentation

Once the backend is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📚 Documentation

Detailed documentation is available in the `docs/` folder:
- [API Specification](./docs/api-spec.md)
- [System Architecture](./docs/architecture.md)
- [Setup Guide](./docs/setup-guide.md)

## 🤝 Contributing

Contributions are welcome! Please follow the coding standards and create a pull request.

## 📝 License

MIT License - Feel free to use this project for personal or commercial purposes.

## 🆘 Support

For issues or questions, please create a GitHub issue.
