while 1:
    n=int(input())
    if n==0:
        break
    a=list(map(int,input().split()))
    print(f"Mary won {a.count(0)} times and John won {a.count(1)} times")