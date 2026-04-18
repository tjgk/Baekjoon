for i in range(int(input())):
    a,b=input().split()
    c=int("".join(reversed(a)))+int("".join(reversed(b)))
    print(int("".join(reversed(str(c)))))