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

    # print("CHECK",P@L@U)

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