"""
PROJECT: Automated Customer Churn Classification Engine
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def run_churn_pipeline():
    # Data Generation
    np.random.seed(42)
    n_samples = 200
    raw_data = {
        "customer_id": [f"CUST_{i:03d}" for i in range(1, n_samples + 1)],
        "tenure_months": np.random.randint(1, 48, size=n_samples),
        "monthly_spend": np.random.uniform(20.0, 250.0, size=n_samples),
        "support_calls": np.random.poisson(lam=1.5, size=n_samples),
        "portal_logins_per_week": np.random.exponential(scale=3.0, size=n_samples)
    }
    df = pd.DataFrame(raw_data)
    
    # Feature Engineering
    df["spend_per_tenure"] = df["monthly_spend"] / (df["tenure_months"] + 1)
    churn_score = (
        (df["support_calls"] > 2).astype(int) * 0.5 +
        (df["portal_logins_per_week"] < 2).astype(int) * 0.4 +
        np.random.normal(0, 0.1, size=n_samples)
    )
    df["churned"] = (churn_score > 0.6).astype(int)

    print("Training the Machine Learning Brain")
    # Select our features (the warning signs) and the target (the answer)
    feature_cols = ["tenure_months", "monthly_spend", "support_calls", "portal_logins_per_week", "spend_per_tenure"]
    X = df[feature_cols]
    y = df["churned"]

    # Split the data: 75% for training, 25% for a secret test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    
    # Initialize and Train the Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Testing the Model on Unseen Data\n")
    # Let the model guess on the test set
    predictions = model.predict(X_test)
    
    print("Confusion Matrix")
    print(confusion_matrix(y_test, predictions))
    
    print("\nClassification Report")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    run_churn_pipeline()