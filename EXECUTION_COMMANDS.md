# Execution Commands Guide

## 🎯 Terminal 1: Dagster UI Server

### Set Dagster Home (Optional - for persistent storage)
```powershell
# Create dagster home directory
mkdir .dagster_home

# Set environment variable for current session
$env:DAGSTER_HOME = "E:\mlops_dvc\dagshub_dvc_dagster_tabular\.dagster_home"

# OR set permanently (run as admin)
[System.Environment]::SetEnvironmentVariable("DAGSTER_HOME", "E:\mlops_dvc\dagshub_dvc_dagster_tabular\.dagster_home", "User")
```

### Start Dagster Web UI
```powershell
# Launch Dagster dev server
python -m dagster dev -f orchestration/dagster_app/definitions.py --port 3001

# Access UI at: http://127.0.0.1:3001
```

### Dagster UI Operations:
1. **Materialize Asset**: Assets → data_pipeline → Materialize
2. **Enable Schedule**: Automation → repro_every_2_min_schedule → Start
3. **Enable Sensor**: Automation → params_change_sensor → Start
4. **View Runs**: Runs → See all executions
5. **View Logs**: Click any run → See detailed logs

---

## 🎯 Terminal 2: DVC Pipeline Operations

### Basic DVC Workflow
```powershell
# 1. Run DVC pipeline
dvc repro

# 2. Check what changed
dvc status

# 3. Stage changes with git
git add .

# 4. Commit the changes
git commit -m "Updated pipeline - data version 1"

# 5. Create git tag for data version
git tag -a data-v1 -m "Dataset version 1"

# 6. Push data to DVC remote (DagHub)
dvc push

# 7. Push git commits and tags
git push github main
git push github --tags
```

### DVC Checkout & Version Control
```powershell
# Checkout specific data version
git checkout data-v1
dvc checkout

# Go back to latest
git checkout main
dvc checkout

# Pull data from remote
dvc pull

# Check DVC remote status
dvc remote list
dvc remote -v
```

### Modify Parameters & Trigger Pipeline
```powershell
# Edit params.yaml (this will trigger sensor if enabled)
notepad params.yaml

# Manually run DVC pipeline
dvc repro

# Force re-run all stages
dvc repro --force

# Run specific stage
dvc repro generate
dvc repro profile
```

---

## 🎯 Terminal 3: Git Branch Operations

### Create Second Branch (dagster-redpanda)
```powershell
# Create and switch to new branch
git checkout -b dagster-redpanda

# Verify branch
git branch

# Stage all files
git add .

# Commit changes
git commit -m "feat: Add Dagster orchestration with DVC integration"

# Push to GitHub
git push -u github dagster-redpanda
```

### Switch Between Branches
```powershell
# Switch to main
git checkout main
dvc checkout

# Switch to dagster-redpanda
git checkout dagster-redpanda
dvc checkout

# View all branches
git branch -a
```

---

## 🎯 Complete End-to-End Workflow

### Session 1: Initial Setup
```powershell
# Terminal 1: Start Dagster
$env:DAGSTER_HOME = ".dagster_home"
python -m dagster dev -f orchestration/dagster_app/definitions.py --port 3001

# Terminal 2: Run DVC Pipeline
dvc repro
git add dvc.lock data.dvc params.yaml
git commit -m "Initial pipeline run"
git tag -a data-v1 -m "First dataset version"
dvc push
git push github main --tags
```

### Session 2: Update Parameters & Create New Version
```powershell
# Terminal 2: Edit parameters
# Change params.yaml (e.g., n_samples: 1000 → 1500)

# Run pipeline
dvc repro

# Version the change
git add .
git commit -m "Updated n_samples to 1500"
git tag -a data-v2 -m "Increased dataset size"
dvc push
git push github main --tags
```

### Session 3: Automated with Dagster
```powershell
# Terminal 1: Dagster UI running
# Go to: http://127.0.0.1:3001/automation

# Enable sensor:
# - Toggle ON "params_change_sensor"

# Enable schedule:
# - Toggle ON "repro_every_2_min_schedule"

# Terminal 2: Edit params
notepad params.yaml
# Save changes
# Wait ~10 seconds - sensor will auto-trigger!

# Check Dagster UI → Runs to see automatic execution
```

---

## 🎯 Push to Second Branch

```powershell
# Create branch
git checkout -b dagster-redpanda

# Add changes
git add .
git commit -m "feat: Dagster orchestration with sensors and schedules"

# Push to GitHub
git push -u github dagster-redpanda

# Verify on GitHub
git branch -a
```

---

## 📊 Key Features Demonstrated

### ✅ Dagster Orchestration
- **Asset**: `data_pipeline` - Wraps `dvc repro`
- **Sensor**: `params_change_sensor` - Auto-triggers on params.yaml changes
- **Schedule**: `repro_every_2_min_schedule` - Runs every 2 minutes

### ✅ DVC Integration
- Pipeline execution via Dagster
- Version control with git tags
- Remote storage on DagHub
- Reproducible workflows

### ✅ Automation
- File-based triggers (params.yaml changes)
- Time-based triggers (cron schedule)
- Manual triggers (UI button)

---

## 🚀 Quick Reference

| Action | Command |
|--------|---------|
| Start Dagster | `python -m dagster dev -f orchestration/dagster_app/definitions.py --port 3001` |
| Run DVC | `dvc repro` |
| Version data | `git tag -a data-v1 -m "msg"` |
| Push data | `dvc push` |
| Push code | `git push github main --tags` |
| Create branch | `git checkout -b branch-name` |
| Switch branch | `git checkout branch-name` |
| Checkout data | `dvc checkout` |

---

**🎓 This setup enables full MLOps workflow with orchestration, versioning, and automation!**
