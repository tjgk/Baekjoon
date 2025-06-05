for i in range(int(input())):
    a=list(map(int,input().split()))
    tf=1
    for i in range(a[0]-2):
        if a[i+1]+a[i+2]!=a[i+3]:
            tf=0
            break
    print("YES" if tf==1 else "NO")