import numpy as np


def standardize(X: np.ndarray):

  mean = np.mean(X, axis=0)
  std = np.std(X, axis=0)
  return (X - mean) / std


def covariance(X: np.ndarray) -> np.ndarray:

  n_samples = X.shape[0]

  X_centered = X - np.mean(X, axis=0)
  
  return (X_centered.T @ X_centered) / (n_samples - 1)



if __name__ == "__main__":
  # Generate test data
  rng = np.random.default_rng(42)
  X = rng.normal(loc=[5, 50], scale=[1, 10], size=(200, 2))

  # Test standardize
  X_std = standardize(X)
  print("Standardized Means (should be ~0):", np.round(np.mean(X_std, axis=0), 10))
  print("Standardized Stds (should be 1):  ", np.std(X_std, axis=0))

  # Test covariance from scratch vs np.cov
  my_cov = covariance(X)
  numpy_cov = np.cov(X, rowvar=False)

  print("\nCustom Covariance Matrix:\n", my_cov)
  print("NumPy Covariance Matrix:\n", numpy_cov)

  # Prove it works using np.allclose
  is_close = np.allclose(my_cov, numpy_cov)
  print("\nResults match using np.allclose:", is_close)