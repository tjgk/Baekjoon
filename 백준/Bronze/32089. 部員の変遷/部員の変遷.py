while 1:
    n=int(input())
    if n==0:
        break
    else:
        a=list(map(int,input().split()))
        M=0
        for i in range(n-2):
            if sum(a[i:i+3])>M:
                M=sum(a[i:i+3])
        print(M)