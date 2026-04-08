# AI Resume Analyzer

AI Resume Analyzer is a Node.js and Express web app that analyzes PDF resumes against selected job roles, calculates ATS-style scoring, identifies skill gaps, and suggests learning resources.

## What It Does

- Parses uploaded PDF resumes
- Detects relevant technical and soft skills by job role
- Calculates match percentage and ATS-style score
- Stores user accounts and analysis history in MongoDB
- Supports password reset flow via email

## Tech Stack

- Node.js 18+
- Express
- MongoDB with Mongoose
- Nunjucks templates
- Cloudinary and Multer for uploads
- Nodemailer for reset emails

## Run Locally

1. Install dependencies.
2. Set environment variables in a .env file.
3. Start the app.
4. Open http://localhost:8080

Commands:

```bash
npm install
npm run dev
# or
npm start
```

## Environment Variables

Required for normal use:

```env
MONGODB_URI=mongodb+srv://...
SESSION_SECRET=replace-with-a-strong-secret
```

Optional but recommended:

```env
PORT=8080
NODE_ENV=development

# Cloudinary (for persistent resume upload storage)
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

# SMTP (for password reset emails)
SMTP_HOST=
SMTP_PORT=587
SMTP_USER=
SMTP_PASS=
SMTP_SECURE=false
FROM_EMAIL=

# Used to build reset-password links
APP_BASE_URL=http://localhost:8080
```

Notes:

- If Cloudinary is not configured, uploads fall back to in-memory storage for development.
- If SMTP is not configured, email preview/test behavior is used when available.

## Project Layout

```text
resume_analyzer/
  server.js
  package.json
  src/
    db/models.js
    data/skills.js
  templates/
  static/
  data/
```

## License

MIT
