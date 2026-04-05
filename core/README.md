# OSOP Core Examples

Minimal workflow examples using **OSOP Core** — 4 node types, 4 edge modes.

## Examples

| File | Description | Nodes | Key Pattern |
|------|-------------|-------|-------------|
| `ai-code-review.osop.yaml` | AI reviews PR diff, human approves | 3 | agent + human + fallback |
| `claude-session-log.osop.yaml` | Standard Claude Code session workflow | 5 | explore → implement → test → review |
| `multi-agent-research.osop.yaml` | Parallel research agents + synthesis | 5 | parallel edges + coordinator |
| `api-health-check.osop.yaml` | Health check with AI failure analysis | 3 | cli + fallback → agent |

## OSOP Core Types

**Nodes:** `agent`, `api`, `cli`, `human`
**Edges:** `sequential`, `conditional`, `parallel`, `fallback`

## Validate

```bash
# Validate against Core schema
osop validate --schema core ai-code-review.osop.yaml

# All examples should pass
for f in *.osop.yaml; do osop validate --schema core "$f"; done
```

## View

Drag any `.osop.yaml` file into https://osop-editor.vercel.app for visual rendering.
