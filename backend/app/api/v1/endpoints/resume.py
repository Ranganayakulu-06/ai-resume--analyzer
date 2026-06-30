"""Resume endpoints."""
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.resume import ResumeResponse

router = APIRouter()


@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """Upload and parse resume file."""
    return {"message": "Resume upload endpoint"}


@router.get("/")
async def list_resumes(db: Session = Depends(get_db)):
    """List all resumes for the user."""
    return {"message": "List resumes endpoint"}


@router.get("/{resume_id}")
async def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
):
    """Get a specific resume."""
    return {"message": f"Get resume {resume_id} endpoint"}
