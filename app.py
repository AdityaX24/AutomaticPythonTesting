from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Body, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import shutil
import subprocess
from typing import List
from pathlib import Path
import logging

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
    test_type: str = Form(...),
    file: UploadFile = File(...)
):
    test_dir = BASE_DIR / "AutomaticPythonTesting" / "questions" / question_id / "tests"
    test_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"test_{len(os.listdir(test_dir)) + 1}_{test_type}.txt"
    file_path = test_dir / filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message": f"Test case {filename} uploaded"}


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
    # scripts = [f for f in os.listdir(BASE_DIR / "AutomaticPythonTesting" / "scripts") if not f.startswith('.')]
    # questions = [f for f in os.listdir(BASE_DIR / "AutomaticPythonTesting" / "questions") if not f.startswith('.')]
    
    scripts = [f for f in os.listdir(BASE_DIR / "AutomaticPythonTesting" / "scripts") if not f.startswith('.')]
    questions = [f for f in os.listdir(BASE_DIR  / "AutomaticPythonTesting" / "questions") if not f.startswith('.')]
    

    return {
        "scripts": scripts,
        "questions": questions
    }