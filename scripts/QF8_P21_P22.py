'''
Problem Statement

Title: Matrix Rank and Nullity

Problem Description:
Given a matrix A of size m×n, your task is to compute the rank and nullity of the matrix. The rank of a matrix is the dimension of its column space (the number of linearly independent columns), and the nullity is the dimension of its null space (the number of free variables in the solution to Ax=0). The rank-nullity theorem states that for any matrix AA, the sum of the rank and nullity equals the number of columns in A.

Input Format:
•	The first line contains two integers m and n, representing the number of rows and columns of the matrix.
•	The next m lines contain n integers each, representing the elements of the matrix.
Output Format:
•	Print two integers: the rank of the matrix followed by the nullity of the matrix.

Constraints:
•	1 ≤ m,n ≤ 100
•	Each element of the matrix is an integer such that -1000 ≤ A[i][j ]≤ 1000.

Example:

Input:
3 4
1 2 1 2
1 2 1 3
3 6 3 7

Output:
2 2
Explanation:
•	The rank of the matrix is 2, as there are 2 linearly independent columns.
•	The nullity is 4 - 2 = 2, as the null space has dimension 2.
•	This satisfies the rank-nullity theorem: rank + nullity = 2 + 2 = 4, which is the number of columns in the matrix.

Sample Input 1:
2 2
1 0
0 1

Sample Output 1:
2 0

Sample Input 2:
3 3
1 2 3
4 5 6
7 8 9

Sample Output 2:
2 1

Sample Input 3:
1 3
0 0 0

Sample Output 3:
0 3

'''


import numpy as np
from numpy.linalg import matrix_rank

def compute_rank_and_nullity(A):
    """
    Computes the rank and nullity of a matrix A.
    """
    m, n = A.shape
    rank = matrix_rank(A)
    nullity = n - rank  # Rank-Nullity Theorem
    return rank, nullity

# Read input
m, n = map(int, input().split())
A = []
for _ in range(m):
    row = list(map(int, input().split()))
    A.append(row)

# Convert to numpy array
A = np.array(A)

# Compute rank and nullity
rank, nullity = compute_rank_and_nullity(A)

# Print the result
print(rank, nullity)