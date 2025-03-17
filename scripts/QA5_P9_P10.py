#1
import numpy as np
from scipy.linalg import lu_factor, lu_solve

def economic_forecast(A, b):
    """
    Solve an economic forecasting system using LU decomposition.

    Args:
        A (numpy.ndarray): Coefficient matrix of size n x n.
        b (numpy.ndarray): Column vector of size n.

    Returns:
        tuple: (x, rank, nullity) where:
               x is the solution vector.
               rank is the rank of A.
               nullity is the nullity of A.
    """
    # LU Factorization and Solution
    LU, piv = lu_factor(A)
    x = lu_solve((LU, piv), b)

    # Compute Rank and Nullity
    rank = np.linalg.matrix_rank(A)
    nullity = A.shape[1] - rank  # Nullity = Columns - Rank

    return x, rank, nullity

# Boilerplate code to handle input and output
def main():
    # Read input from stdin (HackerRank format)
    A, b = [], []
    rows, cols = map(int, input().split())  # Read dimensions of A

    for _ in range(rows):
        A.append(list(map(float, input().split())))

    b = list(map(float, input().split()))  # Read b values

    A = np.array(A)
    b = np.array(b)

    # Perform Economic Forecast Analysis
    result = economic_forecast(A, b)

    # Print results
    x, rank, nullity = result

    print("x =")
    print(" ".join(f"{xi:.4f}" for xi in x))

    print("\nRank =", rank)
    print("Nullity =", nullity)

if __name__ == "__main__":
    main()