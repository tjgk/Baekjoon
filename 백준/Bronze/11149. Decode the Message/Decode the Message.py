for i in range(int(input())):
    a=list(input().split())
    for i in range(len(a)):
        s=0
        for i in a[i]:
            s+=(ord(i)-97)
        print(chr(s%27+97) if s%27!=26 else " ",end="")
    print()