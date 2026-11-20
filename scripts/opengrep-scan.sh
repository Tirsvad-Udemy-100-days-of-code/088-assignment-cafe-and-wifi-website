#!/usr/bin/env bash
# Runs the local static analysis (opengrep) over the repository before a push.
# Usage: scripts/opengrep-scan.sh
# Exit:  0 no finding; 1 findings or opengrep missing
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
bin="${OPENGREP_BIN:-$HOME/.opengrep/cli/latest/opengrep.exe}"
[[ -x "$bin" ]] || bin="$HOME/.opengrep/cli/latest/opengrep"
if [[ ! -x "$bin" ]]; then
  echo "error: opengrep not found; set OPENGREP_BIN" >&2
  exit 1
fi
cd "$root"
"$bin" scan --config auto --error --exclude framework --exclude .venv .
