
"""
PROBLEM:
Take grouped category sales totals, generate a clean bar chart using Matplotlib,
and save the figure to disk as 'category_sales.png'.
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_sales_summary(category_totals):
 
  categories = category_totals.index
  totals = category_totals.values

  # width=6 inches, height=4 inches
  plt.figure(figsize=(6, 4))

  # vertical bars
  plt.bar(categories, totals, color=["skyblue", "salmon"])

  # Add clear labels and title
  plt.title("Total Sales by Category")
  plt.xlabel("Category")
  plt.ylabel("Sales ($)")

  # Prevent label text from clipping at the borders
  plt.tight_layout()

  # Save image to disk and close canvas
  plt.savefig("category_sales.png")
  plt.close()


if __name__ == "__main__":
  
  data = {"Clothing": 45.0, "Electronics": 555.0}
  sample_totals = pd.Series(data)

  plot_sales_summary(sample_totals)
  print("Bar chart saved successfully as category_sales.png")