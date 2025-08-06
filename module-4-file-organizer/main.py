from file_organizer import organize_files_by_date, organize_files_by_type 
import argparse
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize files by type or creation date.')
    parser.add_argument('directory', type=str, help='The directory to organize.')
    parser.add_argument('--type', action='store_true', help='Organize files by type.')
    parser.add_argument('--date', action='store_true', help='Organize files by creation date.')
    args = parser.parse_args()

    if args.type:
        organize_files_by_type(args.directory)
    elif args.date:
        organize_files_by_date(args.directory)
    else:
        logging.error("Please specify either --type or --date.")