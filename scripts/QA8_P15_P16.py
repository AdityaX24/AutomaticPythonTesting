#4
import numpy as np
from sympy import Matrix

def secure_communication(T, M):
    """
    Perform secure message decoding using matrix inversion.

    Args:
        T (numpy.ndarray): Encoding matrix of size n x n.
        M (numpy.ndarray): Encoded message matrix.

    Returns:
        tuple: (C, RREF, rank, nullity) where:
               C is the decoded message.
               RREF is the row-reduced echelon form of T.
               rank is the rank of T.
               nullity is the nullity of T.
    """
    # Compute inverse and decode message
    T_inv = np.linalg.inv(T)
    C = np.dot(T_inv, M)

    # Compute RREF using SymPy
    T_sympy = Matrix(T)
    T_rref, _ = T_sympy.rref()

    # Compute Rank and Nullity
    rank = np.linalg.matrix_rank(T)
    nullity = T.shape[1] - rank  # Nullity = Columns - Rank

    return C, np.array(T_rref.tolist()), rank, nullity

# Boilerplate code to handle input and output
def main():
    # Read input from stdin (HackerRank format)
    T, M = [], []
    rows, cols = map(int, input().split())  # Read dimensions of T

    for _ in range(rows):
        T.append(list(map(float, input().split())))

    rows, cols = map(int, input().split())  # Read dimensions of M
    for _ in range(rows):
        M.append(list(map(float, input().split())))

    T = np.array(T)
    M = np.array(M)

    # Perform Secure Communication Processing
    C, RREF, rank, nullity = secure_communication(T, M)

    # Print results
    print("C =")
    for row in C:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nRREF =")
    for row in RREF:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nRank =", rank)
    print("Nullity =", nullity)

if __name__ == "__main__":
    main()
