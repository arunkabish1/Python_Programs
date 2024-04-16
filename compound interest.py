def ci():
    P=int(input("Enter the value of Principal:"))
    T=int(input("Enter the value of Time:"))
    R=float(input("Enter the value of Rate:"))
    ci=P*(pow((1+R/100),T))
    print("simple interest is",ci)
ci()