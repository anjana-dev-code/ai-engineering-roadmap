import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text

# 8
data = {
    'owns_car': [1,1,1,1,0,0,0,0], # 1 = has car, 0 = doesn't
    'high_credit': [1,1,0,0,1,1,0,0], # 1 = has high credit, 0 = doesn't
    'defaulted': [0,0,0,1,1,1,1,1] # 1 = defaulted
} 
df = pd.DataFrame(data)
print(df)

x = df[['owns_car','high_credit']]
y = df['defaulted']

X_train, X_test, y_train, y_test = train_test_split(
    x,y, test_size=0.25, random_state=42
)

print("Train Size:", len(X_train))
print("Test Size:", len(X_test))

clf = DecisionTreeClassifier(criterion= 'gini', random_state= 42)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
print("Predictions:", predictions)
print("Actual:   ", y_test.values )

tree_rules = export_text(clf, feature_names= ['owns_car','high_credit'])
print(tree_rules)
