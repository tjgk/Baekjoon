n,m,k=map(int,input().split())
t=min(n//2,m)
k-=n-2*t+m-t
print(t if k<=0 else (t*3-k)//3)