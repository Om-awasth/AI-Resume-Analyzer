# Resume Analyzer & Skill Gap Predictor - Setup Complete! ✅

## 🚀 Quick Start Guide

Your complete Resume Analyzer application has been created! Here's how to run it:

### 1. **Test the Demo** (No web browser needed)
```bash
cd /Users/omawasthi/Downloads/files/resume_analyzer
python3 demo.py
```
This shows analysis results for a sample resume across all three job roles.

### 2. **Run the Web Application**
```bash
cd /Users/omawasthi/Downloads/files/resume_analyzer
python3 app.py
```

Then open your browser and go to: **http://localhost:5000**

### 3. **What You'll See**
- Upload page with drag-and-drop support
- Job role selector (Data Analyst, Web Developer, ML Engineer)
- Results with:
  - Skill Match percentage
  - TF-IDF Similarity score
  - Matched skills (green badges)
  - Missing skills (red badges)
  - Personalized learning resources
  - Recommendations

---

## 📁 Project Structure
```
resume_analyzer/
├── app.py                    # Main Flask application
├── demo.py                   # Standalone demo
├── requirements.txt          # Python dependencies
├── model/
│   ├── skills.py            # 80+ skills database & resources
│   └── tfidf_model.py       # TF-IDF similarity calculations
├── utils/
│   ├── pdf_reader.py        # PDF text extraction
│   └── skill_extractor.py   # Skill detection logic
├── templates/
│   └── index.html           # Web interface
├── static/
│   ├── style.css            # Styling
│   └── script.js            # Frontend logic
└── uploads/                 # Temporary file storage
```

---

## 🛠 Technologies Used
- **Backend:** Flask 3.0 (Python web framework)
- **ML/NLP:** scikit-learn (TF-IDF, Cosine Similarity)
- **PDF Processing:** PyPDF2
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Python:** 3.8+

---

## ✨ Features
✅ PDF resume upload (max 5MB)
✅ 80+ skills across 3 job roles
✅ Dual scoring: Skill match % + TF-IDF similarity
✅ Matched vs missing skills visualization
✅ Personalized learning resources (courses, websites, duration)
✅ Contact information extraction
✅ Responsive design
✅ Print-friendly results

---

## 📊 How It Works
1. **Upload PDF** → Extract text
2. **Detect Skills** → Regex pattern matching from database
3. **Calculate Similarity** → TF-IDF + Cosine Similarity
4. **Gap Analysis** → Compare detected vs required skills
5. **Get Recommendations** → Learning resources for missing skills

---

## 🎯 Job Roles Available
- **Data Analyst** - 24 technical + 6 soft skills
- **Web Developer** - 28 technical + 6 soft skills
- **ML Engineer** - 31 technical + 6 soft skills

---

## 🔧 Troubleshooting

### Problem: Port 5000 already in use
Edit `app.py` line 196:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change 5000 to 8080
```

### Problem: PDF not reading
- Ensure PDF is text-based (not scanned)
- Try re-saving from Word or Google Docs
- File should be < 5MB

### Problem: Skills not detected
- Add a "Skills" section to resume
- Use exact skill names (e.g., "Python" not "Programming")
- Skills are matched case-insensitively

---

## 📝 Sample Results
```
Data Analyst Role:
✅ Skill Match: 68% (17/25 skills)
✅ TF-IDF Similarity: 73%
✅ Matched: Python, SQL, Pandas, NumPy, Git...
❌ Missing: Tableau, Power BI, A/B Testing...

Recommendation: "Good match! With minor skill improvements, 
you'll be competitive. 👍"
```

---

## 🎓 Next Steps
1. Test with your own resume
2. Try all three job roles
3. Add custom skills to `model/skills.py`
4. Customize learning resources
5. Deploy to cloud (Heroku, AWS, Google Cloud)

---

## 💻 Command Reference

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run demo:**
```bash
python3 demo.py
```

**Run web app:**
```bash
python3 app.py
```

**Stop web app:**
Press `Ctrl+C` in terminal

---

## 🎉 You're All Set!
The application is ready to use. Start with:
```bash
python3 demo.py
```
Then run:
```bash
python3 app.py
```
Visit: **http://localhost:5000**

Enjoy analyzing resumes! 🚀
