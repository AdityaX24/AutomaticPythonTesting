#1d
import numpy as np

def gauss_jordan_inverse(A):
    """
    Perform Gauss-Jordan elimination on A to compute its inverse.

    Args:
        A (numpy.ndarray): A square matrix of size n x n.

    Returns:
        tuple: (U, C, A_inv) where:
               U is the row echelon form of A.
               C is the transformed identity matrix.
               A_inv is the computed inverse of A.
    """
    n = A.shape[0]
    A_aug = np.hstack((A, np.eye(n)))  # Create [A | I] augmented matrix

    # Apply Gauss-Jordan elimination
    for i in range(n):
        # Normalize pivot row
        A_aug[i] /= A_aug[i, i]
        # Eliminate column values
        for j in range(n):
            if i != j:
                A_aug[j] -= A_aug[i] * A_aug[j, i]

    U = A_aug[:, :n]  # Extract row echelon form
    C = A_aug[:, n:]  # Extract transformed identity matrix
    A_inv = np.linalg.inv(A)  # Compute A^-1 for verification

    return U, C, A_inv

# Boilerplate code to handle input and output
def main():
    # Read input
    n = int(input().strip())  # Read matrix size
    A = np.array([list(map(float, input().split())) for _ in range(n)])  # Read matrix

    # Perform Gauss-Jordan elimination
    U, C, A_inv = gauss_jordan_inverse(A)

    # Print results
    print("U =")
    for row in U:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nC =")
    for row in C:
        print(" ".join(f"{x:.1f}" for x in row))

    print("\nA^-1 =")
    for row in A_inv:
        print(" ".join(f"{x:.1f}" for x in row))

if __name__ == "__main__":
    main()
