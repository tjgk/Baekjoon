for i in range(int(input())):
    x,y=0,0
    for i in range(int(input())):
        a,b=map(float,input().split())
        x+=a
        y+=a*b
    print(int(x),y/x)