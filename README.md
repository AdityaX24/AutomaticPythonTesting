# Python Script Tester

A Python-based testing framework to automatically test and score Python scripts against predefined test cases. This tool is designed to evaluate multiple `.py` files in a folder, run them against test cases, and generate a detailed report of the results.

---

## Features

- **Multiple Question Types**: Supports different types of questions (e.g., stdin input, command-line arguments).
- **Flexible Test Cases**: Test cases can be defined using input/output files or command-line arguments.
- **Scoring System**: Automatically scores scripts based on passed test cases and weights.
- **Detailed Reporting**: Generates a CSV report with results for each script and test case.
- **Timeout Handling**: Prevents infinite loops by enforcing time limits for script execution.
- **Comparison Methods**: Supports exact, fuzzy (numerical), and image-based output comparisons.

---

## Project Structure
root/  
├── questions/ # Folder containing question categories  
│ ├── Q1/ # Question 1  
│ │ ├── tests/ # Test cases for Q1  
│ │ │ ├── test_1_input.txt  
│ │ │ └── test_1_output.txt  
│ │ └── config.json # Configuration for Q1   
│ ├── Q2/ # Question 2 (argument-based)  
│ │ ├── tests/  
│ │ │ ├── test_1_args.txt  
│ │ │ └── test_1_output.txt  
│ │ └── config.json  
├── scripts/ # Folder containing Python scripts to test  
│ ├── Q1_script.py # Scripts follow naming convention  
│ └── Q2_script.py  
├── tester.py # Main testing script  
├── results.csv # Output results (auto-generated)  
├── requirements.txt # Python dependencies  
└── README.md # This file  
  
  
---

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/python-script-tester.git
   cd python-script-tester
2. **Create a Virtual Environment**:
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
3. **Install Dependencies**:
    pip install -r requirements.txt
4. **Organize Your Files**:
    Place your Python scripts in the scripts/ folder. Name them as Q1_script.py, Q2_script.py, etc.
    Add questions and test cases in the questions/ folder. Each question should have:
    A config.json file.
    A tests/ folder with input/output files.


**Configuration**
Each question folder must contain a config.json file with the following fields:

{
  "test_type": "stdin",       // or "args" for command-line arguments
  "timeout": 5,               // Maximum execution time (seconds)
  "output_comparison": "exact", // or "fuzzy", "image"
  "weight": 1.5               // Scoring weight for this question
}

