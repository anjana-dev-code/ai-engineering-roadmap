"""
PROBLEM: Multi-Column Inventory Reconciliation and Restock Audit
Analyze warehouse stock levels and daily sales velocity to flag items needing 
urgent replenishment.

Criteria:
    - Urgent if stock < 15 AND daily_sales > 5
"""

import pandas as pd 

def audit_inventory(df):
    # Element-wise bitwise evaluation for multi-condition filtering
    restock_condition = (df["stock"] < 15) & (df["daily_sales"] > 5)
    df["urgent_restock"] = restock_condition
    
    # Isolate urgent rows
    urgent_df = df[df["urgent_restock"] == True].copy()
    return urgent_df

if __name__ == "__main__":
    inventory_data = {
        "item": ["Monitor", "Mouse", "Keyboard", "Desk Pad", "Webcam"],
        "stock": [8, 45, 12, 5, 30],
        "daily_sales": [10, 4, 8, 2, 6],
        "warehouse": ["North", "East", "North", "West", "East"]
    }
    
    df = pd.DataFrame(inventory_data)
    result = audit_inventory(df)
    print("Urgent Restock Report:\n", result)