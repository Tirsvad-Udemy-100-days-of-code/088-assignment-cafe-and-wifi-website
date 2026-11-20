<#
.SYNOPSIS
Builds the screenshot image and runs the capture inside a container.
.EXAMPLE
pwsh scripts/screenshots/run.ps1 --smoke
#>
$ErrorActionPreference = 'Stop'
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
docker build -t cafe-wifi-shots (Join-Path $root 'scripts\screenshots')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
docker run --rm -v "${root}:/work" -w /work cafe-wifi-shots python scripts/screenshots/capture.py @args
exit $LASTEXITCODE
