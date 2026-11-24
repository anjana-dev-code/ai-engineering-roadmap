import numpy as np 

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

x, w, b, y = 2.0, 0.5, 0.1, 1.0
lr = 0.5

for step in range(5):
    # forward
    z = w * x + b
    a = sigmoid(z)
    loss = (a - y) ** 2

    # backward
    dL_da = 2 * (a - y)
    da_dz = a * (1 - a)
    dz = dL_da * da_dz # delta
    dw = dz * x
    db = dz
    print("dz =", dz)

    # update
    w -= lr * dw
    b -= lr * db
    print(f"step {step}: loss = {loss: .5f}, w= {w: .4f}, b = {b: .4f}")

