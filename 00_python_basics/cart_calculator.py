"""
PROBLEM:
Calculate the total bill for a list of shopping cart items.
Multiply price by quantity for each item, and apply a 10% discount
if the shopper has a VIP membership.

Example:
    Mouse: 25 * 2 = 50
    Keyboard: 80 * 1 = 80
    Cable: 10 * 3 = 30
    Subtotal: 160.0
    VIP Total (-10%): 144.0
"""

def calculate_checkout_total(cart, is_vip= False):
    # Start an accumulator at 0.0
    subtotal = 0.0

    # Loop through each item in the cart
    for item in cart:
        # Multiply price by quantity and add to subtotal
        item_cost = item["price"] * item["qty"]
        subtotal += item_cost

    # Apply discount if customer is VIP
    if is_vip:
        discount = subtotal * 0.10
        final_total = subtotal - discount
    else:
        final_total = subtotal

    return final_total

if __name__ == "__main__":
    my_cart = [
        {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
        {"name": "Gaming Keyboard", "price": 80.0, "qty": 1},
        {"name": "USB Cable", "price": 10.0, "qty": 3}
    ]

    # Test Regular Customer
    regular_bill = calculate_checkout_total(my_cart, is_vip=False)
    print(f"Regular Customer Total: ${regular_bill:.2f}")

    # Test VIP Customer (10% off)
    vip_bill = calculate_checkout_total(my_cart, is_vip=True)
    print(f"VIP Customer Total:     ${vip_bill:.2f}")