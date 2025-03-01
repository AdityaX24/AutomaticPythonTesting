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