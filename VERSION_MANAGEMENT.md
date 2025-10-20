# Version Management Guide

## Current Setup

### V0.1 (Stable)
- **Branch**: `master`
- **Tag**: `v0.1`
- **Status**: ✅ **PRODUCTION READY**
- **Features**: Complete Ethics Readiness Levels Tool with clean UI, real questions, academic branding

### V0.2 (Development)
- **Branch**: `v0.2-dev`
- **Status**: 🚧 **IN DEVELOPMENT**
- **Features**: [To be defined based on feedback]

## Working with Versions

### Switch to V0.1 (Stable)
```bash
git checkout master
# Or specifically to the tagged version:
git checkout v0.1
```

### Switch to V0.2 (Development)
```bash
git checkout v0.2-dev
```

### Running Different Versions
Both versions use the same commands:
```bash
source venv/bin/activate
python app.py
# Open browser to http://localhost:8080
```

## Development Workflow

### Making V0.2 Changes
1. Ensure you're on the development branch:
   ```bash
   git checkout v0.2-dev
   ```

2. Make your changes to files
3. Test thoroughly
4. Commit changes:
   ```bash
   git add .
   git commit -m "Feature: Description of change"
   ```

### When V0.2 is Ready
1. Update version files:
   ```bash
   echo "0.2" > VERSION
   ```
2. Update CHANGELOG.md with new features
3. Tag the release:
   ```bash
   git tag v0.2 -m "Version 0.2 - [Brief description]"
   ```
4. Merge back to master if desired:
   ```bash
   git checkout master
   git merge v0.2-dev
   ```

## Safety Features

- **V0.1 is protected**: Tagged and committed, easy to restore
- **Isolated development**: V0.2 changes won't affect V0.1
- **Easy switching**: Can instantly switch between versions
- **Backup available**: Original files preserved in git history

## Quick Commands

### Check current version/branch
```bash
git branch
git describe --tags
```

### See all versions
```bash
git tag -l
```

### Compare versions
```bash
git diff v0.1..v0.2-dev
```

### Emergency restore to V0.1
```bash
git checkout master
git reset --hard v0.1
```