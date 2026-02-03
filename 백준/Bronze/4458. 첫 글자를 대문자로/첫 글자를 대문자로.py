for i in range(int(input())):
    s=input()
    if ord(s[0])>96:
        print(chr(ord(s[0])-32)+s[1:])
    else:
        print(s)