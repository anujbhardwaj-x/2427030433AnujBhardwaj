s = int(input("Enter a number: "))
sum = 0
while s > 0:
    x = s % 10
    sum += x
    s //= 10
print("Sum of numbers =", sum)