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