#!/bin/bash

# Fresh Repository Setup for Vercel Deployment
# This script prepares your Resume Analyzer for a new GitHub repository

echo "📦 Resume Analyzer - Fresh Repo Setup"
echo "======================================"
echo ""

# Step 1: Clean git history
echo "1️⃣  Removing old git history..."
rm -rf .git
git init
echo "✓ Fresh git repository initialized"

# Step 2: Add all current files
echo ""
echo "2️⃣  Staging files..."
git add .
echo "✓ All files staged"

# Step 3: Create initial commit
echo ""
echo "3️⃣  Creating initial commit..."
git commit -m "🚀 Initial commit: Resume Analyzer with Vercel deployment ready

- Node.js/Express backend with MongoDB integration
- Advanced resume analysis with ATS scoring
- Job description matching feature
- Authentication & password reset
- Premium UI/UX with animations
- Cloudinary for file storage
- Ready for Vercel deployment"
echo "✓ Initial commit created"

# Step 4: Instructions
echo ""
echo "======================================"
echo "✅ Repository is ready!"
echo ""
echo "Next steps:"
echo ""
echo "1. Create a NEW repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Name it 'resume-analyzer' (or your choice)"
echo "   - DON'T initialize with README/gitignore"
echo "   - Click 'Create repository'"
echo ""
echo "2. Add remote and push:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/resume-analyzer.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Vercel:"
echo "   - Go to https://vercel.com/dashboard"
echo "   - Click 'Add New' → 'Project'"
echo "   - Select your GitHub repo"
echo "   - Add environment variables (see VERCEL_DEPLOYMENT.md)"
echo "   - Deploy!"
echo ""
echo "======================================"
