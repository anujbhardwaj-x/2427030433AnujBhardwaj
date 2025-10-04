n = int(input("Enter the number: "))
if n <= 1:
    print(n, "is not prime.")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is prime.")
    else:
        print(n, "is not prime.")