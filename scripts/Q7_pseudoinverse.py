# Application: Smart City Sensor Analysis

#     In a smart city initiative, sensor data from various intersections is gathered
#     into a matrix to help monitor and optimize traffic flow. However, due to sensor
#     errors or redundant readings, the matrix may be singular. This situation can
#     affect further analyses that require matrix inversion, such as forecasting or
#     optimizing traffic signals.

#     Your task is to determine whether the given sensor data matrix is singular.
#     If it is not singular, compute its inverse.
#     The matrix is not necessarily a square matrix.

#     The function should return a tuple where:
#       - The first element is a boolean value: True if the matrix is singular,
#         and False otherwise.
#       - The second element is the inverse of the matrix if it exists, or None if it does not.

#     Note: The input is provided as a NumPy array.

import numpy as np
import json

def analyze_sensor_matrix(matrix):
    """
    
    """
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

if __name__ == "__main__":
    # Input boilerplate:
    # First input: number of experimental readings (matrix rows)
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


# Test case 1

# 3
# 1 2 3
# 0 1 4
# 5 6 0
# The matrix is not singular.
# Inverse of the matrix: 
# [[-24.  18.   5.]
#  [ 20. -15.  -4.]
#  [ -5.   4.   1.]]

# Test case 2

# 3
# 2 4 6
# 1 2 3
# 3 6 9
# The matrix is singular.

# Test case 3

# 4
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# The matrix is not singular.
# Inverse of the matrix: 
# [[-0.48 -0.24 -0.01  0.23]
#  [-0.03 -0.01  0.01  0.03]
#  [ 0.42  0.22  0.03 -0.17]]

# Test case 4

# 3
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# The matrix is not singular.
# Inverse of the matrix: 
# [[-0.38 -0.1   0.18]
#  [-0.15 -0.03  0.08]
#  [ 0.08  0.03 -0.02]
#  [ 0.31  0.1  -0.11]]

# Test case 5

# 5
# 1 0 0 0 0
# 0 2 1 0 0
# 0 0 3 1 0
# 0 0 0 4 1
# 0 0 0 0 5
# The matrix is not singular.
# Inverse of the matrix: 
# [[ 1.    0.    0.    0.    0.  ]
#  [ 0.    0.5  -0.17  0.04 -0.01]
#  [ 0.    0.    0.33 -0.08  0.02]
#  [ 0.   -0.   -0.    0.25 -0.05]
#  [ 0.    0.    0.    0.    0.2 ]]