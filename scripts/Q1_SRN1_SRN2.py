"""
Customer Behavior Analysis for Retail Optimization

Background:
A retail company has collected data from 10,000 customers, tracking 15 behavioral 
metrics (e.g., monthly spending, product returns, session duration, coupon usage). The team wants to 
identify patterns to group customers into segments for targeted marketing. However, visualizing and 
analyzing 15 dimensions is impractical. They need a method to reduce the data to its most "meaningful" 
components while minimizing information loss.

Problem Statement:
Your task is to design a linear algebra pipeline to:

1. Preprocess the data to ensure numerical stability.
2. Identify the key orthogonal directions in which the data varies the most.
3. Project the data onto a low-dimensional subspace (2-3 dimensions) for visualization.
4. Quantify the error introduced by this approximation.
5. Explain why the chosen subspace preserves the geometric structure of the original data.

Deliverables:

1. A mathematical justification for the number of dimensions retained.
2. An analysis of how the original feature space relates to the reduced subspace.
3. A reconstruction of the original data from the reduced subspace and its error.

Constraints:

1. Use only fundamental linear algebra operations (no prebuilt ML libraries like sklearn).
2. Address edge cases (e.g., linearly dependent features).


------------------------------------------------
TEST CASE 1

INPUT:
    5 0
    5 0
    5 0

OUTPUT:
    Centered data:
    [[0. 0.]
    [0. 0.]
    [0. 0.]]

    Top directions:
    No directions (all features are constant)

    Reduced data:
    No reduced data (all features are constant)

    Reconstructed data:
    [0. 0.]

    Reconstruction error: 8.66

------------------------------------------------
TEST CASE 2

INPUT:
    2 4 6
    1 2 3 
    3 6 9

OUTPUT:
    Centered data:
    [[ 0.  0.  0.]
    [-1. -2. -3.]
    [ 1.  2.  3.]]

    Top directions:
    -0.27 -0.53 -0.80

    Reduced data:
    0.00
    3.74
    -3.74

    Reconstructed data:
    [[2. 4. 6.]
    [1. 2. 3.]
    [3. 6. 9.]]

    Reconstruction error: 0.00
"""


import numpy as np
import sys

class DimensionalityReducer:
    def __init__(self):
        self.mean = None
        self.basis = None  # Principal components (rows)
        self.variance_explained = None

    def preprocess(self, X):
        self.mean = np.mean(X, axis=0)
        return X - self.mean

    def compute_key_directions(self, X_centered):
        U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
        self.basis = Vt
        explained_variance = (S ** 2) / (X_centered.shape[0] - 1)
        total_variance = explained_variance.sum()
        if total_variance == 0:
            self.variance_explained = np.zeros_like(explained_variance)
        else:
            self.variance_explained = explained_variance / total_variance

    def reduce_dimensions(self, X_centered, k):
        return X_centered @ self.basis[:k].T

    def reconstruct(self, X_reduced):
        if X_reduced.size == 0:
            return np.empty_like(self.mean)
        return X_reduced @ self.basis[:X_reduced.shape[1]] + self.mean

    def evaluate_error(self, X_original, X_reconstructed):
        return np.linalg.norm(X_original - X_reconstructed, 'fro')

def main():
    # Read input matrix from stdin
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
    A = np.array(A)
    
    reducer = DimensionalityReducer()
    
    # Step 1: Preprocess (center the data)
    try:
        X_centered = reducer.preprocess(A)
    except Exception as e:
        print("Error during preprocessing:", e)
        return
    
    print("Centered data:")
    print(X_centered)
    
    # Step 2: Compute key directions (SVD)
    try:
        reducer.compute_key_directions(X_centered)
    except Exception as e:
        print("Error during key directions computation:", e)
        return
    
    # Determine k for 95% variance
    cumulative_variance = np.cumsum(reducer.variance_explained)
    k = np.argmax(cumulative_variance >= 0.95) + 1
    if k == 0:  # Handle case where no component meets the threshold
        k = len(reducer.variance_explained)
    
    # Handle case when all variances are zero (e.g., constant features)
    if np.allclose(X_centered, 0):
        k = 0
    
    # Step 3: Reduce dimensions
    try:
        if k > 0:
            X_reduced = reducer.reduce_dimensions(X_centered, k)
        else:
            X_reduced = np.zeros((X_centered.shape[0], 0))
    except Exception as e:
        print("Error during dimensionality reduction:", e)
        return
    
    print("\nTop directions:")
    if k > 0:
        for direction in reducer.basis[:k]:
            print(" ".join(f"{x:.2f}" for x in direction))
    else:
        print("No directions (all features are constant)")
    
    print("\nReduced data:")
    if X_reduced.size > 0:
        for row in X_reduced:
            print(" ".join(f"{x:.2f}" for x in row))
    else:
        print("No reduced data (all features are constant)")
    
    # Step 4: Reconstruct data
    try:
        X_reconstructed = reducer.reconstruct(X_reduced)
    except Exception as e:
        print("Error during reconstruction:", e)
        return
    
    print("\nReconstructed data:")
    print(X_reconstructed)
    
    # Step 5: Evaluate reconstruction error
    try:
        error = reducer.evaluate_error(A, X_reconstructed)
    except Exception as e:
        print("Error during error evaluation:", e)
        return
    
    print(f"\nReconstruction error: {error:.2f}")

if __name__ == "__main__":
    main()



"""
TEST CASE 3

INPUT:
    3 0 0 
    0 4 0
    0 0 5 

OUTPUT:
    Centered data:
    [[ 2.         -1.33333333 -1.66666667]
    [-1.          2.66666667 -1.66666667]
    [-1.         -1.33333333  3.33333333]]

    Top directions:
    -0.16 -0.48 0.86
    0.67 -0.69 -0.26

    Reduced data:
    -1.11 2.71
    -2.57 -2.07
    3.67 -0.63

    Reconstructed data:
    [[3.00000000e+00 6.66133815e-16 8.88178420e-16]
    [7.77156117e-16 4.00000000e+00 8.88178420e-16]
    [5.55111512e-16 6.66133815e-16 5.00000000e+00]]

    Reconstruction error: 0.00


TEST CASE 4

INPUT:    
    1.2 3.4 0.5
    -0.3 2.1 1.8
    2.7 -1.5 0.2

OUTPUT:
    Centered data:
    [[ 0.          2.06666667 -0.33333333]
    [-1.5         0.76666667  0.96666667]
    [ 1.5        -2.83333333 -0.63333333]]

    Top directions:
    -0.45 0.87 0.18
    -0.68 -0.47 0.57

    Reduced data:
    1.75 -1.15
    1.52 1.21
    -3.27 -0.05

    Reconstructed data:
    [[ 1.2  3.4  0.5]
    [-0.3  2.1  1.8]
    [ 2.7 -1.5  0.2]]

    Reconstruction error: 0.00

TEST CASE 5

INPUT:
    1.0 2.1 0.9
    2.0 4.0 1.8
    3.0 6.1 2.9
    4.0 8.0 4.1
    5.0 10.2 5.0

OUTPUT:
    Centered data:
    [[-2.   -3.98 -2.04]
    [-1.   -2.08 -1.14]
    [ 0.    0.02 -0.04]
    [ 1.    1.92  1.16]
    [ 2.    4.12  2.06]]

    Top directions:
    0.40 0.81 0.42

    Reduced data:
    -4.90
    -2.57
    -0.00
    2.45
    5.02

    Reconstructed data:
    [[ 1.03031991  2.09990239  0.87131891]
    [ 1.9653891   3.9893801   1.85338699]
    [ 2.99974187  6.0794784   2.93972889]
    [ 3.9857435   8.07187441  3.97528941]
    [ 5.01880562 10.1593647   5.06027579]]

    Reconstruction error: 0.19

"""