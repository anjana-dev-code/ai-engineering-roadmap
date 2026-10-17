"""
PROBLEM: Implement k-NN from scratch in NumPy.
Level 1: Vectorized Euclidean distance calculation.
"""

import numpy as np


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
  """Computes the L2 Euclidean distance between two vectors with no loops."""
  return np.sqrt(np.sum((a - b) ** 2))

def predict_one(
    X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int
) -> int:
  """Computes distances from x_new to all training points, takes the k smallest,

  and returns the majority label.
  """
  # Compute Euclidean distance to all training samples vectorially
  distances = np.sqrt(np.sum((X_train - x_new) ** 2, axis=1))

  # Get indices of the k smallest distances
  k_indices = np.argsort(distances)[:k]

  # Fetch their labels
  k_nearest_labels = y_train[k_indices]

  # Return the most common label (majority vote)
  return np.bincount(k_nearest_labels).argmax()
  