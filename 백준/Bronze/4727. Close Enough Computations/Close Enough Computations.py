while 1:
    a,b,c,d=map(int,input().split())
    if a+b+c+d==0:
        break
    print("yes" if b*9+(c+d)*4-8.5+0.5*([b,c,d].count(0))<a<b*9+(c+d)*4+8.5 else "no")