# OSOP Examples

**Part of SOP Doc.** 113 workflow templates across 20+ domains.

API SOPs (Stripe, GitHub, MediRank), DevOps pipelines, AI agent chains, business processes, data pipelines, compliance workflows. Each example is a valid .osop.yaml file. Browse them at osop.ai/sop-doc.

## Quick Start

```bash
# Clone
git clone https://github.com/Archie0125/osop-examples.git
cd osop-examples

# Validate any example
osop validate devops/github-actions-cicd.osop.yaml

# Dry-run (see what would execute, no side effects)
osop record demo/simple-agent-chain.osop.yaml --dry-run

# Real execution with LLM calls (requires ANTHROPIC_API_KEY)
export ANTHROPIC_API_KEY=sk-ant-...
osop record demo/simple-agent-chain.osop.yaml

# Execute CLI nodes (requires explicit opt-in)
osop record devops/github-actions-cicd.osop.yaml --allow-exec

# Generate execution log
osop record demo/simple-agent-chain.osop.yaml --log output.osoplog.yaml
```

### Security

- CLI nodes (shell commands) are **blocked by default**. Use `--allow-exec` after reviewing commands.
- LLM costs are capped at **$1.00** by default. Override with `--max-cost`.
- Risk assessment runs before execution. Critical findings block without `--allow-exec`.

## Demo Workflow

The `demo/simple-agent-chain.osop.yaml` runs a 3-agent chain: generate an idea, critique it, refine it. Each node calls Claude and passes output to the next.

```bash
osop record demo/simple-agent-chain.osop.yaml
```

## Examples by Domain

### DevOps (6 examples)

| File | Description |
|------|-------------|
| `devops/ci-build-test-deploy.osop.yaml` | Full CI/CD pipeline: build, unit test, integration test, approval, deploy |
| `devops/rollback-on-failure.osop.yaml` | Deployment with automatic rollback via error edges |
| `devops/multi-env-promotion.osop.yaml` | Promote through dev, staging, production with approval gates |
| `devops/hotfix-release.osop.yaml` | Emergency hotfix: branch, fix, fast-track review, deploy |
| `devops/infrastructure-drift-check.osop.yaml` | Scheduled Terraform plan to detect infrastructure drift |
| `devops/secret-rotation.osop.yaml` | Rotate secrets across services with validation steps |

### Testing (4 examples)

| File | Description |
|------|-------------|
| `testing/e2e-test-suite.osop.yaml` | End-to-end test suite with parallel browser tests |
| `testing/load-test-ramp.osop.yaml` | Progressive load testing with ramp-up stages and thresholds |
| `testing/canary-validation.osop.yaml` | Canary deployment with automated health check validation |
| `testing/regression-gate.osop.yaml` | Regression test gate with retry on flaky tests |

### Infrastructure (4 examples)

| File | Description |
|------|-------------|
| `infrastructure/provision-cluster.osop.yaml` | Provision a Kubernetes cluster with networking and monitoring |
| `infrastructure/database-migration.osop.yaml` | Database schema migration with backup and rollback |
| `infrastructure/ssl-cert-renewal.osop.yaml` | Automated SSL certificate renewal with DNS validation |
| `infrastructure/disaster-recovery-failover.osop.yaml` | DR failover: health check, DNS switch, data sync verification |

### AI Agent (3 examples + 1 execution log)

| File | Description |
|------|-------------|
| `ai-agent/rag-pipeline.osop.yaml` | RAG pipeline: ingest, chunk, embed, index, query |
| `ai-agent/model-evaluation.osop.yaml` | LLM evaluation: generate, judge, aggregate scores, report |
| `ai-agent/agent-tool-selection.osop.yaml` | Multi-tool agent: decide tool, execute, validate output, retry |
| `ai-agent/research-and-summarize.osoplog.yaml` | Example `.osoplog` execution record: research workflow with retries, cost tracking, and human approval |

### Data (4 examples)

| File | Description |
|------|-------------|
| `data/etl-pipeline.osop.yaml` | Extract-Transform-Load with validation and error handling |
| `data/data-quality-check.osop.yaml` | Data quality checks: schema, nulls, outliers, freshness |
| `data/batch-export.osop.yaml` | Batch data export with chunking and progress tracking |
| `data/data-anonymization.osop.yaml` | PII detection and anonymization pipeline for compliance |

### API (3 examples)

| File | Description |
|------|-------------|
| `api/api-versioning-release.osop.yaml` | API version release: generate docs, update gateway, notify consumers |
| `api/webhook-retry-handler.osop.yaml` | Webhook delivery with exponential backoff retry |
| `api/rate-limit-monitor.osop.yaml` | Monitor API rate limits and alert on threshold breach |

### Mobile (2 examples)

| File | Description |
|------|-------------|
| `mobile/app-store-release.osop.yaml` | Mobile release: build, sign, screenshot, submit, monitor reviews |
| `mobile/beta-distribution.osop.yaml` | Beta build distribution to TestFlight and Firebase App Distribution |

### Platform (2 examples)

| File | Description |
|------|-------------|
| `platform/feature-flag-rollout.osop.yaml` | Gradual feature flag rollout: 1%, 10%, 50%, 100% with monitoring |
| `platform/tenant-onboarding.osop.yaml` | SaaS tenant onboarding: provision, configure, seed data, notify |

### Business (3 examples)

| File | Description |
|------|-------------|
| `business/employee-onboarding.osop.yaml` | Employee onboarding: accounts, access, equipment, orientation |
| `business/invoice-approval.osop.yaml` | Invoice approval workflow with amount-based routing |
| `business/incident-response.osop.yaml` | Incident response: detect, triage, mitigate, resolve, postmortem |

## Structure

```
devops/
testing/
infrastructure/
ai-agent/
data/
api/
mobile/
platform/
business/
```

Each domain directory contains self-contained `.osop.yaml` files. Every example includes:

- A clear `name` and `description`
- Proper use of OSOP node types (start, end, step, decision, fork, join, etc.)
- Connected edges forming a valid graph
- Realistic actions and conditions
- Comments explaining non-obvious logic

## Contributing

We welcome community-contributed examples. Please ensure your workflow:

1. Passes `osop validate`
2. Uses descriptive node IDs (kebab-case)
3. Includes a `description` on the workflow and non-trivial nodes
4. Targets a real-world use case

Open a pull request with your example in the appropriate domain directory.

## License

Apache License 2.0 — see [LICENSE](LICENSE) for details.
