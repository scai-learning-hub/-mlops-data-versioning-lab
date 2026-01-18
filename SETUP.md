# 🚀 Initial Setup Guide

This guide walks you through setting up the repository from scratch for the first time.

---

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher installed
- Git installed and configured
- A DagsHub account (free) - [Sign up here](https://dagshub.com/)
- Basic command line knowledge

---

## 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/scai-learning-hub/mlops-data-versioning-lab.git
cd mlops-data-versioning-lab
```

---

## 🐍 Step 2: Set Up Python Environment

### Option A: Using venv

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option B: Using conda

```bash
# Create conda environment
conda create -n mlops-dvc python=3.10 -y
conda activate mlops-dvc

# Install dependencies
pip install -r requirements.txt
```

---

## 🔗 Step 3: Connect to DagsHub Remote Storage

### 3.1 Create a DagsHub Repository

1. Go to [DagsHub](https://dagshub.com/)
2. Create a new repository (or connect this one)
3. Note your DagsHub username and repo name

### 3.2 Configure DVC Remote

```bash
# Initialize DVC (if not already done)
dvc init

# Add DagsHub as remote storage
dvc remote add origin https://dagshub.com/<YOUR_USERNAME>/<YOUR_REPO>.dvc

# Set credentials (you'll be prompted)
dvc remote modify origin --local auth basic
dvc remote modify origin --local user <YOUR_DAGSHUB_USERNAME>
dvc remote modify origin --local password <YOUR_DAGSHUB_TOKEN>
```

**Note:** Get your DagsHub token from: Settings → Tokens → Create Token

### 3.3 Alternative: Use DagsHub CLI

```bash
# Install DagsHub
pip install dagshub

# Configure credentials
dagshub login
```

---

## 🎯 Step 4: Generate Your First Dataset

```bash
# Run the DVC pipeline
dvc repro

# This will:
# 1. Generate synthetic dataset (data/tabular/raw/dataset.csv)
# 2. Create data profile report (reports/profile.json)
```

---

## 📤 Step 5: Push Data to Remote

```bash
# Push data to DagsHub storage
dvc push

# Commit the DVC metadata to Git
git add dvc.lock dvc.yaml params.yaml .gitignore
git commit -m "Initial data version (data-v1)"
git tag data-v1
git push origin main
git push --tags
```

---

## ✅ Step 6: Verify Setup

```bash
# Check DVC status
dvc status

# Check DVC remote
dvc remote list

# Check Git tags
git tag
```

You should see:
- ✅ DVC remote configured
- ✅ `data-v1` tag created
- ✅ No uncommitted changes

---

## 🔄 Step 7: Test Rollback (Optional)

```bash
# Create a second version
# Edit params.yaml (change n_samples to 7000)
dvc repro
git add dvc.lock params.yaml
git commit -m "data-v2: increased samples"
git tag data-v2
git push --tags
dvc push

# Now test rollback
git checkout data-v1
dvc checkout

# Return to latest
git checkout main
dvc checkout
```

---

## 🌿 Step 8: Create Additional Branches (Optional)

### For Dagster + Redpanda orchestration:

```bash
git checkout -b dagster-redpanda
# Add Dagster/Redpanda specific code here
git push -u origin dagster-redpanda
```

### For AWS S3 backend:

```bash
git checkout -b aws-dvc
# Reconfigure DVC remote to AWS S3
dvc remote add aws-s3 s3://your-bucket/path
git push -u origin aws-dvc
```

---

## 🐛 Troubleshooting

### Issue: DVC push fails

**Solution:**
```bash
# Check credentials
dvc remote list
dvc config --list

# Re-authenticate
dvc remote modify origin --local auth basic
```

### Issue: Git won't track large files

**Solution:** Ensure `.gitignore` excludes `/data` and `/reports`

### Issue: Python dependencies conflict

**Solution:** Use a fresh virtual environment
```bash
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 📚 Next Steps

- Read the [README.md](README.md) for usage patterns
- Try modifying `params.yaml` to create new dataset versions
- Explore Dagster integration (if on `dagster-redpanda` branch)
- Check out AWS S3 setup (if on `aws-dvc` branch)

---

## 💡 Pro Tips

1. **Always tag data versions** — Makes rollback easy
2. **Push to DVC after every experiment** — Don't lose data
3. **Document parameter changes** — Future you will thank you
4. **Test rollback early** — Make sure it works before you need it

---

## 🆘 Need Help?

- Open an issue on GitHub
- Check DVC docs: https://dvc.org/doc
- Check DagsHub docs: https://dagshub.com/docs

---

**You're all set! 🎉**
