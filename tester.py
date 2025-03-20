import os
import json
import subprocess
from PIL import Image  # For image comparisons
import numpy as np
import sys
from pathlib import Path
import logging
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent

LOG_DIR = BASE_DIR / "AutomaticPythonTesting" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def setup_logger():
    """Configure logging system"""
    logger = logging.getLogger("PythonTestLogger")
    logger.setLevel(logging.INFO)

    # Create file handler which logs even debug messages
    log_file = LOG_DIR / f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    return logger

def load_questions(questions_dir):
    """Load all questions with their configurations and test cases"""
    questions_path = BASE_DIR / "AutomaticPythonTesting" / questions_dir
    questions = {}
    # List only directories and ignore hidden files
    question_dirs = [d for d in os.listdir(questions_path)
                    if os.path.isdir(os.path.join(questions_path, d))
                    and not d.startswith('.')]  # Skip hidden directories
    print(question_dirs)
    for q_dir in question_dirs:
        q_path = os.path.join(questions_path, q_dir)
        config_path = os.path.join(q_path, 'config.json')
        
        print(config_path)
        # Skip if config file is missing
        if not os.path.exists(config_path):
            continue
            
        with open(config_path) as f:
            config = json.load(f)
        
        print(config)
        tests = []
        test_dir = os.path.join(q_path, 'tests')
        if config['test_type'] == 'stdin':
            # Load input/output pairs
            inputs = [f for f in os.listdir(test_dir) if 'input' in f]
            print(inputs)
            for inp in sorted(inputs):
                test_num = inp.split('_')[1]
                with open(os.path.join(test_dir, inp)) as f:
                    input_data = f.read()
                with open(os.path.join(test_dir, f"test_{test_num}_output.txt")) as f:
                    expected = f.read()
                tests.append({
                    'input': input_data,
                    'expected': expected,
                    'type': 'stdin'
                })
        elif config['test_type'] == 'args':
            # Load argument-based tests
            arg_files = [f for f in os.listdir(test_dir) if 'args' in f]
            for arg_file in arg_files:
                test_num = arg_file.split('_')[1]
                with open(os.path.join(test_dir, arg_file)) as f:
                    args = f.read().split()
                with open(os.path.join(test_dir, f"test_{test_num}_output.txt")) as f:
                    expected = f.read()
                tests.append({
                    'args': args,
                    'expected': expected,
                    'type': 'args'
                })
                
        questions[q_dir] = {
            'config': config,
            'tests': tests
        }
    return questions

def run_script(script_path, test_case, config):
    """Run a script with the given test case based on question type"""
    timeout = config.get('timeout', 10)
    
    try:
        if test_case['type'] == 'stdin':
            proc = subprocess.run(
                [sys.executable, script_path],
                input=test_case['input'],
                text=True,
                capture_output=True,
                timeout=timeout
            )
        elif test_case['type'] == 'args':
            proc = subprocess.run(
                [sys.executable, script_path] + test_case['args'],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
        stdout = proc.stdout.strip()
        return {
            'output': stdout,
            'error': proc.stderr,
            'code': proc.returncode
        }
    except subprocess.TimeoutExpired:
        return {'error': 'Timeout', 'code': -1}

def compare_outputs(actual, expected, comparison_type):
    """Compare outputs based on question's comparison type"""
    if comparison_type == 'exact':
        return actual == expected
    elif comparison_type == 'fuzzy':
        # For numerical approximations
        try:
            a = float(actual)
            e = float(expected)
            return abs(a - e) < 1e-6
        except:
            return False
    elif comparison_type == 'image':
        # Compare images using PIL
        try:
            img_actual = Image.open(actual)
            img_expected = Image.open(expected)
            return np.array_equal(img_actual, img_expected)
        except:
            return False
    return False

def main():
    logger = setup_logger()
    questions = load_questions('questions')
    scripts_path = BASE_DIR / "AutomaticPythonTesting" / 'scripts'
    scripts = [f for f in os.listdir(scripts_path) if f.endswith('.py')]
    results = []
    
    for script in scripts:
        script_name = os.path.basename(script)
        # Extract Qn, SRN1, SRN2 from filename
        script_base = script_name.rsplit('.', 1)[0]
        parts = script_base.split('_')
        if len(parts) != 3:
            print(f"Skipping {script_name}: invalid filename format")
            continue
        q_name, srn1, srn2 = parts
        if q_name not in questions:
            print(f"Skipping {script_name}: question {q_name} not found")
            continue
        q_config = questions[q_name]['config']
        q_tests = questions[q_name]['tests']
        
        passed = 0
        test_results = []
        
        for test in q_tests:
            print("Script path:",os.path.join('scripts', script))
            execution = run_script(
                os.path.join('scripts', script),
                test,
                q_config
            )
            
            if execution['code'] != 0:
                test_results.append({
                    'status': 'Failed',
                    'error': execution['error']
                })
                logger.error(
        f"""Test failed for {script_name} on {q_name}

SRNs: {srn1}/{srn2}

Error:
{execution['error']}

Test Type: {test['type']}

Test Input:
{test.get('input', test.get('args', 'No input'))}

Expected Output:
{test['expected']}
--------------------------------------------------"""
    )
                continue
                
            is_passed = compare_outputs(
                execution['output'],
                test['expected'],
                q_config['output_comparison']
            )
            
            if is_passed:
                passed += 1
                test_results.append({'status': 'Passed'})
            else:
                test_results.append({
                    'status': 'Failed',
                    'expected': test['expected'],
                    'actual': execution['output']
                })
                logger.error(
        f"""Test failed for {script_name} on {q_name}

SRNs: {srn1}/{srn2}

Test Type: {test['type']}

Test Input:
{test.get('input', test.get('args', 'No input'))}

Expected Output:
{test['expected']}

Actual Output:
{execution['output']}
--------------------------------------------------"""
    )
        
        score = (passed / len(q_tests)) * q_config['weight']
        results.append({
            'question': q_name,
            'script': script_name, 
            'srn1': srn1,
            'srn2': srn2,
            'score': score, 
            'details': test_results
        })

        print(results)
    # Save results and generate report
    with open('results.csv', 'w') as f:
        f.write('Question,Script_Name,SRN_1,SRN_2,PassedTests,TotalTests,Score\n')
        for res in results:
            # Calculate passed tests count from details
            passed_count = sum(1 for detail in res['details'] if detail['status'] == 'Passed')
            total_tests = len(res['details'])
            
            f.write(f"{res['question']},")
            f.write(f"{res['script']},")
            f.write(f"{res['srn1']},")
            f.write(f"{res['srn2']},")
            f.write(f"{passed_count},")
            f.write(f"{total_tests},")
            f.write(f"{res['score']:.2f}\n")

    

if __name__ == '__main__':
    main()