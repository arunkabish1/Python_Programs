def sumoflist():
    list1=[]
    n=int(input("Enter the number of elements:"))
    for i in range(0,n):
        list1.append(int(input()))
    print("Sum of all elements in given list using sum() function: ",sum(list1))
    # or
    sum1=0
    for element in list1:
        sum1=sum1+element
    print("Sum of all elements in given list using for loop: ",sum1)

sumoflist()