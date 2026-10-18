"""
PROBLEM:
Implement Linear Regression via Gradient Descent from scratch using NumPy.
Level 1: Generate synthetic data with y = 3x + 5 + noise.
Level 2: Write training loop updating w and b using MSE gradients.
"""

import matplotlib.pyplot as plt
import numpy as np

# Level 1: Generate fake data (y = 3x + 5 + noise)
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3.0 * X + 5.0 + np.random.randn(100, 1) * 2.0

# Level 2: Initialize parameters and hyperparameters
w = np.zeros((1, 1))
b = 0.0
lr = 0.01
epochs = 200
n_samples = len(X)

loss_history = []

# Gradient Descent Training Loop
for epoch in range(epochs):
  # Forward pass: predict y
  y_pred = X @ w + b

  # Calculate error
  error = y_pred - y

  # Compute Mean Squared Error (MSE) loss
  loss = (1 / n_samples) * np.sum(error**2)
  loss_history.append(loss)

  # Compute gradients
  dw = (2 / n_samples) * (X.T @ error)
  db = (2 / n_samples) * np.sum(error)

  # Update parameters (step downhill)
  w -= lr * dw
  b -= lr * db

print(f"Trained Weight (w): {w.item():.4f} (Target: ~3.0)")
print(f"Trained Bias (b):    {b:.4f} (Target: ~5.0)")

# Plot and save loss history
plt.plot(loss_history)
plt.title("Gradient Descent Loss Curve")
plt.xlabel("Epochs")
plt.ylabel("MSE Loss")
plt.savefig("03_classical_ml/linreg_loss_curve.png")
print("Loss curve saved successfully!")