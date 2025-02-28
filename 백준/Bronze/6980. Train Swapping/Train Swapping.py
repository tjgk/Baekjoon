for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    c=0
    while a!=b:
        for k in range(n-1):
            if a[k]>a[k+1]:
                a[k],a[k+1]=a[k+1],a[k]
                c+=1
    print(f"Optimal train swapping takes {c} swaps.")