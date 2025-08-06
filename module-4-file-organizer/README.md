# File Organizer

A Python script to organize files by type or creation date in a specified directory.

## Overview

This script uses the `argparse` library to accept a directory path as input and organizes files within that directory into categories based on their file extensions or creation date. The script supports organization of images, documents, archives, and scripts.

## Installation

### Prerequisites

* Python 3.x
* `argparse` library (included with Python 3.x)

### Installation Steps

1. Clone or download the `module-4-file-organizer` repository.
2. Navigate to the `module-4-file-organizer` directory in your terminal or command prompt.
3. Run the script using Python: `python main.py --dir <directory_path>`

## Usage

### Command-Line Options

* `--dir`: Specify the directory path to organize files in.
* `--type`: Organize files by type (default).
* `--date`: Organize files by creation date.
* `--custom-types`: Specify custom file types to organize, e.g., ".txt=Documents".

### Example Usage

* `python main.py --dir /path/to/directory`
* `python main.py --dir /path/to/directory --date`
* `python main.py --dir /path/to/directory --custom-types ".txt=Documents" ".pdf=Reports"`

## Supported File Types

* Images: `.png`, `.jpg`, `.jpeg`
* Documents: `.pdf`, `.docx`
* Archives: `.zip`, `.rar`
* Scripts: `.py`, `.sh`

## Custom File Types

You can specify custom file types using the `--custom-types` option. For example, to organize `.txt` files as "Documents" and `.pdf` files as "Reports", use the following command:

`python main.py --dir /path/to/directory --custom-types ".txt=Documents" ".pdf=Reports"`

## License

This script is released under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Issues

If you encounter any issues or have questions, please open an issue on the GitHub issue tracker.