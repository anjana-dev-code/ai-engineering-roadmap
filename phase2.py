import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = {
    'income_high': [1,1,1,1,1,1,0,0,0,0],
    'defaulted':   [0,0,0,0,0,0,1,1,1,1]
}
df = pd.DataFrame(data)
print(df)

X = df[['income_high']]
y = df['defaulted']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Train size:", len(X_train))
print("Test size:", len(X_test))

clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
print("Predictions:", predictions)
print("Actual:     ", y_test.values)