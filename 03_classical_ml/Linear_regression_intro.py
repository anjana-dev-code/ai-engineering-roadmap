import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = {
    'hours_studied': [1,2,3,4,5,6,7,8],
    'exam_score': [50,60,70,80,90,100,110,120]
}
df = pd.DataFrame(data)

X = df[['hours_studied']]
y = df['exam_score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Prediction:", predictions)
print("Actual:", y_test.values)

print("Weight (w):", model.coef_)
print("Bias (b):", model.intercept_)

