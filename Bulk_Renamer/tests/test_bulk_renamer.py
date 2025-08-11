import os
import shutil
import tempfile
import pytest
from Bulk_Renamer import bulk_rename

@pytest.fixture
def temp_dir():
    """Create a temporary directory with test files."""
    tmp = tempfile.mkdtemp()
    yield tmp
    shutil.rmtree(tmp)

@pytest.fixture
def create_files(temp_dir):
    """Helper to create files in temp_dir."""
    def _create(files):
        paths = []
        for name in files:
            path = os.path.join(temp_dir, name)
            with open(path, "w") as f:
                f.write("test")
            paths.append(path)
        return paths
    return _create


# 1️ Basic renaming
def test_basic_rename(temp_dir, create_files):
    create_files(["file1.txt", "file2.txt"])
    rename_files(temp_dir, pattern="file", replacement="doc")
    assert sorted(os.listdir(temp_dir)) == ["doc1.txt", "doc2.txt"]

# 2️ No matching files
def test_no_match(temp_dir, create_files):
    create_files(["alpha.txt", "beta.txt"])
    rename_files(temp_dir, pattern="zzz", replacement="xxx")
    assert sorted(os.listdir(temp_dir)) == ["alpha.txt", "beta.txt"]

# 3️ Handle name collisions
def test_name_collision(temp_dir, create_files):
    create_files(["a.txt", "b.txt"])
    with pytest.raises(FileExistsError):
        rename_files(temp_dir, pattern="a", replacement="b")

# 4️ Support file extensions unchanged
def test_keep_extensions(temp_dir, create_files):
    create_files(["photo1.jpg", "photo2.jpg"])
    rename_files(temp_dir, pattern="photo", replacement="image")
    assert sorted(os.listdir(temp_dir)) == ["image1.jpg", "image2.jpg"]

# 5️ Recursive renaming
def test_recursive_rename(temp_dir, create_files):
    os.mkdir(os.path.join(temp_dir, "sub"))
    with open(os.path.join(temp_dir, "sub", "file.txt"), "w") as f:
        f.write("test")
    rename_files(temp_dir, pattern="file", replacement="doc", options={"recursive": True})
    assert os.path.exists(os.path.join(temp_dir, "sub", "doc.txt"))

# 6️ Undo support (if implemented)
def test_undo_last_operation(temp_dir, create_files):
    files = create_files(["x.txt", "y.txt"])
    rename_files(temp_dir, pattern="x", replacement="z", options={"track_changes": True})
    # Hypothetical undo
    from bulk_renamer import undo_last_rename
    undo_last_rename()
    assert sorted(os.listdir(temp_dir)) == ["x.txt", "y.txt"]

# 7️ Illegal characters in filenames
def test_illegal_characters(temp_dir, create_files):
    create_files(["bad:file.txt"])
    with pytest.raises(ValueError):
        rename_files(temp_dir, pattern="bad", replacement="good")

# 8️ Long file names (OS limit testing)
def test_long_file_names(temp_dir, create_files):
    long_name = "a" * 240 + ".txt"  # near Windows/Linux limit
    create_files([long_name])
    rename_files(temp_dir, pattern="a", replacement="b")
    assert any("b" in name for name in os.listdir(temp_dir))

# 9️ Empty directory
def test_empty_directory(temp_dir):
    rename_files(temp_dir, pattern="x", replacement="y")  # Should not fail
    assert os.listdir(temp_dir) == []

#  Case sensitivity option
def test_case_sensitivity(temp_dir, create_files):
    create_files(["File.txt", "file.txt"])
    rename_files(temp_dir, pattern="file", replacement="doc", options={"case_sensitive": False})
    assert any("doc" in f.lower() for f in os.listdir(temp_dir))
