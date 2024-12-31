i=0
while 1:
    i+=1
    a,b,c=map(int,input().split())
    if sum([a,b,c])==0:
        break
    elif c==-1:
        print(f"Triangle #{i}")
        print(f"c = {(a**2+b**2)**0.5:.3f}")
    elif b==-1:
        if a>=c:
            print(f"Triangle #{i}")
            print("Impossible.")
        else:
            print(f"Triangle #{i}")
            print(f"b = {(c**2-a**2)**0.5:.3f}")
    else:
        if b>=c:
            print(f"Triangle #{i}")
            print("Impossible.")
        else:
            print(f"Triangle #{i}")
            print(f"a = {(c**2-b**2)**0.5:.3f}")
    print()