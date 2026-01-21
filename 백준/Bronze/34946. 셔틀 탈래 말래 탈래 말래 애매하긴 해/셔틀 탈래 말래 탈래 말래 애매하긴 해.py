a,b,c,d=map(int,input().split())
if a+b<=d:
    if c<=d:
        print("~.~")
    else:
        print("Shuttle")
elif c<=d:
    print("Walk")
else:
    print("T.T")