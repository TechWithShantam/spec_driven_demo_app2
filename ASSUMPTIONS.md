# ASSUMPTIONS.md

This file lists all assumptions made by Copilot during pipeline generation for excel-upload-service.

---

1. The application entry point is `app.py` and exposes a `/health` endpoint returning status 200 and 'healthy'.
2. The Docker image is built from `app.py` and dependencies in `requirements.txt`.
3. The GitHub Actions workflow uses secrets `SLACK_WEBHOOK` and `HEALTHCHECK_ENDPOINT` which must be set in the repository.
4. Terraform backend uses S3 bucket `my-terraform-backend` in region `ap-south-1`.
5. Helm chart values are set for a service running on port 8080.
6. The test runner expects a Flask-like app with a test client in `app.py`.
7. Security scan configuration (Bandit, Trivy) is based on standard usage and may need adjustment for your codebase.
8. Linting uses Black with default settings in `pyproject.toml`.
9. All environment and deployment logic is based strictly on the provided spec files.
10. Manual approval for production deploy uses your email `shantam123000@gmail.com` as reviewer.

---

If any of these assumptions are incorrect, please provide corrections or clarifications.
