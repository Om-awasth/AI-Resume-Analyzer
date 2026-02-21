const mongoose = require('mongoose');

// User Schema
const userSchema = new mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  username: { type: String, unique: true, required: true, lowercase: true },
  password: { type: String, required: true },
  email: { type: String, unique: true, required: true, lowercase: true },
  created_at: { type: Date, default: Date.now }
});

// Analysis Schema
const analysisSchema = new mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  user_id: { type: mongoose.Schema.Types.ObjectId, required: true, ref: 'User' },
  job_role: String,
  tfidf_score: Number,
  ats_score: Number,
  skill_match: {
    matched: [String],
    missing: [String],
    match_percentage: Number,
    matched_count: Number,
    required_count: Number
  },
  recommendation: String,
  detected_skills: [String],
  resume_text: String,
  resume_url: String,
  created_at: { type: Date, default: Date.now }
});

// Password Reset Schema
const passwordResetSchema = new mongoose.Schema({
  _id: mongoose.Schema.Types.ObjectId,
  email: { type: String, required: true },
  token: { type: String, required: true, unique: true },
  reset_ticket: String,
  created_at: { type: Date, default: Date.now, expires: 3600 } // Expires after 1 hour
});

const User = mongoose.model('User', userSchema);
const Analysis = mongoose.model('Analysis', analysisSchema);
const PasswordReset = mongoose.model('PasswordReset', passwordResetSchema);

module.exports = { User, Analysis, PasswordReset };
