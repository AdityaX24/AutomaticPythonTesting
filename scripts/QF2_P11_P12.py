"""
Write a Python function check_linear_independence(matrix) that takes a 
matrix (represented as a list of lists) as input and returns True if 
the vectors (columns) in the matrix are linearly independent, and False otherwise.

Input:
The input will be a list of lists representing the matrix, where each inner list is a row of the matrix.
Note: The matrix may not necessarily be square.

Output:
The output should be a boolean value: True if the vectors are linearly independent, and False otherwise.

Sample Test Case 1
Input:

1 0 0
0 1 0
0 0 1

Expected Output:

True

Sample Test Case 2
Input:

1 2
3 4 
5 6

Expected Output:

True

Note: You should only write your logic in check_linear_independence method and return the required answers. 
Proper printing format will be taken care of by the boilerplate. 

DO NOT CHANGE THE BOILERPLATE.

"""

import numpy as np

def check_linear_independence(matrix):
    """
    Check if the vectors (columns) in the given matrix are linearly independent.
    Returns True if they are linearly independent, False otherwise.
    """

    #Implement your code here
    rank = np.linalg.matrix_rank(matrix)
    is_linearly_independent = (rank == len(matrix[0]))

    return is_linearly_independent

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
    result = check_linear_independence(A)
    print(result)

if __name__ == "__main__":
    main()