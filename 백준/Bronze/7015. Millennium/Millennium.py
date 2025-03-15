for i in range(int(input())):
    y,m,d=map(int,input().split())
    r=0
    r+=590*((y-1)//3)+195*((y-1)%3)
    if y%3!=0:
        if m%2==0:
            r+=39*((m-1)//2)+20
        else:
            r+=39*((m-1)//2)
    else:
        r+=20*(m-1)
    r+=d
    print(196471-r)