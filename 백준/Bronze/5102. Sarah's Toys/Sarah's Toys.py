while 1:
    a,b=map(int,input().split())
    if a==b==0:
        break
    k=a-b
    if k<=1:
        print(0,0)
    elif k%2==1:
        print((k-3)//2,1)
    else:
        print(k//2,0)