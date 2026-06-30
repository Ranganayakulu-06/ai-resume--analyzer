"""ATS compatibility scoring service."""
from typing import Dict, List
import re


class ATSScorer:
    """Score resume ATS compatibility."""

    @staticmethod
    def calculate_score(
        resume_text: str,
        job_requirements: str,
    ) -> float:
        """Calculate ATS compatibility score."""
        score = 0.0

        return min(score, 100.0)

    @staticmethod
    def check_keywords(
        resume_text: str,
        keywords: List[str],
    ) -> Dict[str, float]:
        """Check keyword presence in resume."""
        keyword_scores = {}

        for keyword in keywords:
            pattern = re.compile(re.escape(keyword), re.IGNORECASE)
            matches = len(pattern.findall(resume_text))
            keyword_scores[keyword] = min(matches, 1)

        return keyword_scores

    @staticmethod
    def analyze_formatting(
        resume_text: str,
    ) -> Dict[str, bool]:
        """Analyze resume formatting for ATS compatibility."""
        analysis = {
            "has_clear_sections": False,
            "proper_spacing": False,
            "no_tables": False,
            "no_images": False,
        }

        return analysis
