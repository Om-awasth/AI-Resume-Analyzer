"""
Skill Database and Learning Resources
Contains all job roles, required skills, and learning resources
"""

# Job Skills Database
JOB_SKILLS = {
    "Data Analyst": {
        "technical": [
            "Python", "R", "SQL", "Excel", "Power BI", "Tableau",
            "Pandas", "NumPy", "Matplotlib", "Seaborn", "Statistics",
            "Data Mining", "ETL", "A/B Testing", "Google Analytics",
            "MySQL", "PostgreSQL", "MongoDB", "Scala", "Apache Spark",
            "Looker", "SPSS", "SAS", "JavaScript", "DAX"
        ],
        "soft": [
            "Communication", "Problem Solving", "Attention to Detail",
            "Data Visualization", "Business Acumen", "Critical Thinking"
        ],
        "description": "Analyze data, create visualizations, and provide business insights"
    },
    
    "Web Developer": {
        "technical": [
            "HTML", "CSS", "JavaScript", "React", "Vue", "Angular",
            "Node.js", "Express", "PHP", "Django", "Flask", "Java",
            "C#", "TypeScript", "Git", "SQL", "MongoDB", "MySQL",
            "PostgreSQL", "REST API", "GraphQL", "Docker", "AWS",
            "Google Cloud", "Firebase", "webpack", "npm", "Sass",
            "Bootstrap", "Material UI", "Linux", "Agile"
        ],
        "soft": [
            "Communication", "Teamwork", "Problem Solving", "Creativity",
            "Time Management", "Attention to Detail"
        ],
        "description": "Build and maintain web applications using modern frameworks and technologies"
    },
    
    "ML Engineer": {
        "technical": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow",
            "PyTorch", "Keras", "scikit-learn", "Natural Language Processing",
            "Computer Vision", "Neural Networks", "Pandas", "NumPy",
            "Matplotlib", "Jupyter", "SQL", "Spark", "Hadoop", "AWS",
            "Google Cloud", "Docker", "Git", "Linux", "Statistics",
            "Linear Algebra", "Calculus", "R", "Scala", "Reinforcement Learning",
            "CNN", "RNN", "LSTM", "Transformers", "MLOps", "Kubernetes"
        ],
        "soft": [
            "Problem Solving", "Communication", "Research", "Attention to Detail",
            "Teamwork", "Creativity"
        ],
        "description": "Develop machine learning models and deploy AI solutions"
    }
}

# Learning Resources Database
LEARNING_RESOURCES = {
    # Data Analyst Resources
    "Python": {
        "courses": ["Python for Data Analysis (Coursera)", "Complete Python Bootcamp (Udemy)"],
        "websites": ["python.org", "realpython.com", "w3schools.com"],
        "duration": "4-6 weeks"
    },
    "SQL": {
        "courses": ["SQL for Data Analysis (Udacity)", "MySQL Masterclass (Udemy)"],
        "websites": ["sqlzoo.net", "mode.com/sql-tutorial", "hackerrank.com"],
        "duration": "3-4 weeks"
    },
    "Pandas": {
        "courses": ["Pandas Data Manipulation (Coursera)", "Pandas Course (DataCamp)"],
        "websites": ["pandas.pydata.org", "datacamp.com"],
        "duration": "2-3 weeks"
    },
    "Tableau": {
        "courses": ["Tableau Desktop Specialist (Udemy)", "Tableau Public (LinkedIn)"],
        "websites": ["tableau.com/public", "tableautraining.com"],
        "duration": "4-6 weeks"
    },
    "Power BI": {
        "courses": ["Power BI Desktop (Microsoft Learn)", "Power BI A-Z (Udemy)"],
        "websites": ["microsoft.com/power-bi", "powerbi.microsoft.com/learn"],
        "duration": "3-5 weeks"
    },
    "Statistics": {
        "courses": ["Statistics Fundamentals (Coursera)", "Statistics for Data Analysis (Udacity)"],
        "websites": ["khanacademy.org", "coursera.org"],
        "duration": "6-8 weeks"
    },
    "Excel": {
        "courses": ["Excel Skills for Data Analytics (Coursera)", "Microsoft Excel Course (Udemy)"],
        "websites": ["excel.tips", "support.microsoft.com/excel"],
        "duration": "2-3 weeks"
    },
    
    # Web Developer Resources
    "HTML": {
        "courses": ["HTML5 Basics (Udemy)", "HTML5 & CSS3 (Codecademy)"],
        "websites": ["html.spec.whatwg.org", "mdn.mozilla.org/html"],
        "duration": "1-2 weeks"
    },
    "CSS": {
        "courses": ["CSS3 Masterclass (Udemy)", "CSS from Scratch (Codecademy)"],
        "websites": ["css-tricks.com", "mdn.mozilla.org/css"],
        "duration": "2-3 weeks"
    },
    "JavaScript": {
        "courses": ["JavaScript Fundamentals (Udemy)", "JavaScript Full Course (Codecademy)"],
        "websites": ["developer.mozilla.org", "javascript.info"],
        "duration": "4-6 weeks"
    },
    "React": {
        "courses": ["React - The Complete Guide (Udemy)", "React for Beginners (Scrimba)"],
        "websites": ["react.dev", "reactjs.org"],
        "duration": "4-6 weeks"
    },
    "Node.js": {
        "courses": ["Node.js - The Complete Guide (Udemy)", "Node.js Basics (Coursera)"],
        "websites": ["nodejs.org", "expresjs.com"],
        "duration": "4-6 weeks"
    },
    "Vue": {
        "courses": ["Vue 3 Complete Guide (Udemy)", "Vue.js Basics (Pluralsight)"],
        "websites": ["vuejs.org", "vuetifyjs.com"],
        "duration": "3-5 weeks"
    },
    "Angular": {
        "courses": ["Angular - The Complete Guide (Udemy)", "Angular Fundamentals (Pluralsight)"],
        "websites": ["angular.io", "angularjs.org"],
        "duration": "5-7 weeks"
    },
    "Express": {
        "courses": ["Express.js Course (Udemy)", "Express Fundamentals (Pluralsight)"],
        "websites": ["expressjs.com", "developer.mozilla.org"],
        "duration": "3-4 weeks"
    },
    "MongoDB": {
        "courses": ["MongoDB Complete Course (Udemy)", "MongoDB Basics (MongoDB University)"],
        "websites": ["mongodb.com", "docs.mongodb.com"],
        "duration": "3-4 weeks"
    },
    "Git": {
        "courses": ["Git & GitHub Complete Course (Udemy)", "Git Basics (Codecademy)"],
        "websites": ["git-scm.com", "github.com/git-tips"],
        "duration": "1-2 weeks"
    },
    "Docker": {
        "courses": ["Docker & Kubernetes (Udemy)", "Docker Mastery (Pluralsight)"],
        "websites": ["docker.com", "docs.docker.com"],
        "duration": "3-4 weeks"
    },
    
    # ML Engineer Resources
    "TensorFlow": {
        "courses": ["TensorFlow Complete Guide (Coursera)", "Deep Learning with TensorFlow (Udemy)"],
        "websites": ["tensorflow.org", "tensorflow.org/learn"],
        "duration": "5-7 weeks"
    },
    "PyTorch": {
        "courses": ["PyTorch for Deep Learning (Udemy)", "Deep Learning with PyTorch (DataCamp)"],
        "websites": ["pytorch.org", "pytorch.org/tutorials"],
        "duration": "5-7 weeks"
    },
    "Deep Learning": {
        "courses": ["Deep Learning Specialization (Coursera)", "Deep Learning A-Z (Udemy)"],
        "websites": ["deeplearningbook.org", "fast.ai"],
        "duration": "8-12 weeks"
    },
    "Computer Vision": {
        "courses": ["Computer Vision Specialization (Coursera)", "OpenCV Complete Course (Udemy)"],
        "websites": ["opencv.org", "pyimagesearch.com"],
        "duration": "6-8 weeks"
    },
    "Natural Language Processing": {
        "courses": ["NLP with Deep Learning (Coursera)", "NLP Complete Guide (Udemy)"],
        "websites": ["nlp.stanford.edu", "huggingface.co"],
        "duration": "6-8 weeks"
    },
    "Keras": {
        "courses": ["Keras Tutorial (Coursera)", "Keras Deep Learning (DataCamp)"],
        "websites": ["keras.io", "keras.io/guides"],
        "duration": "3-4 weeks"
    },
    "scikit-learn": {
        "courses": ["scikit-learn Basics (DataCamp)", "Machine Learning with scikit-learn (Coursera)"],
        "websites": ["scikit-learn.org", "scikit-learn.org/stable"],
        "duration": "3-4 weeks"
    },
    "Neural Networks": {
        "courses": ["Neural Networks Fundamentals (Udemy)", "Neural Networks for ML (Coursera)"],
        "websites": ["neuralnetworksanddeeplearning.com"],
        "duration": "5-6 weeks"
    },
    "Spark": {
        "courses": ["Apache Spark Complete Course (Udemy)", "Spark Fundamentals (Coursera)"],
        "websites": ["spark.apache.org", "databricks.com"],
        "duration": "4-6 weeks"
    },
    "AWS": {
        "courses": ["AWS Solutions Architect (Coursera)", "AWS Complete Course (Udemy)"],
        "websites": ["aws.amazon.com", "aws.amazon.com/training"],
        "duration": "4-6 weeks"
    },
    
    # Generic/Common Resources
    "R": {
        "courses": ["R Programming Fundamentals (Coursera)", "R Complete Guide (Udemy)"],
        "websites": ["r-project.org", "rstudio.com"],
        "duration": "4-6 weeks"
    },
    "Linux": {
        "courses": ["Linux Command Line (Udemy)", "Linux Fundamentals (Coursera)"],
        "websites": ["linux.com", "linuxcommand.org"],
        "duration": "3-4 weeks"
    },
    "Communication": {
        "courses": ["Effective Communication (Coursera)", "Public Speaking (Udemy)"],
        "websites": ["toastmasters.org", "coursera.org"],
        "duration": "4-6 weeks"
    },
    "Problem Solving": {
        "courses": ["Problem Solving Techniques (Coursera)", "Critical Thinking (Udemy)"],
        "websites": ["coursera.org", "linkedin.com/learning"],
        "duration": "2-3 weeks"
    },
    "Tableau": {
        "courses": ["Tableau Desktop Specialist (Udemy)", "Tableau Public (LinkedIn Learning)"],
        "websites": ["tableau.com/public", "tableautraining.com"],
        "duration": "4-6 weeks"
    },
    "Power BI": {
        "courses": ["Power BI Desktop (Microsoft Learn)", "Power BI A-Z (Udemy)"],
        "websites": ["microsoft.com/power-bi", "powerbi.microsoft.com/learn"],
        "duration": "3-5 weeks"
    },
    "Data Mining": {
        "courses": ["Data Mining with Python (Udemy)", "Data Mining Fundamentals (Coursera)"],
        "websites": ["kdnuggets.com", "coursera.org"],
        "duration": "5-6 weeks"
    },
    "ETL": {
        "courses": ["ETL Fundamentals (Udemy)", "Data Integration (Coursera)"],
        "websites": ["talend.com/resources", "informatica.com/en"],
        "duration": "4-5 weeks"
    },
    "A/B Testing": {
        "courses": ["A/B Testing Course (Udacity)", "Experimentation at Scale (Coursera)"],
        "websites": ["optimizely.com/resources", "vwo.com/resources"],
        "duration": "2-3 weeks"
    },
    "Google Analytics": {
        "courses": ["Google Analytics Certificate (Google)", "Google Analytics Mastery (Udemy)"],
        "websites": ["analytics.google.com", "marketingplatform.google.com/about"],
        "duration": "2-3 weeks"
    },
    "MySQL": {
        "courses": ["MySQL Complete Course (Udemy)", "MySQL Fundamentals (Pluralsight)"],
        "websites": ["mysql.com", "dev.mysql.com/doc"],
        "duration": "3-4 weeks"
    },
    "PostgreSQL": {
        "courses": ["PostgreSQL Complete Course (Udemy)", "PostgreSQL Fundamentals (Coursera)"],
        "websites": ["postgresql.org", "postgresqltutorial.com"],
        "duration": "3-4 weeks"
    },
    "MongoDB": {
        "courses": ["MongoDB Complete Course (Udemy)", "MongoDB Basics (MongoDB University)"],
        "websites": ["mongodb.com", "docs.mongodb.com"],
        "duration": "3-4 weeks"
    },
    "Matplotlib": {
        "courses": ["Matplotlib Tutorial (DataCamp)", "Data Visualization with Matplotlib (Udemy)"],
        "websites": ["matplotlib.org", "matplotlib.org/stable"],
        "duration": "2-3 weeks"
    },
    "Seaborn": {
        "courses": ["Seaborn Data Visualization (DataCamp)", "Advanced Visualization (Udemy)"],
        "websites": ["seaborn.pydata.org", "kaggle.com/learn/data-visualization"],
        "duration": "2-3 weeks"
    },
    "NumPy": {
        "courses": ["NumPy Basics (DataCamp)", "NumPy Complete Course (Udemy)"],
        "websites": ["numpy.org", "numpy.org/doc"],
        "duration": "2-3 weeks"
    },
    "Data Visualization": {
        "courses": ["Data Visualization Fundamentals (Coursera)", "Visual Analytics (Udemy)"],
        "websites": ["d3js.org", "observable.com"],
        "duration": "4-5 weeks"
    },
    "Attention to Detail": {
        "courses": ["Quality Assurance Training (Udemy)", "Precision and Excellence (LinkedIn)"],
        "websites": ["linkedin.com/learning", "udemy.com"],
        "duration": "1-2 weeks"
    },
    "Teamwork": {
        "courses": ["Teamwork Essentials (Coursera)", "Collaboration Skills (LinkedIn Learning)"],
        "websites": ["linkedin.com/learning", "coursera.org"],
        "duration": "2-3 weeks"
    },
    "Creativity": {
        "courses": ["Creative Thinking (Coursera)", "Innovation and Creativity (Udemy)"],
        "websites": ["coursera.org", "linkedin.com/learning"],
        "duration": "3-4 weeks"
    },
    "Critical Thinking": {
        "courses": ["Critical Thinking Skills (Udemy)", "Logic and Reasoning (Coursera)"],
        "websites": ["linkedin.com/learning", "coursera.org"],
        "duration": "2-3 weeks"
    },
    "Business Acumen": {
        "courses": ["Business Fundamentals (Coursera)", "Business Strategy (LinkedIn)"],
        "websites": ["linkedin.com/learning", "businessnewsdaily.com"],
        "duration": "4-6 weeks"
    },
    "TypeScript": {
        "courses": ["TypeScript Complete Guide (Udemy)", "TypeScript Fundamentals (Pluralsight)"],
        "websites": ["typescriptlang.org", "typescriptlang.org/docs"],
        "duration": "3-4 weeks"
    },
    "PHP": {
        "courses": ["PHP Complete Course (Udemy)", "PHP Fundamentals (Coursera)"],
        "websites": ["php.net", "phptutorial.net"],
        "duration": "4-5 weeks"
    },
    "Django": {
        "courses": ["Django for Beginners (Udemy)", "Django Complete Guide (Coursera)"],
        "websites": ["djangoproject.com", "docs.djangoproject.com"],
        "duration": "4-6 weeks"
    },
    "Flask": {
        "courses": ["Flask by Example (Udemy)", "Flask Fundamentals (Pluralsight)"],
        "websites": ["flask.palletsprojects.com", "flask.palletsprojects.com/en"],
        "duration": "3-4 weeks"
    },
    "Java": {
        "courses": ["Java Programming for Beginners (Udemy)", "Java Fundamentals (Oracle)"],
        "websites": ["java.com", "docs.oracle.com/javase"],
        "duration": "6-8 weeks"
    },
    "C#": {
        "courses": ["C# Complete Course (Udemy)", "C# Fundamentals (Microsoft)"],
        "websites": ["microsoft.com/dotnet/languages/csharp", "docs.microsoft.com/dotnet/csharp"],
        "duration": "5-7 weeks"
    },
    "REST API": {
        "courses": ["REST API Design (Udemy)", "Building REST APIs (Coursera)"],
        "websites": ["restfulapi.net", "docs.microsoft.com/rest"],
        "duration": "3-4 weeks"
    },
    "GraphQL": {
        "courses": ["GraphQL Complete Course (Udemy)", "GraphQL Fundamentals (Pluralsight)"],
        "websites": ["graphql.org", "graphql.org/learn"],
        "duration": "3-4 weeks"
    },
    "Google Cloud": {
        "courses": ["Google Cloud Associate (Coursera)", "GCP Complete Guide (Udemy)"],
        "websites": ["cloud.google.com", "cloud.google.com/training"],
        "duration": "4-6 weeks"
    },
    "Firebase": {
        "courses": ["Firebase Complete Guide (Udemy)", "Firebase Fundamentals (Coursera)"],
        "websites": ["firebase.google.com", "firebase.google.com/docs"],
        "duration": "2-3 weeks"
    },
    "Webpack": {
        "courses": ["Webpack Course (Udemy)", "Module Bundling (Pluralsight)"],
        "websites": ["webpack.js.org", "webpack.js.org/concepts"],
        "duration": "2-3 weeks"
    },
    "npm": {
        "courses": ["npm Mastery (Udemy)", "Node Package Manager (Coursera)"],
        "websites": ["npmjs.com", "docs.npmjs.com"],
        "duration": "1-2 weeks"
    },
    "Sass": {
        "courses": ["Sass & SCSS Complete Course (Udemy)", "Advanced CSS with Sass (Coursera)"],
        "websites": ["sass-lang.com", "sass-lang.com/documentation"],
        "duration": "2-3 weeks"
    },
    "Bootstrap": {
        "courses": ["Bootstrap 5 Course (Udemy)", "Bootstrap Framework (Coursera)"],
        "websites": ["getbootstrap.com", "getbootstrap.com/docs"],
        "duration": "2-3 weeks"
    },
    "Material UI": {
        "courses": ["Material UI Tutorial (Udemy)", "Material Design (Google)"],
        "websites": ["mui.com", "material.io/design"],
        "duration": "2-3 weeks"
    },
    "Agile": {
        "courses": ["Agile Fundamentals (Coursera)", "Scrum Master Certification (Udemy)"],
        "websites": ["agilemanifesto.org", "scrum.org"],
        "duration": "3-4 weeks"
    },
    "Kubernetes": {
        "courses": ["Kubernetes Complete Guide (Udemy)", "Kubernetes Fundamentals (Pluralsight)"],
        "websites": ["kubernetes.io", "kubernetes.io/docs"],
        "duration": "4-6 weeks"
    },
    "MLOps": {
        "courses": ["MLOps Fundamentals (Coursera)", "Machine Learning Ops (Udemy)"],
        "websites": ["mlops.community", "papers.mlops.community"],
        "duration": "5-6 weeks"
    },
    "CNN": {
        "courses": ["Convolutional Neural Networks (Coursera)", "CNN Deep Dive (Udemy)"],
        "websites": ["cs231n.github.io", "deeplearning.ai"],
        "duration": "4-5 weeks"
    },
    "RNN": {
        "courses": ["Recurrent Neural Networks (Coursera)", "RNN Complete Guide (Udemy)"],
        "websites": ["colah.github.io", "karpathy.github.io"],
        "duration": "4-5 weeks"
    },
    "LSTM": {
        "courses": ["LSTM and Sequence Models (Coursera)", "Long Short-Term Memory (Udemy)"],
        "websites": ["colah.github.io", "deeplearning.ai"],
        "duration": "3-4 weeks"
    },
    "Transformers": {
        "courses": ["Transformer Models (Coursera)", "Attention is All You Need (Udemy)"],
        "websites": ["huggingface.co", "jalammar.github.io"],
        "duration": "4-5 weeks"
    },
    "Reinforcement Learning": {
        "courses": ["Deep Reinforcement Learning (Coursera)", "RL Complete Guide (Udemy)"],
        "websites": ["spinningup.openai.com", "deepmind.com"],
        "duration": "6-8 weeks"
    },
    "Calculus": {
        "courses": ["Calculus Fundamentals (Coursera)", "Calculus for Data Science (Udemy)"],
        "websites": ["khanacademy.org/math/calculus", "mathinsight.org"],
        "duration": "5-6 weeks"
    },
    "Linear Algebra": {
        "courses": ["Linear Algebra Essentials (Coursera)", "Math for Machine Learning (Udemy)"],
        "websites": ["khanacademy.org/math/linear-algebra", "3blue1brown.com"],
        "duration": "4-5 weeks"
    },
    "Scala": {
        "courses": ["Scala Programming (Coursera)", "Scala Complete Course (Udemy)"],
        "websites": ["scala-lang.org", "docs.scala-lang.org"],
        "duration": "4-5 weeks"
    },
    "Hadoop": {
        "courses": ["Hadoop Big Data Course (Udemy)", "Hadoop Fundamentals (Coursera)"],
        "websites": ["hadoop.apache.org", "hadoop.apache.org/docs"],
        "duration": "5-6 weeks"
    },
    "SPSS": {
        "courses": ["SPSS Statistics (Udemy)", "IBM SPSS Training (IBM)"],
        "websites": ["ibm.com/spss", "ibm.com/support/spss"],
        "duration": "3-4 weeks"
    },
    "SAS": {
        "courses": ["SAS Programming (SAS)", "SAS Complete Course (Udemy)"],
        "websites": ["sas.com", "support.sas.com/training"],
        "duration": "4-6 weeks"
    },
    "DAX": {
        "courses": ["DAX for Power BI (Udemy)", "DAX Fundamentals (Microsoft)"],
        "websites": ["microsoft.com/power-bi", "dax.guide"],
        "duration": "3-4 weeks"
    },
    "Looker": {
        "courses": ["Google Looker Training (Google)", "Looker Fundamentals (Udemy)"],
        "websites": ["looker.com", "cloud.google.com/looker/docs"],
        "duration": "3-4 weeks"
    }
}

# Job Descriptions for TF-IDF Comparison
JOB_DESCRIPTIONS = {
    "Data Analyst": """
    We are looking for a talented Data Analyst to join our team. 
    In this role, you will analyze complex data sets and provide actionable insights.
    
    Required Skills:
    - Proficiency in Python, R, or SQL
    - Experience with data visualization tools (Tableau, Power BI)
    - Strong understanding of statistics and data mining
    - Experience with Excel and ETL processes
    - Knowledge of databases (MySQL, PostgreSQL)
    - Familiarity with A/B testing and Google Analytics
    
    Responsibilities:
    - Extract and analyze data from various sources
    - Create meaningful visualizations and reports
    - Perform statistical analysis and A/B testing
    - Collaborate with business teams to identify data requirements
    - Optimize data collection and storage processes
    
    Qualifications:
    - Bachelor's degree in Statistics, Mathematics, Computer Science, or related field
    - 2-5 years of experience in data analysis
    - Strong problem-solving and communication skills
    - Attention to detail and data accuracy
    """,
    
    "Web Developer": """
    We are seeking a skilled Web Developer to create and maintain our web applications.
    You will work with modern technologies and collaborate with our design and backend teams.
    
    Required Skills:
    - Proficiency in HTML5, CSS3, and JavaScript
    - Experience with at least one modern framework (React, Vue, or Angular)
    - Backend development experience (Node.js, Express, or similar)
    - Database knowledge (SQL, MongoDB)
    - Version control (Git)
    - Understanding of RESTful APIs
    
    Responsibilities:
    - Develop responsive web applications
    - Implement user interfaces based on design specifications
    - Write clean, maintainable code
    - Collaborate with backend developers and designers
    - Debug and optimize web applications
    
    Qualifications:
    - Bachelor's degree in Computer Science or related field
    - 2-5 years of web development experience
    - Strong problem-solving skills
    - Excellent communication abilities
    - Portfolio of completed projects
    """,
    
    "ML Engineer": """
    We are looking for a Machine Learning Engineer to develop and deploy ML models.
    You will work on challenging problems involving AI and data science.
    
    Required Skills:
    - Strong Python programming skills
    - Deep knowledge of machine learning and deep learning
    - Experience with ML frameworks (TensorFlow, PyTorch)
    - Understanding of NLP and/or Computer Vision
    - Experience with data processing (Pandas, NumPy)
    - Knowledge of cloud platforms (AWS, GCP)
    - Familiarity with MLOps practices
    
    Responsibilities:
    - Design and implement machine learning models
    - Perform feature engineering and data preprocessing
    - Train and evaluate models
    - Deploy models to production
    - Optimize model performance
    - Collaborate with data teams
    
    Qualifications:
    - Bachelor's degree in Computer Science, Mathematics, or related field
    - 3-5 years of ML development experience
    - Understanding of statistics and linear algebra
    - Strong problem-solving skills
    - Research publication record (preferred)
    """
}

# Return functions for easy access
def get_job_skills(job_role):
    """Get skills for a specific job role"""
    return JOB_SKILLS.get(job_role, {})

def get_job_description(job_role):
    """Get job description for TF-IDF comparison"""
    return JOB_DESCRIPTIONS.get(job_role, "")

def get_learning_resource(skill):
    """Get learning resources for a specific skill"""
    return LEARNING_RESOURCES.get(skill, {
        "courses": ["Course not found"],
        "websites": ["Visit official documentation"],
        "duration": "Self-paced"
    })

def get_all_job_roles():
    """Get list of all available job roles"""
    return list(JOB_SKILLS.keys())


# Skill Assessment Questions Database
SKILL_QUESTIONS = {
    "Python": [
        {
            "question": "What keyword is used to create a function in Python?",
            "options": ["def", "function", "func", "define"],
            "correct": 0
        },
        {
            "question": "Which of these is a mutable data type in Python?",
            "options": ["tuple", "string", "list", "frozenset"],
            "correct": 2
        },
        {
            "question": "What does 'len()' function do?",
            "options": ["Returns the length of an object", "Deletes an object", "Creates a new object", "Converts to integer"],
            "correct": 0
        }
    ],
    "SQL": [
        {
            "question": "Which SQL keyword is used to retrieve data?",
            "options": ["GET", "SELECT", "FETCH", "RETRIEVE"],
            "correct": 1
        },
        {
            "question": "What does JOIN do in SQL?",
            "options": ["Combines rows from two or more tables", "Adds new rows", "Deletes rows", "Updates values"],
            "correct": 0
        },
        {
            "question": "Which clause filters records after grouping?",
            "options": ["WHERE", "HAVING", "FILTER", "GROUP"],
            "correct": 1
        }
    ],
    "JavaScript": [
        {
            "question": "What is the correct way to declare a variable in JavaScript?",
            "options": ["var x = 5;", "variable x = 5;", "x := 5;", "declare x = 5;"],
            "correct": 0
        },
        {
            "question": "What does 'typeof' operator return for an array?",
            "options": ["array", "object", "list", "Array"],
            "correct": 1
        },
        {
            "question": "Which method adds an element to the end of an array?",
            "options": ["add()", "push()", "append()", "insert()"],
            "correct": 1
        }
    ],
    "React": [
        {
            "question": "What is a React component?",
            "options": ["A CSS class", "A reusable piece of UI", "A JavaScript function", "Both B and C"],
            "correct": 3
        },
        {
            "question": "What hook is used to manage state in functional components?",
            "options": ["useEffect", "useState", "useContext", "useReducer"],
            "correct": 1
        },
        {
            "question": "What is the virtual DOM in React?",
            "options": ["A physical DOM in the browser", "A JavaScript representation of the UI", "A server-side DOM", "A CSS framework"],
            "correct": 1
        }
    ],
    "Git": [
        {
            "question": "What command creates a new Git repository?",
            "options": ["git create", "git init", "git new", "git setup"],
            "correct": 1
        },
        {
            "question": "Which command saves changes to the repository?",
            "options": ["git save", "git store", "git commit", "git push"],
            "correct": 2
        },
        {
            "question": "What does 'git pull' do?",
            "options": ["Uploads changes", "Fetches and merges remote changes", "Deletes files", "Creates a branch"],
            "correct": 1
        }
    ],
    "Excel": [
        {
            "question": "What symbol is used to start a formula in Excel?",
            "options": [":", "#", "=", "@"],
            "correct": 2
        },
        {
            "question": "Which function calculates the average of cells?",
            "options": ["AVG()", "MEAN()", "AVERAGE()", "SUM()"],
            "correct": 2
        },
        {
            "question": "What is a pivot table used for?",
            "options": ["Creating formulas", "Summarizing and analyzing data", "Drawing charts", "Formatting cells"],
            "correct": 1
        }
    ],
    "HTML": [
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hyperlinks and Text Markup Language"],
            "correct": 0
        },
        {
            "question": "Which tag is used for the largest heading?",
            "options": ["<h6>", "<h1>", "<h9>", "<heading>"],
            "correct": 1
        },
        {
            "question": "What attribute specifies the URL of a link?",
            "options": ["url", "link", "href", "src"],
            "correct": 2
        }
    ],
    "CSS": [
        {
            "question": "What does CSS stand for?",
            "options": ["Computer Style Sheets", "Cascading Style Sheets", "Creative Style System", "Colorful Style Sheets"],
            "correct": 1
        },
        {
            "question": "Which property changes text color?",
            "options": ["text-color", "color", "font-color", "text-style"],
            "correct": 1
        },
        {
            "question": "What is the default display value for div elements?",
            "options": ["inline", "block", "flex", "grid"],
            "correct": 1
        }
    ],
    "Pandas": [
        {
            "question": "What is a Pandas DataFrame?",
            "options": ["A series of numbers", "A 2D tabular data structure", "A Python dictionary", "A list of lists"],
            "correct": 1
        },
        {
            "question": "How do you read a CSV file using Pandas?",
            "options": ["pd.read_file()", "pd.read_csv()", "pd.load_csv()", "pd.open_csv()"],
            "correct": 1
        },
        {
            "question": "What does dropna() do in Pandas?",
            "options": ["Drops columns", "Removes null/NaN values", "Drops rows", "Deletes the dataframe"],
            "correct": 1
        }
    ],
    "NumPy": [
        {
            "question": "What is the basic data structure in NumPy?",
            "options": ["List", "Dictionary", "Array", "Set"],
            "correct": 2
        },
        {
            "question": "How do you create a NumPy array from a list?",
            "options": ["np.list()", "np.array()", "np.create()", "np.make()"],
            "correct": 1
        },
        {
            "question": "What function calculates the sum of array elements?",
            "options": ["np.add()", "np.sum()", "np.total()", "np.calc()"],
            "correct": 1
        }
    ]
}

def get_skill_questions(skill):
    """Get questions for a specific skill"""
    return SKILL_QUESTIONS.get(skill, [])

def get_all_testable_skills():
    """Get list of skills that have questions"""
    return list(SKILL_QUESTIONS.keys())

