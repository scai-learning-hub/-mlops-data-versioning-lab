# Contributing to mlops-data-versioning-lab

Thank you for your interest in contributing! This is a learning-focused repository, and we welcome improvements from the community.

## 🎯 What We're Looking For

- Bug fixes in existing pipelines
- Documentation improvements
- Additional dataset version examples
- Better error handling
- Enhanced data profiling features
- New storage backend examples (Azure, GCP, MinIO, etc.)

## 🚫 What We're NOT Looking For

- Model training code (out of scope)
- Complex ML algorithms
- Deployment/serving infrastructure
- Changes that obscure the core learning objectives

## 📝 How to Contribute

### 1. Fork the Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/mlops-data-versioning-lab.git
cd mlops-data-versioning-lab
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes

- Follow existing code style
- Update documentation if needed
- Test your changes locally

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: brief description of your change"
```

**Commit message format:**
- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation changes
- `refactor:` code refactoring
- `test:` adding tests

### 5. Push and Create a Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a PR on GitHub with:
- Clear description of the change
- Why it's needed
- How it was tested

## 🧪 Testing Guidelines

Before submitting:

```bash
# Run the pipeline
dvc repro

# Verify output
ls -la data/tabular/raw/
ls -la reports/

# Test rollback (if applicable)
git tag test-v1
dvc push
git checkout test-v1
dvc checkout
```

## 📚 Code Style

- Python: Follow PEP 8
- YAML: 2-space indentation
- Markdown: Use clear headings and code blocks

## 🤝 Code of Conduct

- Be respectful and constructive
- Focus on learning and education
- Help others understand your changes

## 💡 Questions?

Open an issue if you're unsure about anything!

---

**Thanks for helping make MLOps education better! 🚀**
