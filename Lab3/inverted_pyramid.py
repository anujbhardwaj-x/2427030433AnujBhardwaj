x = int(input("Enter number of rows: "))
for i in range(x, 0, -1):
    for j in range(x, x - i, -1):
        print(j, end=" ")
    print()