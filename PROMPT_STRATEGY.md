PROMPT STRATEGY DOCUMENT
=================================
Resume Analyzer & Skill Gap Predictor

1. Introduction

The Resume Analyzer & Skill Gap Predictor is an AI-based system designed to help students understand how well their resumes align with a selected job role.
The system combines Machine Learning (TF-IDF + Cosine Similarity) with a structured prompt strategy to perform intelligent resume analysis and skill gap identification.

This document explains the prompt strategy used to guide the AI reasoning layer of the system.

2. Objective of Prompt Strategy

The main objectives of the prompt strategy are:

- To extract relevant technical skills from unstructured resume text

- To define required skills for a given job role

- To compare candidate skills with job requirements

- To identify missing skills (skill gap)

- To generate improvement and learning recommendations

The prompts ensure consistency, clarity, and explainability in AI-driven decision making.

3. Overall Prompt Flow Architecture

The system follows a sequential prompt-based reasoning flow:

1. Resume PDF is uploaded by the user

2. Text is extracted from the resume

3. Skills are identified using NLP prompts

4. Job role skill requirements are generated

5. Resume skills are compared with job skills

6. Skill gaps are identified

7. Learning recommendations are generated

This structured flow allows the AI to break down a complex task into smaller, understandable steps.

4. Prompt Templates Used
------------------------
4.1 Resume Skill Extraction Prompt

Purpose:
To extract all relevant technical skills from unstructured resume text.

Prompt Template:

You are an AI resume parser.

Extract all technical skills, tools, programming languages, and technologies 
from the following resume text.

Return only a clean comma-separated list of skills.

Resume Text:
{resume_text}

Expected Output:

Python, SQL, Machine Learning, Excel, Pandas, Data Visualization

4.2 Job Role Skill Definition Prompt

Purpose:
To identify essential skills required for a selected job role.

Prompt Template:

You are an AI career assistant.

List the essential technical skills required for the job role: {job_role}

Return only skills, without explanation.

Expected Output (Example – Data Analyst):

Python, SQL, Excel, Statistics, Data Visualization, Power BI

4.3 Resume vs Job Role Comparison Prompt

Purpose:
To compare extracted resume skills with job role requirements.

Prompt Template:

You are an AI evaluator.

Given:
Candidate Skills: {resume_skills}
Job Role Skills: {job_skills}

Identify:
1. Matched skills
2. Missing skills

Return the result in a structured format.

Expected Output:

Matched Skills: Python, SQL, Excel
Missing Skills: Statistics, Power BI

4.4 Skill Gap Analysis Prompt

Purpose:
To explain the impact of missing skills on job readiness.

Prompt Template:

You are an AI skill gap analyzer.

Based on the missing skills list:
{missing_skills}

Explain briefly how these skills affect job readiness.

Expected Output:

Lack of Statistics affects data interpretation accuracy.
Power BI is essential for business dashboard reporting.

4.5 Learning Recommendation Prompt

Purpose:
To guide candidates on how to improve their skills.

Prompt Template:

You are an AI mentor.

For the following missing skills:
{missing_skills}

Suggest beginner-friendly learning resources and a short learning path.

Expected Output:

Statistics – Learn probability and hypothesis testing from online courses.
Power BI – Start with beginner dashboard creation tutorials.

5. Integration with Machine Learning

The prompt strategy works alongside Machine Learning techniques:

- TF-IDF Vectorization converts text into numerical features

- Cosine Similarity measures resume-to-job match percentage

- Prompt-based reasoning interprets results and generates explanations

This hybrid approach ensures both quantitative accuracy and qualitative insights.

6. Why This Prompt Strategy Is Effective

- Handles unstructured resume data efficiently

- Breaks down complex analysis into simple AI tasks

- Improves explainability for judges and users

- Mimics real-world Applicant Tracking Systems (ATS)

- Suitable for beginner-friendly ML hackathon projects

7. Conclusion

The prompt strategy forms the AI reasoning backbone of the Resume Analyzer & Skill Gap Predictor.
By combining structured prompts with classical Machine Learning models, the system delivers intelligent, interpretable, and practical career insights for students.
