N,m,M,T,R=map(int,input().split())
x=m
t=0
k=0
while N!=k:
    if m+T>M:
        break
    if x+T<=M:
        t+=1
        k+=1
        x+=T
    else:
        t+=1
        x=max(x-R,m)
print(-1 if t==0 else t)