n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    x,y=map(int,input().split())
    if a[i]==1 and x<y:
        s+=y-x
print(s)