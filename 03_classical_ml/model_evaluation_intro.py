import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

data = {
    'owns_car': [1,1,1,1,0,0,0,0],
    'high_credit': [1,1,0,0,1,1,0,0],
    'defaulted': [0,0,0,1,1,1,1,1]
}
df = pd.DataFrame(data)

X = df[['owns_car', 'high_credit']]
y = df['defaulted']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print("Predictions:", predictions)
print("Actual:     ", y_test.values)

print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1 Score:", f1_score(y_test, predictions))