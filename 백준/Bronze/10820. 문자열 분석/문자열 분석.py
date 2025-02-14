while 1:
    try:
        a=input()
        w,x,y,z=0,0,0,0
        for i in a:
            if i==" ":
                z+=1
            elif 47<ord(i)<58:
                y+=1
            elif 96<ord(i)<123:
                w+=1
            else:
                x+=1
        print(w,x,y,z)
    except:
        break