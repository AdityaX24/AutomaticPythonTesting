# Question: Industrial Sensor Calibration System

# You are a manufacturing engineer calibrating a sensor array with m parameters (e.g., sensitivity, offset) using n experimental readings. The calibration is modeled by an overdetermined system Ax = b, where:

# A: n×m matrix of experimental conditions (each row represents a sensor reading’s dependence on parameters).

# x: Unknown calibration parameters.

# b: Observed sensor outputs.

# Due to measurement noise, the system has no exact solution. Your tasks:

# Compute the best-fit calibration parameters using least squares approximation.

# Calculate the residual error to quantify calibration accuracy.


import numpy as np  
import scipy

def calibrate_sensor(A, b):  
    # Return: best-fit parameters (x), residual error vector
    # Hint: Use least squares for overdetermined systems (n > m)  
    
    x, _, _, _ = np.linalg.lstsq(A, b,rcond=None)  
    n, m = A.shape  
    residual = np.dot(A,x) - b

    return x, residual

# Boilerplate (do not modify)  
def main():  
    n = int(input())  # Number of experimental readings  
    A = []  
    for _ in range(n):  
        row = list(map(float, input().split()))  
        A.append(row)  
    b = np.array(list(map(float, input().split())))  
    A = np.array(A)  
    
    params, residual = calibrate_sensor(A, b)  
    
    print("Best-fit parameters:", np.round(params, 2))  
    print(f"Residual error: {np.round(residual, 2)}")  

if __name__ == "__main__":  
    main()  


# Test case 1

# 5  
# 0.8 1.2  
# 1.0 1.5  
# 1.2 1.8  
# 0.9 1.3  
# 1.1 1.6  
# 4.1 5.0 5.9 4.8 5.7  

# Best-fit parameters: [12.97 -5.32]
# Residual error: [-0.11 -0.02  0.08 -0.05  0.05]


# Test case 2

# 3  
# 1 1  
# 1 2  
# 1 3  
# 3 5 7  

# Best-fit parameters: [1. 2.]
# Residual error: [0. 0. 0.]

# Test case 3

# 4  
# 1 0 2  
# 0 1 3  
# 2 3 1  
# 3 2 0  
# 4 6 14 12
  
# Best-fit parameters: [2. 3. 1.]
# Residual error: [ 0.  0. -0.  0.]

# Test case 4

# 8  
# 5 3 7 2 8  
# 9 1 4 6 3  
# 2 8 5 7 1  
# 6 4 9 3 2  
# 7 5 8 1 4  
# 3 6 2 9 5  
# 8 2 6 4 7  
# 1 7 3 5 9  
# 45 32 28 37 41 29 34 40  

# Best-fit parameters: [1.13 1.56 2.06 0.26 2.11]
# Residual error: [-2.81 -4.09  0.96 -0.39 -0.06  0.74  6.38 -1.5 ]
