"""
PROBLEM: Supervised Classification Baseline & Diagnostic Evaluation

Train a Random Forest classifier to predict customer churn using numerical 
features and evaluate performance with a classification report.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import numpy as np 

def evaluate_churn_classifier():
    np.random.seed(42)
    X = np.random.rand(150, 3) # Features: [tenure, support_calls, monthly_spend]
    y = np.random.choice([0, 1], size=150, p=[0.7, 0.3]) # 1 = Churned, 0 = Retained

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size= 0.25, random_state= 42, stratify= y
    )

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    prediction = model.predict(X_test)
    report = classification_report(y_test, prediction)

    return report

if __name__ == "__main__":
    evaluation_results = evaluate_churn_classifier()
    print("Model Diagnostic Classification Report:\n")
    print(evaluation_results)
