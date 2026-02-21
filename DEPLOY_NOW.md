# Deploy to GitHub & Vercel - Quick Start

Your Resume Analyzer is ready to deploy! Follow these simple steps:

## 📋 Before You Start

Have these ready:
1. GitHub account (https://github.com)
2. Vercel account (https://vercel.com)
3. MongoDB Atlas free cluster
4. Cloudinary account
5. Gmail app password

## 🚀 Step 1: Create GitHub Repository

```bash
# 1. Go to https://github.com/new
# 2. Create NEW repository:
#    - Name: resume-analyzer
#    - Description: AI-powered resume analyzer with ATS scoring
#    - Public (for portfolio)
#    - DON'T check "Initialize with README"
# 3. Copy the repository URL (looks like: https://github.com/YOUR_USERNAME/resume-analyzer.git)
```

## 📤 Step 2: Push Code to GitHub

```bash
cd /Users/omawasthi/Downloads/files/resume_analyzer

# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git
git branch -M main
git push -u origin main

# Verify it worked - check your GitHub repo in browser
```

## 🌐 Step 3: Deploy to Vercel

### Via Dashboard (Recommended)

```
1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Click "Import Git Repository"
4. Select your "resume-analyzer" repo
5. Click "Import"
```

### Configure Deployment

```
Root Directory: resume_analyzer/  (select this folder)
Framework Preset: Other
Install Command: npm install
Build Command: (leave empty)
Output Directory: (leave empty)
```

### Add Environment Variables

In Vercel dashboard, go to Settings → Environment Variables:

```
MONGODB_URI
mongodb+srv://username:password@cluster.mongodb.net/resume_analyzer

SESSION_SECRET
(generate strong random string, min 32 chars)

CLOUDINARY_CLOUD_NAME
your-cloud-name

CLOUDINARY_API_KEY
your-api-key

CLOUDINARY_API_SECRET
your-api-secret

EMAIL_USER
your-email@gmail.com

EMAIL_PASSWORD
your-app-password

NODE_ENV
production
```

Click "Deploy" and wait 2-3 minutes!

## ✅ Verify Deployment

Once Vercel deploys:

1. Click "Visit" to see your live app
2. Test signup with email
3. Try password reset
4. Upload a resume and analyze it
5. Share your portfolio! 🎉

## 📚 Environment Variables Explained

| Variable | Where to Get |
|----------|-------------|
| MONGODB_URI | MongoDB Atlas → Connect → Driver |
| SESSION_SECRET | Generate: `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"` |
| CLOUDINARY_* | Cloudinary Dashboard → Settings → API Keys |
| EMAIL_PASSWORD | Google Account → App passwords → Generate for Mail |

## 🆘 Troubleshooting

**502 Bad Gateway after deployment?**
- Check MongoDB URI in environment variables
- Ensure IP whitelist allows Vercel (MongoDB Atlas → Network Access → Add 0.0.0.0/0)

**Uploads not working?**
- Verify Cloudinary credentials
- Check Cloudinary account has remaining quota

**Email not sending?**
- Gmail requires 2FA enabled
- Use app password, not account password
- Check Gmail → Security → App passwords

**Still have issues?**
- Check Vercel deployment logs
- Read VERCEL_DEPLOYMENT.md for detailed guide

## 🎯 What You Have

✅ Full-stack resume analyzer
✅ MongoDB persistence
✅ Cloudinary file storage
✅ Email authentication
✅ Job Description matching
✅ Premium UI animations
✅ Mobile responsive
✅ Production-ready code

## 📊 Free Tier Limits

- **Vercel**: 10GB bandwidth/month
- **MongoDB**: 512MB storage
- **Cloudinary**: 10GB storage
- **Gmail**: Unlimited app passwords

Plenty for a production app!

## 🎨 Next: Custom Domain (Optional)

In Vercel dashboard:
1. Go to your project
2. Settings → Domains
3. Add your custom domain
4. Follow DNS setup instructions

---

**You're all set! Deploy now and share your link with the world! 🚀**
