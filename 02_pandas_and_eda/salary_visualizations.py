import matplotlib
matplotlib.use('TkAgg')
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


data = {
    "name": ["Ravi", "Neha", "Karan", "Zoya", "Tom"],
    "department": ["Sales", "Tech", "Sales", "Tech", "HR"],
    "salary": [45000, 72000, 51000, 68000, 39000]
}
df = pd.DataFrame(data)

sns.barplot(data=df, x="department", y="salary")
plt.title("Average Salary per Department")
plt.show()

sns.boxplot(data=df, x="department", y="salary")
plt.title("Salary Spread by Department")
plt.show()

plt.hist(df["salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Count")
pit.show()
