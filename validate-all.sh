#!/usr/bin/env bash
# Validate all .osop and .osop.yaml files in osop-examples
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OSOP_DIR="$(dirname "$SCRIPT_DIR")/osop"
PASS=0
FAIL=0
ERRORS=()

echo "=== OSOP Batch Validator ==="
echo "Scanning: $SCRIPT_DIR"
echo ""

# Find all .osop and .osop.yaml files
while IFS= read -r f; do
  rel="${f#$SCRIPT_DIR/}"

  # Step 1: YAML syntax check
  if ! python -c "import yaml; yaml.safe_load(open('$f', encoding='utf-8'))" 2>/dev/null; then
    echo "FAIL (yaml): $rel"
    ERRORS+=("$rel: invalid YAML syntax")
    FAIL=$((FAIL + 1))
    continue
  fi

  # Step 2: Schema validation (if osop module available)
  if python -c "
import sys, yaml
sys.path.insert(0, '$OSOP_DIR')
from osop.validator.schema_validator import validate
with open('$f', encoding='utf-8') as fh:
    wf = yaml.safe_load(fh)
errs = validate(wf)
if errs:
    for e in errs:
        print(f'  {e}', file=sys.stderr)
    sys.exit(1)
" 2>/tmp/osop_validate_err; then
    echo "PASS: $rel"
    PASS=$((PASS + 1))
  else
    echo "FAIL: $rel"
    cat /tmp/osop_validate_err
    ERRORS+=("$rel")
    FAIL=$((FAIL + 1))
  fi
done < <(find "$SCRIPT_DIR" -type f \( -name "*.osop" -o -name "*.osop.yaml" \) | sort)

echo ""
echo "=== Results ==="
echo "PASS: $PASS"
echo "FAIL: $FAIL"
echo "TOTAL: $((PASS + FAIL))"

if [ $FAIL -gt 0 ]; then
  echo ""
  echo "Failed files:"
  for e in "${ERRORS[@]}"; do
    echo "  - $e"
  done
  exit 1
fi
