#!/usr/bin/env python
"""Validate all .osop and .osop.yaml files in osop-examples."""
import sys
import os
import glob
import yaml

# Add osop CLI to path
script_dir = os.path.dirname(os.path.abspath(__file__))
osop_dir = os.path.join(os.path.dirname(script_dir), "osop")
sys.path.insert(0, osop_dir)

from osop.validator.schema_validator import validate

PASS = 0
FAIL = 0
ERRORS = []

print("=== OSOP Batch Validator ===")
print(f"Scanning: {script_dir}")
print()

patterns = [
    os.path.join(script_dir, "**", "*.osop"),
    os.path.join(script_dir, "**", "*.osop.yaml"),
]

files = []
for p in patterns:
    files.extend(glob.glob(p, recursive=True))
files = sorted(set(files))

for f in files:
    rel = os.path.relpath(f, script_dir)

    # Step 1: YAML syntax check
    try:
        with open(f, encoding="utf-8") as fh:
            wf = yaml.safe_load(fh)
    except Exception as e:
        print(f"FAIL (yaml): {rel}")
        print(f"  {e}")
        ERRORS.append(f"{rel}: YAML syntax error")
        FAIL += 1
        continue

    if not isinstance(wf, dict):
        print(f"FAIL (type): {rel}")
        ERRORS.append(f"{rel}: not a dict")
        FAIL += 1
        continue

    # Step 2: Schema validation
    errs = validate(wf)
    if errs:
        print(f"FAIL: {rel}")
        for e in errs[:5]:
            print(f"  {e}")
        ERRORS.append(rel)
        FAIL += 1
    else:
        print(f"PASS: {rel}")
        PASS += 1

print()
print("=== Results ===")
print(f"PASS: {PASS}")
print(f"FAIL: {FAIL}")
print(f"TOTAL: {PASS + FAIL}")

if ERRORS:
    print()
    print(f"Failed files ({len(ERRORS)}):")
    for e in ERRORS[:30]:
        print(f"  - {e}")
    if len(ERRORS) > 30:
        print(f"  ...and {len(ERRORS) - 30} more")
    sys.exit(1)
