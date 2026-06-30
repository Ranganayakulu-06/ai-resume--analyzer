"""AI analysis service using OpenAI/Claude."""
import json
from typing import Dict, Any, Optional
import openai

from app.core.config import settings


class AIAnalyzer:
    """Analyze resumes using AI models."""

    def __init__(self, provider: str = "openai"):
        """Initialize AI analyzer."""
        self.provider = provider
        if provider == "openai":
            openai.api_key = settings.OPENAI_API_KEY

    def analyze_resume(
        self,
        resume_text: str,
        job_description: str,
    ) -> Dict[str, Any]:
        """Analyze resume against job description."""
        prompt = f"""
        Analyze the following resume against the job description and provide:
        1. ATS Compatibility Score (0-100)
        2. Summary of the candidate
        3. Matched skills
        4. Missing skills
        5. Improvement suggestions
        6. Section-wise feedback (Education, Experience, Skills, Projects)
        
        Resume:
        {resume_text}
        
        Job Description:
        {job_description}
        
        Provide response as JSON.
        """

        try:
            if self.provider == "openai":
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional resume analyzer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                )
                return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Error analyzing resume: {e}")
            return {}

    def extract_skills(
        self,
        text: str,
    ) -> list:
        """Extract skills from text."""
        prompt = f"""
        Extract all technical and professional skills from the following text.
        Return as a JSON array of skills.
        
        Text:
        {text}
        """

        try:
            if self.provider == "openai":
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a skills extraction expert."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                )
                return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Error extracting skills: {e}")
            return []
