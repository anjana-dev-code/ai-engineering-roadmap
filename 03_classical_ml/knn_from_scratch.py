"""
PROBLEM:
Implement k-Nearest Neighbors (k-NN) classification entirely from scratch using NumPy.
Compare its accuracy against Scikit-Learn's KNeighborsClassifier on the Iris dataset.

Levels:
    - Level 1: Vectorized Euclidean distance calculation.
    - Level 2: predict_one() using np.argsort() and majority voting.
    - Level 3: predict() batch evaluation on test data.
    - Level 4: Boss comparison matching sklearn accuracy.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
  """Level 1: Compute Euclidean distance between two vectors (no loops)."""
  return np.sqrt(np.sum((a - b) ** 2))


def predict_one(
    X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int
) -> int:
  """Level 2: Compute all distances, find k smallest indices, return majority vote."""
  distances = np.sqrt(np.sum((X_train - x_new) ** 2, axis=1))
  k_indices = np.argsort(distances)[:k]
  k_nearest_labels = y_train[k_indices]
  return np.bincount(k_nearest_labels).argmax()


def predict(
    X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, k: int
) -> np.ndarray:
  """Level 3: Predict labels for an entire test set."""
  return np.array([predict_one(X_train, y_train, x, k) for x in X_test])


# Level 4 (Boss): Benchmark & Comparison ---
if __name__ == "__main__":
  # Load Iris dataset
  iris = load_iris()
  X, y = iris.data, iris.target

  # Split into train and test sets
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.3, random_state=42
  )

  k_value = 5

  # 1. Run our From-Scratch k-NN
  my_preds = predict(X_train, y_train, X_test, k=k_value)
  my_accuracy = accuracy_score(y_test, my_preds)

  # 2. Run Scikit-Learn's KNeighborsClassifier
  skl_model = KNeighborsClassifier(n_neighbors=k_value, metric="euclidean")
  skl_model.fit(X_train, y_train)
  skl_preds = skl_model.predict(X_test)
  skl_accuracy = accuracy_score(y_test, skl_preds)

  print(f"--- k-NN From-Scratch Benchmark (k={k_value}) ---")
  print(f"Our Scratch k-NN Accuracy:   {my_accuracy * 100:.2f}%")
  print(f"Scikit-Learn k-NN Accuracy:  {skl_accuracy * 100:.2f}%")

  # Assert that results match perfectly
  assert np.allclose(
      my_accuracy, skl_accuracy
  ), "Accuracy mismatch between scratch implementation and sklearn."
  print("\nSuccess.Your from-scratch NumPy k-NN matches Scikit-Learn perfectly.")
