"""Job Description Pydantic schemas."""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class JobDescriptionBase(BaseModel):
    """Base job description schema."""
    job_title: str
    company: Optional[str] = None
    description: str


class JobDescriptionCreate(JobDescriptionBase):
    """Job description creation schema."""
    pass


class JobDescriptionResponse(JobDescriptionBase):
    """Job description response schema."""
    id: int
    user_id: int
    required_skills: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
