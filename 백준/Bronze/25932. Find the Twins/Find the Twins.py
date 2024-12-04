for i in range(int(input())):
    a=list(input().split())
    print(" ".join(a))
    if a.count("18")==0:
        if a.count("17")==0:
            print("none")
        else:
            print("zack")
    else:
        if a.count("17")==0:
            print("mack")
        else:
            print("both")
    print("")