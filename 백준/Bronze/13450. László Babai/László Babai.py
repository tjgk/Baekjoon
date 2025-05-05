for i in range(int(input())):
    a,b=[0,0,0],[0,0,0]
    m=int(input())
    for j in range(m):
        x,y=map(int,input().split())
        a[x-1]+=1
        a[y-1]+=1
    n=int(input())
    for j in range(n):
        x,y=map(int,input().split())
        b[x-1]+=1
        b[y-1]+=1
    print("yes" if m==n else "no")