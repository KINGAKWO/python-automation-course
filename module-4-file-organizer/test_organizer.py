from file_organizer import organize_files_by_date, organize_files_by_type, organize_files_by_custom_type

# test_organizer.py
import os
import datetime
import shutil
import pytest
from file_organizer import organize_files_by_type, organize_files_by_date, organize_files_by_custom_type

# Create a test directory
test_dir = "test_directory"
os.mkdir(test_dir)

# Create test files
test_files = [
    "test_image.png",
    "test_document.pdf",
    "test_archive.zip",
    "test_script.py",
    "test_custom.txt"
]

for file in test_files:
    open(os.path.join(test_dir, file), "w").close()

def test_organize_files_by_type():
    organize_files_by_type(test_dir)
    assert os.path.exists(os.path.join(test_dir, "Images"))
    assert os.path.exists(os.path.join(test_dir, "Documents"))
    assert os.path.exists(os.path.join(test_dir, "Archives"))
    assert os.path.exists(os.path.join(test_dir, "Scripts"))
    shutil.rmtree(test_dir)

def test_organize_files_by_date():
    organize_files_by_date(test_dir)
    assert os.path.exists(os.path.join(test_dir, str(datetime.now().year)))
    assert os.path.exists(os.path.join(test_dir, str(datetime.now().year), datetime.now().strftime('%B')))
    shutil.rmtree(test_dir)

def test_organize_files_by_custom_type():
    custom_types = [".txt=Documents"]
    organize_files_by_custom_type(custom_types)
    assert os.path.exists(os.path.join(test_dir, "Documents"))
    shutil.rmtree(test_dir)

def test_organize_files_by_custom_type_invalid_format():
    custom_types = [".txt"]
    with pytest.raises(ValueError):
        organize_files_by_custom_type(custom_types)
    shutil.rmtree(test_dir)

def teardown_module():
    shutil.rmtree(test_dir)