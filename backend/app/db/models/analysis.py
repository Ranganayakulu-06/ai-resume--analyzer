"""Analysis database model."""
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.db.base import Base


class Analysis(Base):
    """Analysis model."""
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    job_description_id = Column(Integer, ForeignKey("job_descriptions.id"), nullable=False)
    ats_score = Column(Float, nullable=True)
    summary = Column(Text, nullable=True)
    matched_skills = Column(Text, nullable=True)
    missing_skills = Column(Text, nullable=True)
    suggestions = Column(Text, nullable=True)
    section_feedback = Column(Text, nullable=True)
    analyzed_at = Column(DateTime(timezone=True), server_default=func.now())
