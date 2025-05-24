n,k=map(int,input().split())
a=list(map(int,input().split()))

for i in range(1,n):
    loc=i-1
    newItem=a[i]
    while loc>=0 and newItem<a[loc]:
        a[loc+1]=a[loc]
        loc-=1
        k-=1
        if k==0:
            r=a[loc+1]
            break
    if k==0:
        break
    if loc+1!=i:
        a[loc+1]=newItem
        k-=1
        if k==0:
            r=newItem
            break

print(r if k==0 else -1)