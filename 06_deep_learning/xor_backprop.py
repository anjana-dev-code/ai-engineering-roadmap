import numpy as np 
np.random.seed(0)

X = np.array([[0,0], [0,1], [1,0], [1,1]], dtype = float)
y = np.array([[0], [1], [1], [0]], dtype = float)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

W1 = np.random.randn(2, 4); b1 = np.zeros((1,4))
W2 = np.random.randn(4, 1); b2 = np.zeros((1,1))
lr = 1.0

for epoch in range(5001):
    # forward
    z1 = X @ W1 + b1; a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2; a2 = sigmoid(z2)
    loss = np.mean((a2 - y) ** 2)

    # backward
    d2 = (2 * (a2 - y) / len(X)) * a2 * (1 - a2)
    dW2 = a1.T @ d2
    db2 = d2.sum(axis=0, keepdims=True)
    d1 = (d2 @ W2.T) * a1 * (1 - a1)
    dW1 = X.T @ d1
    db1 = d1.sum(axis=0, keepdims=True)

    # update
    W2 -= lr * dW2; b2 -= lr * db2
    W1 -= lr * dW1; b1 -= lr * db1

    if epoch % 1000 == 0:
        print(epoch, round(loss, 5))

print(np.round(a2, 3).ravel())
