import os
import json
import subprocess
from PIL import Image  # For image comparisons
import numpy as np
import sys

def load_questions(questions_dir):
    """Load all questions with their configurations and test cases"""
    questions = {}
    # List only directories and ignore hidden files
    question_dirs = [d for d in os.listdir(questions_dir)
                    if os.path.isdir(os.path.join(questions_dir, d))
                    and not d.startswith('.')]  # Skip hidden directories
    print(question_dirs)
    for q_dir in question_dirs:
        q_path = os.path.join(questions_dir, q_dir)
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
    timeout = config.get('timeout', 5)
    
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
    questions = load_questions('questions')
    scripts = [f for f in os.listdir('scripts') if f.endswith('.py')]
    
    print(questions)
    results = []
    
    for script in scripts:
        script_name = os.path.basename(script)
        print(script_name)
        q_name = script_name.split('_')[0]  # Extract Q1 from Q1_script.py
        
        if q_name not in questions:
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
        
        score = (passed / len(q_tests)) * q_config['weight']
        results.append({
            'question': q_name,
            'script': script_name,
            'score': score,
            'details': test_results
        })

        print(results)
    # Save results and generate report
    with open('results.csv', 'w') as f:
        f.write('Question,Script,Test,Status,Score\n')
        for res in results:
            for i, detail in enumerate(res['details']):
                f.write(f"{res['question']},{res['script']},Test_{i+1},{detail['status']},{res['score']}\n")

if __name__ == '__main__':
    main()