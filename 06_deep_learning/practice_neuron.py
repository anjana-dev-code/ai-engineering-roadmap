import numpy as np 

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def decide(x, w, b):
    if sigmoid(z) > 0.5:
        return "go"
    else:
        return "stay"

x, w, b = np.array([1,0,1]), np.array([0.9, -0.2, -0.5]),-0.1
print("Test 1:", np.dot(w, x) + b)

x, w, b = np.array([0,1,1]), np.array([0.9, -0.2, -0.5]),-0.1
print("Test 2:", np.dot(w, x) + b)

x, w, b = np.array([1,1,0]), np.array([0.9, -0.2, -0.5]),-0.1
print("Test 3:", np.dot(w, x) + b)

