for i in range(int(input())):
    tf=1
    a=list(map(int,input().split()))
    for i in range(1,len(a)-1):
        if a[i]*2>a[i+1]:
            tf=0
    if tf==1:
        print("Denominations: ",end="")
        for j in a[1:]:
            print(j,end=" ")
        print("\n"+"Good coin denominations!"+"\n")
    else:
        print("Denominations: ",end="")
        for j in a[1:]:
            print(j,end=" ")
        print("\n"+"Bad coin denominations! "+"\n")