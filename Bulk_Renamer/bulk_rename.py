import os
import re
import argparse
from pathlib import Path

def bulk_rename(directory, pattern, replacement, ext=None, preserve_ext=True, dry_run=True):
    try:
        regex = re.compile(pattern)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        return

    dir_path = Path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        print("Directory does not exist or is not readable.")
        return

    files = [f for f in dir_path.iterdir() if f.is_file()]
    if ext:
        files = [f for f in files if f.suffix == ext]

    if not files:
        print("No matching files found.")
        return

    rename_map = []

    for file in files:
        old_name = file.name
        name_part, extension = os.path.splitext(old_name)

        target = name_part if preserve_ext else old_name
        if not regex.search(target):
            continue

        new_base = regex.sub(replacement, target)
        new_name = new_base + extension if preserve_ext else new_base

        if new_name == old_name:
            continue

        # Handle naming conflicts
        counter = 1
        while (dir_path / new_name).exists():
            name_only, ext_only = os.path.splitext(new_name)
            new_name = f"{name_only}_{counter}{ext_only}"
            counter += 1

        rename_map.append((file, new_name))

    if dry_run:
        print("🔍 Dry Run Preview:")
        for old, new in rename_map:
            print(f"{old.name} → {new}")
        return

    print(" Renaming Files:")
    for old, new in rename_map:
        try:
            old.rename(dir_path / new)
            print(f"Renamed: {old.name} → {new}")
        except PermissionError:
            print(f" Permission denied: {old.name}")
        except Exception as e:
            print(f"Error renaming {old.name}: {e}")

