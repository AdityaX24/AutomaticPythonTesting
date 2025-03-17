"""
Implement a Python function find_basis_and_dimension(matrix) that finds the Basis and Dimension of a 
given matrix A. 
The function should return basis vectors and dimension of the matrix.

Input:
matrix: A matrix of size m * n.

Output:
Return a tuple (basis, dimension)

Sample Test Case 1
Input:

1 0 0 
0 1 0
0 0 1

Expected Output:

Basis vectors for the column space:
[1.0, 0.0, 0.0]
[0.0, 1.0, 0.0]
[0.0, 0.0, 1.0]
Dimension of the column space: 3

Sample Test Case 2
Input:

1 2
3 4
5 6
7 8

Expected Output:

Basis vectors for the column space:
[1.0, 2.0]
[3.0, 4.0]
[5.0, 6.0]
[7.0, 8.0]
Dimension of the column space: 2

Note: You should only write your logic in find_basis_and_dimension method and return the required answers. 
Proper printing format will be taken care of by the boilerplate. 

DO NOT CHANGE THE BOILERPLATE.

"""

import numpy as np

def find_basis_and_dimension(matrix):
    """
    Find the basis and dimension of the column space of the given matrix.
    Returns a tuple containing:
    - A list of basis vectors (as lists) from the original matrix columns.
    - The dimension of the column space (an integer).
    """

    #Implement your code here
    rank = np.linalg.matrix_rank(matrix)
    
    # Extract the first 'rank' columns of Q as the basis
    basis = matrix[:, :rank].tolist()
    dimension = rank
    
    return basis, dimension

# Boilerplate code to handle input and output
def main():
    A = []
    while True:
        try:
            row = input().strip()
            if row:
                A.append(list(map(float, row.split())))
            else:
                break
        except EOFError:
            break
    A=np.array(A)
    basis, dimension = find_basis_and_dimension(A)
    print(f"Basis vectors for the column space:")
    for vec in basis:
        print(vec)
    print(f"Dimension of the column space: {dimension}")

if __name__ == "__main__":
    main()
