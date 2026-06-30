"""CRUD operations for Resume."""
from sqlalchemy.orm import Session
from app.db.models.resume import Resume
from app.models.resume import ResumeCreate


def create_resume(
    db: Session,
    resume: ResumeCreate,
    user_id: int,
    file_path: str,
    extracted_text: str = None,
) -> Resume:
    """Create a new resume."""
    db_resume = Resume(
        user_id=user_id,
        filename=resume.filename,
        file_type=resume.file_type,
        file_path=file_path,
        extracted_text=extracted_text,
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume


def get_resume(
    db: Session,
    resume_id: int,
) -> Resume:
    """Get resume by ID."""
    return db.query(Resume).filter(Resume.id == resume_id).first()


def get_resumes(
    db: Session,
    user_id: int,
) -> list:
    """Get all resumes for a user."""
    return db.query(Resume).filter(Resume.user_id == user_id).all()
