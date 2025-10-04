# WAF to calculate salary after applying bonus rate
def bonus(salary, rate=0.10):
    return salary + salary * rate

# Positional args
print("New salary (positional):", bonus(50000, 0.20))

# Keyword args
print("New salary (keyword):", bonus(salary=50000, rate=0.15))

# Incorrect mixing (will raise error if uncommented)
# print(bonus(50000, rate=0.25, 0.10))
