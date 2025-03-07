a,b=map(int,input().split())
m=int(input())
z=list(map(int,input().split()))
ans=[]
t=0
for i in range(m):
    t+=z[i]*(a**(m-1-i))
i=0
while t!=0:
    i+=1
    ans.append(t%(b**i))
    t-=t%(b**i)
for i in range(len(ans)-1):
    ans[i+1]=ans[i+1]//(b**(i+1))
ans=list(reversed(ans))
print(" ".join(map(str,ans)))