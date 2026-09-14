import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score

# reuse the messier dataset from Week 8
data = {
    'owns_car':    [1,1,1,1,1,0,0,0,0,0,1,0,1,0,1],
    'high_credit': [1,1,0,1,0,1,0,0,1,0,0,1,1,0,0],
    'defaulted':   [0,0,1,0,1,1,1,1,0,1,0,0,0,1,0]
}
df = pd.DataFrame(data)

X = df[['owns_car', 'high_credit']]
y = df['defaulted']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = XGBClassifier(n_estimators=10, learning_rate=0.3, max_depth=2, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Actual:     ", y_test.values)

print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1 Score:", f1_score(y_test, predictions))