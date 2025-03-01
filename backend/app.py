from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import shutil
import subprocess
from typing import List
from pathlib import Path

app = FastAPI()

# Allow CORS for React development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).parent.parent

@app.post("/upload/script")
async def upload_script(file: UploadFile = File(...)):
    script_dir = BASE_DIR / "scripts"
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
    test_dir = BASE_DIR / "questions" / question_id / "tests"
    test_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f"test_{len(os.listdir(test_dir)) + 1}_{test_type}.txt"
    file_path = test_dir / filename
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message": f"Test case {filename} uploaded"}

@app.delete("/delete")
async def delete_item(path: str):
    full_path = BASE_DIR / path
    if not full_path.exists():
        raise HTTPException(status_code=404, detail="Path not found")
    
    if full_path.is_file():
        full_path.unlink()
    else:
        shutil.rmtree(full_path)
    
    return {"message": f"{path} deleted"}

@app.get("/run-tests")
async def run_tests():
    result_file = BASE_DIR / "results.csv"
    
    # Run your existing tester
    subprocess.run(["python", str(BASE_DIR / "backend" / "tester.py")], check=True)
    
    return FileResponse(result_file)

@app.get("/list-files")
async def list_files():
    return {
        "scripts": os.listdir(BASE_DIR / "scripts"),
        "questions": os.listdir(BASE_DIR / "questions")
    }