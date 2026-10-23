"""
PROJECT: Automated Customer Churn Prediction & Risk Scoring Pipeline
COMMIT 4: Actionable Output & Prioritized Risk Export
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

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
    
    # Prepare Feature Matrix (X) and Target Vector (y)
    feature_cols = ["tenure_months", "monthly_spend", "support_calls", "portal_logins_per_week", "spend_per_tenure"]
    X = df[feature_cols].values
    y = df["churned"].values
    
    # New: We are passing df["customer_id"] into the split so we can track exactly who is in the test set
    X_train, X_test, y_train, y_test, ids_train, ids_test = train_test_split(
        X, y, df["customer_id"], test_size=0.25, random_state=42, stratify=y
    )
    
    # Train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predict Probabilities & Evaluate Diagnostics
    y_pred_probs = model.predict_proba(X_test)[:, 1] # Probability of churn
    y_pred = model.predict(X_test)
    
    print("Classification Diagnostic Report:")
    print(classification_report(y_test, y_pred))
    
    auc_score = roc_auc_score(y_test, y_pred_probs)
    print(f"ROC-AUC Score: {auc_score:.4f}\n")
    
    # Generate Prioritized Retention Action List 
    print("Generating Executive Retention Report:")
    test_results_df = pd.DataFrame({
        "customer_id": ids_test,
        "churn_probability": y_pred_probs,
        "actual_churn": y_test
    })
    
    # Sort the list so the highest risk customers are at the top
    prioritized_list = test_results_df.sort_values(by="churn_probability", ascending=False).head(5)
    print("\nTop 5 High-Risk Customers Flagged for Immediate Intervention:")
    print(prioritized_list.to_string(index=False))

if __name__ == "__main__":
    run_churn_pipeline()