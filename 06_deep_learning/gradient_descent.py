"""
06_deep_learning/gradient_descent.py
Step 1: Core 1D Gradient Descent Engine and verification on (w - 3)^2.
"""
import numpy as np


def gradient_descent(grad_fn, w0, lr, steps):
    w = float(w0)
    path = [w]
    for _ in range(steps):
        w = w - lr * grad_fn(w)
        path.append(w)
    return path

def compute_mse(y_pred, y_true):
    return float(np.mean((y_pred - y_true) ** 2))

if __name__ == "__main__":
    # Test on f(w) = (w - 3)^2, where f'(w) = 2 * (w - 3)
    grad_quad = lambda w: 2.0 * (w - 3.0)

    # 3 steps from w=0 with lr=0.1
    path_3 = gradient_descent(grad_quad, w0=0.0, lr=0.1, steps=3)
    print("Path after 3 steps:", [round(x, 4) for x in path_3])
    # Step 0: 0.0 -> Step 1: 0.6 -> Step 2: 1.08 -> Step 3: 1.464
    assert np.isclose(path_3[3], 1.464), f"Expected 1.464, got {path_3[3]}"

    # 100 steps: should settle right at the minimum w = 3
    path_100 = gradient_descent(grad_quad, w0=0.0, lr=0.1, steps=100)
    assert abs(path_100[-1] - 3.0) < 1e-3, f"Expected ~3.0, got {path_100[-1]}"

    print("Commit 1 tests passed")

    lr_paper = (1.0 - (0.5) ** (1 / 3)) / 2.0
    paper_path = gradient_descent(grad_quad, w0=6.0, lr=lr_paper, steps=3)
    assert np.isclose(paper_path[3], 4.5), f"Expected 4.5, got {paper_path[3]}"

    # Prediction for alpha = 1: it will bounce indefinitely between 0 and 6
    path_bounce = gradient_descent(grad_quad, w0=0.0, lr=1.0, steps=6)
    print("\nPath with alpha=1.0 (prediction confirmed):", path_bounce)
    assert path_bounce == [0.0, 6.0, 0.0, 6.0, 0.0, 6.0, 0.0]

    print("Commit 2 tests passed")

    lrs = [0.001, 0.1, 0.9, 1.0, 1.1]
    print("\nLearning Rate Experiment (20 steps)")
    for lr in lrs:
        path = gradient_descent(grad_quad, w0=0.0, lr=lr, steps=20)
        print(f"alpha = {lr:<5} -> final w = {path[-1]:.4f}")

    print("Commit 3 tests passed")

    # Fit line through origin: y = w * x
    x_data = np.array([1.0, 2.0, 3.0, 4.0])
    y_data = np.array([2.0, 4.0, 6.0, 8.0])

    grad_line = lambda w: 2.0 * np.mean(x_data * (w * x_data - y_data))

    line_path = gradient_descent(grad_line, w0=0.0, lr=0.01, steps=200)
    final_w = line_path[-1]
    print(f"\nTrained w (no bias): {final_w:.4f} (target: 2.0)")
    assert np.isclose(final_w, 2.0, atol=1e-2), f"Expected ~2.0, got {final_w}"

    print("Commit 4 tests passed")

    # Fit line with bias: y = w * x + b
    y_bias_data = np.array([3.0, 5.0, 7.0, 9.0])  # y = 2x + 1

    w = 0.0
    b = 0.0
    lr = 0.05
    steps = 2000
    loss_history = []

    for _ in range(steps):
        y_hat = w * x_data + b
        loss_history.append(compute_mse(y_hat, y_bias_data))

        error = y_hat - y_bias_data
        dw = 2.0 * np.mean(x_data * error)
        db = 2.0 * np.mean(error)

        w -= lr * dw
        b -= lr * db

    print(f"\nTrained w: {w:.4f} (target: 2.0)")
    print(f"Trained b: {b:.4f} (target: 1.0)")
    assert np.isclose(w, 2.0, atol=0.01), f"Expected w ~ 2, got {w}"
    assert np.isclose(b, 1.0, atol=0.01), f"Expected b ~ 1, got {b}"

    print("First 5 losses:", [round(l, 4) for l in loss_history[:5]])
    print("Last 5 losses: ", [round(l, 6) for l in loss_history[-5:]])
    assert loss_history[0] > loss_history[-1], "Loss should fall steadily!"

    print("\nCommit 5 passed: All parts complete")