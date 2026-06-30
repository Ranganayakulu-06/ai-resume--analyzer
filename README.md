# AI Resume Analyzer

🚀 Analyze resumes and match them with job descriptions using AI

## 📋 Overview

AI Resume Analyzer is a full-stack web application that helps job seekers:
- Upload and analyze resumes
- Match resumes against job descriptions
- Get ATS compatibility scores
- Receive actionable improvement suggestions

## 🛠 Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **AI**: OpenAI GPT-3.5, Claude
- **File Processing**: PyMuPDF, python-docx

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: CSS3
- **HTTP Client**: Axios
- **Routing**: React Router v6

### DevOps
- **Containerization**: Docker & Docker Compose
- **Orchestration**: Kubernetes
- **Database**: PostgreSQL 15

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local development)
- Python 3.9+ (for local development)
- PostgreSQL 12+ (for local development)

### Using Docker Compose

1. **Clone repository**
   ```bash
   git clone https://github.com/Ranganayakulu-06/ai-resume--analyzer.git
   cd ai-resume--analyzer
   ```

2. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start services**
   ```bash
   docker-compose up -d
   ```

4. **Access application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Local Development

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## 📁 Project Structure

```
ai-resume--analyzer/
├── backend/
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── core/          # Configuration
│   │   ├── crud/          # Database operations
│   │   ├── db/            # Database models
│   │   ├── models/        # Pydantic schemas
│   │   ├── services/      # Business logic
│   │   └── tests/         # Tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── features/      # Feature modules
│   │   ├── pages/         # Route pages
│   │   ├── services/      # API clients
│   │   ├── utils/         # Utilities
│   │   └── styles/        # Global styles
│   ├── package.json
│   └── Dockerfile
├── k8s/                   # Kubernetes configs
├── docker-compose.yml
└── README.md
```

## 🔑 API Endpoints

### Resume
- `POST /api/v1/resume/upload` - Upload resume
- `GET /api/v1/resume/` - List resumes
- `GET /api/v1/resume/{id}` - Get resume details

### Job Description
- `POST /api/v1/job-description/` - Create job description
- `GET /api/v1/job-description/` - List job descriptions
- `GET /api/v1/job-description/{id}` - Get job description

### Analysis
- `POST /api/v1/analysis/` - Analyze resume
- `GET /api/v1/analysis/` - List analyses
- `GET /api/v1/analysis/{id}` - Get analysis details

### Reports
- `GET /api/v1/reports/{id}` - Get report
- `GET /api/v1/reports/{id}/download` - Download PDF report

## 🔐 Environment Variables

See `.env.example` files in backend and frontend directories.

## 📚 Documentation

- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)
- [Deployment Guide](./DEPLOYMENT.md)

## 🧪 Testing

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm test
```

## 🐳 Docker Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed Docker and Kubernetes setup.

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License.

## 📧 Support

For issues and questions, please open an issue on GitHub.
