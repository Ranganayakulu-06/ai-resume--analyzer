"""Analysis endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.analysis import AnalysisCreate, AnalysisResponse

router = APIRouter()


@router.post("/", response_model=AnalysisResponse)
async def analyze_resume(
    analysis: AnalysisCreate,
    db: Session = Depends(get_db),
):
    """Analyze resume against job description."""
    return {"message": "Analyze resume endpoint"}


@router.get("/")
async def list_analyses(db: Session = Depends(get_db)):
    """List all analyses."""
    return {"message": "List analyses endpoint"}


@router.get("/{analysis_id}")
async def get_analysis(
    analysis_id: int,
    db: Session = Depends(get_db),
):
    """Get analysis details."""
    return {"message": f"Get analysis {analysis_id} endpoint"}
