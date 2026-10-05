"""
PROBLEM:
Apply a 5-point curve to an array of exam scores, cap the scores at 100,
and return only the scores that are still failing (< 50).

Example:
    Input:   np.array([45, 62, 38, 75, 90, 52, 28, 84])
    Curved:  [50, 67, 43, 80, 95, 57, 33, 89]
    Failing: [43, 33]
"""

import numpy as np


def analyze_grades(scores: np.ndarray) -> np.ndarray:
  # Step 1: Add 5 points to all scores
  curved_scores = scores + 5

  # Step 2: Cap values between 0 and 100
  capped_scores = np.clip(curved_scores, 0, 100)

  # Step 3: Ask the question (< 50) and filter
  failing_mask = capped_scores < 50
  failing_scores = capped_scores[failing_mask]

  return failing_scores


# --- Quick Test ---
if __name__ == "__main__":
  scores = np.array([45, 62, 38, 75, 90, 52, 28, 84])
  result = analyze_grades(scores)
  print("Failing scores after curve:", result) 