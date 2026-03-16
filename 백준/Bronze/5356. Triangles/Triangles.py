for i in range(int(input())):
    n,s=input().split()
    n=int(n)
    s=ord(s)
    for i in range(n):
        if s>90:
            s-=26
        print(chr(s)*(i+1))
        s+=1
    print()