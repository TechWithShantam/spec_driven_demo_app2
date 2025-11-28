# Pipeline Specification (Canonical Input for Copilot)
# Version: 1.0

## 1. Pipeline Mode
# Options: build-only | test-and-build | full-pipeline
pipeline_mode: full-pipeline


## 2. CI/CD Platform
platform: github-actions
workflow_name: ci-cd-pipeline.yaml


## 3. Application Metadata
service_name: "excel-upload-service"
runtime: python
versioning_strategy: semver


## 4. Build Configuration
language: python
python_version: "3.10"
build_tool: pip

docker_enabled: true
docker:
  registry_type: ghcr               # ghcr | dockerhub | ecr | acr
  registry_url: ghcr.io/my-org
  image_name: excel-upload-service
  image_tag_strategy: git-sha       # git-sha | semver | timestamp
  dockerfile_path: "./Dockerfile"


## 5. Test & Quality Gates
tests_enabled: unit
test_command: "pytest -q"
coverage_required: true
coverage_threshold: 80
linting:
  enabled: true
  tool: black
  command: "black --check ."

security_scans:
  enabled: true
  tools:
    - bandit
    - trivy


## 6. Deployment Configuration
deploy_enabled: true

environments:
  - name: dev
    branch: main
    manual_approval: false
    auto_deploy: true

  - name: stage
    branch: release/*
    manual_approval: false
    auto_deploy: true

  - name: prod
    branch: tags/*
    manual_approval: true
    auto_deploy: false

strategy: rolling-update

kubernetes_enabled: true

helm:
  chart_path: "./charts/excel-upload-service"
  release_name_prefix: excel-upload
  namespace: "apps"
  values_file: "values.yaml"


## 7. Infrastructure-as-Code (IaC)
terraform_enabled: true
terraform:
  module: "aws-ecs-webapp"
  module_source: "git::https://github.com/my-org/terraform-modules.git//ecs-webapp?ref=v1.3.0"
  backend:
    type: s3
    bucket: "my-terraform-backend"
    key_prefix: "excel-upload-service"
    region: "ap-south-1"


## 8. Artifact Storage
artifact_store: s3
artifact_bucket_name: "ci-artifacts-excel-upload"
retain_artifacts_days: 30


## 9. Notifications
notifications:
  type: slack
  channel: "#deployments"
  webhook_secret: "SLACK_WEBHOOK"
  notify_on:
    - pipeline_failure
    - prod_deploy
    - security_scan_fail


## 10. Approvals
approval_required_for_prod: true
approval_process:
  type: github-environment-approval
  reviewers:
    - devops-team-lead
    - sre-oncall


## 11. Observability Hooks
post_deploy_checks:
  enabled: true
  healthcheck_endpoint: "/health"
  timeout_seconds: 120
  retry: 3


## 12. Required Outputs for Copilot
# Copilot MUST generate these based on this spec.
outputs:
  - github_workflow_file
  - Dockerfile
  - scripts
  - terraform_module_skeleton
  - helm_values
  - README
  - ASSUMPTIONS


## 13. Constraints & Rules
max_pipeline_runtime: "30m"
require_code_review_for_merge: true
fail_pipeline_on_lint_errors: true
fail_pipeline_on_coverage_drop: true
branch_protection:
  enabled: true
  require_status_checks: true


## 14. Additional Conditional Flags
feature_flags:
  include_database_migration: false
  include_cache_layer: false
  include_s3_sync: false


## 15. Notes for Copilot
# Copilot must:
# - Use conditional logic for workflow generation
# - Ask clarifying questions if needed
# - Document assumptions in ASSUMPTIONS.md
notes:
  - "If terraform_enabled=true, create terraform/<module_name> structure."
  - "If docker_enabled=true, add docker build + push stages."
  - "If kubernetes_enabled=true, generate helm deploy steps."
  - "Prod deploy must include approval gate."
