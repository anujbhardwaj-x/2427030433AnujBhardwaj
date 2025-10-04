x = []
for i in range(5):
    n = input("Enter name: ")
    x.append(n)
x.sort()
print("Sorted Order:")
for name in x:
    print(name)