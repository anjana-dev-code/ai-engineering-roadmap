import numpy as np

sales = np.array([
    [150, 220, 180, 300, 250],
    [320, 280, 190, 400, 350],
    [100, 170, 210, 260, 200],
    [450, 380, 290, 330, 410]
])

print("1.dimension:",np.ndim(sales))
print("2.shape:", np.shape(sales))
print("3.size:", np.size(sales))
print("4.Total sales per branch:", np.sum(sales, axis= 1))
print("5.Total sales per day:", np.sum(sales, axis= 0))
print("6.Overall average sales:", np.mean(sales))
print("7.Highest sale:", np.max(sales))
print("8.Lowest sale:", np.min(sales))
print("9.Number of sales greater or equal to 300:", np.sum(sales >= 300))

below_200 = sales[sales < 200]
print("10.Number of sales below 200:", len(below_200))
print("11.Sum of all sales below 200:", np.sum(below_200))

adjusted_sales = np.copy(sales)
print("12.adjusted sales:",adjusted_sales)
adjusted_sales[adjusted_sales < 200] += 20
print("13.adding 20 to adjusted sales:",adjusted_sales)

print("14.original array:",sales)
transposed_sales = sales.T
print("15.Transpose of sales:",transposed_sales)

print("16.Stadard deviation of original sales array:", np.std(sales))