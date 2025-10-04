x = int(input("Enter how many elements: "))
n = []
for i in range(x):
    a = int(input("Enter element: "))
    n.append(a)
rev = []
for i in range(len(n)-1, -1, -1):
    rev.append(n[i])
print("Original list:", n)
print("Reversed list:", rev)