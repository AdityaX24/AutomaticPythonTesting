import scipy.linalg
import numpy as np

def plu_factorization(A):
    """
    Perform PLU factorization on the given square matrix A.

    Args:
        A (numpy.ndarray): A square matrix of size n x n.

    Returns:
        tuple: A tuple (P, L, U) where L is the lower triangular matrix and U is the upper triangular matrix.
    """

    P, L, U = scipy.linalg.lu(A)

    return P, L, U

# Boilerplate code to handle input and output
def main():
    # Read input from stdin (HackerRank format)
    A = []
    while True:
        try:
            row = input().strip()  # Read a line of input
            if row:
                # Convert the space-separated string into a list of floats
                A.append(list(map(float, row.split())))
            else:
                break  # Stop reading if an empty line is encountered
        except EOFError:
            break  # Stop reading if end of input is reached
    A=np.array(A)
    # Perform LU factorization
    P, L, U = plu_factorization(A)

    # Print results
    print("P =")
    for row in P:
        print(" ".join(f"{x:.1f}" for x in row))
    print("\nL =")
    for row in L:
        print(" ".join(f"{x:.1f}" for x in row))
    print("\nU =")
    for row in U:
        print(" ".join(f"{x:.1f}" for x in row))


if __name__ == "__main__":
    main()


# Assignment Question:
# Implement a Python function lu_factorization(A) that computes the LU Factorization of a given square matrix 
# A
# A. The function should return two matrices 
# L
# L (lower triangular) and 
# U
# U (upper triangular) such that 
# A
# =
# L
# ⋅
# U
# A=L⋅U.

# Input:
# A: A square matrix (2D list) of size 
# n
# ×
# n
# n×n.

# Output:
# Return a tuple (L, U) where:

# L is the lower triangular matrix with 1's on the diagonal.

# U is the upper triangular matrix.

# Test Case 1
# 2 -1 -2      
# -4 6 3
# -4 -2 8

# A=  [[ 2. -1. -2.]
#  [-4.  6.  3.]
#  [-4. -2.  8.]]
# P =
# 0.0 0.0 1.0
# 1.0 0.0 0.0
# 0.0 1.0 0.0

# L =
# 1.0 0.0 0.0
# 1.0 1.0 0.0
# -0.5 -0.2 1.0

# U =
# -4.0 6.0 3.0
# 0.0 -8.0 5.0
# 0.0 0.0 0.8


# Test Case 2

# 2  -1   3   4
# -4   2  -5  -7
# 6  -3   8  10
# 8  -4   9  13

# A=  [[ 2. -1.  3.  4.]
#  [-4.  2. -5. -7.]
#  [ 6. -3.  8. 10.]
#  [ 8. -4.  9. 13.]]
# P =
# 0.0 0.0 0.0 1.0
# 0.0 1.0 0.0 0.0
# 0.0 0.0 1.0 0.0
# 1.0 0.0 0.0 0.0

# L =
# 1.0 0.0 0.0 0.0
# -0.5 1.0 0.0 0.0
# 0.8 0.0 1.0 0.0
# 0.2 0.0 0.6 1.0

# U =
# 8.0 -4.0 9.0 13.0
# 0.0 0.0 -0.5 -0.5
# 0.0 0.0 1.2 0.2
# 0.0 0.0 0.0 0.6


# Test Case 3
# 1   2   3   4   5
# 2   3   4   5   6
# 3   4   5   6   7
# 4   5   6   7   8
# 5   6   7   8   9

# A=  [[1. 2. 3. 4. 5.]
#  [2. 3. 4. 5. 6.]
#  [3. 4. 5. 6. 7.]
#  [4. 5. 6. 7. 8.]
#  [5. 6. 7. 8. 9.]]

# P =
# 0.0 1.0 0.0 0.0 0.0
# 0.0 0.0 0.0 1.0 0.0
# 0.0 0.0 1.0 0.0 0.0
# 0.0 0.0 0.0 0.0 1.0
# 1.0 0.0 0.0 0.0 0.0

# L =
# 1.0 0.0 0.0 0.0 0.0
# 0.2 1.0 0.0 0.0 0.0
# 0.6 0.5 1.0 0.0 0.0
# 0.4 0.7 0.4 1.0 0.0
# 0.8 0.2 0.5 0.0 1.0

# U =
# 5.0 6.0 7.0 8.0 9.0
# 0.0 0.8 1.6 2.4 3.2
# 0.0 0.0 0.0 0.0 0.0
# 0.0 0.0 0.0 0.0 0.0
# 0.0 0.0 0.0 0.0 0.0