"""
Demo Script - No Dependencies Required
Shows how the resume analyzer works with sample data
"""

from utils.skill_extractor import extract_skills_from_text, analyze_skill_match
from model.skills import (
    get_job_skills, get_job_description, 
    get_learning_resource, get_all_job_roles
)
from model.tfidf_model import calculate_resume_similarity
from utils.pdf_reader import PDFReader

# Sample resume text
SAMPLE_RESUME = """
John Doe
john.doe@email.com | (555) 123-4567 | LinkedIn.com/in/johndoe

SUMMARY
Experienced Data Analyst with 5 years of expertise in data analysis, visualization, and business intelligence. 
Proficient in Python, SQL, and data visualization tools. Strong analytical and problem-solving skills.

PROFESSIONAL EXPERIENCE
Senior Data Analyst - Tech Company (2021-Present)
- Developed Python scripts for data processing and analysis
- Created interactive Tableau dashboards for executive reporting
- Performed statistical analysis and A/B testing on marketing campaigns
- Optimized SQL queries for improved database performance

Data Analyst - Finance Firm (2018-2021)
- Analyzed financial data using Python, Pandas, and NumPy
- Built ETL processes for data integration
- Created Excel reports and Power BI visualizations
- Conducted data mining to identify business opportunities

TECHNICAL SKILLS
Languages: Python, R, SQL, JavaScript
Tools: Tableau, Excel, Jupyter, Git
Libraries: Pandas, NumPy, Matplotlib, Seaborn
Databases: MySQL, PostgreSQL
Concepts: Statistics, Data Mining, ETL, A/B Testing

SOFT SKILLS
Communication, Problem Solving, Attention to Detail, Critical Thinking, Teamwork

EDUCATION
Bachelor of Science in Mathematics
University of Technology (2018)

CERTIFICATIONS
Google Data Analytics Professional Certificate
Advanced Excel for Data Analysis
"""

def print_results(role_name, results):
    """Pretty print analysis results"""
    print(f"\n{'='*70}")
    print(f"ANALYSIS RESULTS: {role_name}")
    print(f"{'='*70}")
    
    skill_match = results['skill_match']
    tfidf_score = results['tfidf_score']
    
    print(f"\n📊 SCORES:")
    print(f"  • Skill Match: {skill_match['match_percentage']}% ({skill_match['matched_count']}/{skill_match['required_count']} skills)")
    print(f"  • TF-IDF Similarity: {tfidf_score}%")
    
    print(f"\n✅ MATCHED SKILLS ({len(skill_match['matched'])}):")
    matched = skill_match['matched']
    for i, skill in enumerate(matched[:10], 1):
        print(f"  {i}. {skill}")
    if len(matched) > 10:
        print(f"  ... and {len(matched) - 10} more")
    
    print(f"\n❌ TOP MISSING SKILLS ({len(skill_match['missing'])}):")
    missing = skill_match['missing']
    for i, skill in enumerate(missing[:5], 1):
        print(f"  {i}. {skill}")
    if len(missing) > 5:
        print(f"  ... and {len(missing) - 5} more")
    
    print(f"\n💡 RECOMMENDATION:")
    print(f"  {results['recommendation']}")
    
    # Show learning resources for top 3 missing skills
    print(f"\n📚 LEARNING RESOURCES (Top 3 Missing Skills):")
    for skill in missing[:3]:
        resource = get_learning_resource(skill)
        print(f"\n  {skill}:")
        if resource.get('courses'):
            print(f"    • Courses: {resource['courses'][0]}")
        if resource.get('websites'):
            print(f"    • Website: {resource['websites'][0]}")
        print(f"    • Duration: {resource['duration']}")


def main():
    """Run the demo"""
    print("\n" + "="*70)
    print("🎓 RESUME ANALYZER & SKILL GAP PREDICTOR - DEMO")
    print("="*70)
    
    print("\n📄 SAMPLE RESUME:")
    print("-" * 70)
    print(SAMPLE_RESUME[:500] + "...")
    print("-" * 70)
    
    # Clean the resume text
    cleaned_resume = PDFReader.clean_text(SAMPLE_RESUME)
    
    # Analyze for each job role
    job_roles = get_all_job_roles()
    
    for role in job_roles:
        # Extract skills
        detected_skills = extract_skills_from_text(cleaned_resume, role)
        
        # Analyze match
        skill_match = analyze_skill_match(detected_skills, role)
        
        # Get TF-IDF score
        job_description = get_job_description(role)
        tfidf_score = calculate_resume_similarity(cleaned_resume, job_description)
        
        # Get recommendation
        skill_match_pct = skill_match['match_percentage']
        if skill_match_pct >= 75 and tfidf_score >= 70:
            recommendation = "Excellent match! You are well-qualified for this role. ✅"
            level = "excellent"
        elif skill_match_pct >= 50 and tfidf_score >= 50:
            recommendation = "Good match! With minor skill improvements, you'll be competitive. 👍"
            level = "good"
        elif skill_match_pct >= 25 or tfidf_score >= 30:
            recommendation = "Moderate match. Focus learning on key missing skills. 📚"
            level = "moderate"
        else:
            recommendation = "Significant skill gaps. Consider extensive preparation. ⚠️"
            level = "weak"
        
        results = {
            'job_role': role,
            'skill_match': skill_match,
            'tfidf_score': tfidf_score,
            'recommendation': recommendation,
            'level': level
        }
        
        print_results(role, results)
    
    print(f"\n{'='*70}")
    print("✨ Demo Complete! Try the web app at: python3 app.py")
    print(f"{'='*70}\n")


if __name__ == '__main__':
    main()
