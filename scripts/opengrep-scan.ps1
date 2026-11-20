<#
.SYNOPSIS
Runs the local static analysis (opengrep) over the repository before a push.
.EXAMPLE
pwsh scripts/opengrep-scan.ps1
#>
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$bin = if ($env:OPENGREP_BIN) { $env:OPENGREP_BIN } else { Join-Path $HOME '.opengrep\cli\latest\opengrep.exe' }
if (-not (Test-Path $bin)) {
    Write-Error "opengrep not found; set OPENGREP_BIN"
    exit 1
}
Set-Location $root
& $bin scan --config auto --error --exclude framework --exclude .venv .
exit $LASTEXITCODE
