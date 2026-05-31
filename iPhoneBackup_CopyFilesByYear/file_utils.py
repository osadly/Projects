import os
import shutil
from datetime import datetime, date

# =========================
# USER CONFIGURATION
# =========================
SOURCE_DIR = r"C:\Users\my_user_name\iCloudPhotos\Photos"
DEST_BASE_DIR = r"C:\!!!PERSONAL_DATA\! Personal\Family Photos & Videos"
USERNAME = "osadl"
TARGET_YEAR = 2022  # <-- change this to the desired year

# =========================
# FUNCTIONS
# =========================

# Osama Wanis - by Claude (19-May-2026) - Start
def copy_file(source_path, destination_folder):
    """Copy a file from source path to destination folder."""
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    if not os.path.isdir(destination_folder):
        raise NotADirectoryError(f"Destination folder not found: {destination_folder}")

    destination_path = shutil.copy2(source_path, destination_folder)
    print(f"File copied to: {destination_path}")
    return destination_path


def get_files_by_file_date(folder_path, target_date: date):
    """Get all filenames where the file date (mtime) matches target_date."""
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Folder not found: {folder_path}")

    matches = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            file_date = date.fromtimestamp(os.path.getmtime(filepath))
            if file_date == target_date:
                matches.append(filename)
    return matches


def get_files_by_creation_date(folder_path, target_date: date):
    """Get all filenames where the file creation date matches target_date.
    Note: On Linux, ctime is metadata-change time, not true creation time.
    True creation date is only reliable on Windows and macOS.
    """
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Folder not found: {folder_path}")

    matches = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            file_date = date.fromtimestamp(os.path.getctime(filepath))
            if file_date == target_date:
                matches.append(filename)
    return matches


def get_files_by_update_date(folder_path, target_date: date):
    """Get all filenames where the last modified date matches target_date."""
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"Folder not found: {folder_path}")

    matches = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            file_date = date.fromtimestamp(os.path.getmtime(filepath))
            if file_date == target_date:
                matches.append(filename)
    return matches
# Osama Wanis - by Claude (19-May-2026) - End


# Osama Wanis - by ChatGPT (02-Jan-2026) - Start
def copy_files_by_creation_year(source_dir, dest_base_dir, username, target_year):
    """
    Copies all files created in target_year from source_dir
    to dest_base_dir\\target_year\\username, preserving metadata.
    """
    destination_dir = os.path.join(dest_base_dir, str(target_year), username)
    os.makedirs(destination_dir, exist_ok=True)

    copied_files = 0

    for root, _, files in os.walk(source_dir):
        for file_name in files:
            source_path = os.path.join(root, file_name)

            try:
                creation_time = os.path.getctime(source_path)
                creation_year = datetime.fromtimestamp(creation_time).year

                if creation_year == target_year:
                    dest_path = os.path.join(destination_dir, file_name)

                    if not os.path.exists(dest_path):
                        shutil.copy2(source_path, dest_path)
                        copied_files += 1

            except Exception as e:
                print(f"Skipped file due to error: {source_path}")
                print(f"Reason: {e}")

    print(f"Completed. {copied_files} files copied to:")
    print(destination_dir)
# Osama Wanis - by ChatGPT (02-Jan-2026) - End


# =========================
# EXECUTION
# =========================
if __name__ == "__main__":
    TEST = "copy_file"  # <-- change this one value to switch tests

    if TEST == "copy_file":
        copy_file(
            r"C:\...\source\file.txt",
            r"C:\...\destination"
        )

    elif TEST == "get_files_by_file_date":
        target = date(2026, 5, 19)
        print(get_files_by_file_date("/path/to/folder", target))

    elif TEST == "get_files_by_creation_date":
        target = date(2026, 5, 19)
        print(get_files_by_creation_date("/path/to/folder", target))

    elif TEST == "get_files_by_update_date":
        target = date(2026, 5, 19)
        print(get_files_by_update_date("/path/to/folder", target))

    elif TEST == "copy_files_by_creation_year":
        copy_files_by_creation_year(SOURCE_DIR, DEST_BASE_DIR, USERNAME, TARGET_YEAR)