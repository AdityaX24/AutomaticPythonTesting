"""
Industrial Sensor Calibration System

You are a manufacturing engineer calibrating a sensor array with m parameters (e.g., sensitivity, offset) 
using n experimental readings. 

The calibration is modeled by an overdetermined system Ax = b, where:

A: n*m matrix of experimental conditions (each row represents a sensor reading's dependence on parameters).
x: Unknown calibration parameters.
b: Observed sensor outputs.

Due to measurement noise, the system has no exact solution. Your tasks:
    Compute the best-fit calibration parameters using least squares approximation.
    Calculate the residual error to quantify calibration accuracy.

Input:
The first line contains an integer n, the rows of the matrix
The next n lines contain n space-separated floating-point numbers, representing the sensor reading's
The last line contains n space-separated floating-point numbers, representing the vector b (Observed sensor outputs).

Output:
Best-fit calibration parameters.
Print the U matrix, rounded to 2 decimal places.
Residual error, rounded to 2 decimal places.

Sample Test Case 1
Input:

5  
0.8 1.2  
1.0 1.5  
1.2 1.8  
0.9 1.3  
1.1 1.6  
4.1 5.0 5.9 4.8 5.7  

Expected Output:

Best-fit parameters: [12.97 -5.32]
Residual error: [-0.11 -0.02  0.08 -0.05  0.05]

Sample Test Case 2
Input:

3  
1 1  
1 2  
1 3  
3 5 7  

Expected Output:

Best-fit parameters: [1. 2.]
Residual error: [0. 0. 0.]


Note: You should only write your logic in calibrate_sensor method and return the required answers. 
Proper printing format will be taken care of by the boilerplate. 

DO NOT CHANGE THE BOILERPLATE.

"""
import numpy as np  
import scipy

def calibrate_sensor(A, b):  
    # Return: best-fit parameters (x), residual error vector
    
    #Implement your code here
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
