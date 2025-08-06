import os
import shutil
import argparse
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a function to organize files by type
def organize_files_by_type(directory):
    """Organize files in the given directory by type."""
    file_types = {
        "Images": [".png", ".jpg", ".jpeg"],
        "Documents": [".pdf", ".docx"],
        "Archives": [".zip", ".rar"],
        "Scripts": [".py", ".sh"]
    }

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

# Define a function to organize files by creation date
def organize_files_by_date(directory):
    """Organize files in the given directory by creation date."""
    for filename in os.listdir(directory):
        if not filename.startswith(".") and os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            timestamp = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            year = str(date.year)
            month = date.strftime('%B')

            year_dir = os.path.join(directory, year)
            month_dir = os.path.join(year_dir, month)

            if not os.path.exists(year_dir):
                os.makedirs(year_dir)
            if not os.path.exists(month_dir):
                os.makedirs(month_dir)

            new_path = os.path.join(month_dir, filename)
            try:
                shutil.move(file_path, new_path)
                logging.info(f"Moved {filename} to {month_dir}")
            except Exception as e:
                logging.error(f"Error moving {filename}: {e}")

