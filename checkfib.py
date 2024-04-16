def checkfib():
    a=int(input("Enter the number: "))
    b=0
    c=1
    d=1
    if a==b or a==c:
        print("True")
    else:
        while d<a:
            d=b+c
            b=c
            c=d
        if d==a:
            print("True")
        else:
            print("False")
    
checkfib()