# Copilot Workspace Instructions (DevOps Pipeline Generator)

## Purpose
This repository uses spec-driven development to generate **complete deployment pipelines**.  
Copilot must ALWAYS read the pipeline spec under `/specs/pipeline-spec.md` before generating anything.

The goal is to allow a user to define conditions (e.g., “full pipeline”, “build only”, “deploy to dev only”, “include Docker”, “include Terraform”, “include unit test step”, etc.) and Copilot generates the corresponding DevOps workflow files.

---

## Mandatory Copilot Behaviors

### 1. Read-First Behavior
Before generating any pipeline, Copilot must:
- Read `/specs/pipeline-spec.md`
- Extract conditions, flags, environment list, required tools, deployment pattern, and validation rules
- Ask clarifying questions *if the spec is incomplete*

### 2. Output Requirements
When a user asks to generate a DevOps pipeline, Copilot must create:
- `.github/workflows/*.yml` OR `Jenkinsfile` OR `azure-pipelines.yml` OR `.gitlab-ci.yml` (based on spec)
- `Dockerfile` (if enabled in the spec)
- `terraform/` module skeletons (if IaC enabled)
- `scripts/` folder for helper shell scripts
- `README.md` explaining how the pipeline works
- `ASSUMPTIONS.md` listing any guesses Copilot made

### 3. Conditional Logic (Very Important)
Copilot must always use the conditions defined in the spec:

Examples of conditions Copilot MUST understand:
- pipeline_mode: build-only | test-and-build | full-pipeline
- environments: dev | stage | prod | custom
- deploy_enabled: true/false
- docker_enabled: true/false
- tests_enabled: unit | integration | both | none
- terraform_enabled: true/false
- notifications: slack | email | none
- approval_required: true/false for prod
- kubernetes_enabled: true/false
- artifact_store: s3 | gcs | azure | none

Based on these conditions, Copilot must:
- Include OR exclude steps
- Add conditional deployment logic
- Generate environment-specific workflows
- Add approvals or gates
- Add post-deploy checks if required

### 4. Code Style Rules
- YAML must be clean, commented, readable.
- Scripts must be POSIX-compliant (`#!/usr/bin/env bash`).
- Terraform templates must validate (`terraform fmt` + `terraform validate`).
- Include clear docstrings in shell scripts.

### 5. Testing Requirements
If tests are enabled in the spec:
- Generate a `tests/` folder
- Add at least basic CI test runners
- Include sample unit test template (if language is defined)

### 6. Ask Before Assuming
If the spec has missing values, Copilot must:
- Ask a clarifying question  
OR  
- Add a line in `ASSUMPTIONS.md` explaining the assumption

### 7. Security
- Never include real secrets.
- Always generate secret placeholders (e.g., `SECRET_TOKEN: ${{ secrets.SECRET_TOKEN }}`).
- Add security linting if enabled in the spec.

### 8. Folder Structure Rules
Copilot should scaffold:

