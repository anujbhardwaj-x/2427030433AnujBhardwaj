n = int(input("Enter number of elements: "))
x = []
for i in range(n):
    a = int(input("Enter value %d:" % (i+1)))
    x.append(a)
print("List in reverse order:")
for i in range(len(x) - 1, -1, -1):
    print(x[i])