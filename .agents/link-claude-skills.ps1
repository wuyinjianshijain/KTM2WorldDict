<#
.SYNOPSIS
  Mirrors .agents/skills into .claude/skills as directory junctions.

.DESCRIPTION
  .agents/skills is the authoritative, vendor-neutral skill tree for this repo.
  Codex reads it natively (its repo skills root is <repo>/.agents/skills).
  Claude Code only scans .claude/skills, and it does not follow a symlinked
  skills root -- but a session does follow symlinked entries inside it.
  So each skill gets its own junction.

  Junctions are not stored in git, so re-run this after cloning the repo or
  after adding, renaming, or removing a skill.

  Windows only. Junctions need no admin rights. On macOS/Linux use:
    ln -s ../../.agents/skills/<name> .claude/skills/<name>
#>

$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$src  = Join-Path $repo '.agents\skills'
$dst  = Join-Path $repo '.claude\skills'

if (-not (Test-Path -LiteralPath $src)) { throw "Authoritative skills tree not found: $src" }
if (-not (Test-Path -LiteralPath $dst)) { New-Item -ItemType Directory -Path $dst -Force | Out-Null }

# Drop stale links whose target no longer exists in .agents/skills.
foreach ($entry in Get-ChildItem -LiteralPath $dst -Force) {
    if ($entry.LinkType -eq 'Junction' -or $entry.LinkType -eq 'SymbolicLink') {
        if (-not (Test-Path -LiteralPath (Join-Path $src $entry.Name))) {
            [System.IO.Directory]::Delete($entry.FullName, $false)
            Write-Host "removed stale link: $($entry.Name)"
        }
    }
}

foreach ($skill in Get-ChildItem -LiteralPath $src -Directory) {
    $link = Join-Path $dst $skill.Name
    if (Test-Path -LiteralPath $link) {
        $existing = Get-Item -LiteralPath $link -Force
        if ($existing.LinkType -eq 'Junction' -or $existing.LinkType -eq 'SymbolicLink') {
            [System.IO.Directory]::Delete($existing.FullName, $false)
        } else {
            Write-Warning "$link is a real directory, not a link. Skipping - move or delete it first."
            continue
        }
    }
    # New-Item -Path/-Target glob, and this repo's folder name contains
    # [brackets]; mklink takes its arguments literally.
    cmd.exe /c mklink /J "$link" "$($skill.FullName)" | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "mklink failed for $($skill.Name)" }
    Write-Host "linked: $($skill.Name)"
}
