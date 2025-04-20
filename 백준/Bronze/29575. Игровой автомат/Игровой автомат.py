n={}
t=[]
r=0
for i in range(int(input())):
    a,b=map(int,input().split())
    n[a]=b
m=int(input())
for i in range(m):
    c=int(input())
    if c in n:
        r+=n[c]
print(r-10*m)