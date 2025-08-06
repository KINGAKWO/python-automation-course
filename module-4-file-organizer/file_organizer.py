import os
import shutil
import argparse
import logging 

images=[]
documents = []
archives = []
script = []

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx"],
    "Archives": [".zip", ".rar"],
    "Scripts": [".py", ".sh"]
}

parser = argparse.ArgumentParser(description='organize files by type')
parser.add_argument('--dir',help='path to the directory', required=True)
parser.add_argument('--dry-run', action='store_true', help='simulate organization without moving files')
parser.add_argument('--custom-types',help='add your own extension ')
args = parser.parse_args()
directory = args.dir

logging.basicConfig(level=logging.INFO)

for filename in os.listdir('data_directory'):
    filepath = os.path.join(directory, filename)
    if not os.path.isfile(filepath):
        continue
    
    moved = False
    for category, extensions in FILE_TYPES.items():
        if filename.endswith(tuple(FILE_TYPES["Images"])):
            images.append(filename)
            target_folder = os.path.join(directory, category)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(target_folder, filename))
            if args.dry_run:
                logging.info(f"[DRY RUN] would move {filename} to {category}/")
            else:
                shutil.move(filepath, target_folder)
                logging.info(f"Moved {filename} to {category}/")
            moved = True
            break
        
    if not moved:
        logging.info(f"No matching category for {filename}")
            
        
