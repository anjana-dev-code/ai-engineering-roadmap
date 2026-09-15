import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

data = {
    'owns_car':    [1,1,1,1,1,0,0,0,0,0,1,0,1,0,1],
    'high_credit': [1,1,0,1,0,1,0,0,1,0,0,1,1,0,0],
    'defaulted':   [0,0,1,0,1,1,1,1,0,1,0,0,0,1,0]
}

df = pd.DataFrame(data)

X = df[['owns_car', 'high_credit']]
y = df['defaulted']

clf = DecisionTreeClassifier(criterion='gini', random_state=42)

scores = cross_val_score(clf, X, y, cv=5)
print("Scores for each fold:", scores)
print("Average score:", scores.mean())