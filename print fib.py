def printfib():
    num = int(input("Enter the number: "))
    # a=int(input("Enter the number 1:"))
    # b=int(input("Enter the number 2:"))
    a = 0
    b = 1
    print("Fibonacci sequence:")
    print(a)
    print(b)
    for i in range(2, num + 1):
        c = a + b
        print(c)
        a = b
        b = c

printfib()