import numpy as np 

def sigmoid(z):
    # Squashes any number into a probability between 0 and 1.
    return 1 / (1 + np.exp(-z))

if __name__ == "__main__":
    print(f"sigmoid(0) = {sigmoid(0)} (Expected: 0.5)")
    assert sigmoid(0) == 0.5, "sigmoid of 0 must be 0.5."
