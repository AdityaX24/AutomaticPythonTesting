'''
Fundamental Subspace Dimensions
Problem Description
Given a matrix A of size m×n, determine the dimensions of two of the four fundamental subspaces associated with the matrix: the column space C(A) and the null space N(A).
Concept Used
This problem tests understanding of the fundamental subspaces in linear algebra, specifically:

The column space C(A): the span of the columns of matrix A
The null space N(A): the set of all vectors x such that Ax = 0
The rank-nullity theorem, which states that dim(C(A)) + dim(N(A)) = n for an m×n matrix

Input Format

The first line contains two integers m and n (1 ≤ m, n ≤ 100), the number of rows and columns of matrix A.
The next m lines contain n space-separated numbers each, representing the entries of the matrix A.

Output Format
Two space-separated integers representing:

The dimension of the column space C(A)
The dimension of the null space N(A)

Constraints

1 ≤ m, n ≤ 100
Matrix entries will be between -10^6 and 10^6
All calculations will result in integer dimensions

Sample Input 1
3 4
1 2 1 2
1 2 1 3
3 6 3 7

Sample Output 1
2 2

Sample Input 2
3 3
1 0 0
0 1 0
0 0 1

Sample Output 2
3 0


'''

import numpy as np

def find_fundamental_subspaces(matrix):
    """
    Find the dimensions of column space and null space of a given matrix.
    
    Args:
        matrix: A 2D numpy array
    
    Returns:
        A dictionary with the dimensions of column space and null space
    """
    A = np.array(matrix, dtype=float)
    
    # Compute the rank of the matrix
    rank = np.linalg.matrix_rank(A)
    
    # Get matrix shape
    m, n = A.shape
    
    # Calculate dimensions
    column_space_dim = rank
    null_space_dim = n - rank
    
    return {
        'column_space_dim': column_space_dim,
        'null_space_dim': null_space_dim
    }

if __name__ == "__main__":
    # Get matrix dimensions from user
    m, n = map(int, input().strip().split())
    
    # Get matrix entries
    matrix = []
    for i in range(m):
        row = list(map(float, input().strip().split()))
        if len(row) != n:
            print(f"Error: Expected {n} elements in row {i+1}, but got {len(row)}")
            exit(1)
        matrix.append(row)
    
    result = find_fundamental_subspaces(matrix)
    
    print(result['column_space_dim'], result['null_space_dim'])