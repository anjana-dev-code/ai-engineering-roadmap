"""
PROBLEM:
Train a baseline Logistic Regression model to predict loan approvals (1=Approved, 0=Denied)
using credit score and annual income. Evaluate with an accuracy score.

"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def evaluate_loan_classifier(features, labels):
  # Split data (75% training, 25% testing)
  X_train, X_test, y_train, y_test = train_test_split(
      features, labels, test_size=0.25, random_state=42
  )

  # 
  model = LogisticRegression()
  model.fit(X_train, y_train)

  # Predict on unseen test data
  y_pred = model.predict(X_test)

  # Measure performance
  acc = accuracy_score(y_test, y_pred)

  return acc, y_pred, y_test



if __name__ == "__main__":
  # [Credit Score, Income in $k]
  X = [
      [720, 85],
      [580, 32],
      [750, 110],
      [610, 45],
      [800, 120],
      [520, 28],
      [690, 75],
      [600, 40],
  ]
  # 1 = Approved, 0 = Denied
  y = [1, 0, 1, 0, 1, 0, 1, 0]

  accuracy, preds, actual = evaluate_loan_classifier(X, y)
  print(f"Model Test Accuracy: {accuracy * 100:.1f}%")
  print("Predictions:        ", list(preds))
  print("Actual:             ", actual)