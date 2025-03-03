# Python Script Tester

A full-stack testing framework with React frontend and FastAPI backend to automatically test Python scripts against predefined test cases.

This tool is designed to evaluate multiple `.py` files in a folder, run them against test cases, and generate a detailed report of the results.

---

## Features

- **Web Interface**: React-based dashboard for file management and test execution
- **REST API**: FastAPI backend for test execution and file management
- **Real-time Results**: Instant test results display in the web interface
- **Multiple Question Types**: Supports stdin input, command-line arguments, and different comparison methods
- **Scoring System**: Automated scoring with configurable weights
- **File Management**: Web interface for uploading scripts and test cases

---

## Project Structure

```bash
root
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

```

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/python-script-tester.git
   cd python-script-tester
   ```
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Navigate to frontend directory and install dependencies**:
   ```bash
   cd frontend
   npm install
   npm start
   ```
5. **In a new terminal go to backend directory**:
   ```bash
   cd backend
   uvicorn app:app --reload --port 8000
   ```

**Usage**

1. Acess the web interface at http://localhost:3000
2. Upload scripts and test cases using the web interface
3. Configure questions via the backend questions/ directory
4. Run tests through the web interface
5. View results in the dashboard and download CSV reports

**API Endpoints**

```bash
| Endpoint       | Method | Description                  |
|:---------------|:------:|------------------------------|
| `/upload`      | POST   | Upload scripts/test cases    |
| `/delete`      | POST   | Delete files                 |
| `/run-tests`   | POST   | Execute all tests            |
| `/list-files`  | GET    | Get available files          |
| `/results`     | GET    | Download CSV report          |
```

**Configuration**
Each question folder must contain a config.json file with the following fields:

```bash
{
  "test_type": "stdin",       // or "args" for command-line arguments
  "timeout": 5,               // Maximum execution time (seconds)
  "output_comparison": "exact", // or "fuzzy", "image"
  "weight": 1.5               // Scoring weight for this question
}
```

**TO-DO**

1. In the Test Result section, show the table properly, Instead of Script Column, Take the [1] position of the script file names (2 srn).

2. Allow to download the displayed result as csv.

3. Allow option to upload multiple scripts at once in upload script tab.
