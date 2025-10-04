# WAF to calculate total bill using *items (tuples of name, price)
def totalBill(*items):
    total = 0
    for name, price in items:
        total += price
    return total

# Example call
print("Total Bill =", totalBill(("Tea", 20), ("Coffee", 30), ("Sandwich", 50)))
