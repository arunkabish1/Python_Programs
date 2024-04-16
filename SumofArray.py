def SumArray():
    arr = []
    n =int(input("Enter the number of elements: "))
    for i in range(0,n):
        arr.append(int(input("Enter the element %d :"%(i+1))))
    sum = 0
    for i in range(0,n):
        sum = sum + arr[i]
    print("Sum of all elements in given array: ",sum)

SumArray()