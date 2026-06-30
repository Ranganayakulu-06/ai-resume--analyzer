# AI Resume Analyzer Configuration

## Environment Setup

Create a `.env` file in the root directory:

```bash
# Database
DB_USER=postgres
DB_PASSWORD=your_secure_password
DB_NAME=ai_resume_analyzer
DB_PORT=5432

# API Keys
OPENAI_API_KEY=your_openai_api_key
CLAUDE_API_KEY=your_claude_api_key
SECRET_KEY=your_secret_key_change_in_production

# Ports
BACKEND_PORT=8000
FRONTEND_PORT=5173

# Debug
DEBUG=False
```

## Docker Setup

### Build and Run

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Access Services

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Database Migration

```bash
# Inside backend container
docker-compose exec backend alembic upgrade head
```

## Kubernetes Deployment

### Prerequisites
- kubectl configured
- Docker images pushed to registry

### Deploy

```bash
# Create secrets
kubectl create secret generic ai-resume-secrets \
  --from-literal=database-url='postgresql://...' \
  --from-literal=openai-api-key='your-key'

# Apply deployment
kubectl apply -f k8s/deployment.yaml

# Check status
kubectl get pods
kubectl get services
```

## Scaling

```bash
# Scale backend
kubectl scale deployment ai-resume-backend --replicas=3

# Scale frontend
kubectl scale deployment ai-resume-frontend --replicas=2
```

## Monitoring

```bash
# View pod logs
kubectl logs deployment/ai-resume-backend -f

# Port forward
kubectl port-forward service/ai-resume-frontend-service 8080:80
```
