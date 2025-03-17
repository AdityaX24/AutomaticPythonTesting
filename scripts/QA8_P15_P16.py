#3
import numpy as np
from sympy import Matrix

def analyze_traffic(A):
    """
    Analyze traffic flow by computing RREF and Rank-Nullity.

    Args:
        A (numpy.ndarray): Traffic flow matrix of size m x n.

    Returns:
        tuple: (RREF, rank, nullity) where:
               RREF is the row-reduced echelon form of A.
               rank is the rank of A.
               nullity is the nullity of A.
    """
    A_sympy = Matrix(A)
    rref_matrix, pivot_columns = A_sympy.rref()  # Compute RREF using SymPy
    rank = len(pivot_columns)
    nullity = A.shape[1] - rank  # Nullity = Columns - Rank

    return np.array(rref_matrix.tolist()), rank, nullity

# Boilerplate code to handle input and output
def main():
    # Read input from stdin (HackerRank format)
    A = []
    rows, cols = map(int, input().split())  # Read dimensions of A

    for _ in range(rows):
        A.append(list(map(float, input().split())))

    A = np.array(A)

    # Perform Traffic Analysis
    RREF, rank, nullity = analyze_traffic(A)

    # Print results
    print("RREF =")
    for row in RREF:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nRank =", rank)
    print("Nullity =", nullity)

if __name__ == "__main__":
    main()
