a,b=map(int,input().split())
k,x=map(int,input().split())
s=0
for i in range(a,b+1):
    if k-x<=i<=k+x:
        s+=1
print(s if s!=0 else "IMPOSSIBLE")