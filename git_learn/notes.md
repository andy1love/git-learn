# Git Learning Notes

## Basic Git Commands

### 1. Initialize Repository
```bash
git init
```

### 2. Check Status
```bash
git status
```

### 3. Add Files
```bash
git add filename.txt          # Add specific file
git add .                     # Add all files
git add *.py                  # Add all Python files
```

### 4. Commit Changes
```bash
git commit -m "Your commit message"
```

### 5. View History
```bash
git log
git log --oneline
```

### 6. Remote Operations
```bash
git remote add origin <url>   # Add remote repository
git push origin main          # Push to remote
git pull origin main          # Pull from remote
```

## Git Workflow

1. **Working Directory** - Where you make changes
2. **Staging Area** - Where you prepare changes for commit
3. **Repository** - Where committed changes are stored

## Cursor Interface Tips

- Use Command Palette (Cmd+Shift+P) to access Git commands
- Source Control panel shows file changes
- Integrated terminal for Git commands
- Built-in diff viewer for changes

## Learning Progress

- [x] Create initial files
- [ ] Initialize Git repository
- [ ] Stage files
- [ ] Make first commit
- [ ] Create remote repository
- [ ] Push to remote
- [ ] Practice workflow
