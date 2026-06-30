"""CRUD operations for JobDescription."""
from sqlalchemy.orm import Session
from app.db.models.job_description import JobDescription
from app.models.job_description import JobDescriptionCreate


def create_job_description(
    db: Session,
    job_desc: JobDescriptionCreate,
    user_id: int,
) -> JobDescription:
    """Create a new job description."""
    db_job_desc = JobDescription(
        user_id=user_id,
        job_title=job_desc.job_title,
        company=job_desc.company,
        description=job_desc.description,
    )
    db.add(db_job_desc)
    db.commit()
    db.refresh(db_job_desc)
    return db_job_desc


def get_job_description(
    db: Session,
    job_id: int,
) -> JobDescription:
    """Get job description by ID."""
    return db.query(JobDescription).filter(JobDescription.id == job_id).first()


def get_job_descriptions(
    db: Session,
    user_id: int,
) -> list:
    """Get all job descriptions for a user."""
    return db.query(JobDescription).filter(JobDescription.user_id == user_id).all()
