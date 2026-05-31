@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM =========================
REM USER CONFIGURATION
REM =========================
set "SOURCE_DIR=C:\Users\osadl\iCloudPhotos\Photos"
set "DEST_BASE_DIR=C:\!!!PERSONAL_DATA\! Personal\Family Photos & Videos"
set "OWNER_NAME=osadl"
set "TARGET_YEAR=2022"

REM =========================
REM BUILD DESTINATION PATH
REM =========================
set "DEST_DIR=%DEST_BASE_DIR%\%TARGET_YEAR%\%OWNER_NAME%"

REM Validate source directory exists
if not exist "%SOURCE_DIR%" (
    echo ERROR: Source directory not found:
    echo %SOURCE_DIR%
    pause
    exit /b 1
)

REM Create destination directory if it does not exist
if not exist "%DEST_DIR%" (
    mkdir "%DEST_DIR%"
    if errorlevel 1 (
        echo ERROR: Could not create destination directory:
        echo %DEST_DIR%
        pause
        exit /b 1
    )
    echo Created destination directory: %DEST_DIR%
)

REM =========================
REM POWERSHELL FILE COPY
REM =========================
echo.
echo Scanning for files with LastWriteTime year = %TARGET_YEAR% ...
echo Source : %SOURCE_DIR%
echo Dest   : %DEST_DIR%
echo.

REM NOTE: LastWriteTime (file modified date) is used instead of CreationTime,
REM because CreationTime reflects when a file was copied to this PC, not when
REM the photo was originally taken. LastWriteTime is usually preserved on transfer
REM and is far more reliable for photo sorting by year.
REM For true EXIF DateTaken accuracy, a tool like ExifTool is recommended.

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "$src = '%SOURCE_DIR%'; $dst = '%DEST_DIR%'; $year = %TARGET_YEAR%; $copied = 0; $skipped = 0;" ^
    "Get-ChildItem -Path $src -Recurse -File |" ^
    "Where-Object { $_.LastWriteTime.Year -eq $year } |" ^
    "ForEach-Object {" ^
    "    $target = Join-Path $dst $_.Name;" ^
    "    if (Test-Path $target) {" ^
    "        Write-Host ('SKIPPED (already exists): ' + $_.Name) -ForegroundColor Yellow;" ^
    "        $skipped++;" ^
    "    } else {" ^
    "        Copy-Item $_.FullName -Destination $dst;" ^
    "        Write-Host ('Copied: ' + $_.Name) -ForegroundColor Green;" ^
    "        $copied++;" ^
    "    }" ^
    "};" ^
    "Write-Host '';" ^
    "Write-Host '========================================';" ^
    "Write-Host ('Files copied  : ' + $copied)  -ForegroundColor Green;" ^
    "Write-Host ('Files skipped : ' + $skipped) -ForegroundColor Yellow;" ^
    "Write-Host '========================================';"

echo.
echo ========================================
echo Done. Target year  : %TARGET_YEAR%
echo Destination folder : %DEST_DIR%
echo ========================================

ENDLOCAL
pause