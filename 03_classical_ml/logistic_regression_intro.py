import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = {
    'hours_studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'passed':        [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[['hours_studied']]
y = df['passed']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Actual:     ", y_test.values)

probabilities = model.predict_proba(X_test)
print("Probabilities:", probabilities)

print("Weight (w):", model.coef_)
print("Bias (b):", model.intercept_)
