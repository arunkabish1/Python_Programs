def arm():
    num = input("Enter the number:")
    n=len(num)
    sum = 0
    for digits in num: 
        sum += int(digits) ** n

    if int(num) == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

arm()