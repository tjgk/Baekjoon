n,k=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n-1,0,-1):
    if max(a[:i])>a[i]:
        k-=1
        x,y=a[i],a[a.index(max(a[:i]))]
        a[i],a[a.index(max(a[:i]))]=a[a.index(max(a[:i]))],a[i]
    if k==0:
        break

if k==0:
    print(x,y)
else:
    print(-1)