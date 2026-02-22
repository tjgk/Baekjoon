for i in range(int(input())):
    a=input()
    for i in a:
        if i=="a":
            print("e",end="")
        elif i=="i":
            print("o",end="")
        elif i=="u":
            print("y",end="")
        elif i=="y":
            print("a",end="")
        elif i=="e":
            print("i",end="")
        elif i=="o":
            print("u",end="")
        elif i=="A":
            print("E",end="")
        elif i=="I":
            print("O",end="")
        elif i=="U":
            print("Y",end="")
        elif i=="Y":
            print("A",end="")
        elif i=="E":
            print("I",end="")
        elif i=="O":
            print("U",end="")
        else:
            print(i,end="")
    print()