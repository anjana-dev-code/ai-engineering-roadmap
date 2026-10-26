import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt

conn = sqlite3.connect("Chinook.db")

query = """
SELECT BillingCountry AS country, ROUND(SUM(Total), 2) AS revenue
FROM Invoice
GROUP BY BillingCountry
ORDER BY revenue DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)   # SQL result -> DataFrame
conn.close()
print(df.head())

ax = df.plot(kind="bar", x="country", y="revenue", legend=False, figsize=(9, 5))
ax.set_title("Chinook: top 10 countries by revenue")
ax.set_xlabel("Country")
ax.set_ylabel("Revenue ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("05_sql/revenue_by_country.png")
plt.show()

share = df["revenue"].iloc[0] / df["revenue"].sum() * 100
print(f"Top country share of top-10 revenue: {share:.1f}%")

