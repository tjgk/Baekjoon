while 1:
    a=input()
    if a=="#":
        break
    else:
        for i in a:
            if i==" ":
                print("%20",end="")
            elif i=="!":
                print("%21",end="")
            elif i=="$":
                print("%24",end="")
            elif i=="%":
                print("%25",end="")
            elif i=="(":
                print("%28",end="")
            elif i==")":
                print("%29",end="")
            elif i=="*":
                print("%2a",end="")
            else:
                print(i,end="")
        print()