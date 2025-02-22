x,y=map(int,input().split())
n=int(input())
dis=list(map(int,input().split()))
for i in range(n-1):
    a,b=map(int,input().split())
    if abs(x-dis[0])+abs(y-dis[1])>abs(x-a)+abs(y-b):
        dis=[a,b]
print(dis[0],dis[1])