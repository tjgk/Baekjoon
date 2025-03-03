a=list(map(int,input().split()))
a.sort()
print(sum(a) if a[0]+a[1]>a[2] else (a[0]+a[1])*2-1)