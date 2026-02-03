"""
Resume Analyzer & Skill Gap Predictor
Main Flask Application
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import uuid
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
from werkzeug.utils import secure_filename
from utils.pdf_reader import extract_pdf_text, get_contact_info
from utils.skill_extractor import extract_skills_from_text, analyze_skill_match
from model.skills import (
    get_job_skills, get_job_description, get_learning_resource, 
    get_all_job_roles, get_skill_questions, get_all_testable_skills
)
from model.tfidf_model import calculate_resume_similarity
from model.users import create_user, authenticate_user, save_analysis, get_history, SessionLocal, User, Analysis, create_password_reset, reset_password_with_token
from utils.email_sender import send_email
import requests

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('RESUME_ANALYZER_SECRET', 'dev-secret-change-me')
app.config['ENV'] = os.environ.get('FLASK_ENV', 'development')
app.config['DEBUG'] = app.config['ENV'] == 'development'

# Configuration
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file size
ALLOWED_EXTENSIONS = {'pdf'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render home page"""
    # Require authentication for main site
    if not session.get('user_id'):
        return redirect(url_for('login_page'))
    job_roles = get_all_job_roles()
    return render_template('index.html', job_roles=job_roles)


@app.route('/analyze', methods=['POST'])
def analyze_resume():
    """Analyze uploaded resume"""
    # Require authentication to run an analysis
    if not session.get('user_id'):
        return jsonify({'error': 'Authentication required'}), 401
    try:
        # Check if file was uploaded
        if 'resume' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['resume']
        job_role = request.form.get('job_role', '')
        
        # Validate file and job role
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files are allowed'}), 400
        
        if job_role not in get_all_job_roles():
            return jsonify({'error': 'Invalid job role'}), 400
        
        # Save file
        filename = secure_filename(str(uuid.uuid4()) + '.pdf')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from PDF
        resume_text = extract_pdf_text(filepath)
        
        if not resume_text:
            return jsonify({'error': 'Could not extract text from PDF. Ensure it is not scanned.'}), 400
        
        # Extract contact information
        contact_info = get_contact_info(resume_text)
        
        # Extract skills for the selected job role
        detected_skills = extract_skills_from_text(resume_text, job_role)
        
        # Analyze skill match
        skill_match = analyze_skill_match(detected_skills, job_role)
        
        # Calculate TF-IDF similarity
        job_description = get_job_description(job_role)
        tfidf_score = calculate_resume_similarity(resume_text, job_description)
        
        # Get learning resources for missing skills
        top_missing_skills = skill_match['missing'][:10]  # Top 10 missing skills
        resources = {}
        for skill in top_missing_skills:
            resources[skill] = get_learning_resource(skill)
        
        # Generate recommendation based on scores
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
        
        # Clean up uploaded file
        os.remove(filepath)
        
        # Prepare response
        results = {
            'job_role': job_role,
            'contact': contact_info,
            'skill_match': skill_match,
            'tfidf_score': tfidf_score,
            'detected_skills': detected_skills,
            'resources': resources,
            'recommendation': recommendation,
            'level': level
        }
        
        # If user is logged in, save a compact summary of the analysis
        user_id = session.get('user_id')
        if user_id:
            try:
                save_payload = {
                    'job_role': job_role,
                    'tfidf_score': tfidf_score,
                    'skill_match': skill_match,
                    'recommendation': recommendation,
                    'detected_skills': detected_skills
                }
                save_analysis(user_id, save_payload)
            except Exception:
                pass

        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500


@app.route('/about')
def about():
    """About page"""
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/preview')
def preview_page():
    # public preview of the main site for background visuals
    job_roles = get_all_job_roles()
    return render_template('preview.html', job_roles=job_roles)


@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/skill-test/<skill>')
def get_skill_test(skill):
    """Get skill assessment questions"""
    try:
        questions = get_skill_questions(skill)
        
        if not questions:
            return jsonify({'error': 'No questions available for this skill'}), 404
        
        # Don't send answers to client
        questions_to_send = []
        for q in questions:
            questions_to_send.append({
                'question': q['question'],
                'options': q['options']
            })
        
        return jsonify({
            'skill': skill,
            'questions': questions_to_send,
            'total': len(questions_to_send)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    phone = data.get('phone')
    if not password or (not username and not phone):
        return jsonify({'error': 'provide password and username or phone'}), 400

    user = create_user(username, password, phone_number=phone)
    if user is None:
        return jsonify({'error': 'username or phone already exists'}), 400

    session['user_id'] = user['id']
    session['username'] = user.get('username')
    return jsonify({'message': 'user created', 'username': user.get('username'), 'phone': user.get('phone_number')})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    phone = data.get('phone')
    password = data.get('password')
    identifier = phone or username
    if not identifier or not password:
        return jsonify({'error': 'identifier (username or phone) and password required'}), 400

    user = authenticate_user(identifier, password)
    if user is None:
        return jsonify({'error': 'invalid credentials'}), 401

    session['user_id'] = user['id']
    session['username'] = user.get('username')
    return jsonify({'message': 'logged in', 'username': user.get('username'), 'phone': user.get('phone_number')})


@app.route('/request-otp', methods=['POST'])
def request_otp():
    # OTP login removed. This endpoint is deprecated.
    return jsonify({'error': 'OTP login is disabled'}), 410


@app.route('/verify-otp', methods=['POST'])
def verify_otp_route():
    # OTP login removed. This endpoint is deprecated.
    return jsonify({'error': 'OTP login is disabled'}), 410


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return jsonify({'message': 'logged out'})


@app.route('/forgot-password')
def forgot_password_page():
    return render_template('forgot_password.html')


@app.route('/forgot-password', methods=['POST'])
def forgot_password_request():
    data = request.get_json() or {}
    identifier = data.get('email') or data.get('identifier')
    if not identifier:
        return jsonify({'error': 'email required'}), 400
    try:
        token = create_password_reset(identifier)
        if not token:
            return jsonify({'error': 'user not found'}), 404
        subject = 'Resume Analyzer — Password Reset'
        plain = f'Use this token to reset your password: {token}\nThis token expires in 60 minutes.'
        html = f'<p>Use this token to reset your password: <b>{token}</b></p><p>This token expires in 60 minutes.</p>'

        # Prefer external email microservice if configured
        email_service = os.environ.get('EMAIL_SERVICE_URL')
        if email_service:
            try:
                resp = requests.post(
                    f"{email_service.rstrip('/')}/send-reset",
                    json={"to": identifier, "subject": subject, "text": plain, "html": html},
                    timeout=10,
                )
                if resp.ok:
                    data = resp.json()
                    # include preview link from Ethereal if present
                    return jsonify({'message': 'reset_created', 'sent': True, 'preview': data.get('preview')})
                else:
                    # fallback to local SMTP helper if microservice failed
                    pass
            except Exception:
                # microservice unreachable; fall through to SMTP helper
                pass

        # Try to email via local SMTP helper; if not configured return token (dev fallback)
        ok, info = send_email(identifier, subject, plain, html)
        if ok:
            return jsonify({'message': 'reset_created', 'sent': True})
        return jsonify({'message': 'reset_created', 'sent': False, 'token': token, 'info': info})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/reset-password')
def reset_password_page():
    token = request.args.get('token')
    return render_template('reset_password.html', token=token)


@app.route('/reset-password', methods=['POST'])
def reset_password_action():
    data = request.get_json() or {}
    token = data.get('token')
    new_password = data.get('password')
    if not token or not new_password:
        return jsonify({'error': 'token and password required'}), 400
    try:
        ok = reset_password_with_token(token, new_password)
        if not ok:
            return jsonify({'error': 'invalid or expired token'}), 400
        return jsonify({'message': 'password_reset'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/user', methods=['GET'])
def get_user():
    """Get current user info if logged in"""
    if not session.get('user_id'):
        return jsonify({'user': None}), 200
    
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == session.get('user_id')).first()
        if user:
            return jsonify({'user': {'username': user.username, 'phone_number': user.phone_number}})
        return jsonify({'user': None})
    finally:
        db.close()


@app.route('/history')
def history():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login_page'))
    return render_template('history.html')


@app.route('/api/history')
def api_history():
    """Get user's analysis history as JSON"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'not authenticated'}), 401
    
    try:
        db = SessionLocal()
        try:
            # Get user info
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({'user': None, 'analyses': []})
            
            # Get all analyses for this user
            analyses = db.query(Analysis).filter(Analysis.user_id == user_id).order_by(Analysis.timestamp).all()
            
            analyses_data = []
            for a in analyses:
                import json
                try:
                    skill_match = json.loads(a.skill_match_json) if a.skill_match_json else {}
                    analysis_json = json.loads(a.analysis_json) if a.analysis_json else {}
                    skills = analysis_json.get('detected_skills', []) if analysis_json else []
                except:
                    skill_match = {}
                    skills = []
                
                # extract missing skills list if present
                missing = []
                try:
                    missing = skill_match.get('missing', []) if isinstance(skill_match, dict) else []
                except Exception:
                    missing = []

                analyses_data.append({
                    'id': a.id,
                    'timestamp': a.timestamp.isoformat() if a.timestamp else '',
                    'job_role': a.job_role or 'Unknown',
                    'tfidf_score': float(a.tfidf_score or 0),
                    # keep skill_match as fraction (0-1) for backward compatibility
                    'skill_match': float(skill_match.get('match_percentage', 0) / 100 if skill_match.get('match_percentage') else 0),
                    'skills_count': len(skills),
                    'skills': skills,
                    'missing_skills': missing
                })
            
            return jsonify({
                'user': {'username': user.username, 'phone_number': user.phone_number},
                'analyses': analyses_data
            })
        finally:
            db.close()
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/check-answers', methods=['POST'])
def check_answers():
    """Check skill test answers"""
    try:
        data = request.get_json()
        skill = data.get('skill')
        answers = data.get('answers', [])
        
        questions = get_skill_questions(skill)
        
        if not questions or len(answers) != len(questions):
            return jsonify({'error': 'Invalid test data'}), 400
        
        # Calculate score
        correct = 0
        results = []
        
        for i, (question, user_answer) in enumerate(zip(questions, answers)):
            is_correct = user_answer == question['correct']
            if is_correct:
                correct += 1
            
            results.append({
                'question': question['question'],
                'user_answer': question['options'][user_answer],
                'correct_answer': question['options'][question['correct']],
                'is_correct': is_correct
            })
        
        score = round((correct / len(questions)) * 100, 2)
        
        return jsonify({
            'skill': skill,
            'score': score,
            'correct': correct,
            'total': len(questions),
            'results': results,
            'passed': score >= 70
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({'error': 'File too large. Maximum size is 5MB.'}), 413


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=port)
