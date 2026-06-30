"""Reports endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()


@router.get("/{analysis_id}")
async def get_report(
    analysis_id: int,
    db: Session = Depends(get_db),
):
    """Get detailed analysis report."""
    return {"message": f"Get report for analysis {analysis_id} endpoint"}


@router.get("/{analysis_id}/download")
async def download_report(
    analysis_id: int,
    db: Session = Depends(get_db),
):
    """Download report as PDF."""
    return {"message": f"Download report for analysis {analysis_id} endpoint"}
