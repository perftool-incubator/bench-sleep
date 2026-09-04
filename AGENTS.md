# Bench-sleep

## Purpose
Minimal benchmark that exercises the full crucible pipeline without adding workload. Used for CI testing, framework validation, and observing a system at its current state without introducing additional load.

## Language
- Bash for client execution scripts
- Python for post-processing (`sleep-post-process.py`)

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client script and post-processing |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and CDM-indexed source/type list (consumed by `crucible benchmarks list`) |
| `sleep-client` | Client-side execution (runs sleep) |
| `sleep-get-runtime` | Extracts runtime from command-line options |
| `sleep-post-process.py` | Post-processing script |
| `workshop.json` | Engine image build requirements |

## Conventions
- Primary branch is `main`
- Standard Bash modelines and 4-space indentation
- Python code follows 4-space indentation with standard modelines
