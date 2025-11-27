# Setting Up Your GitHub Repository

This guide will help you save this repo to your own GitHub account.

## Step 1: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Choose a repository name (e.g., `deepagents-quickstarts-contextual` or `deepagents-contextual-ai`)
3. Choose whether it should be public or private
4. **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

## Step 2: Update the Remote and Push

After creating the repository, GitHub will show you the repository URL. Use one of the following commands:

### Option A: If you want to replace the existing remote (recommended for a fork)

```bash
# Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual values
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### Option B: If you want to keep the original as upstream and add yours as origin

```bash
# Rename current remote to upstream
git remote rename origin upstream

# Add your new repo as origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

## Step 3: Commit Your Changes

```bash
# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Add ContextualAI RAG search integration

- Added contextual_search tool for RAG-based document search
- Updated READMEs with ContextualAI setup instructions
- Added contextual package to dependencies
- Tool retrieves full content text with attribution metadata"
```

## Step 4: Push to Your Repository

```bash
# Push to your new repository
git push -u origin main
```

If you get an error about the branch name, try:
```bash
git push -u origin main:main
```

## Step 5: Verify

Visit your GitHub repository URL to verify all files are there and the changes are committed.

## Quick Setup Script

Alternatively, you can run this script (replace the variables first):

```bash
#!/bin/bash
# Replace these with your GitHub username and repo name
GITHUB_USERNAME="your-username"
REPO_NAME="your-repo-name"

# Update remote
git remote set-url origin https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git

# Stage, commit, and push
git add .
git commit -m "Add ContextualAI RAG search integration

- Added contextual_search tool for RAG-based document search
- Updated READMEs with ContextualAI setup instructions
- Added contextual package to dependencies
- Tool retrieves full content text with attribution metadata"

git push -u origin main
```

