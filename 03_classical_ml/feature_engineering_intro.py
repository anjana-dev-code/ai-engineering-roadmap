import pandas as pd 
from sklearn.preprocessing import LabelEncoder

data = {
    'sex': ['Male', 'Female', 'Female', 'Male'],
    'education': ['High School', "Bachelor's", "Master's", 'PhD'],
    'age': [25, None, 30, 40]
}
df = pd.DataFrame(data)
print("Before\n:", df)

# 1. Handle missing values = fill age with mean
df['age'] = df['age'].fillna(df['age'].mean())

# 2. One-Hot Encode 'sex' (no natural order)
df = pd.get_dummies(df, columns=['sex'])

# 3. real order
education_order = {'High School': 0, "Bachelor's": 1, "Master's": 2, 'PhD': 3}
df['education'] = df['education'].map(education_order)

print("\nAfter:\n", df)
