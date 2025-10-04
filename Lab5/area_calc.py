# WAF to calculate area: rectangle or square
def area(L, W=None):
    if W is None:
        return L * L
    else:
        return L * W

# Example call
print("Square area =", area(5))
print("Rectangle area =", area(5, 10))
