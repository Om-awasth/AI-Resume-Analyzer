# Deploy to Railway

## Quick Start

### Step 1: Set up GitHub repository
```bash
cd /Users/omawasthi/Downloads/files/resume_analyzer
git init
git add .
git commit -m "Initial commit: Resume Analyzer app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git
git push -u origin main
```

**Replace:**
- `YOUR_USERNAME` with your GitHub username
- Create repo on GitHub first at https://github.com/new

---

### Step 2: Deploy to Railway

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub"
3. Connect your GitHub account
4. Select `resume-analyzer` repository
5. Railway automatically detects Python + Procfile
6. Add Environment Variables:
   - `FLASK_ENV`: `production`
   - `RESUME_ANALYZER_SECRET`: Generate with `python -c "import secrets; print(secrets.token_hex(32))"`
   - `DATABASE_URL`: (auto-generated if you add PostgreSQL)

7. Click "Deploy" ✅

---

### Step 3: Add PostgreSQL (Optional but Recommended)

1. In Railway dashboard, click "+ New"
2. Select "PostgreSQL"
3. Railway auto-adds `DATABASE_URL` env var
4. App will use PostgreSQL in production

---

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your settings

# Run app
python app.py
```

Visit: http://localhost:8080

---

## Environment Variables Needed

See `.env.example` for all options. Key ones:

- `FLASK_ENV`: `production` or `development`
- `RESUME_ANALYZER_SECRET`: Random secret key
- `DATABASE_URL`: PostgreSQL connection (Railway provides this)
- `MAIL_*`: Email config for password resets (optional)

---

## Troubleshooting

**App crashes on deploy?**
- Check Railway logs: Dashboard → Deployments → View Logs
- Ensure all env vars are set
- Check `requirements.txt` has all dependencies

**Database issues?**
- Add PostgreSQL via Railway Dashboard
- Railway auto-sets `DATABASE_URL`
- Migrations run automatically

**Logo/images not showing?**
- Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+R)
- Check Railway storage for uploaded files

---

## Next Steps After Deploy

1. Share your Railway URL with friends
2. Continue improving features
3. Push updates to GitHub → Auto-deploys
4. Monitor in Railway Dashboard

**Your app will be live at:** `your-app-name.railway.app`
