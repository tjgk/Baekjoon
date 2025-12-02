n=int(input())
tf=1
a,b=map(int,input().split())
for i in range(n-1):
    x,y=map(int,input().split())
    if x>=a and y>=b:
        pass
        a,b=x,y
    else:
        tf=0
if tf==1:
    print("yes")
else:
    print("no")