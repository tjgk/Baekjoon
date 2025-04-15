for i in range(int(input())):
    n=int(input())
    r=0
    for j in range(1,n+1):
        if n%j==0:
            r+=1
    print(n,r)