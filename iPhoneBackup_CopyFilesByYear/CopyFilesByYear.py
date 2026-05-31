# test_file_utils.py

import os
from datetime import date
from file_utils import (
    copy_file,
    get_files_by_file_date,
    get_files_by_creation_date,
    get_files_by_update_date,
    copy_files_by_creation_year,
)

# =========================
# TEST CONFIGURATION
# =========================
SOURCE_FILE   = r"C:\!!!PERSONAL_DATA\! Osama\!!!!!!!!!Projects (Interesting)\iPhoneBackup_CopyFilesByYear\Test\source\file.txt"
SOURCE_FOLDER = r"C:\!!!PERSONAL_DATA\! Osama\!!!!!!!!!Projects (Interesting)\iPhoneBackup_CopyFilesByYear\Test\source"
DEST_FOLDER   = r"C:\!!!PERSONAL_DATA\! Osama\!!!!!!!!!Projects (Interesting)\iPhoneBackup_CopyFilesByYear\Test\destination"
TARGET_DATE   = date(2026, 5, 19)

SOURCE_DIR    = r"C:\Users\my_user_name\iCloudPhotos\Photos"
DEST_BASE_DIR = r"C:\!!!PERSONAL_DATA\! Personal\Family Photos & Videos"
USERNAME      = "osadl"
TARGET_YEAR   = 2022

# =========================
# TESTS
# =========================

def test_copy_file():
    copy_file(SOURCE_FILE, DEST_FOLDER)

def test_get_files_by_file_date():
    results = get_files_by_file_date(SOURCE_FOLDER, TARGET_DATE)
    print(f"Files matching file date {TARGET_DATE}: {results}")

def test_get_files_by_creation_date():
    results = get_files_by_creation_date(SOURCE_FOLDER, TARGET_DATE)
    print(f"Files matching creation date {TARGET_DATE}: {results}")

def test_get_files_by_update_date():
    results = get_files_by_update_date(SOURCE_FOLDER, TARGET_DATE)
    print(f"Files matching update date {TARGET_DATE}: {results}")

def test_copy_files_by_creation_year():
    copy_files_by_creation_year(SOURCE_DIR, DEST_BASE_DIR, USERNAME, TARGET_YEAR)

# =========================
# EXECUTION
# =========================
if __name__ == "__main__":

    TEST = "test_copy_file"  # <-- change this one value to switch tests
    print("testing " + TEST + "...\n")

    if TEST == "test_copy_file":
        test_copy_file()

    elif TEST == "test_get_files_by_file_date":
        test_get_files_by_file_date()

    elif TEST == "test_get_files_by_creation_date":
        test_get_files_by_creation_date()

    elif TEST == "test_get_files_by_update_date":
        test_get_files_by_update_date()

    elif TEST == "test_copy_files_by_creation_year":
        test_copy_files_by_creation_year()