"""Resume text extraction service."""
import fitz
from docx import Document
from typing import Optional


class ResumeParser:
    """Parse resume files and extract text."""

    @staticmethod
    def extract_from_pdf(file_path: str) -> Optional[str]:
        """Extract text from PDF file."""
        try:
            pdf = fitz.open(file_path)
            text = ""
            for page_num in range(len(pdf)):
                page = pdf[page_num]
                text += page.get_text()
            pdf.close()
            return text
        except Exception as e:
            print(f"Error extracting PDF: {e}")
            return None

    @staticmethod
    def extract_from_docx(file_path: str) -> Optional[str]:
        """Extract text from DOCX file."""
        try:
            doc = Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            print(f"Error extracting DOCX: {e}")
            return None

    @staticmethod
    def extract_text(file_path: str, file_type: str) -> Optional[str]:
        """Extract text from resume based on file type."""
        if file_type.lower() == "pdf":
            return ResumeParser.extract_from_pdf(file_path)
        elif file_type.lower() == "docx":
            return ResumeParser.extract_from_docx(file_path)
        else:
            return None
