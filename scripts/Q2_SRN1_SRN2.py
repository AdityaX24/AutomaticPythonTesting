"""
Smart City Traffic Flow Optimization

A futuristic city is rapidly expanding its transportation infrastructure. 
At several critical intersections, traffic flow sensors record vehicle counts throughout the day. 
However, the raw sensor data is plagued by a couple of challenges:

1. High Dimensionality & Correlation: The measurements are taken across many different times and conditions. 
Due to overlapping rush hours, event-driven spikes, and common weather conditions, the data from different sensors tend to be highly correlated.

2. Noise & Redundancy: Although the sensors collect a large volume of data, a significant part of this 
information is redundant, making it harder to extract truly meaningful trends.

3. Near-Singular Behavior: When the data is used to model the behavior of traffic adjustments, 
the resulting mathematical system can be nearly singular, meaning that small errors in the data might 
lead to unstable or non-unique solutions if not handled properly.


Your city's transportation engineers have proposed a model where the impact of sensor measurements is 
condensed into a set of transformation equations. These equations are then used to generate 
adjustments (such as modifying the timing of traffic signals) that aim to streamline traffic flow and reduce congestion.


**The Problem**

Objective:
Using the sensor data, your goal is to identify the essential features of the traffic patterns, construct a 
linear system that models the relationship between the data and the optimal traffic adjustments, and then compute those adjustments. 
Your solution must also verify that the adjustments make sense by checking the consistency of the model.

What You Need to Do:

1. Transform the High-Dimensional Data:
The sensor data contains many measurements, some of which are redundant and noisy. 
Your first task is to reduce this data to the core features that effectively represent the overall patterns in traffic flow. 
Think about how you might extract these key features from the raw measurements.

2. Formulate a System of Equations:
Once you have the transformed data, use it to construct a system of linear equations of the form:
Ax = B

Here, the matrix A and the vector b should be built from the transformed data along with an additional parameter 
vector provided by the city planners. The relationship between the sensor data and the adjustments should mimic a realistic 
scenario where optimal traffic signal changes depend on a weighted contribution from various features.

3. Solve the System Robustly:
Solving the system for the adjustment vector x might be straightforward; however, be aware that your constructed system can 
sometimes be nearly singular. In such cases, a direct solution might be unstable. You need to recognize these situations and 
apply a strategy to compute x in a robust manner.

4. Evaluate the Solution:
After calculating x, it is essential to assess your solution by verifying that the computed adjustments indeed produce the 
desired outcome on the model. Evaluate the quality of the solution by calculating how well the proposed adjustments satisfy the original system.

5. Document your understanding and approach of your question with proper explanation and submit as a pdf file. 

Important Notes
Data Interpretation: The sensor data is provided as a matrix where each row represents an intersection's series of measurements. 
You need to uncover the underlying structure of this data.

Constructing the Model: The manner in which you construct A and b should be rooted in the patterns you find in the data and the parameters 
given by the planners.

Robustness Considerations: Since the data may lead to near-singularity, careful attention is required when solving the system to avoid unstable computations.

------------------------------------------------
TEST CASE 1

INPUT:
    10 12 14
    20 22 24
    30 32 34

    1

OUTPUT:
    Transformed Data:
    [[-17.32]
    [  0.  ]
    [ 17.32]]
    Matrix A:
    [[600.]]
    Vector b:
    [600.]
    Solution x:
    [1.]
    Residual norm:
    0.00


------------------------------------------------
TEST CASE 2

INPUT:
    1 2 3
    4 5 6
    7 8 10
    9 10 13

    0.5

OUTPUT:
    Transformed Data:
    [[-7.81]
    [-2.65]
    [ 3.18]
    [ 7.29]]
    Matrix A:
    [[131.26]]
    Vector b:
    [65.63]
    Solution x:
    [0.5]
    Residual norm:
    0.00

NOTE:  DO NOT CHANGE THE BOILERPLATE. Only Fill in the methods definition. Do not import any models other than the ones already imported.


"""

import numpy as np
from scipy.linalg import lu_factor, lu_solve

def transform_data(X, threshold=0.95):
    """
    Reduce the dimensionality of the high-dimensional sensor data X.
    
    Parameters:
    - X: np.ndarray; a matrix where each row corresponds to an intersection's measurements.
    - threshold: float; the cumulative contribution to the total variance to retain.
    
    Returns:
    - X_reduced: np.ndarray; the transformed data capturing the essential features.
    """

    X_centered = X - np.mean(X, axis=0)
    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
    explained_variance = (S**2) / np.sum(S**2)
    cumulative_variance = np.cumsum(explained_variance)
    num_components = np.searchsorted(cumulative_variance, threshold) + 1

    X_reduced = np.dot(U, np.diag(S))[:, :num_components]
    return X_reduced

def construct_equations(transformed_data, params):
    """
    Construct the linear system A*x = b based on the transformed data and a parameter vector.
    
    Parameters:
    - transformed_data: np.ndarray; the output from transform_data.
    - params: np.ndarray; a vector of parameters whose length equals the effective dimension (number of columns of transformed_data).
    
    Returns:
    - A: np.ndarray; the coefficient matrix.
    - b: np.ndarray; the right-hand side vector.

    """
    A = np.dot(transformed_data.T, transformed_data)
    b = np.dot(transformed_data.T, np.dot(transformed_data, params))
    return A, b

def compute_adjustments(A, b, tol=1e-10):
    """
    Solve the system A*x = b to compute the adjustments x.
    
    If A is ill-conditioned, handle accordingly.
    """
    cond_A = np.linalg.cond(A)
    if cond_A > 1/tol:
        x = np.dot(np.linalg.pinv(A), b)
    else:
        lu, piv = lu_factor(A)
        x = lu_solve((lu, piv), b)
    return x

def evaluate_solution(A, x, b):
    """
    Compute the Euclidean norm ||Ax - b||_2.
    """
    residual = np.dot(A, x) - b
    return np.linalg.norm(residual, 2)

def main():
    ##DO NOT CHANGE CODE HERE
    sensor_data_list = []
    while True:
        try:
            row = input().strip()
            if row:
                sensor_data_list.append(list(map(float, row.split())))
            else:
                break 
        except EOFError:
            break
    sensor_data = np.array(sensor_data_list)
    
    param_line = ""
    while True:
        try:
            param_line = input().strip()
            if param_line:
                break
        except EOFError:
            break
    params = np.array(list(map(float, param_line.split())))
    
    transformed = transform_data(sensor_data)
    A_mat, b_vec = construct_equations(transformed, params)
    x = compute_adjustments(A_mat, b_vec)
    residual = evaluate_solution(A_mat, x, b_vec)
    
    print("Transformed Data:")
    print(np.array2string(transformed, precision=2, suppress_small=True))
    print("Matrix A:")
    print(np.array2string(A_mat, precision=2, suppress_small=True))
    print("Vector b:")
    print(np.array2string(b_vec, precision=2, suppress_small=True))
    print("Solution x:")
    print(np.array2string(x, precision=2, suppress_small=True))
    print("Residual norm:")
    print(f"{residual:.2f}")

if __name__ == "__main__":
    main()


"""
TEST CASE 3

INPUT:
    1 2 3 4
    2 4 6 8
    3 6 9 12
    4 7 10 13
    5 8 11 14
    6 9 12 15

    1

OUTPUT:
    Transformed Data:
    [[-10.06]
    [ -4.63]
    [  0.8 ]
    [  2.71]
    [  4.63]
    [  6.55]]
    Matrix A:
    [[195.05]]
    Vector b:
    [195.05]
    Solution x:
    [1.]
    Residual norm:
    0.00    


TEST CASE 4

INPUT:
    1 2 3 4
    4 3 2 1
    5 6 7 8
    8 7 6 5
    10 11 12 13

    0.5 1.0

OUTPUT:
    Transformed Data:
    [[-6.52  2.62]
    [-7.08 -1.82]
    [ 1.41  1.63]
    [ 0.86 -2.81]
    [11.34  0.38]]
    Matrix A:
    [[223.94  -0.  ]
    [ -0.    20.86]]
    Vector b:
    [111.97  20.86]
    Solution x:
    [0.5 1. ]
    Residual norm:
    0.00

    
TEST CASE 5

INPUT:
    2 3 1 0
    4 1 5 2
    3 6 7 8
    1 2 3 4
    5 7 9 6

    0.3 0.7 -0.2

OUTPUT:
    Transformed Data:
    [[-5.46 -0.08  1.96]
    [-2.28 -2.15 -1.73]
    [ 4.65  1.77 -0.13]
    [-2.49  2.01 -0.98]
    [ 5.57 -1.54  0.88]]
    Matrix A:
    [[93.85  0.    0.  ]
    [ 0.   14.14 -0.  ]
    [ 0.   -0.    8.62]]
    Vector b:
    [28.16  9.9  -1.72]
    Solution x:
    [ 0.3  0.7 -0.2]
    Residual norm:
    0.00
    
"""