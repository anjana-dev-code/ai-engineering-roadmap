import numpy as np 

sales = np.array([[100, 150, 200],   
                   [120, 130, 180],   
                   [90, 160, 210]])  

print("Sales matrix:\n", sales)
print("Shape: ", sales.shape)

store_total = sales.sum(axis=1)
print("Total sales per store:", store_total)

month_total = sales.sum(axis=0)
print("Total sales per month:", month_total)

# Store with highest average sales
store_avg = sales.mean(axis=1)
best_store_index = store_avg.argmax()
print("Average sales per store:", store_avg)
print("Best performing store index:", best_store_index)  