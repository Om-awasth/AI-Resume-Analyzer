# Pre-Deployment Checklist ✅

Copy and paste this checklist to track your progress:

## 🔧 Local Setup (30 seconds)

- [ ] Installed Node.js 18+: `node --version`
- [ ] Run `npm install` in resume_analyzer folder
- [ ] Created `.env` file with all variables from `.env.example`
- [ ] Server starts: `npm start`

## 📊 MongoDB Atlas Setup (5 minutes)

- [ ] Created MongoDB Atlas account
- [ ] Created free M0 cluster
- [ ] Created database user
- [ ] Added IP whitelist: `0.0.0.0/0` (for Vercel)
- [ ] Copied connection string
- [ ] Added to `.env` as `MONGODB_URI`

## ☁️ Cloudinary Setup (3 minutes)

- [ ] Created Cloudinary account
- [ ] Copied Cloud Name
- [ ] Generated API Key and Secret
- [ ] Added to `.env` as `CLOUDINARY_*`

## 📧 Gmail Setup (2 minutes)

- [ ] Enabled 2FA on Gmail account
- [ ] Generated app password for Mail
- [ ] Added to `.env` as `EMAIL_USER` and `EMAIL_PASSWORD`

## 🔐 Security (2 minutes)

- [ ] Generated SESSION_SECRET: `node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"`
- [ ] Added to `.env` as `SESSION_SECRET`
- [ ] Updated `.env.example` (never commit actual secrets)

## 🧪 Local Testing (5 minutes)

- [ ] App runs without errors: `npm start`
- [ ] Can access http://localhost:8080
- [ ] Can sign up and log in
- [ ] Can upload and analyze resume
- [ ] Password reset email works

## 📤 GitHub Setup (3 minutes)

- [ ] Created new GitHub repository
- [ ] Copied repository URL
- [ ] Run these commands:
  ```bash
  cd /Users/omawasthi/Downloads/files/resume_analyzer
  git remote add origin YOUR_REPO_URL
  git branch -M main
  git push -u origin main
  ```
- [ ] Verified code appears on GitHub

## 🚀 Vercel Deployment (10 minutes)

- [ ] Created Vercel account
- [ ] Connected GitHub account
- [ ] Imported repository from Vercel dashboard
- [ ] Selected correct root directory: `resume_analyzer/`
- [ ] Added all environment variables in Vercel:
  - [ ] MONGODB_URI
  - [ ] SESSION_SECRET
  - [ ] CLOUDINARY_CLOUD_NAME
  - [ ] CLOUDINARY_API_KEY
  - [ ] CLOUDINARY_API_SECRET
  - [ ] EMAIL_USER
  - [ ] EMAIL_PASSWORD
  - [ ] NODE_ENV = production
- [ ] Clicked "Deploy"
- [ ] Deployment completed (green checkmark)

## ✨ Post-Deployment (5 minutes)

- [ ] Visited live URL (Vercel provides it)
- [ ] Signed up with test account
- [ ] Tested password reset flow
- [ ] Uploaded test resume
- [ ] Ran analysis successfully
- [ ] Tested job matching feature
- [ ] All features work without errors

## 🎉 Optional - Polish (5 minutes)

- [ ] Added custom domain (optional)
- [ ] Set up Google Analytics
- [ ] Configured CI/CD email notifications
- [ ] Shared link on portfolio/LinkedIn

---

## 📝 Key Notes

1. **Never commit `.env`** - Already in `.gitignore`
2. **Keep credentials secret** - Don't share screenshots with env vars visible
3. **Database backup** - MongoDB Atlas has auto backups
4. **Monitoring** - Check Vercel dashboard for errors
5. **Updates** - Git push to auto-deploy changes

---

## ⏱️ Time Estimate

- **First time**: 30-45 minutes total
- **Repeat deploys**: 2-3 minutes (just git push!)

---

## 🔗 Helpful Links

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- [Cloudinary](https://cloudinary.com)
- [Gmail App Passwords](https://myaccount.google.com/apppasswords)
- [Vercel Dashboard](https://vercel.com/dashboard)
- [Your Repo on GitHub](https://github.com/YOUR_USERNAME/resume-analyzer)

---

**Status: Ready to deploy! 🚀**

Start with MongoDB setup, then GitHub, then Vercel. You've got this! 💪
