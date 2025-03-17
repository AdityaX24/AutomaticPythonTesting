#2
import numpy as np
from sympy import Matrix

def robot_movement(T, P):
    """
    Compute the transformed position of the robot and analyze the transformation matrix.

    Args:
        T (numpy.ndarray): Transformation matrix of size n x n.
        P (numpy.ndarray): Position matrix.

    Returns:
        tuple: (P_transformed, RREF, T_inv) where:
               P_transformed is the transformed position matrix.
               RREF is the row-reduced echelon form of T.
               T_inv is the computed inverse of T.
    """
    # Apply transformation
    P_transformed = np.dot(T, P)

    # Compute RREF using SymPy
    T_sympy = Matrix(T)
    T_rref, _ = T_sympy.rref()

    # Compute inverse using NumPy
    T_inv = np.linalg.inv(T)

    return P_transformed, np.array(T_rref.tolist()), T_inv

# Boilerplate code to handle input and output
def main():
    # Read input from stdin (HackerRank format)
    T, P = [], []
    rows, cols = map(int, input().split())  # Read dimensions of T

    for _ in range(rows):
        T.append(list(map(float, input().split())))

    rows, cols = map(int, input().split())  # Read dimensions of P
    for _ in range(rows):
        P.append(list(map(float, input().split())))

    T = np.array(T)
    P = np.array(P)

    # Perform Robot Movement Analysis
    P_transformed, RREF, T_inv = robot_movement(T, P)

    # Print results
    print("P' =")
    for row in P_transformed:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nRREF =")
    for row in RREF:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nT^-1 =")
    for row in T_inv:
        print(" ".join(f"{x:.3f}" for x in row))

if __name__ == "__main__":
    main()
