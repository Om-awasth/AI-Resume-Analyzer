// Resume Analyzer JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const resumeFile = document.getElementById('resumeFile');
    const fileStatus = document.getElementById('fileStatus');
    const fileInputWrapper = document.querySelector('.file-input-wrapper');

    // File input handling
    resumeFile.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            if (file.type !== 'application/pdf') {
                fileStatus.textContent = '❌ Only PDF files are allowed';
                fileStatus.className = 'file-status error';
                resumeFile.value = '';
            } else if (file.size > 5 * 1024 * 1024) {
                fileStatus.textContent = '❌ File is too large (max 5MB)';
                fileStatus.className = 'file-status error';
                resumeFile.value = '';
            } else {
                fileStatus.textContent = `✅ ${file.name} selected`;
                fileStatus.className = 'file-status success';
            }
        }
    });

    // Drag and drop
    fileInputWrapper.addEventListener('dragover', function(e) {
        e.preventDefault();
        fileInputWrapper.style.backgroundColor = 'rgba(37, 99, 235, 0.2)';
    });

    fileInputWrapper.addEventListener('dragleave', function(e) {
        e.preventDefault();
        fileInputWrapper.style.backgroundColor = 'rgba(37, 99, 235, 0.05)';
    });

    fileInputWrapper.addEventListener('drop', function(e) {
        e.preventDefault();
        fileInputWrapper.style.backgroundColor = 'rgba(37, 99, 235, 0.05)';
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            resumeFile.files = files;
            const event = new Event('change', { bubbles: true });
            resumeFile.dispatchEvent(event);
        }
    });

    // Form submission
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const file = resumeFile.files[0];
        const jobRole = document.getElementById('jobRole').value;

        // Validation
        if (!file) {
            showError('Please select a resume file');
            return;
        }

        if (!jobRole) {
            showError('Please select a job role');
            return;
        }

        // Show loading state
        showLoading();

        // Prepare form data
        const formData = new FormData();
        formData.append('resume', file);
        formData.append('job_role', jobRole);

        try {
            // Send request
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                showError(data.error || 'An error occurred');
                hideLoading();
                return;
            }

            // Display results
            displayResults(data);
            hideLoading();
            showResults();

        } catch (error) {
            console.error('Error:', error);
            showError('Network error. Please try again.');
            hideLoading();
        }
    });
});

function showLoading() {
    document.getElementById('uploadForm').style.display = 'none';
    document.getElementById('loadingState').style.display = 'flex';
    document.getElementById('errorState').style.display = 'none';
}

function hideLoading() {
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('uploadForm').style.display = 'flex';
}

function showError(message) {
    document.getElementById('errorMessage').textContent = '❌ ' + message;
    document.getElementById('errorState').style.display = 'flex';
    document.getElementById('uploadForm').style.display = 'flex';
}

function showResults() {
    document.querySelector('.analyzer-section').scrollIntoView({ behavior: 'smooth' });
    document.getElementById('resultsSection').style.display = 'block';
}

function displayResults(data) {
    // Set job role
    document.querySelector('.results-container').dataset.jobRole = data.job_role;

    // Update scores
    document.getElementById('skillMatchScore').textContent = 
        data.skill_match.match_percentage + '%';
    document.getElementById('skillMatchDetail').textContent = 
        `${data.skill_match.matched_count}/${data.skill_match.required_count} skills`;
    document.getElementById('tfidfScore').textContent = 
        Math.round(data.tfidf_score) + '%';

    // Update recommendation
    document.getElementById('recommendationText').textContent = data.recommendation;
    const recommendationBox = document.getElementById('recommendationBox');
    recommendationBox.className = 'recommendation-box ' + data.level;

    // Update contact information
    if (data.contact.email || data.contact.phone) {
        document.getElementById('contactSection').style.display = 'block';
        document.getElementById('contactEmail').textContent = 
            data.contact.email || 'Not provided';
        document.getElementById('contactPhone').textContent = 
            data.contact.phone || 'Not provided';
    } else {
        document.getElementById('contactSection').style.display = 'none';
    }

    // Display matched skills
    displaySkills(data.skill_match.matched, 'matchedSkillsContainer', 'matched');

    // Display missing skills
    displaySkills(data.skill_match.missing, 'missingSkillsContainer', 'missing');

    // Display learning resources
    displayResources(data.resources);

    // Display improvement tips
    displayImprovementTips(data.tfidf_score, data.skill_match.match_percentage, data.job_role);
}

function displaySkills(skills, containerId, type) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';

    if (skills.length === 0) {
        container.innerHTML = '<p style="color: #64748b;">No skills found</p>';
        return;
    }

    skills.forEach(skill => {
        const badge = document.createElement('span');
        badge.className = `skill-badge ${type}`;
        badge.textContent = skill;
        container.appendChild(badge);
    });
}

function displayResources(resources) {
    const container = document.getElementById('resourcesContainer');
    container.innerHTML = '';

    if (Object.keys(resources).length === 0) {
        container.innerHTML = '<p style="color: #64748b; grid-column: 1/-1;">No missing skills to learn!</p>';
        return;
    }

    Object.entries(resources).forEach(([skill, resource]) => {
        const card = document.createElement('div');
        card.className = 'resource-card';

        let coursesHtml = '';
        if (resource.courses && resource.courses.length > 0) {
            coursesHtml = `
                <div class="resource-item">
                    <strong>📚 Courses:</strong><br>
                    ${resource.courses.slice(0, 2).join('<br>')}
                </div>
            `;
        }

        let websiteHtml = '';
        if (resource.websites && resource.websites.length > 0) {
            websiteHtml = `
                <div class="resource-item">
                    <strong>🌐 Website:</strong><br>
                    ${resource.websites[0]}
                </div>
            `;
        }

        card.innerHTML = `
            <div class="resource-skill-name">${skill}</div>
            ${coursesHtml}
            ${websiteHtml}
            <div class="resource-item">
                <strong>⏱️ Duration:</strong><br>
                ${resource.duration}
            </div>
        `;

        container.appendChild(card);
    });
}

function resetForm() {
    document.getElementById('uploadForm').reset();
    document.getElementById('fileStatus').textContent = '';
    document.getElementById('resultsSection').style.display = 'none';
    document.querySelector('.analyzer-section').scrollIntoView({ behavior: 'smooth' });
}

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Skill Testing Functions
function displaySkillTests(detectedSkills) {
    const container = document.getElementById('skillTestButtons');
    container.innerHTML = '';

    // Filter skills that have available tests
    const testableSkills = [
        'Python', 'SQL', 'JavaScript', 'React', 'Git', 'Excel', 
        'HTML', 'CSS', 'Pandas', 'NumPy'
    ];

    const skillsToTest = detectedSkills.filter(skill => testableSkills.includes(skill));

    if (skillsToTest.length === 0) {
        document.getElementById('skillTestSection').style.display = 'none';
        return;
    }

    document.getElementById('skillTestSection').style.display = 'block';

    skillsToTest.forEach(skill => {
        const badge = document.createElement('span');
        badge.className = 'skill-badge';
        badge.textContent = skill;
        badge.style.cursor = 'pointer';
        badge.onclick = () => startSkillTest(skill);
        container.appendChild(badge);
    });
}

async function startSkillTest(skill) {
    try {
        const response = await fetch(`/skill-test/${skill}`);
        const data = await response.json();

        if (!response.ok) {
            alert('No test available for this skill');
            return;
        }

        // Display quiz modal
        document.getElementById('quizTitle').textContent = `${skill} Assessment`;
        displayQuizQuestions(data.questions);
        document.getElementById('quizModal').style.display = 'block';

        // Store current skill for submission
        window.currentTestSkill = skill;
    } catch (error) {
        console.error('Error loading test:', error);
        alert('Failed to load test');
    }
}

function displayQuizQuestions(questions) {
    const container = document.getElementById('questionContainer');
    container.innerHTML = '';

    questions.forEach((q, index) => {
        const questionBox = document.createElement('div');
        questionBox.className = 'question-box';

        const questionNum = document.createElement('div');
        questionNum.className = 'question-number';
        questionNum.textContent = `Question ${index + 1}`;

        const questionText = document.createElement('div');
        questionText.className = 'question-text';
        questionText.textContent = q.question;

        const optionsList = document.createElement('div');
        optionsList.className = 'options-list';

        q.options.forEach((option, optIndex) => {
            const optionDiv = document.createElement('div');
            optionDiv.className = 'option';

            const radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = `question-${index}`;
            radio.id = `q${index}_opt${optIndex}`;
            radio.value = optIndex;
            radio.dataset.questionIndex = index;

            const label = document.createElement('label');
            label.htmlFor = radio.id;
            label.textContent = option;
            label.style.margin = '0';

            optionDiv.appendChild(radio);
            optionDiv.appendChild(label);
            optionsList.appendChild(optionDiv);
        });

        questionBox.appendChild(questionNum);
        questionBox.appendChild(questionText);
        questionBox.appendChild(optionsList);
        container.appendChild(questionBox);
    });
}

function closeQuiz() {
    document.getElementById('quizModal').style.display = 'none';
    window.currentTestSkill = null;
}

async function submitQuiz() {
    try {
        // Get all answers
        const answers = [];
        const questions = document.querySelectorAll('.question-box');

        questions.forEach((_, index) => {
            const selected = document.querySelector(`input[name="question-${index}"]:checked`);
            if (!selected) {
                alert('Please answer all questions');
                throw new Error('Incomplete');
            }
            answers.push(parseInt(selected.value));
        });

        // Submit to backend
        const response = await fetch('/check-answers', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                skill: window.currentTestSkill,
                answers: answers
            })
        });

        const results = await response.json();

        if (!response.ok) {
            alert('Error checking answers');
            return;
        }

        // Display results
        displayTestResults(results);

    } catch (error) {
        if (error.message !== 'Incomplete') {
            console.error('Error:', error);
        }
    }
}

function displayTestResults(results) {
    const container = document.getElementById('resultsContent');
    
    const scoreClass = results.passed ? 'passed' : 'failed';
    const statusText = results.passed ? '✅ Passed!' : '❌ Needs Improvement';

    let resultsHTML = `
        <div class="score-display">${results.score}%</div>
        <div class="score-text">${results.correct} out of ${results.total} correct</div>
        <div class="result-status ${scoreClass}">${statusText}</div>
        <div class="result-details">
    `;

    results.results.forEach(r => {
        const resultClass = r.is_correct ? 'correct' : 'incorrect';
        const resultIcon = r.is_correct ? '✅' : '❌';

        resultsHTML += `
            <div class="result-item ${resultClass}">
                <div class="result-question">${r.question}</div>
                <div class="result-answer">
                    Your answer: <strong>${r.user_answer}</strong>
                </div>
        `;

        if (!r.is_correct) {
            resultsHTML += `
                <div class="result-answer">
                    Correct answer: <strong class="result-correct">${r.correct_answer}</strong>
                </div>
            `;
        }

        resultsHTML += `</div>`;
    });

    resultsHTML += `</div>`;

    container.innerHTML = resultsHTML;
    closeQuiz();
    document.getElementById('resultsModal').style.display = 'block';
}

function closeResults() {
    document.getElementById('resultsModal').style.display = 'none';
}

function displayImprovementTips(tfidfScore, skillMatch, jobRole) {
    const tipsContainer = document.getElementById('tipsSection');
    const tfidfTipsList = document.getElementById('tfidfTips');
    const keywordsContainer = document.getElementById('keywordsContainer');

    // Show tips section if score is below 80%
    if (tfidfScore >= 80 && skillMatch >= 75) {
        tipsContainer.style.display = 'none';
        return;
    }

    tipsContainer.style.display = 'block';

    // Generate TF-IDF improvement tips
    const tips = [
        "✏️ Add specific keywords from the job description to your resume",
        "📝 Use the same terminology and phrases found in the job posting",
        "🎯 Include relevant job titles and role-specific terms",
        "💼 Highlight projects and achievements using industry keywords",
        "🔑 Add technical skills and tools mentioned in the job description",
        "📋 Use action verbs that match the job requirements (led, developed, designed, etc.)",
        "🏆 Mention metrics and results using similar language to the posting",
        "🔍 Include any certifications or qualifications mentioned in the role",
        "📄 Ensure your professional summary contains relevant keywords",
        "💡 Focus on outcomes that directly relate to the job role"
    ];

    tfidfTipsList.innerHTML = '';
    tips.forEach(tip => {
        const li = document.createElement('li');
        li.textContent = tip;
        tfidfTipsList.appendChild(li);
    });

    // Generate relevant keywords based on job role
    const keywordsByRole = {
        'Data Analyst': [
            'Data visualization', 'SQL queries', 'Python analysis', 'Statistical analysis',
            'Business intelligence', 'Dashboard creation', 'Data extraction', 'Report generation',
            'Data cleaning', 'Trend analysis', 'Excel pivot tables', 'Data modeling'
        ],
        'Web Developer': [
            'Responsive design', 'Frontend development', 'Backend integration', 'API development',
            'Database design', 'Version control', 'Code optimization', 'Bug fixes',
            'User interface', 'Full-stack development', 'Testing and debugging', 'Performance optimization'
        ],
        'ML Engineer': [
            'Model training', 'Neural networks', 'Data preprocessing', 'Feature engineering',
            'Deep learning', 'Algorithm development', 'Model evaluation', 'Production deployment',
            'Data pipeline', 'Optimization techniques', 'Computer vision', 'NLP implementation'
        ]
    };

    const relevantKeywords = keywordsByRole[jobRole] || keywordsByRole['Data Analyst'];

    keywordsContainer.innerHTML = '';
    relevantKeywords.forEach(keyword => {
        const badge = document.createElement('span');
        badge.className = 'keyword-badge';
        badge.textContent = keyword;
        keywordsContainer.appendChild(badge);
    });
}

// --- User account interactions ---
async function signup(username, password, phone) {
    const res = await fetch('/signup', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, phone, password })
    });
    return res.json();
}

async function login(username, password, phone) {
    const res = await fetch('/login', {
        method: 'POST',
        credentials: 'same-origin',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, phone, password })
    });
    return res.json();
}

async function logout() {
    await fetch('/logout', { method: 'POST', credentials: 'same-origin' });
    document.getElementById('btnLogout').style.display = 'none';
    document.getElementById('btnHistory').style.display = 'none';
}

async function fetchHistory() {
    const res = await fetch('/history', { credentials: 'same-origin' });
    const data = await res.json();
    if (!res.ok) {
        alert(data.error || 'Could not fetch history');
        return;
    }

    // Simple display of recent history
    const html = data.history.map(h => {
        const d = new Date(h.timestamp).toLocaleString();
        return `${d} — ${h.analysis.job_role} — TF-IDF: ${Math.round(h.analysis.tfidf_score)}% — Skill Match: ${h.analysis.skill_match.match_percentage}%`;
    }).join('\n');

    if (!html) {
        alert('No history found');
    } else {
        alert(html);
    }
}

// Note: Login/Signup UI moved to dedicated /login page. Functions `login`, `signup`, `logout`, and `fetchHistory`
// remain available for other UIs to call (e.g., nav buttons). The previous DOM wiring was removed.
