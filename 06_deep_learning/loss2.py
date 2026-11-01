import numpy as np
from forward_pass import forward
from loss import mse, bce


def mae(y, p):
    return np.mean(np.abs(y - p))


def rmse(y, p):
    return np.sqrt(mse(y, p))


def accuracy(y, p, threshold=0.5):
    return np.mean((p > threshold).astype(int) == y)


if __name__ == "__main__":
    y = np.array([10, 12, 11, 50])
    p = np.array([11, 11, 12, 12])
    print(f"MAE  = {mae(y, p):.2f}")     # 10.25
    print(f"MSE  = {mse(y, p):.2f}")     # 361.75
    print(f"RMSE = {rmse(y, p):.2f}")    # 19.02
    assert np.isclose(mae(y, p), 10.25)
    assert np.isclose(mse(y, p), 361.75)
    assert np.isclose(rmse(y, p), np.sqrt(mse(y, p)))

    y = np.array([1, 0, 1])
    model_a = np.array([0.9, 0.1, 0.8])
    model_b = np.array([0.51, 0.49, 0.55])
    for name, p in [("A", model_a), ("B", model_b)]:
        print(f"Model {name}: accuracy = {accuracy(y, p):.2f}, BCE = {bce(y, p):.4f}")
    assert accuracy(y, model_a) == accuracy(y, model_b) == 1.0
    assert np.isclose(bce(y, model_a), 0.1446, atol=1e-3)
    assert np.isclose(bce(y, model_b), 0.6482, atol=1e-3)

    loss_a = bce(np.array([1]), np.array([0.6]))
    loss_b = bce(np.array([1]), np.array([0.01]))
    print(f"Forecaster A: {loss_a:.3f}, Forecaster B: {loss_b:.3f}")
    assert loss_b > 7 * loss_a

   
    x = np.array([[2.0, 1.0]])
    W1 = np.array([[1.0, -1.0], [0.5, 2.0]])
    b1 = np.array([[0.0, -1.0]])
    W2 = np.array([[2.0], [1.0]])
    b2 = np.array([[-1.0]])
    out = forward(x, W1, b1, W2, b2)    
    loss_if_1 = bce(np.array([[1.0]]), out)
    loss_if_0 = bce(np.array([[0.0]]), out)
    print(f"Output {out[0, 0]:.3f} | BCE if y=1: {loss_if_1:.4f} | BCE if y=0: {loss_if_0:.4f}")
    assert np.isclose(loss_if_1, 0.0181, atol=1e-3)
    assert np.isclose(loss_if_0, 4.0181, atol=1e-3)

    print("All tests passed")