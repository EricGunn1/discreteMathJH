# This is main for Project 1

import os
import sys
import argparse
import projectOneIO as pio

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

names, name_statement_dict = pio.read_names_and_statements(filePath)

for name in names:
    statement = name_statement_dict.get(name, "")
    print(f'"{name}":"{statement}"')

