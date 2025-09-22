while 1:
    n,m=map(int,input().split())
    M=0
    if n+m==0:
        break
    a=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if M<=a[i]+a[j]<=m:
                M=a[i]+a[j]
    if M==0:
        print("NONE")
    else:
        print(M)