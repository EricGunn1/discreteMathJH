# Input/Output Scheme

## Input

The program expects **two command-line arguments**:
1. The name of the input file (e.g., `statements.txt`)
2. The name of the output file (e.g., `results.txt`)

**Example usage:**
```
python main.py statements.txt results.txt
```

- The input file should be located in the current working directory.
- Each line in the input file should be in the format:  
  `Name says, "Statement."`

## Output

- The program creates an `output` directory in the current working directory if it does not already exist.
- The output file will be saved inside the `output` directory, with the name you provided as the second argument.
- If a file with that name already exists, a number will be appended to the filename (e.g., `results1.txt`, `results2.txt`, etc.) to avoid overwriting.

**Output contents:**  
- The output file will contain one name per line, extracted from the input file.

---
**Summary:**  
- Place your input file in the current directory.
- Run the program with the input and output filenames as arguments.
- Find your results in