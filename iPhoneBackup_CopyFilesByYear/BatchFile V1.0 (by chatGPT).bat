@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM =========================
REM USER CONFIGURATION
REM =========================
set SOURCE_DIR=C:\Users\my_user_name\iCloudPhotos\Photos
set DEST_BASE_DIR=C:\!!!PERSONAL_DATA\! Personal\Family Photos & Videos
set USERNAME=my_user_name
set TARGET_YEAR=2022

REM =========================
REM BUILD DESTINATION PATH
REM =========================
set DEST_DIR=%DEST_BASE_DIR%\%TARGET_YEAR%\%USERNAME%

REM Create destination directory if it does not exist
if not exist "%DEST_DIR%" (
    mkdir "%DEST_DIR%"
)

REM =========================
REM POWERSHELL FILE FILTER
REM =========================
powershell -NoProfile -ExecutionPolicy Bypass ^
    -Command ^
    "Get-ChildItem -Path '%SOURCE_DIR%' -Recurse -File | " ^
    "Where-Object { $_.CreationTime.Year -eq %TARGET_YEAR% } | " ^
    "ForEach-Object { " ^
    "   Copy-Item $_.FullName '%DEST_DIR%' -Force -Verbose " ^
    "}"

echo.
echo ========================================
echo Files created in %TARGET_YEAR% copied to:
echo %DEST_DIR%
echo ========================================

ENDLOCAL
pause
