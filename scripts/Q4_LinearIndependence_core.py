import numpy as np

def check_linear_independence(matrix):
    """
    Check if the vectors (columns) in the given matrix are linearly independent.
    Returns True if they are linearly independent, False otherwise.
    """
    # Students will implement the logic here
    # Hint: Use the rank of the matrix to determine linear independence
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(matrix[0])

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
    # Check for Linear Independence
    result = check_linear_independence(A)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()


# Write a Python function check_linear_independence(matrix) that takes a matrix (represented as a list of lists) as input and returns True if the vectors (columns) in the matrix are linearly independent, and False otherwise.

# Input Format:

# The input will be a list of lists representing the matrix, where each inner list is a row of the matrix.

# The matrix may not necessarily be square.

# Output Format:

# The output should be a boolean value: True if the vectors are linearly independent, and False otherwise.


# Test case 1

# 1 0 0
# 0 1 0
# 0 0 1

# True

# Test case 2

# 1 2 3
# 4 5 6
# 7 8 9

# False

# Test case 3

# 1 2
# 3 4 
# 5 6

# True

# Test case 4

# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

# False