# The Bridge Stability Analysis with Intermediate Steps

# Background:
# You are a structural engineer working on the design of a new suspension bridge. The bridge consists of multiple interconnected beams and supports, and the stability of the entire structure depends on the forces acting on each beam. To ensure the bridge is safe, you need to analyze the forces in the beams and verify that they are within acceptable limits.

# The forces in the beams can be modeled using a system of linear equations, where each equation represents the equilibrium of forces at a specific joint in the bridge. Solving this system will give you the forces in each beam.

# Problem:
# You are given a system of linear equations that represents the forces acting on the joints of the bridge. Your task is to solve this system efficiently and determine the forces in each beam. The system is represented as:

# A
# ⋅
# x
# =
# b
# A⋅x=b
# Where:

# A
# A is a square matrix representing the coefficients of the system.

# x
# x is a vector of unknown forces in the beams.

# b
# b is a vector of known external forces acting on the joints.

# To solve this system, you must first decompose the matrix 
# A
# A into two triangular matrices 
# L
# L (lower triangular) and 
# U
# U (upper triangular) such that 
# A
# =
# L
# ⋅
# U
# A=L⋅U. Then, use these matrices to solve for 
# x
# x.

# Input:
# The first line contains an integer 
# n
# n, the size of the matrix 
# A
# A (number of joints).

# The next 
# n
# n lines contain 
# n
# n space-separated floating-point numbers, representing the rows of matrix 
# A
# A.

# The last line contains 
# n
# n space-separated floating-point numbers, representing the vector 
# b
# b.

# Output:
# Print the 
# L
# L matrix, rounded to 2 decimal places.

# Print the 
# U
# U matrix, rounded to 2 decimal places.

# Print the solution vector 
# x
# x, rounded to 2 decimal places.

import numpy as np
import scipy.linalg

def lu_decomposition(A):
    """
    Perform LU decomposition on the given square matrix A.

    Args:
        A (numpy.ndarray): Coefficient matrix of size n x n.

    Returns:
        tuple: A tuple (L, U) where L is the lower triangular matrix and U is the upper triangular matrix.
    """
    P, L, U = scipy.linalg.lu(A)
    
    return L,U


def solve_system(L, U, b):
    """
    Solve the system of linear equations A * x = b using LU decomposition.

    Args:
        L (numpy.ndarray): Lower triangular matrix.
        U (numpy.ndarray): Upper triangular matrix.
        b (numpy.ndarray): Right-hand side vector of size n.

    Returns:
        numpy.ndarray: Solution vector x of size n.
    """
    n = L.shape[0]
    y = np.zeros(n)  # Intermediate vector for forward substitution
    x = np.zeros(n)  # Solution vector for backward substitution

    # Forward substitution (solve Ly = b)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Backward substitution (solve Ux = y)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x



# Boilerplate code to handle input and output
def main():
    # Read input
    n = int(input())
    A = []
    for _ in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    b = list(map(float, input().split()))

    # Convert to NumPy arrays
    A = np.array(A)
    b = np.array(b)

    # Perform LU decomposition
    L, U = lu_decomposition(A)

    # Solve the system
    x = solve_system(L, U, b)

    # Print results
    print("L =")
    print(np.round(L, 2))
    print("\nU =")
    print(np.round(U, 2))
    print("\nx =")
    print(" ".join(f"{val:.2f}" for val in x))


if __name__ == "__main__":
    main()


# Test Case 1
# 3
# 2 -1 -2
# -4 6 3
# -4 -2 8
# 3 7 10
# CHECK [[ 2. -1. -2.]
#  [-4.  6.  3.]
#  [-4. -2.  8.]]
# Calculated x [26.625       9.91666667 16.66666667]
# Actual Answer:
# [26.625       9.91666667 16.66666667]
# L =
# [[ 1.    0.    0.  ]
#  [ 1.    1.    0.  ]
#  [-0.5  -0.25  1.  ]]

# U =
# [[-4.    6.    3.  ]
#  [ 0.   -8.    5.  ]
#  [ 0.    0.    0.75]]

# x =
# 26.62 9.92 16.67

# Test case 2
# 4
# 4  1  0  2
# 1  5  3 -1
# 2  0  6  1
# 3  2  1  7
# 10 8 15 20
# CHECK [[ 4.  1.  0.  2.]
#  [ 1.  5.  3. -1.]
#  [ 2.  0.  6.  1.]
#  [ 3.  2.  1.  7.]]
# Calculated x [1.43220339 0.6440678  1.72033898 1.81355932]
# Actual Answer:
# [1.43220339 0.6440678  1.72033898 1.81355932]
# L =
# [[ 1.    0.    0.    0.  ]
#  [ 0.25  1.    0.    0.  ]
#  [ 0.5  -0.11  1.    0.  ]
#  [ 0.75  0.26  0.03  1.  ]]

# U =
# [[ 4.    1.    0.    2.  ]
#  [ 0.    4.75  3.   -1.5 ]
#  [ 0.    0.    6.32 -0.16]
#  [ 0.    0.    0.    5.9 ]]

# x =
# 1.43 0.64 1.72 1.81

# Test case 3

# 5
# 5  2  1  0  3
# 2  6  0  1 -1
# 1  0  7  2  4
# 0  1  2  8  0
# 3 -1  4  0  9
# 12 8 25 18 30
# CHECK [[ 5.  2.  1.  0.  3.]
#  [ 2.  6.  0.  1. -1.]
#  [ 1.  0.  7.  2.  4.]
#  [ 0.  1.  2.  8.  0.]
#  [ 3. -1.  4.  0.  9.]]
# Calculated x [-0.35691318  1.67236419  1.42359113  1.68505669  3.00541547]
# Actual Answer:
# [-0.35691318  1.67236419  1.42359113  1.68505669  3.00541547]
# L =
# [[ 1.    0.    0.    0.    0.  ]
#  [ 0.4   1.    0.    0.    0.  ]
#  [ 0.2  -0.08  1.    0.    0.  ]
#  [ 0.    0.19  0.31  1.    0.  ]
#  [ 0.6  -0.42  0.48 -0.08  1.  ]]

# U =
# [[ 5.    2.    1.    0.    3.  ]
#  [ 0.    5.2  -0.4   1.   -2.2 ]
#  [ 0.    0.    6.77  2.08  3.23]
#  [ 0.    0.    0.    7.17 -0.57]
#  [ 0.    0.    0.    0.    4.68]]

# x =
# -0.36 1.67 1.42 1.69 3.01