"""Job description database model."""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.db.base import Base


class JobDescription(Base):
    """Job description model."""
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_title = Column(String, nullable=False)
    company = Column(String, nullable=True)
    description = Column(Text, nullable=False)
    required_skills = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
