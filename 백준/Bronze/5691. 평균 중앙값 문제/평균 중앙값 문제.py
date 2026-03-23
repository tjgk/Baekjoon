while 1:
    a,b=map(int,input().split())
    if a==b==0:
        break
    print(min(a,b)*2-max(a,b))