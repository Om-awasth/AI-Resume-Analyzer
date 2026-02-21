const path = require("path");
const fs = require("fs");
const express = require("express");
const session = require("express-session");
const dotenv = require("dotenv");
const nunjucks = require("nunjucks");
const multer = require("multer");
const pdfParse = require("pdf-parse");
const bcrypt = require("bcryptjs");
const nodemailer = require("nodemailer");
const { v4: uuidv4 } = require("uuid");

const {
  getJobDescription,
  getLearningResource,
  getAllJobRoles,
  getSkillQuestions,
  getJobSkills
} = require("./src/data/skills");

dotenv.config();

const app = express();
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 5 * 1024 * 1024 }
});

const dataDir = path.join(__dirname, "data");
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}
const storePath = process.env.JSON_DB_PATH || path.join(dataDir, "app.json");

function loadStore() {
  if (!fs.existsSync(storePath)) {
    const initial = { users: [], analyses: [], password_resets: [] };
    fs.writeFileSync(storePath, JSON.stringify(initial, null, 2));
    return initial;
  }
  try {
    const parsed = JSON.parse(fs.readFileSync(storePath, "utf8"));
    return {
      users: Array.isArray(parsed.users) ? parsed.users : [],
      analyses: Array.isArray(parsed.analyses) ? parsed.analyses : [],
      password_resets: Array.isArray(parsed.password_resets) ? parsed.password_resets : []
    };
  } catch {
    return { users: [], analyses: [], password_resets: [] };
  }
}

function saveStore(store) {
  fs.writeFileSync(storePath, JSON.stringify(store, null, 2));
}

function getSmtpConfig() {
  const host = process.env.SMTP_HOST || process.env.MAIL_SERVER;
  const port = Number(process.env.SMTP_PORT || process.env.MAIL_PORT || 587);
  const user = process.env.SMTP_USER || process.env.MAIL_USERNAME;
  const pass = process.env.SMTP_PASS || process.env.MAIL_PASSWORD;
  const secureRaw = process.env.SMTP_SECURE || process.env.MAIL_USE_SSL || "false";
  const secure = ["true", "1", "yes"].includes(String(secureRaw).toLowerCase()) || port === 465;

  if (!host || !port || !user || !pass) {
    return null;
  }

  return {
    host,
    port,
    secure,
    auth: { user, pass }
  };
}

async function sendResetEmail(to, otpCode) {
  let smtpConfig = getSmtpConfig();
  let transporter;
  let fromAddress;

  if (smtpConfig) {
    transporter = nodemailer.createTransport(smtpConfig);
    fromAddress = process.env.FROM_EMAIL || process.env.SMTP_FROM || smtpConfig.auth.user;
  } else {
    try {
      const testAccount = await nodemailer.createTestAccount();
      smtpConfig = {
        host: testAccount.smtp.host,
        port: testAccount.smtp.port,
        secure: testAccount.smtp.secure,
        auth: {
          user: testAccount.user,
          pass: testAccount.pass
        }
      };
      transporter = nodemailer.createTransport(smtpConfig);
      fromAddress = process.env.FROM_EMAIL || `Resume Analyzer <${testAccount.user}>`;
    } catch {
      return { sent: false, reason: "smtp_not_configured" };
    }
  }

  const appBaseUrl = process.env.APP_BASE_URL || `http://localhost:${process.env.PORT || 8080}`;
  const resetUrl = `${appBaseUrl.replace(/\/$/, "")}/reset-password?email=${encodeURIComponent(to)}`;

  const info = await transporter.sendMail({
    from: fromAddress,
    to,
    subject: "Resume Analyzer — Password Reset OTP",
    text: `Your password reset OTP is: ${otpCode}\nThis OTP expires in 60 minutes.\nOpen: ${resetUrl}`,
    html: `<p>Your password reset OTP is: <b>${otpCode}</b></p><p>This OTP expires in 60 minutes.</p><p><a href="${resetUrl}">Open Reset Page</a></p>`
  });

  const preview = nodemailer.getTestMessageUrl(info) || null;
  return { sent: true, preview };
}

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(session({
  secret: process.env.RESUME_ANALYZER_SECRET || "dev-secret-change-me",
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,
    sameSite: "lax",
    secure: process.env.NODE_ENV === "production"
  }
}));

app.use("/static", express.static(path.join(__dirname, "static")));

const njkEnv = nunjucks.configure(path.join(__dirname, "templates"), {
  autoescape: true,
  express: app
});

njkEnv.addGlobal("url_for", function urlFor(routeName, kwargs) {
  if (routeName === "static" && kwargs && kwargs.filename) {
    return `/static/${kwargs.filename}`;
  }
  return "/";
});

function allowedFile(filename) {
  return filename && filename.toLowerCase().endsWith(".pdf");
}

function cleanText(text) {
  if (!text) return "";
  const squashed = text.replace(/\s+/g, " ").trim();
  return squashed.replace(/[^\w\s@.\-+,#:\/]/g, "");
}

function getContactInfo(text) {
  const emailMatch = text.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/);
  const phonePatterns = [
    /\+1\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}/,
    /\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}/,
    /\+\d{1,3}\s?\d{4,14}/
  ];

  let phone = null;
  for (const pattern of phonePatterns) {
    const match = text.match(pattern);
    if (match) {
      phone = match[0];
      break;
    }
  }

  return {
    email: emailMatch ? emailMatch[0] : null,
    phone
  };
}

function extractSkillsFromText(text, jobRole) {
  const job = getJobSkills(jobRole);
  if (!job.technical || !job.soft) return [];
  const allSkills = [...job.technical, ...job.soft];
  const textLower = text.toLowerCase();

  return allSkills.filter((skill) => {
    const escaped = skill.toLowerCase().replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const regex = new RegExp(`\\b${escaped}\\b`, "i");
    return regex.test(textLower);
  });
}

function analyzeSkillMatch(detectedSkills, jobRole) {
  const job = getJobSkills(jobRole);
  const required = [...(job.technical || []), ...(job.soft || [])];
  if (!required.length) {
    return {
      matched: [],
      missing: [],
      match_percentage: 0,
      matched_count: 0,
      required_count: 0
    };
  }

  const detectedSet = new Set(detectedSkills);
  const requiredSet = new Set(required);
  const matched = [...requiredSet].filter((skill) => detectedSet.has(skill)).sort();
  const missing = [...requiredSet].filter((skill) => !detectedSet.has(skill)).sort();
  const matchPercentage = Number(((matched.length / required.length) * 100).toFixed(2));

  return {
    matched,
    missing,
    match_percentage: matchPercentage,
    matched_count: matched.length,
    required_count: required.length
  };
}

function tokenize(text) {
  const stopWords = new Set([
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "on", "with", "at", "by", "from", "is", "are", "was", "were", "be", "as", "that", "this", "it", "your", "you"
  ]);
  return (text.toLowerCase().match(/[a-z0-9+#.]+/g) || []).filter((token) => token.length > 1 && !stopWords.has(token));
}

function tfVector(tokens) {
  const map = new Map();
  for (const token of tokens) {
    map.set(token, (map.get(token) || 0) + 1);
  }
  const total = tokens.length || 1;
  for (const [key, value] of map.entries()) {
    map.set(key, value / total);
  }
  return map;
}

function cosineSimilarity(mapA, mapB) {
  const keys = new Set([...mapA.keys(), ...mapB.keys()]);
  let dot = 0;
  let normA = 0;
  let normB = 0;

  for (const key of keys) {
    const a = mapA.get(key) || 0;
    const b = mapB.get(key) || 0;
    dot += a * b;
    normA += a * a;
    normB += b * b;
  }

  if (!normA || !normB) return 0;
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

function calculateResumeSimilarity(resumeText, jobDescription) {
  const resumeTokens = tokenize(resumeText);
  const jobTokens = tokenize(jobDescription);
  const score = cosineSimilarity(tfVector(resumeTokens), tfVector(jobTokens));
  return Number((score * 100).toFixed(2));
}

function createUser(username, password, phoneNumber = null, email = null) {
  const store = loadStore();
  const existing = store.users.find((user) =>
    (username && user.username === username) ||
    (phoneNumber && user.phone_number === phoneNumber) ||
    (email && user.email === email)
  );
  if (existing) return null;

  const id = uuidv4();
  const createdAt = new Date().toISOString();
  const passwordHash = bcrypt.hashSync(password, 10);
  const finalUsername = username || `user_${id.slice(0, 8)}`;

  const user = { id, username: finalUsername, email, phone_number: phoneNumber, password_hash: passwordHash, created_at: createdAt };
  store.users.push(user);
  saveStore(store);

  return { id, username: finalUsername, email, phone_number: phoneNumber, created_at: createdAt };
}

function authenticateUser(identifier, password) {
  if (!identifier) return null;
  const store = loadStore();
  const clean = String(identifier).trim();
  const phoneLike = clean.replace(/[+-]/g, "").replace(/\s/g, "").match(/^\d+$/);

  let user;
  if (phoneLike) {
    user = store.users.find((row) => row.phone_number === clean);
  }
  if (!user) {
    user = store.users.find((row) => row.username === clean || row.email === clean);
  }
  if (!user) return null;
  if (!bcrypt.compareSync(password, user.password_hash)) return null;

  return {
    id: user.id,
    username: user.username,
    email: user.email,
    phone_number: user.phone_number,
    created_at: user.created_at
  };
}

function saveAnalysis(userId, analysis) {
  const store = loadStore();
  const id = uuidv4();
  const timestamp = new Date().toISOString();
  store.analyses.push(
    {
    id,
    user_id: userId,
    timestamp,
    job_role: analysis.job_role,
    tfidf_score: Number(analysis.tfidf_score || 0),
    ats_score: Number(analysis.ats_score || 0),
    skill_match_json: JSON.stringify(analysis.skill_match || {}),
    recommendation: analysis.recommendation || "",
    analysis_json: JSON.stringify(analysis)
  }
  );
  saveStore(store);
}

function createPasswordReset(identifier) {
  const store = loadStore();
  const clean = String(identifier || "").trim();
  if (!clean) return null;
  let user;

  if (clean.includes("@")) {
    user = store.users.find((row) => row.email === clean);
  }
  if (!user && clean.replace(/[+-]/g, "").replace(/\s/g, "").match(/^\d+$/)) {
    user = store.users.find((row) => row.phone_number === clean);
  }
  if (!user) {
    user = store.users.find((row) => row.username === clean);
  }
  if (!user) return null;

  const otpCode = String(Math.floor(100000 + Math.random() * 900000));
  const now = new Date();
  const expires = new Date(now.getTime() + 60 * 60 * 1000).toISOString();

  store.password_resets = store.password_resets.filter((entry) => entry.user_id !== user.id);

  store.password_resets.push({
    id: uuidv4(),
    user_id: user.id,
    token: otpCode,
    identifier: clean,
    expires_at: expires,
    created_at: now.toISOString()
  });
  saveStore(store);

  return {
    otp: otpCode,
    email: user.email || clean
  };
}

function verifyPasswordResetOtp(identifier, otpCode) {
  const store = loadStore();
  const clean = String(identifier || "").trim();
  const code = String(otpCode || "").trim();
  if (!clean || !code) {
    return { ok: false, error: "email and otp required" };
  }

  let user = null;
  if (clean.includes("@")) {
    user = store.users.find((row) => row.email === clean);
  }
  if (!user && clean.replace(/[+-]/g, "").replace(/\s/g, "").match(/^\d+$/)) {
    user = store.users.find((row) => row.phone_number === clean);
  }
  if (!user) {
    user = store.users.find((row) => row.username === clean);
  }
  if (!user) {
    return { ok: false, error: "user not found" };
  }

  const row = store.password_resets.find((entry) => entry.user_id === user.id && entry.token === code);
  if (!row) {
    return { ok: false, error: "invalid otp" };
  }

  if (new Date(row.expires_at).getTime() < Date.now()) {
    store.password_resets = store.password_resets.filter((entry) => entry.id !== row.id);
    saveStore(store);
    return { ok: false, error: "expired otp" };
  }

  const resetTicket = uuidv4().replace(/-/g, "");
  row.reset_ticket = resetTicket;
  row.reset_ticket_expires_at = new Date(Date.now() + 10 * 60 * 1000).toISOString();
  row.verified_at = new Date().toISOString();
  saveStore(store);

  return { ok: true, reset_ticket: resetTicket };
}

function resetPasswordWithToken(token, newPassword, identifier = null, resetTicket = null) {
  const store = loadStore();
  let row = null;

  if (resetTicket) {
    row = store.password_resets.find((entry) => entry.reset_ticket === resetTicket);
  } else {
    row = store.password_resets.find((entry) => entry.token === token);
  }
  if (!row) return false;

  if (resetTicket) {
    if (!row.reset_ticket_expires_at || new Date(row.reset_ticket_expires_at).getTime() < Date.now()) {
      store.password_resets = store.password_resets.filter((entry) => entry.id !== row.id);
      saveStore(store);
      return false;
    }
  }

  if (identifier) {
    const clean = String(identifier).trim();
    const user = store.users.find((entry) => entry.id === row.user_id);
    const matchesIdentifier = user && (
      user.email === clean ||
      user.username === clean ||
      user.phone_number === clean
    );
    if (!matchesIdentifier) {
      return false;
    }
  }

  if (new Date(row.expires_at).getTime() < Date.now()) {
    store.password_resets = store.password_resets.filter((entry) => entry.token !== token);
    saveStore(store);
    return false;
  }

  const hash = bcrypt.hashSync(newPassword, 10);
  const user = store.users.find((entry) => entry.id === row.user_id);
  if (!user) return false;
  user.password_hash = hash;
  store.password_resets = store.password_resets.filter((entry) => entry.token !== token);
  saveStore(store);
  return true;
}

app.get("/", (req, res) => {
  if (!req.session.user_id) {
    return res.redirect("/login");
  }
  return res.render("index.html", { job_roles: getAllJobRoles() });
});

app.post("/analyze", upload.single("resume"), async (req, res) => {
  if (!req.session.user_id) {
    return res.status(401).json({ error: "Authentication required" });
  }

  try {
    const file = req.file;
    const jobRole = req.body.job_role || "";

    if (!file) {
      return res.status(400).json({ error: "No file provided" });
    }
    if (!allowedFile(file.originalname)) {
      return res.status(400).json({ error: "Only PDF files are allowed" });
    }
    if (!getAllJobRoles().includes(jobRole)) {
      return res.status(400).json({ error: "Invalid job role" });
    }

    const parsed = await pdfParse(file.buffer);
    const resumeText = cleanText(parsed.text || "");
    if (!resumeText) {
      return res.status(400).json({ error: "Could not extract text from PDF. Ensure it is not scanned." });
    }

    const contact = getContactInfo(resumeText);
    const detectedSkills = extractSkillsFromText(resumeText, jobRole);
    const skillMatch = analyzeSkillMatch(detectedSkills, jobRole);
    const tfidfScore = calculateResumeSimilarity(resumeText, getJobDescription(jobRole));

    const topMissingSkills = skillMatch.missing.slice(0, 10);
    const resources = {};
    for (const skill of topMissingSkills) {
      resources[skill] = getLearningResource(skill);
    }

    // Calculate true ATS Score (weighted combination)
    // ATS systems typically weight skills heavily (65%) and keyword relevance (35%)
    const atsScore = Number((
      (skillMatch.match_percentage * 0.65) + 
      (tfidfScore * 0.35)
    ).toFixed(2));

    let recommendation;
    let level;
    if (atsScore >= 75) {
      recommendation = "Excellent match! You are well-qualified for this role. ✅";
      level = "excellent";
    } else if (atsScore >= 60) {
      recommendation = "Good match! With minor skill improvements, you'll be competitive. 👍";
      level = "good";
    } else if (atsScore >= 40) {
      recommendation = "Moderate match. Focus learning on key missing skills. 📚";
      level = "moderate";
    } else {
      recommendation = "Significant skill gaps. Consider extensive preparation. ⚠️";
      level = "weak";
    }

    const results = {
      job_role: jobRole,
      contact,
      skill_match: skillMatch,
      tfidf_score: tfidfScore,
      ats_score: atsScore,
      detected_skills: detectedSkills,
      resources,
      recommendation,
      level
    };

    try {
      saveAnalysis(req.session.user_id, {
        job_role: jobRole,
        tfidf_score: tfidfScore,
        ats_score: atsScore,
        skill_match: skillMatch,
        recommendation,
        detected_skills: detectedSkills
      });
    } catch (error) {
      // best-effort history save
    }

    return res.json(results);
  } catch (error) {
    return res.status(500).json({ error: `Processing error: ${error.message}` });
  }
});

// Job Description Match API
app.post("/api/analyze-job-match", (req, res) => {
  try {
    const { resume_text, job_description, detected_skills } = req.body;

    if (!resume_text || !job_description) {
      return res.status(400).json({ error: "Resume text and job description are required" });
    }

    // Extract keywords from job description
    const jdKeywords = extractKeywords(job_description);
    const resumeKeywords = extractKeywords(resume_text);
    
    // Calculate match percentage
    const matched = jdKeywords.filter(keyword => 
      resumeKeywords.includes(keyword) || 
      resume_text.toLowerCase().includes(keyword.toLowerCase()) ||
      (detected_skills && detected_skills.some(skill => 
        skill.toLowerCase().includes(keyword.toLowerCase()) ||
        keyword.toLowerCase().includes(skill.toLowerCase())
      ))
    );

    const matchPercentage = jdKeywords.length > 0 
      ? Math.round((matched.length / jdKeywords.length) * 100)
      : 0;

    // Find missing keywords
    const missingKeywords = jdKeywords.filter(keyword => !matched.includes(keyword));

    // Generate suggestions
    const suggestions = generateMatchSuggestions(
      missingKeywords.slice(0, 5),
      resume_text,
      job_description
    );

    return res.json({
      match_percentage: Math.min(100, Math.max(0, matchPercentage)),
      total_keywords: jdKeywords.length,
      matched_keywords: matched.length,
      missing_keywords: missingKeywords.slice(0, 20),
      suggestions: suggestions
    });

  } catch (error) {
    console.error('Job match error:', error);
    return res.status(500).json({ error: `Analysis error: ${error.message}` });
  }
});

// Helper function to extract keywords from text
function extractKeywords(text) {
  if (!text) return [];
  
  // Common words to ignore
  const stopwords = new Set([
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
    'is', 'are', 'was', 'were', 'be', 'been', 'being', 'has', 'have', 'had', 'do',
    'does', 'did', 'will', 'would', 'should', 'could', 'can', 'may', 'might', 'must',
    'by', 'from', 'as', 'that', 'which', 'who', 'what', 'where', 'when', 'why', 'how',
    'if', 'we', 'you', 'he', 'she', 'it', 'they', 'them', 'their', 'this', 'these',
    'that', 'those', 'about', 'above', 'after', 'before', 'between', 'during', 'under',
    'your', 'our', 'our', 'its', 'more', 'most', 'through', 'into', 'during', 'including'
  ]);

  // Extract words, clean them
  const words = text
    .toLowerCase()
    .match(/\b[\w\-]+\b/g) || [];

  // Filter and deduplicate
  const keywords = new Set();
  words.forEach(word => {
    if (word.length > 2 && !stopwords.has(word)) {
      keywords.add(word);
    }
  });

  return Array.from(keywords);
}

// Helper function to generate improvement suggestions
function generateMatchSuggestions(missingKeywords, resumeText, jobDescription) {
  const suggestions = [];

  if (missingKeywords.length > 0) {
    const topMissing = missingKeywords.slice(0, 3).join(', ');
    suggestions.push(`Add mentions of: ${topMissing}`);
  }

  // Check for common patterns
  if (!resumeText.toLowerCase().includes('achievement') && 
      jobDescription.toLowerCase().includes('achievement')) {
    suggestions.push('Highlight specific achievements and measurable results in your resume');
  }

  if (!resumeText.toLowerCase().includes('experience') && 
      jobDescription.toLowerCase().includes('experience')) {
    suggestions.push('Emphasize your direct experience with the required technologies');
  }

  if (jobDescription.toLowerCase().includes('project') && 
      !resumeText.toLowerCase().includes('project')) {
    suggestions.push('Include details about projects you\'ve worked on');
  }

  // Generic suggestions if not enough specific ones
  if (suggestions.length < 3) {
    suggestions.push('Tailor your experience section to align with job requirements');
    suggestions.push('Use same terminology as in the job description');
    suggestions.push('Quantify your accomplishments with metrics and numbers');
  }

  return suggestions.slice(0, 4);
}

app.get("/about", (req, res) => res.render("index.html", { job_roles: getAllJobRoles() }));
app.get("/login", (req, res) => res.render("login.html"));
app.get("/preview", (req, res) => res.render("preview.html", { job_roles: getAllJobRoles() }));
app.get("/signup", (req, res) => res.render("signup.html"));

app.get("/skill-test/:skill", (req, res) => {
  try {
    const skill = req.params.skill;
    const questions = getSkillQuestions(skill);
    if (!questions.length) {
      return res.status(404).json({ error: "No questions available for this skill" });
    }

    const questionsToSend = questions.map((q) => ({ question: q.question, options: q.options }));
    return res.json({ skill, questions: questionsToSend, total: questionsToSend.length });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.post("/signup", (req, res) => {
  const data = req.body || {};
  const username = data.username || null;
  const password = data.password;
  const phone = data.phone || null;
  const email = data.email || (username && username.includes("@") ? username : null);

  if (!password || (!username && !phone && !email)) {
    return res.status(400).json({ error: "provide password and username, phone, or email" });
  }

  const user = createUser(username, password, phone, email);
  if (!user) {
    return res.status(400).json({ error: "username, phone, or email already exists" });
  }

  req.session.user_id = user.id;
  req.session.username = user.username;
  return res.json({ message: "user created", username: user.username, email: user.email, phone: user.phone_number });
});

app.post("/login", (req, res) => {
  const data = req.body || {};
  const username = data.username;
  const phone = data.phone;
  const password = data.password;
  const identifier = phone || username;

  if (!identifier || !password) {
    return res.status(400).json({ error: "identifier (username or phone) and password required" });
  }

  const user = authenticateUser(identifier, password);
  if (!user) {
    return res.status(401).json({ error: "invalid credentials" });
  }

  req.session.user_id = user.id;
  req.session.username = user.username;
  return res.json({ message: "logged in", username: user.username, phone: user.phone_number });
});

app.post("/request-otp", (req, res) => res.status(410).json({ error: "OTP login is disabled" }));
app.post("/verify-otp", (req, res) => res.status(410).json({ error: "OTP login is disabled" }));

app.post("/logout", (req, res) => {
  req.session.user_id = null;
  req.session.username = null;
  return res.json({ message: "logged out" });
});

app.get("/forgot-password", (req, res) => res.render("forgot_password.html"));

app.post("/forgot-password", async (req, res) => {
  const data = req.body || {};
  const identifier = data.email || data.identifier;
  if (!identifier) {
    return res.status(400).json({ error: "email required" });
  }

  try {
    const resetData = createPasswordReset(identifier);
    if (!resetData) {
      return res.status(404).json({ error: "user not found" });
    }
    try {
      const emailResult = await sendResetEmail(resetData.email, resetData.otp);
      if (emailResult.sent) {
        return res.json({ message: "reset_created", sent: true, preview: emailResult.preview || null });
      }
      return res.json({ message: "reset_created", sent: false, otp: resetData.otp, info: emailResult.reason });
    } catch (mailError) {
      return res.json({ message: "reset_created", sent: false, otp: resetData.otp, info: mailError.message });
    }
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.post("/verify-reset-otp", (req, res) => {
  const data = req.body || {};
  const identifier = data.email || data.identifier;
  const otp = data.otp;

  if (!identifier || !otp) {
    return res.status(400).json({ error: "email and otp required" });
  }

  try {
    const result = verifyPasswordResetOtp(identifier, otp);
    if (!result.ok) {
      return res.status(400).json({ error: result.error || "invalid or expired otp" });
    }
    return res.json({ message: "otp_verified", reset_ticket: result.reset_ticket });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.get("/reset-password", (req, res) => {
  const token = req.query.token || "";
  const email = req.query.email || "";
  return res.render("reset_password.html", { token, email });
});

app.post("/reset-password", (req, res) => {
  const data = req.body || {};
  const token = data.token;
  const otp = data.otp;
  const identifier = data.email || data.identifier;
  const resetTicket = data.reset_ticket;
  const newPassword = data.password;

  if (!newPassword) {
    return res.status(400).json({ error: "password required" });
  }

  const verificationCode = otp || token;
  if (!verificationCode && !resetTicket) {
    return res.status(400).json({ error: "otp or reset_ticket required" });
  }

  if (otp && !identifier && !resetTicket) {
    return res.status(400).json({ error: "email required with otp" });
  }

  try {
    const ok = resetPasswordWithToken(verificationCode, newPassword, identifier || null, resetTicket || null);
    if (!ok) {
      return res.status(400).json({ error: "invalid or expired otp" });
    }
    return res.json({ message: "password_reset" });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.get("/api/user", (req, res) => {
  if (!req.session.user_id) {
    return res.json({ user: null });
  }

  const store = loadStore();
  const found = store.users.find((row) => row.id === req.session.user_id);
  const user = found ? { username: found.username, phone_number: found.phone_number } : null;
  if (!user) {
    return res.json({ user: null });
  }
  return res.json({ user });
});

app.get("/history", (req, res) => {
  if (!req.session.user_id) {
    return res.redirect("/login");
  }
  return res.render("history.html");
});

app.get("/api/history", (req, res) => {
  const userId = req.session.user_id;
  if (!userId) {
    return res.status(401).json({ error: "not authenticated" });
  }

  try {
    const store = loadStore();
    const found = store.users.find((row) => row.id === userId);
    const user = found ? { username: found.username, phone_number: found.phone_number } : null;
    if (!user) {
      return res.json({ user: null, analyses: [] });
    }

    const analyses = store.analyses
      .filter((row) => row.user_id === userId)
      .sort((a, b) => String(a.timestamp).localeCompare(String(b.timestamp)));
    const analysesData = analyses.map((a) => {
      let skillMatch = {};
      let analysisJson = {};
      try {
        skillMatch = a.skill_match_json ? JSON.parse(a.skill_match_json) : {};
      } catch (error) {
        skillMatch = {};
      }
      try {
        analysisJson = a.analysis_json ? JSON.parse(a.analysis_json) : {};
      } catch (error) {
        analysisJson = {};
      }

      const skills = Array.isArray(analysisJson.detected_skills) ? analysisJson.detected_skills : [];
      const missing = Array.isArray(skillMatch.missing) ? skillMatch.missing : [];
      const matchPct = Number(skillMatch.match_percentage || 0);

      return {
        id: a.id,
        timestamp: a.timestamp || "",
        job_role: a.job_role || "Unknown",
        tfidf_score: Number(a.tfidf_score || 0),
        ats_score: Number(a.ats_score || 0),
        skill_match: matchPct ? matchPct / 100 : 0,
        skills_count: skills.length,
        skills,
        missing_skills: missing
      };
    });

    return res.json({ user, analyses: analysesData });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.post("/check-answers", (req, res) => {
  try {
    const data = req.body || {};
    const skill = data.skill;
    const answers = data.answers || [];
    const questions = getSkillQuestions(skill);

    if (!questions.length || answers.length !== questions.length) {
      return res.status(400).json({ error: "Invalid test data" });
    }

    let correct = 0;
    const results = questions.map((question, index) => {
      const userAnswer = Number(answers[index]);
      const isCorrect = userAnswer === question.correct;
      if (isCorrect) correct += 1;
      return {
        question: question.question,
        user_answer: question.options[userAnswer] || "",
        correct_answer: question.options[question.correct],
        is_correct: isCorrect
      };
    });

    const score = Number(((correct / questions.length) * 100).toFixed(2));
    return res.json({
      skill,
      score,
      correct,
      total: questions.length,
      results,
      passed: score >= 70
    });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.get("/debug/users", (req, res) => {
  const secret = req.query.secret;
  if (secret !== (process.env.DEBUG_SECRET || "debug-secret-change-me")) {
    return res.status(403).json({ error: "unauthorized" });
  }

  try {
    const store = loadStore();
    const users = store.users.map((user) => ({
      id: user.id,
      username: user.username,
      email: user.email,
      phone_number: user.phone_number,
      created_at: user.created_at
    }));
    return res.json({ total: users.length, users });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.post("/debug/delete-all-users", (req, res) => {
  const secret = req.query.secret;
  if (secret !== (process.env.DEBUG_SECRET || "debug-secret-change-me")) {
    return res.status(403).json({ error: "unauthorized" });
  }

  try {
    const store = loadStore();
    const deleted = store.users.length;
    const deletedAnalyses = store.analyses.length;
    store.users = [];
    store.analyses = [];
    store.password_resets = [];
    saveStore(store);
    return res.json({ deleted, deleted_analyses: deletedAnalyses });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});

app.use((err, req, res, next) => {
  if (err && err.code === "LIMIT_FILE_SIZE") {
    return res.status(413).json({ error: "File too large. Maximum size is 5MB." });
  }
  return next(err);
});

app.use((req, res) => {
  res.status(404).json({ error: "Page not found" });
});

app.use((err, req, res, next) => {
  res.status(500).json({ error: "Internal server error" });
});

const port = Number(process.env.PORT || 8080);
app.listen(port, "0.0.0.0", () => {
  console.log(`Resume Analyzer JS server listening on ${port}`);
});
