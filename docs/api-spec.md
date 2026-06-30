# API Specification

## Base URL
```
http://localhost:8000/api/v1
```

## Endpoints

### Resume
- `POST /resume/upload` - Upload resume
- `GET /resume/` - List resumes
- `GET /resume/{id}` - Get resume

### Job Description
- `POST /job-description/` - Create job description
- `GET /job-description/` - List job descriptions
- `GET /job-description/{id}` - Get job description

### Analysis
- `POST /analysis/` - Create analysis
- `GET /analysis/` - List analyses
- `GET /analysis/{id}` - Get analysis

### Reports
- `GET /reports/{id}` - Get report
- `GET /reports/{id}/download` - Download PDF report
