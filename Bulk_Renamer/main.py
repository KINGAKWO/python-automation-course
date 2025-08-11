# Command-line interface
from Bulk_Renamer import bulk_rename
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk file renamer with regex support.")
    parser.add_argument("directory", help="Target directory")
    parser.add_argument("pattern", help="Regex pattern to match")
    parser.add_argument("replacement", help="Replacement string")
    parser.add_argument("--ext", help="Filter by file extension (e.g., .txt)")
    parser.add_argument("--no-preserve-ext", action="store_true", help="Rename full filename including extension")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default is dry-run)")

    args = parser.parse_args()

    bulk_rename(
        directory=args.directory,
        pattern=args.pattern,
        replacement=args.replacement,
        ext=args.ext,
        preserve_ext=not args.no_preserve_ext,
        dry_run=not args.apply
    )