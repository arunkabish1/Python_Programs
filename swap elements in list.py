def swap():
    list1=[]
    n=int(input("Enter the number of elements:"))
    for i in range(0,n):
        list1.append(int(input()))
    print("Original list:",list1)
    list1[0],list1[-1]=list1[-1],list1[0]
    print("Swapped list:",list1)
swap()