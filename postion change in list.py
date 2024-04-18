def positiion():
    list1=[]
    n=int(input("Enter the number of elements:"))
    for i in range(0,n):
        list1.append(int(input()))
    print("Original list:",list1)
    pos1=int(input("Enter the position of the 1st element to be changed:"))
    pos2=int(input("Enter the position of the 2nd element to be changed:"))
    list1[pos1],list1[pos2] = list1[pos2],list1[pos1]    
    print("Swapped list:",list1)

positiion()