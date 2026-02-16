# security-pipeline

Secure CI/CD pipeline example with a small Python app and reusable workflows for SAST, DAST, dependency scanning, and secrets management.

## Pipeline layout

- Main pipeline: [./.github/workflows/ci.yml](.github/workflows/ci.yml)
- Reusable pipelines:
  - Build and test: [./.github/workflows/build-test.yml](.github/workflows/build-test.yml)
  - SAST (Semgrep): [./.github/workflows/sast.yml](.github/workflows/sast.yml)
  - Dependency scan (pip-audit): [./.github/workflows/dependency-scan.yml](.github/workflows/dependency-scan.yml)
  - Secrets scan (Gitleaks): [./.github/workflows/secrets-scan.yml](.github/workflows/secrets-scan.yml)
  - DAST (OWASP ZAP baseline): [./.github/workflows/dast.yml](.github/workflows/dast.yml)

## Security pipeline process (example flow)

1. Build and test validate the application behavior.
2. SAST scans code patterns and produces SARIF for security reporting.
3. Dependency scan checks Python packages for known vulnerabilities.
4. Secrets scan detects hard-coded credentials and leaks.
5. DAST runs an OWASP ZAP baseline scan against a running instance of the app.

Artifacts include SARIF and JSON reports for inspection.

## Example app

- App module: [./app/app.py](app/app.py)
- Tests: [./tests/test_app.py](tests/test_app.py)

### Run locally

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python -m app.app
```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/health.

### Run tests

```bash
pytest -q
```
