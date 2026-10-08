"""PROBLEM:
Create a two-panel side-by-side business performance dashboard:
- Panel 1: Line plot of Monthly Revenue ($k)
- Panel 2: Bar plot of Total Orders Placed
Save the completed figure as 'monthly_business_dashboard.png'.
"""

import matplotlib.pyplot as plt 

def generate_business_dashboard(months, revenue_k, orders):
    # create a figure canvas with 1 row and 2 side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12,5))

    # left panel (ax1): Revenue Line Plot
    ax1.plot(months, revenue_k, marker= "o",color= '#2ca02c', linewidth=2)
    ax1.set_title("Monthly Revenue ($ in Thousands)")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue ($k)")
    ax1.grid(True, linestyle= "--", alpha=0.5)

    # right panel (ax2): Orders Bar Chart
    ax2.bar(months, orders, color="#1f77b4", width = 0.6)
    ax2.set_title("Total orders placed")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Number of Orders")
    ax2.grid(axis = "y", linestyle= "--", alpha= 0.5)

    # clean spacing and save to disk
    plt.tight_layout()
    plt.savefig("monthly_business_dashboard.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    months = ["January", "February", "March", "April","May", "June" ]
    revenue = [12.5, 14.0, 18.2, 16.5, 22.0, 25.4]
    orders = [110, 130, 175, 160, 205, 240]

    generate_business_dashboard(months, revenue, orders)
    print(
        "Dashboard successfully saved to disk as monthly_business_dashboard.png"
    )

    