# System Architecture

## Overview

AI Resume Analyzer is a full-stack application with a separation of concerns between frontend and backend.

## Technology Stack

### Backend
- FastAPI for REST API
- SQLAlchemy for ORM
- PostgreSQL for data persistence
- OpenAI/Claude for AI analysis

### Frontend
- React for UI
- Vite for bundling
- Axios for HTTP calls

## Data Flow

1. User uploads resume (PDF/DOCX)
2. Frontend sends file to backend
3. Backend extracts text from document
4. User provides job description
5. Backend analyzes resume vs job description using AI
6. AI generates scores and recommendations
7. Results stored in database
8. Frontend displays analysis and recommendations
