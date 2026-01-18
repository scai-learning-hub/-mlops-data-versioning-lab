# Branches Overview

This repository uses a **multi-branch strategy** to demonstrate different MLOps patterns.

## 🌿 Branch Strategy

```
main (master)
│
├── dagster-redpanda    # Orchestration variant
│
└── aws-dvc             # Cloud storage variant
```

---

## 🔹 `main` / `master` - Core Data Versioning

**Purpose:** Foundation of the repository  
**Focus:** DVC + DagsHub integration  
**Stability:** Stable ✅

### What's Here:
- DVC pipeline (`dvc.yaml`)
- Dataset generator (`src/make_tabular_data.py`)
- Data profiler (`src/profile_tabular.py`)
- DagsHub S3 remote storage
- Git tags for data versions (`data-v1`, `data-v2`, `data-v3`)

### Use This Branch When:
- Learning DVC basics
- Understanding data versioning
- Testing rollback functionality
- Starting from scratch

### Key Commands:
```bash
git checkout main
dvc repro
dvc push
git tag data-v1
```

---

## 🔹 `dagster-redpanda` - Orchestration Layer

**Purpose:** Production-style orchestration  
**Focus:** Dagster + Redpanda integration  
**Stability:** Extension 🚧

### What's Different:
- Dagster assets for pipeline orchestration
- Redpanda for event-driven ingestion
- Same DVC versioning underneath
- Focus on data movement, not training

### What's NOT Different:
- Dataset generation logic (same)
- DVC tracking (same)
- Storage backend (same DagsHub)

### Use This Branch When:
- Building scheduled pipelines
- Exploring orchestration patterns
- Integrating streaming data
- Preparing for production workflows

### Key Commands:
```bash
git checkout dagster-redpanda
dagster dev -f orchestration/dagster_app/definitions.py
```

---

## 🔹 `aws-dvc` - Cloud Backend Variant

**Purpose:** Enterprise cloud storage  
**Focus:** AWS S3 as DVC remote  
**Stability:** Extension 🚧

### What's Different:
- DVC remote points to AWS S3 (not DagsHub)
- Requires AWS credentials
- Enterprise-grade storage setup

### What's NOT Different:
- Pipeline logic (same)
- Dataset generation (same)
- Versioning workflow (same)

### Use This Branch When:
- Working in AWS environments
- Testing S3 integration
- Exploring multi-cloud setups
- Preparing for enterprise deployment

### Key Commands:
```bash
git checkout aws-dvc
dvc remote add aws-s3 s3://your-bucket/path
dvc push -r aws-s3
```

---

## 🔄 Switching Between Branches

```bash
# From main to orchestration
git checkout dagster-redpanda
dvc checkout

# From orchestration to cloud
git checkout aws-dvc
dvc checkout

# Back to main
git checkout main
dvc checkout
```

**Important:** Always run `dvc checkout` after switching branches to sync data versions.

---

## 🎯 Which Branch Should I Use?

| Scenario | Recommended Branch |
|----------|-------------------|
| Learning DVC basics | `main` |
| Understanding data versioning | `main` |
| Building pipelines with Dagster | `dagster-redpanda` |
| Using AWS infrastructure | `aws-dvc` |
| Interview prep (general) | `main` |
| Interview prep (orchestration) | `dagster-redpanda` |

---

## 🚀 Workflow Across Branches

```bash
# Start on main
git checkout main
dvc repro
git tag data-v1
dvc push

# Try orchestration
git checkout dagster-redpanda
# Dagster uses the same data-v1
dagster dev

# Try AWS storage
git checkout aws-dvc
# Configure AWS remote
dvc remote add aws s3://bucket/path
dvc push -r aws
```

---

## 📚 Learn More

- See [README.md](README.md) for overall repo structure
- See [SETUP.md](SETUP.md) for initial configuration
- See individual branch READMEs for branch-specific details

---

**Each branch teaches a different aspect of MLOps data management! 🎓**
