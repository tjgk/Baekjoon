n=int(input())
a=list(map(int,input().split()))
a.sort()
x=int(input())
l,r=0,n-1
ans=0
while l<r:
    if a[l]+a[r]<x:
        l+=1
    elif a[l]+a[r]>x:
        r-=1
    else:
        ans+=1
        l+=1
print(ans)