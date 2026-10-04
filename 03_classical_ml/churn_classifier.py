"""
PROBLEM:
Train an end-to-end customer churn classification baseline using Scikit-Learn.
Split the dataset, train a RandomForestClassifier, and evaluate accuracy.

Input:
    Features (X): [Account_Months, Monthly_Spend, Support_Calls]
    Labels (y):   0 (Retained) or 1 (Cancelled)

"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Synthetic customer dataset
# Features: [Months_Active, Monthly_Charge, Support_Tickets]
X = [
    [2, 80, 5],
    [35, 30, 0],
    [5, 95, 4],
    [40, 25, 1],
    [1, 110, 6],
    [50, 20, 0],
    [3, 85, 3],
    [45, 35, 1],
]
# Labels: 1 = Cancelled, 0 = Stayed
y = [1, 0, 1, 0, 1, 0, 1, 0]

# 1. Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 2. Instantiate and Fit Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 3. Predict on Test Set
predictions = clf.predict(X_test)

if __name__ == "__main__":
  print("Predictions:", list(predictions))
  print("Actual:     ", y_test)
  print(f"Accuracy:    {accuracy_score(y_test, predictions):.2f}")
  print("\nDiagnostic Report:\n", classification_report(y_test, predictions))