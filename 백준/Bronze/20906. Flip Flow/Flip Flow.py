t,s,n=map(int,input().split())
a=list(map(int,input().split()))
u,d=s,0
for i in range(len(a)-1):
    u=max(0,u-(a[i+1]-a[i]))
    d=min(s,d+a[i+1]-a[i])
    u,d=d,u
u=max(0,u-(t-a[-1]))
print(u)