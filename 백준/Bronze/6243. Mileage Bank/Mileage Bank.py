m=0
while 1:
    t=list(input().split())
    if len(t)==1:
        if t[0]=="0":
            print(m)
            m=0
            continue
        else:
            break
    if t[3]=="F":
        m+=int(t[2])*2
    elif t[3]=="B":
        m+=int(t[2])+int(t[2])//2+(1 if int(t[2])%2==1 else 0)
    else:
        if int(t[2])>500:
            m+=int(t[2])
        else:
            m+=500