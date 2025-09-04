for i in range(int(input())):
    n,a,d=map(int,input().split())
    print((n*(a*2+(n-1)*d))//2)