# File Manager CLI

A command-line file manager built with Python, following **Clean Architecture** principles. It allows you to create, read, edit, rename,delete,list and sort files directly from your terminal.


## Features
- **delete** a file from a specific folder
- **Create** new files with a specified name and extension
- **Read** file content directly in the terminal
- **Edit** existing file content
- **Rename** files
- **Sort** files automatically by extension into predefined folders
- **list** files from a specific directory
### Sorting System

The sort feature organizes files into predefined folders based on their extension:

| Folder | Extensions |
|PDF|'.pdf'|
|WORD | '.docx'|
|TEXTE| '.txt' |
| PYTHON | '.py'|
|JAVASCRIPT| '.js' |
| POWER_POINT | '.ppt' |


## Architecture

This project follows **Clean Architecture**:

- **EN--entities** — 'File' and 'Folder' entities with business rules, no external dependencies
- **Use cases** use cases (create, read, edit, rename, sort,delete, list)
- **Inyerface adapters** — File system operations
- **frameworks and drivers** — CLI layer using 'argparse'

## Usage

```bash
# Create a file
python main.py create --name report --extension pdf

# Read a file
python main.py read --path documents/report.pdf

# Edit a file
python main.py edit --path documents/report.pdf

# Rename a file
python main.py rename --path documents/report.pdf --new-name summary

# Sort files in a directory
python main.py sort --path ./my-folder
```
