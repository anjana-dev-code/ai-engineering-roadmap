import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

def neuron(x, w, b, activation):
    z = np.dot(w,x) + b
    return activation(z)

x, w, b = np.array([2,3]), np.array([0.5, -1]), 1
assert np.isclose(neuron(x, w, b, relu), 0)
assert np.isclose(neuron(x, w, b, sigmoid), 0.2689, atol = 1e-4)

x, w, b = np.array([1, 4, 2]), np.array([0.2, 0.5, -0.3]), -0.5
assert np.isclose(neuron(x, w, b, relu), 1.1)
assert np.isclose(neuron(x, w, b, sigmoid), 0.7503, atol=1e-4)

assert relu(-3) == 0
assert np.isclose(sigmoid(-3), 0.0474, atol=1e-4)


print("All tests are correct")

