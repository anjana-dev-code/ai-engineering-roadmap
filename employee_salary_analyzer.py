import pandas as pd

data = {
    "name": ["Ravi", "Neha", "Karan", "Zoya", "Tom"],
    "department": ["Sales", "Tech", "Sales", "Tech", "HR"],
    "salary": [45000, 72000, 51000, 68000, 39000]
}

df = pd.DataFrame(data)
print(df)

print("\n--- Quick stats ---")
print(df.describe())

print("\n--- Employees earning above 50000 ---")
high_earners = df[df["salary"] > 50000]
print(high_earners)

print("\n--- Average salary per department ---")
print(df.groupby("department")["salary"].mean())

print("\n--- Add salary bracket column ---")
df["bracket"] = df["salary"].apply(lambda x: "High" if x >= 60000 else "Low")
print(df)

print("\n--- Sorted by salary, highest first ---")
print(df.sort_values("salary", ascending=False))