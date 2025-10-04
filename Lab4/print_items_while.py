n = int(input("Enter number of elements: "))
x = []
for i in range(n):
    value = input("Enter element %d:" % (i+1))
    x.append(value)
i = 0
print("All items:")
while i < len(x):
    print(x[i])
    i += 1