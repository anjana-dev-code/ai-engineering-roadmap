import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = {
    'owns_car': [1,1,1,1,0,0,0,0],
    'high_credit': [1,1,0,0,1,1,0,0],
    'defaulted': [0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[['owns_car', 'high_credit']]
y = df['defaulted']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size= 0.25, random_state= 42
)

clf = KNeighborsClassifier(n_neighbors= 3)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
print("Predictions:", predictions)
print("Actual:", y_test.values) 