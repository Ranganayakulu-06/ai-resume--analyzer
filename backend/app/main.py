"""Main FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.api.v1.endpoints import resume, analysis, job_description, reports


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 AI Resume Analyzer Starting...")
    yield
    # Shutdown
    print("👋 AI Resume Analyzer Shutting Down...")


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    app = FastAPI(
        title="AI Resume Analyzer API",
        description="Analyze resumes and match them with job descriptions",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(
        resume.router,
        prefix="/api/v1/resume",
        tags=["Resume"],
    )
    app.include_router(
        job_description.router,
        prefix="/api/v1/job-description",
        tags=["Job Description"],
    )
    app.include_router(
        analysis.router,
        prefix="/api/v1/analysis",
        tags=["Analysis"],
    )
    app.include_router(
        reports.router,
        prefix="/api/v1/reports",
        tags=["Reports"],
    )

    @app.get("/")
    async def root():
        return {
            "message": "Welcome to AI Resume Analyzer API",
            "version": "1.0.0",
            "docs": "/docs",
        }

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app


app = create_app()
