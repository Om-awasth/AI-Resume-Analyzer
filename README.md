# AI Resume Analyzer

[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-4.x-black.svg)](https://expressjs.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Ready-00ed64.svg)](https://mongodb.com)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-000000.svg)](https://vercel.com)

**Production-ready AI-powered resume analyzer** with skill-gap detection, ATS scoring, job matching, and personalized learning recommendations. Deploy to Vercel in 25 minutes.

## ✨ Features

- 📊 **ATS Score Analysis** - Evaluate resume against job descriptions
- 🎯 **Skill Detection** - Extract and match required skills
- 🤖 **Job Matching** - Compare resume to job descriptions
- 📚 **Learning Resources** - Personalized recommendations
- 🔐 **User Authentication** - Secure login/signup
- 👥 **Analysis History** - Track improvements over time
- ✨ **Premium UI** - Animated, responsive design
- ☁️ **Cloud Storage** - Resume persistence

## 🚀 Deploy to Vercel (25 minutes)

**⭐ START HERE:** Read [DEPLOYMENT_ROADMAP.md](./DEPLOYMENT_ROADMAP.md)

Quick steps:
1. Create GitHub repo
2. Push code: `git push -u origin main`
3. Deploy on Vercel (connect GitHub)
4. Add environment variables (MongoDB, Cloudinary, Gmail)
5. Done! ✨

**Free tier pricing:** $0/month (Vercel, MongoDB, Cloudinary, Gmail all free)

## 🏃 Quick Start (Local Development)

### Prerequisites
- Node.js 18+
- MongoDB (local or Atlas)
- Cloudinary account (optional, for uploads)

### Installation

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git
cd resume_analyzer

# Install dependencies
npm install

# Create .env file
cp .env.example .env
# Edit .env with your MongoDB URI, Cloudinary keys, etc.

# Start server
npm start

# Open http://localhost:8080
```

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Runtime** | Node.js 18+ |
| **Framework** | Express 4.x |
| **Database** | MongoDB + Mongoose |
| **Storage** | Cloudinary |
| **Auth** | express-session + bcryptjs |
| **Email** | Nodemailer |
| **Frontend** | HTML5 + CSS3 + Vanilla JS |
| **Deployment** | Vercel |

## 📁 Project Structure

```
resume_analyzer/
├── server.js              # Main backend
├── vercel.json            # Deployment config
├── package.json           # Dependencies
├── .env.example          # Environment template
├── src/
│   ├── db/
│   │   └── models.js     # MongoDB schemas
│   └── data/
│       └── skills.js     # Job roles & resources
├── templates/            # HTML pages
├── static/              # CSS, JS, images
└── data/                # Local storage (development)
```

## 📚 Documentation

- [DEPLOYMENT_ROADMAP.md](./DEPLOYMENT_ROADMAP.md) - **Start here for Vercel**
- [DEPLOY_NOW.md](./DEPLOY_NOW.md) - Quick deployment checklist
- [CHECKLIST.md](./CHECKLIST.md) - Pre-deployment verification
- [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md) - Detailed guide

## 🔧 Environment Variables

Create `.env` file with:

```env
MONGODB_URI=mongodb+srv://...
SESSION_SECRET=your-secret-key
CLOUDINARY_CLOUD_NAME=your-cloud
CLOUDINARY_API_KEY=your-key
CLOUDINARY_API_SECRET=your-secret
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
NODE_ENV=production
```

See `.env.example` for all variables.

## 📦 Main Files

- **`server.js`** — Express server, routes, backend logic
- **`src/db/models.js`** — MongoDB schemas (User, Analysis, PasswordReset)
- **`src/data/skills.js`** — Job roles, resources, quiz data
- **`templates/`** — Nunjucks HTML templates
- **`static/script.js`** — Frontend animations & API calls
- **`static/style.css`** — Premium UI styling

## 🧪 Local Testing

```bash
# Development mode (auto-reload)
npm run dev

# Production mode
npm start

# Syntax check
node --check server.js
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/login` | Login page |
| GET | `/signup` | Signup page |
| POST | `/signup` | Create account |
| POST | `/login` | Login user |
| POST | `/analyze` | Analyze resume |
| POST | `/api/analyze-job-match` | Match to job description |
| GET | `/api/history` | Get user history |
| POST | `/forgot-password` | Request password reset |

## 💡 Usage Examples

### Analyze Resume
```javascript
const formData = new FormData();
formData.append('resume', pdfFile);
formData.append('job_role', 'Software Engineer');

fetch('/analyze', {
  method: 'POST',
  body: formData
}).then(r => r.json()).then(data => {
  console.log('ATS Score:', data.ats_score);
  console.log('Skills:', data.skill_match);
});
```

### Match Job Description
```javascript
fetch('/api/analyze-job-match', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    resume_text: 'Your resume content...',
    job_description: 'Job posting text...'
  })
}).then(r => r.json()).then(data => {
  console.log('Match %:', data.match_percentage);
  console.log('Missing:', data.missing_keywords);
});
```

## 🚨 Troubleshooting

### 502 Bad Gateway on Vercel?
- Check MongoDB connection string
- Ensure MongoDB IP whitelist includes `0.0.0.0/0`

### File uploads failing?
- Verify Cloudinary credentials
- Check Cloudinary quota not exceeded

### Email not sending?
- Ensure Gmail 2FA is enabled
- Use App Password, not account password

## 📊 Performance

- Response time: <500ms
- Database queries: Indexed
- File uploads: Cloudinary CDN
- API rate limits: None set (add if needed)

## 🔒 Security

- Passwords hashed with bcryptjs
- Sessions server-side only
- CSRF protection ready
- Environment variables secured
- No secrets in git (.gitignore)

## 📝 License

MIT - Build and deploy freely!

## 🤝 Contributing

Contributions welcome! Fork, create feature branch, submit PR.

## ❓ Support

- Check documentation files
- Review deployment guides
- Check error logs on Vercel dashboard

---

**Ready to deploy?** Start with [DEPLOYMENT_ROADMAP.md](./DEPLOYMENT_ROADMAP.md) 🚀
