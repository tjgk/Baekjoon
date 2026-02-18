while 1:
    a=list(map(int,input().split()))
    if a==[0,0,0,0,0,0]:
        break
    a.sort()
    a=a[1:-1]
    if int(sum(a)/len(a))==sum(a)/len(a):
        print(int(sum(a)/len(a)))
    else:
        print(f"{sum(a)/len(a)}")