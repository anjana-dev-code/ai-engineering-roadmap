import numpy as np 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# LEVEL 1: The Sigmoid Squasher
def sigmoid(z):
    # Squashes any number into a probability between 0 and 1.
    return 1 / (1 + np.exp(-z))

# LEVEL 2: The Training Loop
def train_logistic_regression(X, y, lr=0.1, epochs=1000):
    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0

    for _ in range(epochs):
        # Forward pass (predict probabilities)
        z = X @ w + b
        y_pred = sigmoid(z)
        
        # Compute gradients
        error = y_pred - y
        dw = (1 / n_samples) * (X.T @ error)
        db = np.mean(error)
        
        # Update parameters
        w -= lr * dw
        b -= lr * db
        
    return w, b

# LEVEL 3: Prediction Helper
def predict(X, w, b):
    probabilities = sigmoid(X @ w + b)
    return (probabilities >= 0.5).astype(int)

if __name__ == "__main__":
    # Test Level 1 
    print("LEVEL 1: Sigmoid Test")
    print(f"sigmoid(0) = {sigmoid(0)} (Expected: 0.5)")
    assert sigmoid(0) == 0.5, "sigmoid of 0 must be 0.5."
    
#  Test Levels 2 & 3: Scratch Model 
    print("LEVEL 2 & 3: Scratch Training")
    data = load_breast_cancer()
    X, y = data.data, data.target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    w, b = train_logistic_regression(X_train_scaled, y_train, lr=0.1, epochs=1000)
    scratch_preds = predict(X_test_scaled, w, b)
    scratch_acc = accuracy_score(y_test, scratch_preds)
    
    print(f"Scratch Model Accuracy: {scratch_acc * 100:.2f}%\n")


    print("Sklearn Parity")
    sk_model = LogisticRegression(random_state=42)
    sk_model.fit(X_train_scaled, y_train)
    
    sk_preds = sk_model.predict(X_test_scaled)
    sk_acc = accuracy_score(y_test, sk_preds)
    
    print(f"Scratch Model Accuracy: {scratch_acc * 100:.2f}%")
    print(f"Sklearn Model Accuracy: {sk_acc * 100:.2f}%")
