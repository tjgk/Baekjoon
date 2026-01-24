while 1:
    n=int(input())
    s=0
    if n==0:
        break
    for a in range(1,n+1):
        for b in range(1,n+1):
            s+=a*b
    print(s)