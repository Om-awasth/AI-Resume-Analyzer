"""
Skill Extractor Module
Detects skills in resume text using keyword matching
"""

import re
from model.skills import JOB_SKILLS

class SkillExtractor:
    """Extract skills from resume text using regex matching"""
    
    @staticmethod
    def extract_skills(text, job_role):
        """
        Extract skills from text that match the job role requirements
        
        Args:
            text (str): Resume text to analyze
            job_role (str): Job role to match skills for
            
        Returns:
            list: List of detected skills
        """
        if not text or job_role not in JOB_SKILLS:
            return []
        
        detected_skills = []
        
        # Get skills for this job role
        job_skills = JOB_SKILLS[job_role]
        all_skills = job_skills['technical'] + job_skills['soft']
        
        # Convert text to lowercase for matching
        text_lower = text.lower()
        
        # Search for each skill in text
        for skill in all_skills:
            # Create regex pattern with word boundaries
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            
            if re.search(pattern, text_lower):
                detected_skills.append(skill)
        
        return detected_skills
    
    @staticmethod
    def calculate_skill_match(detected_skills, required_skills):
        """
        Calculate skill match percentage
        
        Args:
            detected_skills (list): Skills found in resume
            required_skills (list): Skills required for job
            
        Returns:
            dict: Match information
        """
        if not required_skills:
            return {
                'matched': [],
                'missing': [],
                'match_percentage': 0.0,
                'matched_count': 0,
                'required_count': 0
            }
        
        # Find matched and missing skills
        detected_set = set(detected_skills)
        required_set = set(required_skills)
        
        matched_skills = list(detected_set & required_set)
        missing_skills = list(required_set - detected_set)
        
        # Calculate percentage
        match_percentage = round(
            (len(matched_skills) / len(required_set)) * 100, 2
        ) if required_set else 0.0
        
        return {
            'matched': sorted(matched_skills),
            'missing': sorted(missing_skills),
            'match_percentage': match_percentage,
            'matched_count': len(matched_skills),
            'required_count': len(required_set)
        }
    
    @staticmethod
    def get_job_requirements(job_role):
        """
        Get all required skills for a job role
        
        Args:
            job_role (str): Job role name
            
        Returns:
            list: Combined list of technical and soft skills
        """
        if job_role not in JOB_SKILLS:
            return []
        
        job_info = JOB_SKILLS[job_role]
        return job_info['technical'] + job_info['soft']


def extract_skills_from_text(text, job_role):
    """
    Wrapper function to extract skills
    
    Args:
        text (str): Resume text
        job_role (str): Job role
        
    Returns:
        list: Detected skills
    """
    return SkillExtractor.extract_skills(text, job_role)


def analyze_skill_match(detected_skills, job_role):
    """
    Wrapper function to analyze skill match
    
    Args:
        detected_skills (list): Detected skills
        job_role (str): Job role
        
    Returns:
        dict: Match analysis
    """
    required_skills = SkillExtractor.get_job_requirements(job_role)
    return SkillExtractor.calculate_skill_match(detected_skills, required_skills)
