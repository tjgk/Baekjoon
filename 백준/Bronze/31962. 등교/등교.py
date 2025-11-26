n,x=map(int,input().split())
m=-1
for i in range(n):
    s,t=map(int,input().split())
    if s+t<=x and m<s:
        m=s
print(m)