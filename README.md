# Git Learning Project

This is a project to learn Git fundamentals including:
- add
- commit  
- push
- pull
- branch
- merge

## Getting Started

1. Initialize Git repository
2. Add files to staging
3. Commit changes
4. Push to remote repository
5. Pull changes from remote

## Files

- `hello.txt` - A simple text file
- `calculator.py` - A Python calculator
- `notes.md` - Learning notes

## Git Commands Cheat Sheet

### Basic Commands
```bash
git init                    # Initialize repository
git status                  # Check repository status
git add <file>              # Stage file
git add .                   # Stage all files
git commit -m "message"     # Commit changes
git log                     # View commit history
```

### Remote Commands
```bash
git remote add origin <url> # Add remote repository
git push origin main        # Push to remote
git pull origin main        # Pull from remote
git clone <url>             # Clone repository
```

### Branching
```bash
git branch                  # List branches
git checkout -b <branch>    # Create and switch to branch
git checkout <branch>       # Switch to branch
git merge <branch>          # Merge branch
```
