n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(set(map(int,input().split())))
t=0
for i in b:
    t+=a.count(i)
print(t)