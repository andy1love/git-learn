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
- [x] Initialize Git repository
- [x] Stage files
- [x] Make first commit
- [x] Create remote repository
- [x] Push to remote
- [x] Practice workflow

## Daily Git Workflow

### 1. Start Your Day
```bash
git pull origin main    # Get latest changes from team
```

### 2. Make Changes
- Edit files in your editor
- Create new files
- Delete files

### 3. Review Your Changes
```bash
git status              # See what files changed
git diff               # See what changed in files
```

### 4. Stage Changes
```bash
git add filename       # Stage specific file
git add .              # Stage all changes
git add *.py           # Stage all Python files
```

### 5. Commit Changes
```bash
git commit -m "Add new feature: user authentication"
```

### 6. Push Changes
```bash
git push origin main
```
