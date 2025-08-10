import os
import shutil
import argparse
import logging
import re

def bulk_rename(directory, pattern , replacement , options):
    #validate directory exists and is a readable
    if not os.path.isdir(directory):
        logging.error(f"Directory {directory} does not exist or is not readable.")
        return
    #compile the regex pattern(handle invalid regex errors)
    try:
        regex = re.compile(pattern)
    except re.error as e:
        logging.error(f"Invalid regex pattern: {e}")
        return
    
    