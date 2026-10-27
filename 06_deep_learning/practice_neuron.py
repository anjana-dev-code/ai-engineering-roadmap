import numpy as np 

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def decide(x, w, b):
    z = np.dot(w, x) + b          
    if sigmoid(z) > 0.5:
        return "go"
    else:
        return "stay"


w, b = np.array([0.9, -0.2, -0.5]), -0.1

scenarios = {
    "Scenario 1": np.array([1, 0, 1]),
    "Scenario 2": np.array([0, 1, 1]),
    "Scenario 3": np.array([1, 1, 0]),
}

for name, x in scenarios.items():
    z = np.dot(w, x) + b
    print(f"{name}: z = {z:.2f}, sigmoid = {sigmoid(z):.3f}, decision = {decide(x, w, b)}")

