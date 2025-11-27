a=list(map(int,input().split()))
b=list(map(int,input().split()))
if a[0]+a[1]*2+a[2]*3>b[0]+b[1]*2+b[2]*3:
    print(1)
elif a[0]+a[1]*2+a[2]*3<b[0]+b[1]*2+b[2]*3:
    print(2)
else:
    print(0)