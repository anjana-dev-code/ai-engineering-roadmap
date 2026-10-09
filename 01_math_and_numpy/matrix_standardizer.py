"""
PROBLEM:
Standardize a 2D feature matrix column-by-column (Z-score normalization)
with defensive handling for zero-variance (constant) columns.

Formula:
    Z = (X - mean) / std

Edge Case:
    If std == 0, set standardized values to 0.0 to prevent division by zero.

Example Input:
    [[10.0, 5.0, 100.0],
     [20.0, 5.0, 200.0],
     [30.0, 5.0, 300.0]]
"""

import numpy as np 

def standardize_features(matrix):
    # Compute mean and std down each column (axis=0)
    means = np.mean(matrix, axis = 0)
    stds = np.std(matrix, axis = 0)

    # Prevent division by zero on constant columns
    safe_stds = np.where(stds == 0, 1.0, stds)

    # Vectorized broadcast subtraction and division
    standardized_matrix = (matrix - means) / safe_stds

    return standardized_matrix

if __name__ == "__main__":
    raw_data = np.array([
        [10.0, 5.0, 100.0],
        [20.0, 5.0, 200.0],
        [30.0, 5.0, 300.0]
    ])

    result = standardize_features(raw_data)
    print("Original matrix ( column 2 is constant):\n", raw_data)
    print("\nStandardized Matrix (Safe 0.0 for column 2):\n", np.round(result, 2))
