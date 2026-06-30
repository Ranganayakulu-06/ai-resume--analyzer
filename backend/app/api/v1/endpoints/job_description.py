"""Job description endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.job_description import JobDescriptionCreate, JobDescriptionResponse

router = APIRouter()


@router.post("/", response_model=JobDescriptionResponse)
async def create_job_description(
    job_desc: JobDescriptionCreate,
    db: Session = Depends(get_db),
):
    """Create a new job description."""
    return {"message": "Create job description endpoint"}


@router.get("/")
async def list_job_descriptions(db: Session = Depends(get_db)):
    """List all job descriptions."""
    return {"message": "List job descriptions endpoint"}


@router.get("/{job_id}")
async def get_job_description(
    job_id: int,
    db: Session = Depends(get_db),
):
    """Get a specific job description."""
    return {"message": f"Get job description {job_id} endpoint"}
