# import numpy

def multiply():
    list1=[]
    n=int(input("Enter the number of elements:"))
    for i in range(0,n):
        list1.append(int(input()))
    # print("using mul() function: ",numpy.prod(list1)) for python 3
    # or
    value=1
    for element in list1:
        value=value*element

    print("using for loop: ",value)

multiply()