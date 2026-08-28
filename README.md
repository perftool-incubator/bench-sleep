# bench-sleep
[![CI Actions Status](https://github.com/perftool-incubator/bench-sleep/workflows/crucible-ci/badge.svg)](https://github.com/perftool-incubator/bench-sleep/actions)

Scripts and configuration to run the sleep benchmark within the [crucible](https://github.com/perftool-incubator/crucible) performance testing framework. This is a minimal benchmark that exercises the full crucible pipeline without adding workload to the system. It can be used for CI testing, framework validation, and observing a system at its current state without introducing additional load.

## Key Files

| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: client script and post-processing |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `benchmark-metadata.json` | Machine-readable description and CDM-indexed source/type list (consumed by `crucible benchmarks list`) |
| `sleep-client` | Client-side execution (runs sleep) |
| `sleep-get-runtime` | Extracts runtime from command-line options |
| `sleep-post-process` | Post-processing script |
| `workshop.json` | Engine image build requirements |

