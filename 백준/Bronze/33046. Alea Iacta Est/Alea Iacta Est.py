a,b=map(int,input().split())
c,d=map(int,input().split())
print((a+b+c+d-1)%4 if (a+b+c+d-1)%4!=0 else 4)