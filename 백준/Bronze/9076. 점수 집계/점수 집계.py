for i in range(int(input())):
    n=list(map(int,input().split()))
    n=sorted(n)[1:4]
    print(sum(n) if n[2]-n[0]<4 else "KIN")