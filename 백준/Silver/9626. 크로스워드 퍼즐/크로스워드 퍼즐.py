m,n=map(int,input().split())
u,l,r,d=map(int,input().split())
a=[]
for i in range(m):
    a.append(input())
t=["#","."]
b=[[] for i in range(u+m+d)]
for i in range(u+m+d):
    for j in range(l+n+r):
        b[i].append(t[(i+j)%2])
for i in range(m):
    for j in range(n):
        b[u+i][l+j]=a[i][j]
for i in b:
    print("".join(i))