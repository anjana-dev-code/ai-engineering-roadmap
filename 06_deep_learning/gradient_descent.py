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
    print("Path with alpha=1.0 (prediction confirmed):", path_bounce)
    assert path_bounce == [0.0, 6.0, 0.0, 6.0, 0.0, 6.0, 0.0]

    print("Commit 2 tests passed")