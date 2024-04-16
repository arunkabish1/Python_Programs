def si():
    print("Enter the value of Principal,Time without pressing Enter.(give space between them)")
    P,T,R=map(int,input("Enter the value of Principal,Time,Rate:").split())
    Si=(P*T*R)/100
    print("simple interest is",Si)
si()