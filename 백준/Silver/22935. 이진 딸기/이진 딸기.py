for i in range(int(input())):
    n=int(input())
    if n%28==0:
        s="0010"
    elif 1<=n%28<=15:
        s=bin(n%28)[2:]
    else:
        s=bin(30-n%28)[2:]
    s="0"*(4-len(s))+s
    for i in s:
        print("V" if i=="0" else "딸기",end="")
    print()