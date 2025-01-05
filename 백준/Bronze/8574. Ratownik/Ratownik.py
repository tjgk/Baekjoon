n,k,x,y=map(int,input().split())
s=0
for i in range(n):
    a,b=map(int,input().split())
    if (x-a)**2+(y-b)**2>k**2:
        s+=1
print(s)