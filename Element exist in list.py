def exist():
    list1=[]
    n=int(input("Enter the number of elements:"))
    for i in range(0,n):
        list1.append(int(input()))
    # print("The list is:",list1)
    element=int(input("Enter the element to search:"))
    if element in list1:
        print("The element exist in the list")
    else:
        print("The element does not exist in the list")
        
exist()