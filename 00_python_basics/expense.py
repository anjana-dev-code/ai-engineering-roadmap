# Starting budget
monthly_allowance = 100.0

# Stored expenses: (item_name, cost)
expenses = [
    ("Coffee", 4.50),
    ("Book", 15.00),
    ("Sandwich", 7.25),
    ("Headphones", 35.00),
]

# 1. Calculate total spending
total_spent = 0.0
for item, cost in expenses:
    total_spent += cost

# 2. Find the remaining money
money_left = monthly_allowance - total_spent

# 3. Find the most expensive item
highest_item = ""
highest_cost = 0.0
for item, cost in expenses:
    if cost > highest_cost:
        highest_cost = cost
        highest_item = item

# 4. Print the final summary
print("--- Monthly Budget Summary ---")
print(f"Total Allowance: ${monthly_allowance:.2f}")
print(f"Total Spent:     ${total_spent:.2f}")
print(f"Money Remaining: ${money_left:.2f}")
print(f"Biggest Expense: {highest_item} (${highest_cost:.2f})")