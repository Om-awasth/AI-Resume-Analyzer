# Vercel Deployment Guide

## Prerequisites

1. **GitHub Account** - Push code to GitHub
2. **Vercel Account** - Sign up at https://vercel.com
3. **MongoDB Atlas Account** - Create free cluster at https://www.mongodb.com/cloud/atlas
4. **Cloudinary Account** - Free file storage at https://cloudinary.com
5. **Gmail Account** - For password reset emails

---

## Step 1: Set Up MongoDB Atlas

1. Go to https://www.mongodb.com/cloud/atlas
2. Create account and new project
3. Create M0 Cluster (free tier)
4. Click "Connect" → "Drivers" → Copy connection string
5. Format: `mongodb+srv://username:password@cluster.mongodb.net/resume_analyzer?retryWrites=true&w=majority`
6. Replace `username` and `password` with your credentials

---

## Step 2: Set Up Cloudinary

1. Go to https://cloudinary.com and sign up
2. Go to Dashboard
3. Copy these values:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

---

## Step 3: Connect Email Service

Gmail setup for password resets:

1. Enable 2FA on your Google Account
2. Create App Password: https://myaccount.google.com/apppasswords
3. Select "Mail" and "Other (custom name)"
4. Generate 16-character password
5. Use this password in `.env`

---

## Step 4: Push to GitHub

```bash
cd /Users/omawasthi/Downloads/files/resume_analyzer

# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Resume Analyzer with Vercel setup"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git
git branch -M main
git push -u origin main
```

---

## Step 5: Deploy to Vercel

### Option A: Via Vercel Dashboard (Easiest)

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Import GitHub repository
4. Select `resume_analyzer` folder as root
5. Click "Environment Variables" and add:

```
MONGODB_URI = mongodb+srv://...
SESSION_SECRET = generate-random-key-here
CLOUDINARY_CLOUD_NAME = your-cloud-name
CLOUDINARY_API_KEY = your-api-key
CLOUDINARY_API_SECRET = your-api-secret
EMAIL_USER = your-email@gmail.com
EMAIL_PASSWORD = google-app-password
NODE_ENV = production
```

6. Click "Deploy"

### Option B: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
cd /Users/omawasthi/Downloads/files/resume_analyzer
vercel --prod

# Follow prompts to add environment variables
```

---

## Step 6: Verify Deployment

After deployment completes:

1. Visit your Vercel app URL
2. Test sign up with email
3. Test password reset flow
4. upload a resume and run analysis
5. Check history

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 502 Bad Gateway | Check MongoDB connection string in env vars |
| File upload fails | Verify Cloudinary credentials |
| Email not sending | Enable 2FA on Gmail, use app password |
| Session not persisting | Ensure SESSION_SECRET is set |

---

## Production Checklist

- [ ] MongoDB URI set correctly
- [ ] Cloudinary credentials added
- [ ] Email service configured
- [ ] SESSION_SECRET is strong (min 32 chars)
- [ ] All environment variables added to Vercel
- [ ] HTTPS redirects working
- [ ] Tests run successfully locally

---

## Cost Estimate

- **Vercel**: Free tier (up to 10GB bandwidth)
- **MongoDB**: Free tier M0 cluster
- **Cloudinary**: Free tier (10GB storage)
- **Gmail**: Free

**Total: $0/month** (or upgrade as needed)

---

## Next Steps

1. Set up custom domain (optional)
2. Configure analytics
3. Enable CORS for API access
4. Set up continuous deployment
