while 1:
    n,d=map(int,input().split())
    if n==d==0:
        break
    t=[1 for _ in range(n)]
    for i in range(d):
        a=list(map(int,input().split()))
        for i in range(n):
            t[i]*=a[i]
    print("yes" if t.count(1)>0 else "no")