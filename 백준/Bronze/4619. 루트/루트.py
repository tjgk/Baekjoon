while 1:    
    b,n=map(int,input().split())
    if b==0:
        break
    t=1
    for i in range(2,b+1):
        if abs(i**n-b)<abs(t**n-b):
            t=i
        if i**n>=b:
            break
    print(t)