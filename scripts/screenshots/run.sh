#!/usr/bin/env bash
# Builds the screenshot image and runs the capture inside a container.
# Usage: scripts/screenshots/run.sh [--smoke] [--steps 1 2 3]
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && { pwd -W 2>/dev/null || pwd; })"
docker build -t cafe-wifi-shots "$root/scripts/screenshots"
docker run --rm -v "$root:/work" -w /work cafe-wifi-shots \
  python scripts/screenshots/capture.py "$@"
