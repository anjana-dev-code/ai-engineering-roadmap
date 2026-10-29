import numpy as np


def relu(z):
    return np.maximum(0, z)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def layer_forward(X, W, b, activation):
    return activation(X @ W + b)


def forward(X, W1, b1, W2, b2, verbose=False):
    A1 = layer_forward(X, W1, b1, relu)
    out = layer_forward(A1, W2, b2, sigmoid)
    if verbose:
        print(f"X: {X.shape} -> A1: {A1.shape} -> out: {out.shape}")
    return out


def count_params(W1, b1, W2, b2):
    return W1.size + b1.size + W2.size + b2.size


if __name__ == "__main__":
    
    x = np.array([[1.0, 2.0]])
    W1 = np.array([[0.5, -1.0], [1.0, 0.5]])
    b1 = np.array([[0.0, 1.0]])
    W2 = np.array([[1.0], [-2.0]])
    b2 = np.array([[0.5]])

    out = forward(x, W1, b1, W2, b2, verbose=True)
    print(f"Worked example output: {out[0, 0]:.4f}")
    assert np.isclose(out[0, 0], 0.7311, atol=1e-4)

    
    x = np.array([[2.0, 1.0]])
    W1 = np.array([[1.0, -1.0], [0.5, 2.0]])
    b1 = np.array([[0.0, -1.0]])
    W2 = np.array([[2.0], [1.0]])
    b2 = np.array([[-1.0]])

    out = forward(x, W1, b1, W2, b2)
    print(f"Paper problem output: {out[0, 0]:.4f}")
    assert np.isclose(out[0, 0], 0.9820, atol=1e-4)

    
    assert count_params(W1, b1, W2, b2) == 9

    print("All tests passed")