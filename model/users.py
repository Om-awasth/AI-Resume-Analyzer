import os
import json
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import random
from datetime import timedelta
import os

try:
    from twilio.rest import Client as TwilioClient
except Exception:
    TwilioClient = None

from sqlalchemy import (
    create_engine, Column, String, DateTime, Text, Integer, Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(40), unique=True, nullable=True)
    password_hash = Column(String(256), nullable=False)
    created_at = Column(DateTime, nullable=False)


class Analysis(Base):
    __tablename__ = 'analyses'
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), nullable=False, index=True)
    timestamp = Column(DateTime, nullable=False)
    job_role = Column(String(150))
    tfidf_score = Column(Float)
    skill_match_json = Column(Text)
    recommendation = Column(Text)
    analysis_json = Column(Text)


class OTP(Base):
    __tablename__ = 'otps'
    id = Column(String(36), primary_key=True)
    phone_number = Column(String(40), nullable=False, index=True)
    code = Column(String(16), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)


class PasswordReset(Base):
    __tablename__ = 'password_resets'
    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), nullable=False, index=True)
    token = Column(String(128), nullable=False, unique=True, index=True)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)


# DB setup: prefer MYSQL_URL, fallback to sqlite file in data/
def _get_engine():
    mysql_url = os.environ.get('MYSQL_URL')
    if mysql_url:
        engine = create_engine(mysql_url, pool_pre_ping=True)
        return engine

    # fallback sqlite
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    sqlite_path = os.path.join(data_dir, 'app.db')
    engine = create_engine(f'sqlite:///{sqlite_path}', connect_args={"check_same_thread": False})
    return engine


ENGINE = _get_engine()
SessionLocal = sessionmaker(bind=ENGINE)


def _init_db():
    Base.metadata.create_all(bind=ENGINE)


_init_db()


def create_user(username, password, phone_number=None):
    """Create a new user. Returns user dict or None if exists."""
    db = SessionLocal()
    try:
        # Check username and phone uniqueness
        if username:
            existing = db.query(User).filter(User.username == username).first()
            if existing:
                return None
        if phone_number:
            existing_phone = db.query(User).filter(User.phone_number == phone_number).first()
            if existing_phone:
                return None

        user_id = str(uuid.uuid4())
        u = User(
            id=user_id,
            username=username or f'user_{user_id[:8]}',
            phone_number=phone_number,
            password_hash=generate_password_hash(password, method='pbkdf2:sha256'),
            created_at=datetime.utcnow()
        )
        db.add(u)
        db.commit()
        return {'id': u.id, 'username': u.username, 'phone_number': u.phone_number, 'created_at': u.created_at.isoformat()}
    finally:
        db.close()


def authenticate_user(identifier, password):
    """Authenticate by username or phone number (identifier)."""
    db = SessionLocal()
    try:
        user = None
        if identifier is None:
            return None
        # crude phone detection: digits and +
        id_clean = str(identifier).strip()
        if id_clean.replace('+', '').replace('-', '').isdigit():
            user = db.query(User).filter(User.phone_number == id_clean).first()
        if not user:
            user = db.query(User).filter(User.username == id_clean).first()
        if not user:
            return None
        if check_password_hash(user.password_hash, password):
            return {'id': user.id, 'username': user.username, 'phone_number': user.phone_number, 'created_at': user.created_at.isoformat()}
        return None
    finally:
        db.close()


def get_user_by_username(username):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return None
        return {'id': user.id, 'username': user.username, 'created_at': user.created_at.isoformat()}
    finally:
        db.close()


def save_analysis(user_id, analysis):
    db = SessionLocal()
    try:
        rec = Analysis(
            id=str(uuid.uuid4()),
            user_id=user_id,
            timestamp=datetime.utcnow(),
            job_role=analysis.get('job_role'),
            tfidf_score=float(analysis.get('tfidf_score') or 0.0),
            skill_match_json=json.dumps(analysis.get('skill_match', {})),
            recommendation=analysis.get('recommendation'),
            analysis_json=json.dumps(analysis)
        )
        db.add(rec)
        db.commit()
        return {'id': rec.id, 'timestamp': rec.timestamp.isoformat(), 'analysis': analysis}
    finally:
        db.close()


def get_history(user_id, limit=50):
    db = SessionLocal()
    try:
        rows = db.query(Analysis).filter(Analysis.user_id == user_id).order_by(Analysis.timestamp.desc()).limit(limit).all()
        out = []
        for r in rows:
            try:
                analysis = json.loads(r.analysis_json)
            except Exception:
                analysis = {}
            out.append({'id': r.id, 'timestamp': r.timestamp.isoformat(), 'analysis': analysis})
        return out
    finally:
        db.close()


def _send_sms_via_twilio(phone, body):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    from_number = os.environ.get('TWILIO_FROM')
    if not (account_sid and auth_token and from_number and TwilioClient):
        return False, 'twilio not configured'
    client = TwilioClient(account_sid, auth_token)
    try:
        msg = client.messages.create(body=body, from_=from_number, to=phone)
        return True, msg.sid
    except Exception as e:
        return False, str(e)


def create_otp(phone, length=6, ttl_minutes=5):
    """Create and store an OTP code for a phone number and return the code."""
    db = SessionLocal()
    try:
        code = ''.join(str(random.randint(0, 9)) for _ in range(length))
        now = datetime.utcnow()
        rec = OTP(
            id=str(uuid.uuid4()),
            phone_number=phone,
            code=code,
            expires_at=now + timedelta(minutes=ttl_minutes),
            created_at=now
        )
        db.add(rec)
        db.commit()
        return code
    finally:
        db.close()


def send_otp(phone):
    """Create OTP, attempt to send via Twilio, fallback to returning code for debug."""
    code = create_otp(phone)
    body = f"Your Resume Analyzer login code is: {code}. It expires in 5 minutes."
    ok, info = _send_sms_via_twilio(phone, body)
    if ok:
        return True, 'sent'
    # fallback: return code in response for development
    return False, code


def verify_otp(phone, code):
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        otp_row = db.query(OTP).filter(OTP.phone_number == phone, OTP.code == code).first()
        if not otp_row:
            return False
        if otp_row.expires_at < now:
            # expired; delete row
            db.delete(otp_row)
            db.commit()
            return False
        # valid; delete used otp
        db.delete(otp_row)
        db.commit()
        return True
    finally:
        db.close()


def create_password_reset(identifier, ttl_minutes=60):
    """Create a password reset token for a user identified by username or phone.
    Returns token (string) or None if user not found."""
    db = SessionLocal()
    try:
        user = None
        id_clean = str(identifier).strip()
        if id_clean.replace('+', '').replace('-', '').isdigit():
            user = db.query(User).filter(User.phone_number == id_clean).first()
        if not user:
            user = db.query(User).filter(User.username == id_clean).first()
        if not user:
            return None

        token = uuid.uuid4().hex
        now = datetime.utcnow()
        rec = PasswordReset(
            id=str(uuid.uuid4()),
            user_id=user.id,
            token=token,
            expires_at=now + timedelta(minutes=ttl_minutes),
            created_at=now
        )
        db.add(rec)
        db.commit()
        return token
    finally:
        db.close()


def reset_password_with_token(token, new_password):
    """Verify token and set new password. Returns True on success."""
    db = SessionLocal()
    try:
        now = datetime.utcnow()
        pr = db.query(PasswordReset).filter(PasswordReset.token == token).first()
        if not pr:
            return False
        if pr.expires_at < now:
            try:
                db.delete(pr)
                db.commit()
            except Exception:
                pass
            return False

        user = db.query(User).filter(User.id == pr.user_id).first()
        if not user:
            return False

        user.password_hash = generate_password_hash(new_password, method='pbkdf2:sha256')
        db.delete(pr)
        db.commit()
        return True
    finally:
        db.close()

