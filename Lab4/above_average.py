n = int(input("Enter number of students: "))
x = []
for i in range(n):
    a = int(input("Enter marks of student %d:" % (i+1)))
    x.append(a)
avg = sum(x) / n
print("Average marks:", avg)
print("Students scoring above average:")
for m in x:
    if m > avg:
        print(m)