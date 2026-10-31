# CodeAlpha Password Generator

A beginner-friendly desktop Password Generator built with Python and Tkinter.

## Features
- Generate random passwords using Python's secure `secrets` module
- Choose a password length from 8 to 64 characters
- Select lowercase letters, uppercase letters, numbers, and symbols
- Includes at least one character from each selected character type
- Copy the generated password to the clipboard
- Simple graphical user interface (GUI)

## Requirements
- Python 3.10 or newer recommended
- Tkinter (usually included with Python on Windows)

No third-party packages are required.

## How to Run on Windows
1. Extract this ZIP file.
2. Open the extracted folder in Visual Studio Code.
3. Open Terminal → New Terminal.
4. Run `python main.py` (or `py main.py`).

## How to Use
1. Choose the password length.
2. Select the character types to include.
3. Click **Generate Password**.
4. Click **Copy to Clipboard** to copy it.

## Security Note
This app uses Python's `secrets` module for password generation. Do not share passwords with anyone. For important accounts, consider using a trusted password manager and enable two-factor authentication where available.

## Project Structure
```text
CodeAlpha_Password_Generator/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

This project can be added to the `codealpha_tasks` GitHub repository in its own folder.
