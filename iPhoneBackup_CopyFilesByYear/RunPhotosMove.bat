@echo off
SETLOCAL

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

echo.
echo Running PowerShell move script...
echo Source: %SOURCE_DIR%
echo Dest  : %DEST_DIR%
echo Year  : %TARGET_YEAR%
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0PhotoMove.ps1" ^
    -Source "%SOURCE_DIR%" ^
    -Destination "%DEST_DIR%" ^
    -Year %TARGET_YEAR%

echo.
echo ========================================
echo Done. Target year  : %TARGET_YEAR%
echo Destination folder : %DEST_DIR%
echo ========================================

ENDLOCAL
pause