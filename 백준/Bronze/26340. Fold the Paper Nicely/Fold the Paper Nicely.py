for i in range(int(input())):
    a,b,c=map(int,input().split())
    print(f"Data set: {a} {b} {c}")
    for j in range(c):
        if a>=b:
            a//=2
        else:
            b//=2
    print(max(a,b),min(a,b))
    print()