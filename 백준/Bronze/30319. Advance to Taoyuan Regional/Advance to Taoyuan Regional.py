y,m,d=map(int,input().split("-"))
if m==9:
    if d<=16:
        print("GOOD")
    else:
        print("TOO LATE")
elif m<9:
    print("GOOD")
else:
    print("TOO LATE")