while 1:
    a,b,c=input().split()
    if a=="0" and b=="W" and c=="0":
        break
    a,c=int(a),int(c)
    if b=="W":
        print(a-c if a-c>=-200 else "Not allowed")
    else:
        print(a+c)