param(
    [string]$Source,
    [string]$Destination,
    [int]$Year
)

# =========================
# VALIDATE INPUTS
# =========================
if (-not (Test-Path $Source)) {
    Write-Host "ERROR: Source directory not found: $Source" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $Destination)) {
    Write-Host "ERROR: Destination directory not found: $Destination" -ForegroundColor Red
    exit 1
}

# =========================
# MOVE FILES
# =========================
$moved   = 0
$skipped = 0
$failed  = 0

Write-Host ""
Write-Host "Scanning for files with LastWriteTime year = $Year ..." -ForegroundColor Cyan
Write-Host ""

Get-ChildItem -Path $Source -Recurse -File |
    Where-Object { $_.LastWriteTime.Year -eq $Year } |
    ForEach-Object {
        $target = Join-Path $Destination $_.Name

        if (Test-Path $target) {
            Write-Host "SKIPPED (already exists): $($_.Name)" -ForegroundColor Yellow
            $skipped++
        }
        else {
            try {
                Move-Item $_.FullName -Destination $Destination -ErrorAction Stop
                Write-Host "Moved: $($_.Name)" -ForegroundColor Green
                $moved++
            }
            catch {
                Write-Host "FAILED: $($_.Name) — $($_.Exception.Message)" -ForegroundColor Red
                $failed++
            }
        }
    }

# =========================
# OPTIONAL: REMOVE EMPTY SUBDIRECTORIES FROM SOURCE
# Uncomment the block below if you want a clean source folder after moving.
# This only removes directories that are completely empty after the move.
# =========================
# Get-ChildItem -Path $Source -Recurse -Directory |
#     Sort-Object FullName -Descending |
#     Where-Object { (Get-ChildItem $_.FullName -Force).Count -eq 0 } |
#     ForEach-Object {
#         Remove-Item $_.FullName -Force
#         Write-Host "Removed empty folder: $($_.FullName)" -ForegroundColor DarkGray
#     }

# =========================
# SUMMARY
# =========================
Write-Host ""
Write-Host "========================================"
Write-Host "Files moved   : $moved"   -ForegroundColor Green
Write-Host "Files skipped : $skipped" -ForegroundColor Yellow
Write-Host "Files failed  : $failed"  -ForegroundColor Red
Write-Host "========================================"

if ($failed -gt 0) {
    Write-Host ""
    Write-Host "WARNING: Some files could not be moved. Check the output above." -ForegroundColor Red
    exit 1
}
