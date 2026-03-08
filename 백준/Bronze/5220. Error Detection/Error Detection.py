for i in range(int(input())):
    a,b=map(int,input().split())
    a=bin(a)[2:]
    print("Valid" if a.count("1")%2==b else "Corrupt")