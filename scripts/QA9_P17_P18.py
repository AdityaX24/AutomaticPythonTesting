import numpy as np

def check_transpose(A, B):
    """
    Check if matrix B is the transpose of matrix A.
    
    Args:
        A (numpy.ndarray): First matrix
        B (numpy.ndarray): Second matrix
        
    Returns:
        bool: True if B is the transpose of A, False otherwise
    """
    return np.array_equal(B, A.T)

def check_invertibility(A):
    """
    Check if matrix A is invertible.
    
    Args:
        A (numpy.ndarray): Matrix to check
        
    Returns:
        bool: True if A is invertible, False otherwise
    """
    det_A = np.linalg.det(A)
    return not np.isclose(det_A, 0)

def recover_original_signals(A, received_signals):
    """
    Recover original signals using the inverse of matrix A.
    
    Args:
        A (numpy.ndarray): Channel matrix
        received_signals (numpy.ndarray): Matrix of received signals
        
    Returns:
        numpy.ndarray: Matrix of original signals
    """
    A_inv = np.linalg.inv(A)
    return np.dot(A_inv, received_signals.T).T

def main():
    # Read matrix size
    n = int(input().strip())
    
    # Read matrix A
    A = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        A.append(row)
    A = np.array(A)
    
    # Read matrix B
    B = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        B.append(row)
    B = np.array(B)
    
    # Read number of received signals
    m = int(input().strip())
    
    # Read received signal vectors
    received_signals = []
    for _ in range(m):
        signal = list(map(int, input().strip().split()))
        received_signals.append(signal)
    received_signals = np.array(received_signals)
    
    # Check if B is the transpose of A
    is_transpose = check_transpose(A, B)
    print("True" if is_transpose else "False")
    
    # Check if A is invertible
    is_invertible = check_invertibility(A)
    print("True" if is_invertible else "False")
    
    # Process received signals only if A is invertible
    if is_invertible:
        # Compute original signals
        original_signals = recover_original_signals(A, received_signals)
        
        # Print original signals
        for signal in original_signals:
            print(" ".join(f"{x:.2f}" for x in signal))

if __name__ == "__main__":
    main()