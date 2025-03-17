#3d
import numpy as np
from sympy import Matrix

def rref_matrix(A):
    """
    Compute the Row-Reduced Echelon Form (RREF) of A.

    Args:
        A (numpy.ndarray): A matrix of size m x n.

    Returns:
        numpy.ndarray: The RREF of A.
    """
    A_sympy = Matrix(A)
    rref_matrix, _ = A_sympy.rref()  # Compute RREF using SymPy

    return np.array(rref_matrix.tolist())

# Boilerplate code to handle input and output
def main():
    # Read input
    m, n = map(int, input().split())  # Read dimensions
    A = np.array([list(map(float, input().split())) for _ in range(m)])  # Read matrix

    # Compute RREF
    R = rref_matrix(A)

    # Print results
    print("RREF =")
    for row in R:
        print(" ".join(f"{x:.1f}" for x in row))

if __name__ == "__main__":
    main()
