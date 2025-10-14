for i in range(int(input())):
    a=list(input().split())
    s=0
    for i in a:
        if i=="Franklin":
            s+=100
        elif i=="Grant":
            s+=50
        elif i=="Jackson":
            s+=20
        elif i=="Hamilton":
            s+=10
        elif i=="Lincoln":
            s+=5
        else:
            s+=1
    print(f"${s}")