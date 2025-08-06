import os
import shutil
import argparse
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define file types
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".sh"]
}

def organize_files_by_type(directory):
    """Organize files in the given directory by type."""
    file_types = FILE_TYPES.copy()

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if not os.path.isfile(filepath):
            continue

        for category, extensions in file_types.items():
            if filename.endswith(tuple(extensions)):
                target_folder = os.path.join(directory, category)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(filepath, target_folder)
                logging.info(f"Moved {filename} to {category}/")
                break
        else:
            logging.info(f"No matching category for {filename}")

def organize_files_by_date(directory):
    """Organize files in the given directory by creation date."""
    for filename in os.listdir(directory):
        if not filename.startswith(".") and os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            timestamp = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(timestamp)
            year_dir = os.path.join(directory, str(date.year))
            month_dir = os.path.join(year_dir, date.strftime('%B'))

            os.makedirs(year_dir, exist_ok=True)
            os.makedirs(month_dir, exist_ok=True)

            new_path = os.path.join(month_dir, filename)
            try:
                shutil.move(file_path, new_path)
                logging.info(f"Moved {filename} to {month_dir}")
            except Exception as e:
                logging.error(f"Error moving {filename}: {e}")

def organize_files_by_custom_type(args):
    """Organize files by custom types."""
    if args.custom_types:
        for custom in args.custom_types:
            try:
                ext, category = custom.split("=")
                ext = ext.strip()
                category = category.strip()
                if category in FILE_TYPES:
                    FILE_TYPES[category].append(ext)
                else:
                    FILE_TYPES[category] = [ext]
            except ValueError:
                print(f"Invalid format: {custom}. Use .ext=Category")