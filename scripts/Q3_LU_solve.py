# Question: The Adaptive Bridge Safety System

# Your coastal city now uses a smart sensor grid to monitor multiple bridges with varying numbers of support joints. Each bridge’s stability is governed by Ax = b, where A is an n×n force distribution matrix and b is the dynamic load vector. Sensors sometimes scramble equation orders (hint: organization matters) and safety thresholds vary by bridge age. Write a program to:

# Factorize A accounting for potential sensor errors

# Solve for force vector x

import numpy as np 
import scipy 

def decompose_and_solve(A, b):  
    # Student's task: Implement LU decomposition with row exchanges for any n×n matrix  
    # Return permutation matrix P, lower triangular L, upper triangular U, and solution x  
    P, L, U = scipy.linalg.lu(A)
    
    x = np.linalg.solve(A, b)
    
    return P, L, U, x  

# Boilerplate (do not modify)  
def main():   
    n = int(input())
    A = []
    for _ in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    b = list(map(float, input().split()))

    A=np.array(A)
    b=np.array(b)

    P, L, U, x = decompose_and_solve(A, b)  
    
    print(f"P ({n}x{n}):\n", np.round(P,2))  
    print(f"L ({n}x{n}):\n", np.round(L,2))  
    print(f"U ({n}x{n}):\n", np.round(U,2))  
    print("Force magnitudes:", np.round(x,2))  

if __name__ == "__main__":  
    main()  

# Test case 1

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

# P (3x3):
#  [[0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]
# L (3x3):
#  [[1.         0.         0.        ]
#  [0.14285714 1.         0.        ]
#  [0.57142857 0.5        1.        ]]
# U (3x3):
#  [[ 7.00000000e+00  8.00000000e+00  9.00000000e+00]
#  [ 0.00000000e+00  8.57142857e-01  1.71428571e+00]
#  [ 0.00000000e+00  0.00000000e+00 -1.58603289e-16]]
# Force magnitudes: [-25.33333333  41.66666667 -16.        ]


# Test case 2

# 4
# 2  -1   0   0
# -1  2  -1   0
# 0  -1   2  -1
# 0   0  -1   2
# 1  0  1  0

# P (4x4):
#  [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
# L (4x4):
#  [[ 1.          0.          0.          0.        ]
#  [-0.5         1.          0.          0.        ]
#  [ 0.         -0.66666667  1.          0.        ]
#  [ 0.          0.         -0.75        1.        ]]
# U (4x4):
#  [[ 2.         -1.          0.          0.        ]
#  [ 0.          1.5        -1.          0.        ]
#  [ 0.          0.          1.33333333 -1.        ]
#  [ 0.          0.          0.          1.25      ]]
# Force magnitudes: [1.2 1.4 1.6 0.8]


# # Test case 3

# 5
# 3  1  0  2  1
# 1  4  2  0  1
# 0  2  5  1  0
# 2  0  1  6  2
# 1  1  0  2  7
# 10  20  30  40  50

# P (5x5):
#  [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
# L (5x5):
#  [[ 1.          0.          0.          0.          0.        ]
#  [ 0.33333333  1.          0.          0.          0.        ]
#  [ 0.          0.54545455  1.          0.          0.        ]
#  [ 0.66666667 -0.18181818  0.34883721  1.          0.        ]
#  [ 0.33333333  0.18181818 -0.09302326  0.38857143  1.        ]]
# U (5x5):
#  [[ 3.          1.          0.          2.          1.        ]
#  [ 0.          3.66666667  2.         -0.66666667  0.66666667]
#  [ 0.          0.          3.90909091  1.36363636 -0.36363636]
#  [ 0.          0.          0.          4.06976744  1.58139535]
#  [ 0.          0.          0.          0.          5.89714286]]
# Force magnitudes: [-2.55813953  2.09302326  4.18604651  4.88372093  5.81395349]