"""Resume Pydantic schemas."""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ResumeBase(BaseModel):
    """Base resume schema."""
    filename: str
    file_type: str


class ResumeCreate(ResumeBase):
    """Resume creation schema."""
    pass


class ResumeResponse(ResumeBase):
    """Resume response schema."""
    id: int
    user_id: int
    file_path: str
    extracted_text: Optional[str] = None
    uploaded_at: datetime

    class Config:
        from_attributes = True
