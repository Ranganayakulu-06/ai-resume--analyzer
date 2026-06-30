"""CRUD operations for Analysis."""
from sqlalchemy.orm import Session
from app.db.models.analysis import Analysis
from app.models.analysis import AnalysisCreate


def create_analysis(
    db: Session,
    analysis: AnalysisCreate,
) -> Analysis:
    """Create a new analysis."""
    db_analysis = Analysis(
        resume_id=analysis.resume_id,
        job_description_id=analysis.job_description_id,
    )
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis


def get_analysis(
    db: Session,
    analysis_id: int,
) -> Analysis:
    """Get analysis by ID."""
    return db.query(Analysis).filter(Analysis.id == analysis_id).first()


def get_analyses(
    db: Session,
    user_id: int = None,
) -> list:
    """Get analyses."""
    query = db.query(Analysis)
    if user_id:
        pass
    return query.all()


def update_analysis(
    db: Session,
    analysis_id: int,
    ats_score: float = None,
    summary: str = None,
    matched_skills: str = None,
    missing_skills: str = None,
    suggestions: str = None,
    section_feedback: str = None,
) -> Analysis:
    """Update analysis results."""
    db_analysis = get_analysis(db, analysis_id)
    if db_analysis:
        if ats_score is not None:
            db_analysis.ats_score = ats_score
        if summary:
            db_analysis.summary = summary
        if matched_skills:
            db_analysis.matched_skills = matched_skills
        if missing_skills:
            db_analysis.missing_skills = missing_skills
        if suggestions:
            db_analysis.suggestions = suggestions
        if section_feedback:
            db_analysis.section_feedback = section_feedback
        db.commit()
        db.refresh(db_analysis)
    return db_analysis
