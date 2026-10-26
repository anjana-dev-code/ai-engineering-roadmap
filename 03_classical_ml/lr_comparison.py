import matplotlib.pyplot as plt
import numpy as np

# Fake data: y = 3x + 5 + noise
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3.0 * X + 5.0 + np.random.randn(100, 1) * 2.0


def train(lr, epochs):
    """Run gradient descent and return w, b and the loss at every epoch."""
    w = np.zeros((1, 1))
    b = 0.0
    n = len(X)
    history = []
    for _ in range(epochs):
        error = X @ w + b - y
        history.append(np.mean(error ** 2))
        w -= lr * (2 / n) * (X.T @ error)
        b -= lr * (2 / n) * np.sum(error)
    return w.item(), b, history


settings = {
    "too small (lr=0.0001)": 0.0001,
    "just right (lr=0.01)": 0.01,
    "too big (lr=1.5)": 1.5,
}

plt.figure(figsize=(8, 5))
for label, lr in settings.items():
    w, b, history = train(lr, epochs=200)
    print(f"{label}: w={w:.3f}, b={b:.3f}")
    plt.plot(history, label=label)

plt.yscale("log")  # log scale so the exploding curve doesn't hide the others
plt.title("Gradient descent: effect of learning rate")
plt.xlabel("Epoch")
plt.ylabel("MSE loss (log scale)")
plt.legend()
plt.savefig("03_classical_ml/lr_comparison.png")