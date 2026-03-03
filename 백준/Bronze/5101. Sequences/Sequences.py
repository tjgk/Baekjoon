while 1:
    a,b,c=map(int,input().split())
    if a==b==c==0:
        break
    if (b>0 and a>c) or (b<0 and a<c):
        print("X")
    elif (c-a)%b==0:
        print((c-a)//b+1)
    else:
        print("X")