def fact():
    num = int(input("Enter the number: "))
    fact = 1
    if num==0:
        print("factorial of 0 is 1")
    else:
      for i in range(1,num+1):
         fact=fact*i
      print("Factorial of",num,"is",fact)
fact()