while 1:
    a=input()
    t=0
    if a=="END":
        break
    else:
        for i in a:
            if i!=" " and a.count(i)>=2:
                t=1
                continue
        if t==0:
            print(a)