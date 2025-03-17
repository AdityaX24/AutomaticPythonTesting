"""
The Bridge Stability Analysis with Intermediate Steps

Problem Statement:
You are a structural engineer working on the design of a new suspension bridge. 
The bridge consists of multiple interconnected beams and supports, 
and the stability of the entire structure depends on the forces acting on each beam. 
To ensure the bridge is safe, you need to analyze the forces in the beams and verify 
that they are within acceptable limits.

The forces in the beams can be modeled using a system of linear equations, 
where each equation represents the equilibrium of forces at a specific joint in the bridge. 
Solving this system will give you the forces in each beam.

You are given a system of linear equations that represents the forces 
acting on the joints of the bridge. Your task is to solve this system efficiently 
and determine the forces in each beam. The system is represented as:

A⋅x=b
Where: A is a square matrix representing the coefficients of the system.
       x is a vector of unknown forces in the beams.
       b is a vector of known external forces acting on the joints.

To solve this system, you must first decompose the matrix A into two triangular matrices 
L (lower triangular) and U (upper triangular) such that : A=L⋅U. 

Then, use these matrices to solve for x.

Input:
The first line contains an integer n, the size of the matrix A (number of joints).
The next n lines contain n space-separated floating-point numbers, representing the rows of matrix A.
The last line contains n space-separated floating-point numbers, representing the vector b.

Output:
Print the L matrix, rounded to 2 decimal places.
Print the U matrix, rounded to 2 decimal places.
Print the solution vector x, rounded to 2 decimal places.

Sample Test Case 1
Input:

3
2 -1 -2
-4 6 3
-4 -2 8
3 7 10

Expected Output:

L =
[[ 1.    0.    0.  ]
 [ 1.    1.    0.  ]
 [-0.5  -0.25  1.  ]]

U =
[[-4.    6.    3.  ]
 [ 0.   -8.    5.  ]
 [ 0.    0.    0.75]]

x =
26.62 9.92 16.67

Sample Test Case 2
Input:

4
4  1  0  2
1  5  3 -1
2  0  6  1
3  2  1  7
10 8 15 20

Expected Output:

L =
[[ 1.    0.    0.    0.  ]
 [ 0.25  1.    0.    0.  ]
 [ 0.5  -0.11  1.    0.  ]
 [ 0.75  0.26  0.03  1.  ]]

U =
[[ 4.    1.    0.    2.  ]
 [ 0.    4.75  3.   -1.5 ]
 [ 0.    0.    6.32 -0.16]
 [ 0.    0.    0.    5.9 ]]

x =
1.43 0.64 1.72 1.81


Note: You should only write your logic in lu_decomposition and solve_system methods and return the required answers. 
Proper printing format will be taken care of by the boilerplate. 

DO NOT CHANGE THE BOILERPLATE.

"""


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

    #Implement your code here
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
    
    #Implement your code here
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
    n = int(input())
    A = []
    for _ in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    b = list(map(float, input().split()))
    A = np.array(A)
    b = np.array(b)
    L, U = lu_decomposition(A)
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

