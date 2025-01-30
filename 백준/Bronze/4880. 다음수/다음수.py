while 1:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    elif a+c==b*2:
        print("AP",c*2-b)
    else:
        print("GP",c*(c//b))