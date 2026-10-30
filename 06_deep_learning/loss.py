import numpy as np
from forward_pass import forward 

def mse(y, p):
    return np.mean((y - p) ** 2)


def bce(y, p):
    p = np.clip(p, 1e-12, 1 - 1e-12)   # stop ln(0)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))


if __name__ == "__main__":
    
    y = np.array([1, 0, 1])
    p = np.array([0.9, 0.2, 0.6])
    assert np.isclose(mse(y, p), 0.07)
    assert np.isclose(bce(y, p), 0.2798, atol=1e-3)

    
    assert np.isclose(mse(y, y.astype(float)), 0)
    assert np.isclose(bce(y, y.astype(float)), 0, atol=1e-9)

    
    print("p      loss")
    for p_val in [0.99, 0.9, 0.5, 0.1, 0.01]:
        loss = bce(np.array([1]), np.array([p_val]))
        print(f"{p_val:<6} {loss:.3f}")

    
    x = np.array([[1.0, 2.0]])
    W1 = np.array([[0.5, -1.0], [1.0, 0.5]])
    b1 = np.array([[0.0, 1.0]])
    W2 = np.array([[1.0], [-2.0]])
    b2 = np.array([[0.5]])

    out = forward(x, W1, b1, W2, b2)       # about 0.731
    y_true = np.array([[1.0]])
    print(f"Network output: {out[0, 0]:.4f}, BCE vs y=1: {bce(y_true, out):.4f}")
    assert np.isclose(bce(y_true, out), 0.3133, atol=1e-3)

    print("All tests passed")