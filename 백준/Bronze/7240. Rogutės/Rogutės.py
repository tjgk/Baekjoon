n,s=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
t=0
for i in range(n):
    t+=a[i]
    if t>s and i!=n-1:
        t-=1
print(t)