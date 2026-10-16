import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def train_purchase_tree(features, labels, feature_names):
  # Train / Test Split
  X_train, X_test, y_train, y_test = train_test_split(
      features, labels, test_size=0.2, random_state=42
  )

  # Initialize Decision Tree with Restricted Depth
  model = DecisionTreeClassifier(max_depth=3, random_state=42)

  # Train the Model
  model.fit(X_train, y_train)

  # Predict Unseen Test Data & Measure Accuracy
  prediction = model.predict(X_test)
  accuracy = accuracy_score(y_test, prediction)

  # Feature Importance Inspection
  importance_summary = pd.DataFrame(
      {"Feature": feature_names, "Importance": model.feature_importances_}
  ).sort_values(by="Importance", ascending=False)

  return model, accuracy, importance_summary

if __name__ == "__main__":
  # Synthetic visitor behavior: [Time_Mins, Pages_Visited, Has_Coupon (0/1)]
  X = [
      [15.5, 6, 1],
      [2.0, 1, 0],
      [12.0, 5, 1],
      [3.5, 2, 0],
      [25.0, 8, 1],
      [1.5, 1, 0],
      [18.0, 7, 0],
      [4.0, 2, 1],
      [30.0, 9, 1],
      [5.0, 2, 0],
  ]
  # 1 = Bought, 0 = Left without buying
  y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
  feature_names = ["time_on_site", "pages_visited", "has_coupon"]

  tree_model, test_acc, importances = train_purchase_tree(X, y, feature_names)

  print(f"Model Accuracy: {test_acc * 100:.1f}%\n")
  print("Feature Importance Ranking:")
  print(importances.to_string(index=False))