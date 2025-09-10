# This is main for Project 1

import os
import sys
import argparse
import projectOneIO as pio

# Set up argument parser. Two arguments are expected: input filename and output filename (not full paths)
parser = argparse.ArgumentParser(description="Process input and output filenames.")
parser.add_argument("input_filename", type=str, help="Name of the input file (not the full path)")
parser.add_argument("output_filename", type=str, help="Name of the output file (not the full path)")
args = parser.parse_args()

workingDir = os.getcwd()
filePath = os.path.join(workingDir, args.input_filename)
if not os.path.exists(filePath):
    print(f"File does not exist: {filePath}")
    sys.exit(1)

# Read names and statements from the file
names, name_statement_dict = pio.read_names_and_statements(filePath)

# Create 'output' directory in the current working directory if it doesn't exist
output_dir = os.path.join(workingDir, "output")
os.makedirs(output_dir, exist_ok=True)

# Write names to output file
output_file_path = os.path.join(output_dir, args.output_filename)
pio.write_output(output_file_path, names)