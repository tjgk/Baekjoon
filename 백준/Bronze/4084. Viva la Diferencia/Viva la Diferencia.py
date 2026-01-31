while 1:
    a,b,c,d=map(int,input().split())
    i=0
    if a==0: 
        break
    while 1:
        if a==b==c==d:
            print(i)
            break
        i+=1
        a,b,c,d=abs(a-b),abs(b-c),abs(c-d),abs(d-a)