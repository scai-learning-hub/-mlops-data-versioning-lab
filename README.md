# 🧪 mlops-data-versioning-lab

A hands-on MLOps lab demonstrating dataset versioning, reproducibility, and rollback using DVC and DagsHub, with extensions into orchestration and cloud storage backends.

**This repository focuses on data lifecycle management, not model training.**

---

## 🎯 What This Repo Is About

Modern ML systems fail more often due to **data issues** than model issues.

This lab shows how to:

- ✅ Version datasets safely (v1 → v2 → v3)
- ✅ Roll back to a stable dataset when experiments fail
- ✅ Store large data outside Git using remote storage
- ✅ Keep experiments reproducible and auditable
- ✅ Extend the same pipeline to orchestration and cloud setups

---

## 🌿 Branch Structure (Very Important)

### 🔹 `master` / `main` — Core Data Versioning

**Status:** Stable  
**Focus:** DVC + DagsHub integration

- Dataset versions tracked via Git tags (`data-v1`, `data-v2`, `data-v3`)
- DagsHub S3 used as remote data storage
- Demonstrates rollback without recomputation

👉 **This branch is the foundation of the repo.**

### 🔹 `dagster-redpanda` — Orchestration Layer

**Status:** Extension  
**Focus:** Data orchestration & streaming

- Dagster for data orchestration
- Redpanda for stream/event-driven ingestion
- Focus on data movement & pipelines
- DVC remains the single source of truth for data versions

👉 **Shows how versioned data fits into orchestrated systems.**

### 🔹 `aws-dvc` — Cloud Backend Variant

**Status:** Extension  
**Focus:** Enterprise cloud storage

- DVC remote switched from DagsHub S3 → AWS S3
- Same pipeline, different storage backend
- Enterprise-style cloud configuration

👉 **Shows how storage can change without changing pipelines.**

---

## 📁 Project Structure (Master Branch)

```
mlops-data-versioning-lab/
├── data/tabular/raw/        # DVC-tracked data (NOT in Git)
├── reports/                 # DVC-tracked outputs
├── src/
│   ├── make_tabular_data.py # Dataset generator
│   └── profile_tabular.py   # Data profiler
├── orchestration/           # Dagster assets (other branch)
│   └── dagster_app/
│       ├── assets.py
│       └── definitions.py
├── dvc.yaml                 # Pipeline definition
├── dvc.lock                 # Exact data hashes (critical)
├── params.yaml              # Dataset configuration
├── workspace.yaml           # Dagster workspace
├── requirements.txt
└── .gitignore
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git
- DVC
- DagsHub account (free)

### Installation

```bash
# Clone the repository
git clone https://github.com/scai-learning-hub/mlops-data-versioning-lab.git
cd mlops-data-versioning-lab

# Install dependencies
pip install -r requirements.txt

# Initialize DVC (if not already done)
dvc remote add origin <your-dagshub-s3-url>

# Pull data from remote
dvc pull
```

---

## 🔁 Dataset Versioning Workflow

### Creating a New Dataset Version

```bash
# Modify parameters in params.yaml (e.g., change n_samples)
# Regenerate the dataset
dvc repro

# Commit the changes
git add dvc.lock params.yaml
git commit -m "data-v2: increased samples to 7000"
git tag data-v2

# Push to Git and DVC remote
git push
git push --tags
dvc push
```

Each version is:
- **Immutable** — Can't be changed
- **Traceable** — Git history shows when/why
- **Reproducible** — Exact same data every time

---

## 🔄 Rollback (Core Concept)

### Roll Back to a Previous Dataset

```bash
# Switch to a previous data version
git checkout data-v1
dvc checkout
```

**What happens:**
1. Git switches metadata (`dvc.lock`, `params.yaml`)
2. DVC restores the exact dataset snapshot
3. Data is pulled from remote storage if missing locally
4. **No regeneration, no recomputation**

### Return to Latest

```bash
git checkout master
dvc checkout
```

---

## 🧠 How This Works in Real ML Systems

**Typical flow:**

```
data-v1 → train → metrics OK ✅
data-v2 → train → metrics improved ✅
data-v3 → train → metrics drop ❌
rollback → data-v2 → retrain ✅
```

Each training run:
- Creates a new experiment
- Uses a **known dataset version**
- Is fully reproducible later

---

## ☁️ Storage Strategy

| Storage Backend | Branch | Use Case |
|----------------|--------|----------|
| **DagsHub S3** | `master` | Default, managed, simple |
| **AWS S3** | `aws-dvc` | Enterprise setup |

**Key points:**
- Data is **never stored in Git**
- Git only tracks **metadata & pointers**
- Large files stay in remote storage

---

## 🧪 Pipeline Stages

### 1. Generate Dataset

```bash
dvc repro generate
```

- Generates synthetic tabular data
- Configured via `params.yaml`
- Outputs to `data/tabular/raw/dataset.csv`

### 2. Profile Dataset

```bash
dvc repro profile
```

- Creates data quality report
- Outputs to `reports/profile.json`

### Run Entire Pipeline

```bash
dvc repro
```

---

## 🚫 Out of Scope (By Design)

This repo intentionally excludes:

- ❌ Model training
- ❌ Hyperparameter tuning
- ❌ Model deployment
- ❌ Production inference

**Why?** This repo is about **data correctness first**. Models come later.

---

## 🧪 Who This Repo Is For

- 🎓 MLOps learners
- 💼 Engineers preparing for interviews
- 🏢 Teams building reproducible ML pipelines
- 🔬 Anyone who wants to understand **data rollback done right**

---

## 📚 Related Resources

- [DVC Documentation](https://dvc.org/doc)
- [DagsHub Documentation](https://dagshub.com/docs)
- [Dagster Documentation](https://docs.dagster.io)

---

## ✅ Key Takeaway

> **Models change. Code changes.**  
> **But without versioned data, nothing is reproducible.**

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

This is a learning repository. Feel free to:
- Fork and experiment
- Submit PRs for improvements
- Open issues for questions

---

## 📧 Contact

For questions or discussions, open an issue on GitHub.

---

**Made with ❤️ for the MLOps community**
