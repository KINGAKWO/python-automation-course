import unittest
import tempfile
import shutil
from pathlib import Path
from Bulk_Renamer import bulk_rename

class TestBulkRenamer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.dir_path = Path(self.test_dir)

        # Create sample files
        (self.dir_path / "file_draft.txt").write_text("Sample")
        (self.dir_path / "file_draft.txt").write_text("Sample")
        (self.dir_path / "report_draft.txt").write_text("Sample")
        (self.dir_path / "unchanged.txt").write_text("Sample")

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)

    def test_basic_rename(self):
        bulk_rename(self.test_dir, "draft", "final", ext=".txt", dry_run=False)
        files = [f.name for f in self.dir_path.iterdir()]
        self.assertIn("file_final.txt", files)
        self.assertIn("report_final.txt", files)

    def test_preserve_extension(self):
        bulk_rename(self.test_dir, "file", "doc", ext=".txt", preserve_ext=True, dry_run=False)
        self.assertTrue((self.dir_path / "doc_draft.txt").exists())

    def test_conflict_resolution(self):
        # Create a conflicting file
        (self.dir_path / "report_final.txt").write_text("Conflict")
        bulk_rename(self.test_dir, "draft", "final", ext=".txt", dry_run=False)
        files = [f.name for f in self.dir_path.iterdir()]
        self.assertTrue(any("report_final_" in f for f in files))

    def test_dry_run(self):
        original_files = set(f.name for f in self.dir_path.iterdir())
        bulk_rename(self.test_dir, "draft", "final", ext=".txt", dry_run=True)
        after_files = set(f.name for f in self.dir_path.iterdir())
        self.assertEqual(original_files, after_files)

    def test_skip_unchanged(self):
        bulk_rename(self.test_dir, "unchanged", "unchanged", ext=".txt", dry_run=False)
        self.assertTrue((self.dir_path / "unchanged.txt").exists())

if __name__ == "__main__":
    unittest.main()