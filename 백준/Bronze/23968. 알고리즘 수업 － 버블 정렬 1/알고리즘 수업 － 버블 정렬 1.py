n,k=map(int,input().split())
a=list(map(int,input().split()))

for last in range(n-1,0,-1):
    sorted=1
    for i in range(last):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            sorted=0
            k-=1
        if k==0:
            x,y=a[i],a[i+1]
            break
    if k==0 or sorted==1:
        break

print(x,y) if k==0 else print(-1)