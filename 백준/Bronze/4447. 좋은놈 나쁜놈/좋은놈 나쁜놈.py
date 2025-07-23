for i in range(int(input())):
    a=input()
    g=a.count("G")+a.count("g")
    b=a.count("B")+a.count("b")
    if g>b:
        print(a,"is","GOOD")
    elif g<b:
        print(a,"is","A BADDY")
    else:
        print(a,"is","NEUTRAL")