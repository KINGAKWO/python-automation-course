# File Organizer

A Python script to organize files by type in a specified directory.

## Overview

This script uses the `argparse` library to accept a directory path as input and organizes files within that directory into categories based on their file extensions. The script supports organization of images, documents, archives, and scripts.

## Installation

### Prerequisites

* Python 3.x
* `argparse` library (included with Python 3.x)

### Installation Steps

1. Clone or download the `module-4-file-organizer` repository.
2. Navigate to the `module-4-file-organizer` directory in your terminal or command prompt.
3. Run the script using Python: `python file_organizer.py --dir <directory_path>`

## Usage

### Command-Line Options

* `--dir`: Specify the directory path to organize files in.
* `--dry-run`: Simulate the organization process without moving files.

### Example Usage

* `python file_organizer.py --dir /path/to/directory`
* `python file_organizer.py --dir /path/to/directory --dry-run`

## Supported File Types

* Images: `.png`, `.jpg`, `.jpeg`
* Documents: `.pdf`, `.docx`
* Archives: `.zip`, `.rar`
* Scripts: `.py`, `.sh`

## License

This script is released under the MIT License. See the LICENSE file for details.