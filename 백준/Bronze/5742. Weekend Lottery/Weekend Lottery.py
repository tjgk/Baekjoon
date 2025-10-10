while 1:
    n,c,k=map(int,input().split())
    a=[0 for i in range(k)]
    if n+c+k==0:
        break
    for i in range(n):
        b=list(map(int,input().split()))
        for j in b:
            a[j-1]+=1
    for j in range(k):
        if min(a)==a[j]:
            print(j+1,end=" ")
    print()