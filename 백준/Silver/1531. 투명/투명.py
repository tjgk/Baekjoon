n,m=map(int,input().split())
p=[[0 for i in range(101)] for i in range(101)]
for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            p[y][x]+=1
s=0
for i in p:
    for j in i:
        if j>m:
            s+=1
print(s)