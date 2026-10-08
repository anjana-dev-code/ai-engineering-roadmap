"""
PROBLEM:
Train a Decision Tree Classifier to predict customer purchases
based on website browsing behavior. Evaluate test accuracy and inspect
feature importance scores.

Features:
    [Time_On_Site_Minutes, Pages_Visited, Discount_Applied (0/1)]

Target:
    1 = Purchase, 0 = No Purchase
"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd 

def train_purchase_tree(features, labels, feature_names):
    # split the data (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state= 42
    )

    #initialise Decision Tree with restricted depth
    model = DecisionTreeClassifier(max_depth=3, random_state=42)

    # train the model
    model.fit(X_train, y_train)

    # predict the unseen data
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)

    # check which feature was most influential
    importance_summary = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)


    return model, accuracy, importance_summary

if __name__ == "__main__":
    # Synthetic visitor behavior: [Time_Mins, Pages, Has_Coupon]
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
        [5.0, 2, 0]
    ]
    # 1 = Bought, 0 = Left without buying
    y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    feature_names = ["time_on_site", "pages_visited", "has_coupon"]

    tree_model, test_acc, importances = train_purchase_tree(X, y, feature_names)

    print(f"Model Accuracy: {test_acc * 100:.1f}%\n")
    print("Feature Importance Ranking:")
    print(importances.to_string(index=False))
