for i in range(int(input())):
    a,b=0,0
    for j in range(int(input())):
        x,y=input().split()
        if x=="S":
            if y=="R":
                b+=1
            elif y=="P":
                a+=1
        elif x=="R":
            if y=="S":
                a+=1
            elif y=="P":
                b+=1
        else:
            if y=="S":
                b+=1
            elif y=="R":
                a+=1
    if a>b:
        print("Player 1")
    elif a<b:
        print("Player 2")
    else:
        print("TIE")