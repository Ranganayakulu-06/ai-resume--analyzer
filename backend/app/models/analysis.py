"""Analysis Pydantic schemas."""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class AnalysisBase(BaseModel):
    """Base analysis schema."""
    resume_id: int
    job_description_id: int


class AnalysisCreate(AnalysisBase):
    """Analysis creation schema."""
    pass


class AnalysisResponse(AnalysisBase):
    """Analysis response schema."""
    id: int
    ats_score: Optional[float] = None
    summary: Optional[str] = None
    matched_skills: Optional[str] = None
    missing_skills: Optional[str] = None
    suggestions: Optional[str] = None
    section_feedback: Optional[str] = None
    analyzed_at: datetime

    class Config:
        from_attributes = True
