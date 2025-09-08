while 1:
    n=input()
    if n=="0":
        break
    t=0
    for i in range(len(n)):
        if int(n[t])<int(n[i]):
            t=i
    if int(n[t])%2==1:
        n=n[:t]+"0"+n[t+1:]
    else:
        if int(n[t])>=6:
            n=n[:t]+str(int(n[t])+4)[1]+n[t+1:]
        else:
            n=n[:t]+str(int(n[t])+4)+n[t+1:]
    print(str(int(n)))