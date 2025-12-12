p,q=map(int,input().split())
a,b=map(int,input().split())
print(min(p,q)*a+max(0,q-p)*b)