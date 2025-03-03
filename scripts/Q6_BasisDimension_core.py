import numpy as np
import scipy

def find_basis_and_dimension(matrix):
    """
    Find the basis and dimension of the column space of the given matrix.
    Returns a tuple containing:
    - A list of basis vectors (as lists) from the original matrix columns.
    - The dimension of the column space (an integer).
    """
    # Students will implement the logic here

    rank = np.linalg.matrix_rank(matrix)
    
    # Extract the first 'rank' columns of Q as the basis
    basis = matrix[:, :rank].tolist()
    dimension = rank
    
    return basis, dimension

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
    
    basis, dimension = find_basis_and_dimension(A)
    print(f"Basis vectors for the column space:")
    for vec in basis:
        print(vec)
    print(f"Dimension of the column space: {dimension}")

if __name__ == "__main__":
    main()


# Test case 1

# 1 0 0 
# 0 1 0
# 0 0 1

# Basis vectors for the column space:
# [1.0, 0.0, 0.0]
# [0.0, 1.0, 0.0]
# [0.0, 0.0, 1.0]
# Dimension of the column space: 3

# Test case 2

# 1 2
# 3 4
# 5 6
# 7 8

# Basis vectors for the column space:
# [1.0, 2.0]
# [3.0, 4.0]
# [5.0, 6.0]
# [7.0, 8.0]
# Dimension of the column space: 2

# Test case 3

# 1 2 3
# 4 5 6
# 7 8 9

# Basis vectors for the column space:
# [1.0, 2.0]
# [4.0, 5.0]
# [7.0, 8.0]
# Dimension of the column space: 2

# Test case 4

# 1 0 1 2
# 0 1 1 3
# 0 0 1 4
# 0 0 0 0

# Basis vectors for the column space:
# [1.0, 0.0, 1.0]
# [0.0, 1.0, 1.0]
# [0.0, 0.0, 1.0]
# [0.0, 0.0, 0.0]
# Dimension of the column space: 3


# Test case 5

# 3 5 9 5
# 3 5 4 0
# 2 5 3 8
# 4 5 7 1

# Basis vectors for the column space:
# [3.0, 5.0, 9.0, 5.0]
# [3.0, 5.0, 4.0, 0.0]
# [2.0, 5.0, 3.0, 8.0]
# [4.0, 5.0, 7.0, 1.0]
# Dimension of the column space: 4
