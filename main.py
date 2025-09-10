# This is main for Project 1

import os
import sys
import argparse
import projectOneIO as pio

# Set up argument parser. A single argument is expected: the filename (not full path), e.g., statements.txt

parser = argparse.ArgumentParser(description="Process a filename.")
parser.add_argument("filename", type=str, help="Name of the file (not the full path)")
args = parser.parse_args()

workingDir = os.getcwd()
filePath = os.path.join(workingDir, args.filename)
if os.path.exists(filePath):
    print(f"Full path to the file: {filePath}")
else:
    print(f"File does not exist: {filePath}")
    sys.exit(1)

# Read names and statements from the file
names, name_statement_dict = pio.read_names_and_statements(filePath)

# Create 'output' directory in the current working directory if it doesn't exist
output_dir = os.path.join(workingDir, "output")
os.makedirs(output_dir, exist_ok=True)

# Write names to output file
output_file_path = os.path.join(output_dir, "output.txt")
pio.write_output(output_file_path, names)