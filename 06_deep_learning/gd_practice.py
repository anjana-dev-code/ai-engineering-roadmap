import numpy as np
from gradient_descent import gradient_descent
from loss import mse


def fit_line(x, y, lr, steps):
    """Fit y_hat = w*x + b by gradient descent on MSE. Returns w, b, losses."""
    w, b = 0.0, 0.0
    losses = []
    for _ in range(steps):
        y_hat = w * x + b
        losses.append(mse(y, y_hat))
        err = y_hat - y
        dw = 2.0 * np.mean(x * err)
        db = 2.0 * np.mean(err)
        w -= lr * dw
        b -= lr * db
    return w, b, losses

if __name__ == "__main__":
    # Part A: L(w) = (w - 7)^2, start w = 2 
    def grad_a(w):
        return 2.0 * (w - 7.0)

    path = gradient_descent(grad_a, w0=2.0, lr=0.3, steps=3)
    print("A, alpha=0.3:", path)
    assert np.allclose(path, [2.0, 5.0, 6.2, 6.68])

    path = gradient_descent(grad_a, w0=2.0, lr=1.0, steps=4)
    print("A, alpha=1.0:", path)
    assert path == [2.0, 12.0, 2.0, 12.0, 2.0]

    path = gradient_descent(grad_a, w0=2.0, lr=0.5, steps=2)
    print("A, alpha=0.5:", path)
    assert path == [2.0, 7.0, 7.0]

    path = gradient_descent(grad_a, w0=2.0, lr=1.2, steps=4)
    print("A, alpha=1.2:", [round(p, 2) for p in path])
    assert abs(path[-1] - 7.0) > abs(path[0] - 7.0)