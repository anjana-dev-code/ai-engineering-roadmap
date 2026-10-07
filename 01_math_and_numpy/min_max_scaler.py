"""
PROBLEM:
Scale a 1D array of numerical readings to a normalized [0, 1] range using
the Min-Max normalization formula.

Formula:
    X_scaled = (X - min) / (max - min)


"""

import numpy as np


def min_max_scale(values):
  
  min_val = np.min(values)
  max_val = np.max(values)

  range_span = max_val - min_val
  if range_span == 0:
    return np.zeros_like(values)
    
  scaled_values = (values - min_val) / range_span

  return scaled_values


if __name__ == "__main__":
  raw_readings = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
  scaled = min_max_scale(raw_readings)
  print("Original:", raw_readings)
  print("Scaled:  ", scaled)