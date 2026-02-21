# AI Resume Analyzer

[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-4.x-black.svg)](https://expressjs.com/)

AI-powered resume analyzer with skill-gap detection, text similarity scoring, and personalized learning resources.

## Quick Start (Local Only)

1. Install dependencies

```bash
npm install
```

2. Configure env (optional)

```bash
cp .env.example .env
```

3. Run

```bash
npm start
```

Open http://localhost:8080

## Stack

- Backend: Node.js + Express
- Auth: Session-based login/signup
- Storage: JSON file (`data/app.json`)
- PDF parsing: `pdf-parse`
- Frontend: HTML/CSS/JS + Chart.js

## Main Files

- `server.js` — Main backend server
- `src/data/skills.js` — Roles, resources, quiz data
- `templates/` — HTML templates
- `static/` — CSS/JS assets
- `data/app.json` — Local app data

## Notes

- This project is configured for local usage (no Railway config).
- Upload limit is 5MB and PDF-only.
