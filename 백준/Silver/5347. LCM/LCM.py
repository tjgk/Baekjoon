for i in range(int(input())):
    a,b=map(int,input().split())
    c=[max(a,b),min(a,b)]
    while c[-1]!=0:
        c.append(c[-2]%c[-1])
    print((a*b)//c[-2])