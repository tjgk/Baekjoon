for i in range(int(input())):
    a=[]
    n,m=map(int,input().split())
    for i in range(n):
        a.append(0)
    for i in range(m):
        b=list(map(int,input().split()))
        for i in range(n):
            a[i]+=b[i]
    print(a.index(max(a))+1)