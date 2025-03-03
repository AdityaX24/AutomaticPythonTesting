from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Body, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import shutil
import subprocess
from typing import List
from pathlib import Path
import logging
import json

logger = logging.getLogger("my_logger")

app = FastAPI()

# Allow CORS for React development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).parent.parent

@app.post("/upload/script")
async def upload_script(file: UploadFile = File(...)):
    script_dir = BASE_DIR / "AutomaticPythonTesting" / "scripts"
    script_dir.mkdir(exist_ok=True)
    
    file_path = script_dir / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"Script {file.filename} uploaded"}

@app.post("/upload/testcase")
async def upload_testcase(
    question_id: str = Form(...),
    input_file: UploadFile = File(...),
    output_file: UploadFile = File(...)
):
    test_dir = BASE_DIR / "AutomaticPythonTesting" / "questions" / question_id / "tests"
    test_dir.mkdir(parents=True, exist_ok=True)

    # Create/check config file in question directory
    question_dir = test_dir.parent
    config_path = question_dir / "config.json"
    
    if not config_path.exists():
        default_config = {
            "test_type": "stdin",
            "timeout": 10,
            "output_comparison": "exact",
            "weight": 100
        }
        try:
            with open(config_path, 'w') as config_file:
                json.dump(default_config, config_file, indent=4)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to create config file: {str(e)}"
            )
        
    # Get existing test numbers
    existing_files = os.listdir(test_dir)
    test_numbers = []
    for filename in existing_files:
        if filename.startswith("test_") and (filename.endswith("_input.txt") or filename.endswith("_output.txt")):
            parts = filename.split('_')
            if len(parts) >= 3:
                try:
                    test_numbers.append(int(parts[1]))
                except ValueError:
                    continue
    new_test_number = max(test_numbers) + 1 if test_numbers else 1

    # Save input file
    input_filename = f"test_{new_test_number}_input.txt"
    input_path = test_dir / input_filename
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(input_file.file, buffer)
    
    # Save output file
    output_filename = f"test_{new_test_number}_output.txt"
    output_path = test_dir / output_filename
    with open(output_path, "wb") as buffer:
        shutil.copyfileobj(output_file.file, buffer)
    
    return {"message": f"Test case {new_test_number} uploaded successfully"}

@app.post("/delete-scripts")
async def delete_item(data: dict = Body(...)):  # Accept path from the body
    path = data.get("path")
    print(path)
    full_path = BASE_DIR / "AutomaticPythonTesting" / path
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="Path not found")
    
    if full_path.is_file():
        full_path.unlink()
    else:
        shutil.rmtree(full_path)
    
    return {"message": f"{path} deleted"}

@app.post("/delete-testcases")
async def delete_item(data: dict = Body(...)):
    path = data.get("path")
    full_path = BASE_DIR / "AutomaticPythonTesting" / path
    
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="Path not found")
    
    try:
        if full_path.is_file():
            full_path.unlink()
        else:
            shutil.rmtree(full_path)
        return {"message": f"{path} deleted"}
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Delete failed: {str(e)}"
        )

@app.get("/run-tests")
async def run_tests(background_tasks: BackgroundTasks):
       result_file = BASE_DIR / "AutomaticPythonTesting" / "results.csv"

       venv_python = BASE_DIR / "AutomaticPythonTesting" / ".venv" / "bin" / "python3.12"  # Adjust this path as necessary
       # Run the tester script and capture output
       try:
           result = subprocess.run(
               [str(venv_python), str(BASE_DIR / "AutomaticPythonTesting" / "tester.py")],
               check=True,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE
           )
           print("STDOUT:", result.stdout.decode())
           print("STDERR:", result.stderr.decode())
       except subprocess.CalledProcessError as e:
           print("Error running tester.py:", e.stderr.decode())
           raise HTTPException(status_code=500, detail="Error running tests")

       return FileResponse(result_file)

@app.get("/list-files")
async def list_files():
    base_path = BASE_DIR / "AutomaticPythonTesting"
    scripts = [
        f for f in os.listdir(base_path / "scripts") 
        if not f.startswith('.')
    ]
    
    questions = {}
    questions_dir = base_path / "questions"
    for q_dir in os.listdir(questions_dir):
        if q_dir.startswith('.'):
            continue
        test_dir = questions_dir / q_dir / "tests"
        if test_dir.exists():
            questions[q_dir] = os.listdir(test_dir)
        else:
            questions[q_dir] = []
    
    return {
        "scripts": scripts,
        "questions": questions  # Now returns {question_id: [test_files]}
    }