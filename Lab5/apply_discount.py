# Lambda function to apply discount
applyDiscount = lambda price, discount: price - (price * discount / 100)

# Example call
print("Price after discount =", applyDiscount(1000, 10))
