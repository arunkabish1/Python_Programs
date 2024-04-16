def print_prime():
    num = int(input("Enter the number: "))
    prime_numbers = []

    for n in range(2, num + 1):
        is_prime = True
        for divisor in range(2, n):
            if n % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)
            print(n, end=" ")
    # print("Prime numbers up to", num, "are:", prime_numbers)

print_prime()
