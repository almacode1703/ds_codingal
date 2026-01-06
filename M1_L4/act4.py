number = int(input("Enter a number to check if it is prime: "))

if number <= 1:
    print("Enter a number greater than 1")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not Prime")
