"""
PROBLEM:
1. Impute missing values (np.nan) in the 'price' column using the column mean.
2. Group by 'category' and calculate the total sum of sales for each category.

Example Input:
    category     price
    Electronics  120.0
    Clothing       NaN
    Electronics  250.0
    Clothing      45.0
    Electronics    NaN
"""

import numpy as np
import pandas as pd


def process_sales_data(df):
  # Step 1: Calculate mean and fill missing blanks in price
  df["price"] = df["price"].fillna(df["price"].mean())

  # Step 2: Group by category and sum up sales
  category_totals = df.groupby("category")["price"].sum()

  return category_totals

# Quick test
if __name__ == "__main__":
  data = {
      "category": [
          "Electronics",
          "Clothing",
          "Electronics",
          "Clothing",
          "Electronics",
      ],
      "price": [120.0, np.nan, 250.0, 45.0, np.nan],
  }

  sales_df = pd.DataFrame(data)
  result = process_sales_data(sales_df)
  print(result)

