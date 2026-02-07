while 1:
    n=int(input())
    if n==0: break
    a=list(map(int,input().split()))
    s=0
    for i in a:
        if s+i<=300:
            s+=i
    print(s)