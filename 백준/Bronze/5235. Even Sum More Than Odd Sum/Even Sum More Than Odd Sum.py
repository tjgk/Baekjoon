for i in range(int(input())):
    a=list(map(int,input().split()))
    e,o=0,0
    for i in a[1:]:
        if i%2==0:
            e+=i
        else:
            o+=i
    if e>o:
        print("EVEN")
    elif e<o:
        print("ODD")
    else:
        print("TIE")