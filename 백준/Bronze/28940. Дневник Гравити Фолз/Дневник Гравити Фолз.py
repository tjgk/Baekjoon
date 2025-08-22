w,h=map(int,input().split())
n,a,b=map(int,input().split())
x=(w//a)*(h//b)
if x==0:
    print(-1)
else:
    print(n//x+1 if n/x!=n//x else n//x)