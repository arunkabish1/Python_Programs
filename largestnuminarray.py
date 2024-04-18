def larger():
    arr=[]
    size = int(input("Enter the size of the array: "))
    for i in range(size):
        arr.append(int(input()))
    print("Largest element is:",max(arr))
larger()