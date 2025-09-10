import os
import re

def read_names_and_statements(file_path):
    """
    Reads a file line by line, extracting names and statements using regex.
    Returns a list of names and a dictionary mapping names to statements.
    """
    names = []
    name_statement_dict = {}
    pattern = re.compile(r'^\s*(\w+)\s+says,\s*"(.*)"\s*$')  # Matches: Name: Statement

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                name = match.group(1)
                statement = match.group(2)
                names.append(name)
                name_statement_dict[name] = statement

    return names, name_statement_dict

def get_unique_filepath(file_path):
    """
    If file_path exists, append an incrementing digit before the file extension.
    Example: output.txt -> output1.txt, output1.txt -> output2.txt, etc.
    """
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_path = file_path
    while os.path.exists(new_path):
        new_path = f"{base}{counter}{ext}"
        counter += 1
    return new_path

def write_output(file_path, output_list):
    """
    Writes the given list of strings to the specified file, each item on its own line.
    If the file exists, appends an incrementing digit to the filename.
    """
    file_path = get_unique_filepath(file_path)
    output_string = '\n'.join(output_list)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(output_string)
