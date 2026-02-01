#!/usr/bin/env python3
"""Create sample resumes with high TF-IDF scores"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

# Data Analyst Resume
data_analyst = """
JOHN ANDERSON
john.anderson@email.com | (555) 123-4567 | LinkedIn.com/in/johnanalyst | San Francisco, CA

PROFESSIONAL SUMMARY
Experienced Data Analyst with 5+ years expertise in SQL queries, Python analysis, and data visualization. Skilled in statistical analysis, business intelligence, and dashboard creation. Proficient in data extraction, report generation, and trend analysis. Strong background in Excel pivot tables and data modeling for enterprise applications. Proven track record delivering actionable insights through advanced analytics.

PROFESSIONAL EXPERIENCE

Senior Data Analyst | Tech Solutions Inc | 2022-Present
• Led complex SQL queries to extract and analyze large datasets from multiple enterprise databases
• Created interactive dashboards for business intelligence reporting using Tableau and Power BI
• Performed statistical analysis on customer behavior patterns using Python and pandas
• Optimized data extraction processes, reducing report generation time by 40%
• Conducted comprehensive trend analysis and forecasting for strategic business planning
• Designed advanced data modeling frameworks for improved data visualization capabilities
• Generated quarterly business reports using Excel pivot tables and advanced analytics
• Managed data cleaning and transformation for multiple analytics projects

Data Analyst | Finance Solutions Corp | 2020-2022
• Executed complex SQL queries for financial data analysis and regulatory reporting
• Developed business intelligence dashboards and real-time visualizations
• Performed statistical analysis to identify market trends and insights
• Created Python analysis scripts for automated data processing and reporting
• Generated trend analysis reports for executive stakeholder presentations
• Utilized advanced Excel pivot tables for data summarization and analysis
• Supported data extraction from SQL databases and data warehouses

Junior Data Analyst | StartUp Innovations | 2018-2020
• Supported data extraction and database query development using SQL
• Assisted in dashboard creation and data visualization projects
• Performed basic statistical analysis on operational data
• Contributed to report generation and data cleaning initiatives

TECHNICAL SKILLS
Data Visualization, SQL queries, Python analysis, Statistical analysis, Business intelligence, Dashboard creation, Data extraction, Report generation, Data cleaning, Trend analysis, Excel pivot tables, Data modeling, Tableau, Power BI, Advanced Excel, Database management, SQL optimization, ETL processes, Data warehouse, Forecasting, Data transformation

CERTIFICATIONS & EDUCATION
Google Data Analytics Professional Certificate
Microsoft Certified: Data Analyst Associate
Bachelor of Science in Statistics | State University | 2018
"""

# Web Developer Resume
web_developer = """
SARAH WILLIAMS
sarah.williams@email.com | (555) 987-6543 | GitHub.com/sarahdev | Austin, TX

PROFESSIONAL SUMMARY
Full-stack Web Developer with 6+ years of expertise in responsive design and frontend development. Proven track record in backend integration, API development, and database design. Skilled in version control, code optimization, bug fixes, and user interface development. Experienced in full-stack development, testing and debugging, and performance optimization across modern frameworks.

PROFESSIONAL EXPERIENCE

Senior Web Developer | Digital Solutions Agency | 2021-Present
• Developed responsive design implementations using HTML5, CSS3, and JavaScript
• Built robust backend integration systems with RESTful API development
• Optimized frontend performance through advanced code optimization and caching strategies
• Implemented comprehensive testing and debugging protocols across projects
• Led performance optimization initiatives improving page load times by 50%
• Managed version control using Git and GitHub for team collaboration
• Designed and implemented scalable database design schemas for applications
• Conducted user interface improvements based on usability research and feedback

Full-Stack Developer | Web Solutions Company | 2019-2021
• Created responsive design layouts for mobile and desktop platforms
• Implemented API development for third-party service integrations
• Performed code optimization to reduce technical debt and improve efficiency
• Fixed critical bugs in production environments and deployed hotfixes
• Managed database design and optimization for application performance
• Contributed to version control processes and participated in code reviews
• Improved user interface components for better user experience

Junior Web Developer | StartUp Hub | 2017-2019
• Supported frontend development with HTML, CSS, and JavaScript
• Assisted in backend integration and API development tasks
• Participated in bug fixes and testing and debugging activities
• Learned responsive design principles and mobile-first implementation

TECHNICAL SKILLS
Responsive design, Frontend development, Backend integration, API development, Database design, Version control, Code optimization, Bug fixes, User interface, Full-stack development, Testing and debugging, Performance optimization, JavaScript, React, Node.js, Express.js, MongoDB, REST APIs, Git, HTML5, CSS3, Agile development, Web accessibility, AWS

CERTIFICATIONS & EDUCATION
Full-Stack Web Development Bootcamp Certificate
AWS Certified Cloud Practitioner
Bachelor of Science in Computer Science | Tech University | 2017
"""

# ML Engineer Resume
ml_engineer = """
ALEX KUMAR
alex.kumar@email.com | (555) 456-7890 | LinkedIn.com/in/alexmleng | Seattle, WA

PROFESSIONAL SUMMARY
Experienced Machine Learning Engineer specializing in model training and neural networks development. Expert in data preprocessing, feature engineering, and deep learning implementations. Proficient in algorithm development, model evaluation, and production deployment. Strong background in data pipeline management, optimization techniques, computer vision, and NLP implementation for enterprise solutions.

PROFESSIONAL EXPERIENCE

Senior ML Engineer | AI Research Labs | 2021-Present
• Designed and implemented neural networks for image classification using TensorFlow
• Conducted extensive data preprocessing and feature engineering for model optimization
• Led model training initiatives achieving 95% accuracy on validation datasets
• Deployed machine learning models to production environments at enterprise scale
• Developed automated data pipeline infrastructure for efficient data processing
• Implemented advanced deep learning solutions for computer vision applications
• Conducted NLP implementation projects for text analysis and document classification
• Performed comprehensive model evaluation using cross-validation and performance metrics
• Optimized algorithms for improved inference speed and accuracy

ML Engineer | Tech Innovations Inc | 2019-2021
• Built neural networks for predictive analytics and forecasting applications
• Implemented algorithm development for custom machine learning solutions
• Performed data preprocessing and advanced feature engineering on large datasets
• Conducted model training and evaluation for production deployment
• Created scalable data pipeline processes for efficient data handling
• Applied deep learning techniques for classification and regression tasks
• Implemented optimization techniques for enhanced model performance

Junior Data Scientist | DataCorp Analytics | 2017-2019
• Supported model training and neural network development projects
• Assisted in data preprocessing and feature engineering workflows
• Contributed to algorithm development and research initiatives
• Participated in model evaluation and testing activities

TECHNICAL SKILLS
Model training, Neural networks, Data preprocessing, Feature engineering, Deep learning, Algorithm development, Model evaluation, Production deployment, Data pipeline, Optimization techniques, Computer vision, NLP implementation, TensorFlow, PyTorch, Scikit-learn, Python, Pandas, NumPy, Jupyter, Keras, CUDA, Git, AWS, GCP, Azure, MLOps

CERTIFICATIONS & EDUCATION
Deep Learning Specialization Certificate (Coursera)
TensorFlow Developer Certificate
AWS Certified Machine Learning Specialty
Master of Science in Machine Learning | Tech Institute | 2019
Bachelor of Science in Mathematics | State University | 2017
"""

def create_resume_pdf(filename, content, title):
    """Create a PDF resume from text content"""
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    
    # Custom style for normal text
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        alignment=TA_LEFT
    )
    
    story = []
    
    for line in content.split('\n'):
        if line.strip():
            if len(line) > 80 and line[0] != ' ':
                # Heading
                heading_style = ParagraphStyle(
                    'Heading',
                    parent=styles['Normal'],
                    fontSize=11 if line.isupper() else 10,
                    leading=14,
                    textColor='#1f2937',
                    fontName='Helvetica-Bold' if line.isupper() else 'Helvetica'
                )
                story.append(Paragraph(line, heading_style))
            else:
                story.append(Paragraph(line, normal_style))
        else:
            story.append(Spacer(1, 0.08*inch))
    
    doc.build(story)
    print(f"✅ Created {title}")

# Create all three resumes
create_resume_pdf(
    '/Users/omawasthi/Downloads/files/sample_data_analyst_high_score.pdf',
    data_analyst,
    'Data Analyst Resume (High TF-IDF)'
)

create_resume_pdf(
    '/Users/omawasthi/Downloads/files/sample_web_developer_high_score.pdf',
    web_developer,
    'Web Developer Resume (High TF-IDF)'
)

create_resume_pdf(
    '/Users/omawasthi/Downloads/files/sample_ml_engineer_high_score.pdf',
    ml_engineer,
    'ML Engineer Resume (High TF-IDF)'
)

print("\n✅ All 3 sample resumes created successfully!")
print("📁 Location: /Users/omawasthi/Downloads/files/")
print("\nFiles created:")
print("  • sample_data_analyst_high_score.pdf")
print("  • sample_web_developer_high_score.pdf")
print("  • sample_ml_engineer_high_score.pdf")
