for i in range(int(input())):
    a=list(map(int,input().split()))
    print(a[0],a[1],a[2])
    a.sort()
    if a[2]>=10:
        if a[1]>=10:
            if a[0]>=10:
                print("triple-double")
            else:
                print("double-double")
        else:
            print("double")
    else:
        print("zilch")
    print("")