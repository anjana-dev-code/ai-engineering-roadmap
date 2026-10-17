"""
PROBLEM: Implement k-NN from scratch in NumPy.
Level 1: Vectorized Euclidean distance calculation.
"""

import numpy as np


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
  """Computes the L2 Euclidean distance between two vectors with no loops."""
  return np.sqrt(np.sum((a - b) ** 2))