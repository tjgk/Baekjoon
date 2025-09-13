for i in range(int(input())):
    a,b=map(int,input().split())
    a,b=max(a,b),min(a,b)
    x,y=a,b
    while 1:
        if x%y==0:
            print((a*b)//y)
            break
        else:
            p,q=x,y
            x,y=q,p%q
