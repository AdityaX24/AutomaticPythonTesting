"""
Smart City Sensor Analysis

In a smart city initiative, sensor data from various intersections is gathered
into a matrix to help monitor and optimize traffic flow. However, due to sensor
errors or redundant readings, the matrix may be singular. This situation can
affect further analyses that require matrix inversion, such as forecasting or
optimizing traffic signals.

Your task is to determine whether the given sensor data matrix is singular and then compute its inverse.

Note: The matrix is not necessarily a square matrix.

Input:
The first line contains an integer n, the size of the matrix A.
The next n lines contain n space-separated floating-point numbers, representing the rows of matrix A.

Output:
The function should return a tuple where:
  - The first element is a boolean value: True if the matrix is singular, and False otherwise.
  - The second element is the inverse of the matrix if it exists, or None if it does not.

Sample Test Case 1
Input:

3
1 2 3
0 1 4
5 6 0

Expected Output:

The matrix is not singular.
Inverse of the matrix: 
[[-24.  18.   5.]
 [ 20. -15.  -4.]
 [ -5.   4.   1.]]

Sample Test Case 2
Input:

3
2 4 6
1 2 3
3 6 9

Expected Output:

The matrix is singular.

Note: You should only write your logic in analyze_sensor_matrix method and return the required answers. 
Proper printing format will be taken care of by the boilerplate. 

DO NOT CHANGE THE BOILERPLATE.

"""

import numpy as np
import json

def analyze_sensor_matrix(matrix):
    """
    Input is a matrix of m * n dimension. 
    """
    
    #Implement your code here
    m, n = matrix.shape

    if m!=n:
       inv_matrix = np.linalg.pinv(matrix)
       return (False, inv_matrix)
    
    # Check for singularity by comparing the rank with the matrix's dimension.
    if np.linalg.matrix_rank(matrix) < m:
            return (True, None)
    # If the matrix is non-singular, compute its inverse.
    inv_matrix = np.linalg.pinv(matrix)
    return (False, inv_matrix)
    
    return (is_singular, inv_matrix)

if __name__ == "__main__":
    n = int(input())  
    A = []  
    for _ in range(n):  
        row = list(map(float, input().split()))  
        A.append(row)  
    A = np.array(A)
    
    is_singular, inv_matrix = analyze_sensor_matrix(A)
    
    if is_singular:
        print("The matrix is singular.")
    else:
        print("The matrix is not singular.")
        print("Inverse of the matrix: ")
        print(np.round(inv_matrix,2))
