while 1:
    l=[]
    try:
        l.append(int(input()))
    except:
        break
    i=0
    while 1:
        i+=1
        l.append(len(str(l[-1])))
        if l[-1]==l[-2]:
            print(i)
            break