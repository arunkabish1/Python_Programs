def length():
    list1 = []
    print("If you want to stop the list enter 'Stop'")
    while True:
        temp=input("Enter the element:")
        if temp=="Stop":
            break
        list1.append(temp)
    using_len=len(list1)
    print("The length of the list is:",using_len) 

length()

# works great  ... :)