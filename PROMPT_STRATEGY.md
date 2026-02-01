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

---

## Purpose

- Document how to interact with the assistant to perform common developer tasks (edits, deploy fixes, debugging).  
- Provide reusable prompt templates for contributors and maintainers.  
- Preserve the session prompts used during development for reproducibility and auditing.

---

## Prompt Strategy (high level)

- Be explicit about the file paths and exact edits required.  
- For deployments/debugging, paste full error blocks and screenshots when possible.  
- For CLI operations, copy-paste terminal outputs (not screenshots) for easier parsing.  
- Prefer small, atomic changes with clear commit messages.  
- When asking the assistant to run commands or edit files in the repo, include the repository path and target branch.

---

## Reusable Prompt Templates

Use these templates when asking the assistant to perform common tasks.

- Patch & commit

  "Edit `path/to/file` to change X into Y, commit with message 'MSG', and push to `main`."

- Add documentation

  "Create `docs/NAME.md` that explains X, include examples and usage, commit and push."

- Debug deploy

  "Check Railway deploy logs for project `<project-name>` and identify any package build errors; suggest minimal changes to `requirements.txt` or `runtime.txt` and push fixes." 

- CLI help

  "Give exact Railway CLI commands to link the repo and stream logs, and explain expected outputs and where to paste them back." 

- Feature implementation

  "Implement feature `<short-description>`: modify backend, templates, and add tests. Provide a small example and commit with message 'feat: <short-description>'."

---

## Example Prompts Used During This Project

The following are the user prompts that were used in this development session (developer-supplied inputs). They are recorded here for reproducibility and context.

1. you push the change
2. yes
3. guide
4. ok i grant railway cli access
5. option a
6. where i can find railway api key
7. cannot find
8. option a
9. Paste your Railway API key here and I’ll login and stream the build logs. (developer supplied CLI feedback instead of key)
10. cannot find
11. ok i grant railway cli access
12. option a
13. where i can find railway api key
14. cannot find
15. this happened (attached Railway 404 screenshot)
16. again failed (attached build error screenshot)
17. yes
18. B
19. ok i grant railway cli access
20. option a
21. where i can find railway api key
22. cannot find
23. ok
24. what to do next
25. omawasthi@Oms-MacBook-Air ~ % npm i -g @railway/cli (terminal output pasted)
26. screenshot showing `npx @railway/cli@latest link`
27. what to do next
28. omawasthi@Oms-MacBook-Air ~ % npx @railway/cli@latest logs -f (error output pasted)
29. this happened (attached build logs screenshot)
30. again failed
31. this (Python runtime error screenshot)
32. what to do next
33. npx @railway/cli@latest logs -f --service web (error pasted)
34. this is showing (deploy logs showing Gunicorn boot)
35. but i thought the name of the website will come as ai humananalyxer
36. ok
37. no i want Prompt Template used and prompts used for this project
38. yes
39. no i want Prompt Template used and prompts used for this project (repeat)
40. yes (confirm show session prompts)
41. does my repo include the following items
42. ok add

---

## How to Reuse

- Copy any template above and fill in the placeholders (paths, messages).  
- When collaborating, include the branch name and intended commit message.  
- For troubleshooting, include CLI outputs and screenshots in the issue or chat.

---

## Security & Privacy

- Do not store or publish API keys, secrets, or private data in prompts or repository files.  
- Review logs and screenshots for sensitive information before pasting them into public channels.  
- If an API key must be provided for CLI automation, use a short-lived project-scoped token and rotate it immediately afterwards.

---

If you want this file adjusted (more examples, different wording, or removal of any prompts), tell me what to change and I will update it and push a new commit.
