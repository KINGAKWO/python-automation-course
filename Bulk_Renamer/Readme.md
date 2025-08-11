```markdown
#  Bulk File Renamer

A Python utility to rename multiple files in a directory using pattern matching and replacement. Supports dry runs, extension filtering, conflict resolution, and regex-based renaming.

---

## 📦 Features

- ✅ Rename files using simple string replacement or regex
- ✅ Filter by file extension
- ✅ Preserve original file extensions
- ✅ Dry-run mode to preview changes
- ✅ Automatically resolves filename conflicts
- ✅ Skips unchanged filenames

---

## 🚀 Getting Started

### Requirements

- Python 3.7+
- No external dependencies

### Installation

Clone the repo:

```bash
git clone https://github.com/your-username/bulk-renamer.git
cd bulk-renamer
```

---

## ⚙️ Usage

```bash
python bulk_rename.py --dir /path/to/files --find "draft" --replace "final"
```

### Options

| Argument       | Description                                 |
|----------------|---------------------------------------------|
| `--dir`        | Target directory containing files           |
| `--find`       | Substring or regex pattern to find          |
| `--replace`    | Replacement string                          |
| `--ext`        | Filter files by extension (e.g. `.txt`)     |
| `--preserve`   | Preserve original file extensions           |
| `--regex`      | Treat `--find` as a regex pattern           |
| `--dry-run`    | Preview changes without renaming files      |
| `--verbose`    | Print detailed output during execution      |

---

## 🧪 Running Tests

Tests are written using Python’s `unittest` framework.

```bash
python test_bulk_renamer.py
```

Tests cover:
- Basic renaming
- Extension handling
- Conflict resolution
- Dry-run behavior
- Regex replacement
- Skipping unchanged files

---

## 📁 Example

Before:
```
report_draft.txt
summary_draft.txt
```

Command:
```bash
python bulk_rename.py --dir ./docs --find "draft" --replace "final"
```

After:
```
report_final.txt
summary_final.txt
```

---

## 🛠️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

## 🙌 Acknowledgments

Inspired by the need to batch rename files during data cleaning and documentation workflows.
