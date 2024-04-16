def primeornot():
    num=int(input("Enter the number:"))
    if num == 0 or num ==1:
        print(num," is Not Prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print(num," is Not Prime")
                break
        else:
            print(num," is Prime")
primeornot()